#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>

template <typename T>
double lagrange(T x, std::vector<T> x_values, std::vector<T> y_values) {
    double result = 0;
    for (int i = 0; i < x_values.size(); i++) {
        double term = y_values[i];
        for (int j = 0; j < x_values.size(); j++) {
            if (j != i) {
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j]);
            }
        }
        result += term;
    }
    return result;
}


void part1() {
    std::ifstream file("input.txt");
    std::string line;
    
    int total = 0;
    while (std::getline(file, line)) {
        std::vector<int> x_vals;
        std::vector<int> y_vals;
        std::istringstream iss(line);
        std::string token;
        int i = 0;
        while (std::getline(iss, token, ' ')) {
            x_vals.push_back(i);
            y_vals.push_back(std::stoi(token));
            i++;
        }
        total += std::round(lagrange(i, x_vals, y_vals));
    }
    std::cout << total << std::endl;
}


void part2() {
    std::ifstream file("input.txt");
    std::string line;
    
    int total = 0;
    while (std::getline(file, line)) {
        std::vector<int> x_vals;
        std::vector<int> y_vals;
        // each line is space separated y values only, x values are 0, 1, ...
        std::istringstream iss(line);
        std::string token;
        int i = 0;
        while (std::getline(iss, token, ' ')) {
            x_vals.push_back(i);
            y_vals.push_back(std::stoi(token));
            i++;
        }
        total += std::round(lagrange(-1, x_vals, y_vals));
    }
    std::cout << total << std::endl;
}

int main() {
    part1();
    part2();
    return 0;
}