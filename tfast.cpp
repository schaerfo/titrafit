/*
Copyright (C) 2019  Christian Schärf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <algorithm>
#include <cmath>
#include <numeric>
#include <utility>
#include <vector>
#include <chrono>
#include <iostream>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

using float_type = double;

constexpr float_type Kw = 1e-14;
constexpr float_type epsilon = 1e-8;

/*template<typename T>
std::vector<T> py_obj_to_vec(boost::python::object const& o){
    std::vector<T> res;
    for (std::size_t i=0; i<boost::python::len(o); ++i) {
        T x = boost::python::extract<T>(o[i]);
        res.emplace_back(x);
    }
    return res;
}*/

class Titration{
public:
    struct Result {
        // Input
        float_type c0_s;
        float_type c0_b;
        
        // Result
        float_type HA;
        float_type A;
    };
    
    explicit Titration(std::vector<float_type> pKs):
            m_Ks{[pKs = std::move(pKs)](){
                std::vector<float_type> res;
                std::transform(pKs.begin(), pKs.end(), std::back_inserter(res), [](auto val){ // Lambda-ception
                    return std::pow(10, -val);
                });
                return res;
            }()}
            //,A(1., m_Ks.size())
    {
    }
    
    Titration(std::initializer_list<float_type> pKs):
            Titration{std::vector<float_type>{pKs}}
    {
    }

    /*explicit Titration (const boost::python::object& pKs):
            Titration{py_obj_to_vec<float_type>(pKs)}
    {
    }*/

    float_type operator()(float_type c0_b, float_type c0_s) const{
        std::vector<float_type> A(m_Ks.size(), 1);
        float_type HA = 1;
        if (!m_result_cache.empty())
            std::tie(HA, A[0]) = find_closest_result(c0_s, c0_b);

        
        for(;;){
            float_type H;
            for(;;){
                H = m_Ks[0] * HA / A[0];
                float_type OH = Kw/H;
                for (std::size_t i=1; i<m_Ks.size(); ++i)
                    A[i] = m_Ks[i] * A[i-1] / H;

                float_type anion_sum = OH;
                for (std::size_t i=0; i<A.size(); ++i)
                    anion_sum += static_cast<float_type>(i+1)* A[i];
                float_type el = (H + c0_b) / anion_sum;
                
                if (std::abs(el-1) < epsilon)
                    break;
                A[0] *= std::sqrt(el);
            }

            float_type x = c0_s / (HA + std::accumulate(A.begin(), A.end(), 0.0));
            if (std::abs(x-1) < epsilon){
                m_result_cache.push_back({c0_s, c0_b, HA, A[0]});
                return -std::log10(H);
            }
            HA *= x;
        }
    }

    float_type percentage(float_type percentage, float_type c0_s) {
        return (*this)(c0_s * percentage, c0_s);
    }

private:
    const std::vector<float_type> m_Ks;
    mutable std::vector<Result> m_result_cache;

    //mutable float_type HA = 1;
    //mutable std::vector<float_type> A;

    std::pair<float_type, float_type> find_closest_result(float_type c0_s, float_type c0_b) const{
        auto min = std::min_element(m_result_cache.begin(), m_result_cache.end(), [c0_s, c0_b](auto a, auto b){
            auto key = [c0_s, c0_b](auto res) {
                auto d_s = c0_s - res.c0_s;
                auto d_b = c0_b - res.c0_b;
                return d_s*d_s + d_b*d_b;
            };
            return key(a) < key(b);
        });
        return std::make_pair(min->HA, min->A);
    }
};

class TitrationVolume : public Titration{
public:
    TitrationVolume(float_type V0, float_type c0_b, std::vector<float_type> pKs)
         : Titration{std::move(pKs)}
         , m_c0_b{c0_b}
         , m_V0{V0}
    {
    }
    
    /*TitrationVolume(float_type V0, float_type c0_b, const boost::python::object& pKs):
         TitrationVolume{V0, c0_b, py_obj_to_vec<float_type>(pKs)}
    {
    }*/

    float_type operator() (float_type V_b, float_type n0_s){
        float_type V = m_V0 + V_b,
                   c_b = m_c0_b * V_b / V,
                   c_s = n0_s / V;
        
        return Titration::operator()(c_b, c_s);
    }
    
    float_type percentage(float_type percentage, float_type n0_s) {
        return (*this)(percentage*n0_s / m_c0_b, n0_s);
    }

private:
    const float_type m_c0_b, m_V0;
};

PYBIND11_MODULE(tfast, m) {
    using namespace pybind11;
    class_<Titration>(m, "Titration")
            .def(init<std::vector<float_type>>())
            .def("__call__", &Titration::operator())
            .def("percentage", &Titration::percentage);
    
    class_<TitrationVolume>(m, "TitrationVolume")
            .def(init<float_type, float_type, std::vector<float_type>>())
            .def("__call__", &TitrationVolume::operator())
            .def("percentage", &TitrationVolume::percentage);
}

int main(int argc, char const *argv[])
{
    Titration t{4};
    std::vector<float_type> res;

    //res.reserve(0.2/0.15);
    auto start = std::chrono::steady_clock::now();
    for (float_type p = 0.; p < 0.2; p+= 0.001)
        res.emplace_back(t(0.1, p));
    std::chrono::duration<double> interval = std::chrono::steady_clock::now() - start;

    for (auto val : res)
        std::cout << val << '\n';

    std::cout << "Duration: " << interval.count() << '\n';

    return 0;
}
