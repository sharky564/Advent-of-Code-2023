#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>


template <typename T, typename U>
struct std::hash<std::pair<T, U>> {
    inline size_t operator()(const std::pair<T, U>& v) const {
        std::hash<T> hasher;
        std::hash<U> hasher2;
        size_t seed = 0;
        seed ^= hasher(v.first) + 0x9e3779b9 + (seed<<6) + (seed>>2);
        seed ^= hasher2(v.second) + 0x9e3779b9 + (seed<<6) + (seed>>2);
        return seed;
    }
};

template <typename T>
struct std::hash<std::vector<T>> {
    inline size_t operator()(const std::vector<T>& v) const {
        std::hash<T> hasher;
        size_t seed = 0;
        for (int i = 0; i < v.size(); i++) {
            seed ^= hasher(v[i]) + 0x9e3779b9 + (seed<<6) + (seed>>2);
        }
        return seed;
    }
};

std::unordered_map<std::pair<std::vector<int>, std::string>, long long int> mem;
long long int num_sols_mem(std::vector<int> nums_to_fit, std::string curr_vals);

long long int num_sols(std::vector<int> nums_to_fit,
                       std::string curr_vals) {
    if (nums_to_fit.size() == 0) {
        for (int i = 0; i < curr_vals.size(); i++) {
            if (curr_vals[i] == '#') {
                return 0;
            }
        }
        return 1;
    }
    std::string modified = curr_vals + ".";
    long long int total = 0;
    int num_to_fit = nums_to_fit[0];
    nums_to_fit.erase(nums_to_fit.begin());
    int i = 0;
    while (i < curr_vals.length()) {
        while ((i < curr_vals.length()) && (modified[i] == '.')) {
            i++;
        }
        int j = i;
        bool damaged = false;
        while ((j < curr_vals.length()) && (modified[j] != '.')) {
            if (modified[j] == '#') {
                damaged = true;
            }
            if (j - i + 1 >= num_to_fit) {
                if (modified[j - num_to_fit] == '#') {
                    j = curr_vals.length();
                }
                else if (modified[j + 1] != '#') {
                    if (j + 2 <= curr_vals.length()) {
                        std::string new_curr_vals = curr_vals.substr(j + 2);
                        total = total + num_sols_mem(nums_to_fit, new_curr_vals);
                    }
                    else {
                        total = total + num_sols_mem(nums_to_fit, "");
                    }
                }
            }
            j++;
        }
        if (damaged) {
            break;
        }
        i = j;
    }
    return total;
}

long long int num_sols_mem(std::vector<int> nums_to_fit, std::string curr_vals) {
    std::pair<std::vector<int>, std::string> key = std::make_pair(nums_to_fit, curr_vals);
    if (mem.find(key) != mem.end()) {
        return mem[key];
    }
    long long int x = num_sols(nums_to_fit, curr_vals);
    mem[key] = x;
    return x;
}


void part1() {
    std::ifstream file("input.txt");
    std::string line;
    
    long long int total = 0;
    while (std::getline(file, line)) {
        std::vector<int> nums_to_fit;
        std::string curr_vals;
        std::stringstream ss(line);
        std::getline(ss, curr_vals, ' ');
        std::string num_to_fit;
        while (std::getline(ss, num_to_fit, ',')) {
            nums_to_fit.push_back(std::stoi(num_to_fit));
        }
        long long int x = num_sols(nums_to_fit, curr_vals);
        total = total + x;
    }
    std::cout << total << std::endl;
}


void part2() {
    std::ifstream file("input.txt");
    std::string line;
    
    long long int total = 0;
    while (std::getline(file, line)) {
        std::vector<int> nums_to_fit;
        std::string curr_vals;
        std::stringstream ss(line);
        std::getline(ss, curr_vals, ' ');
        std::string num_to_fit;
        while (std::getline(ss, num_to_fit, ',')) {
            nums_to_fit.push_back(std::stoi(num_to_fit));
        }
        std::vector<int> new_nums_to_fit;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < nums_to_fit.size(); j++) {
                new_nums_to_fit.push_back(nums_to_fit[j]);
            }
        }
        std::string new_curr_vals = "";
        for (int i = 0; i < 5; i++) {
            new_curr_vals = new_curr_vals + curr_vals;
            if (i != 4) {
                new_curr_vals = new_curr_vals + "?";
            }
        }
        long long int x = num_sols(new_nums_to_fit, new_curr_vals);
        total = total + x;
    }
    std::cout << total << std::endl;
}

int main() {
    part1();
    part2();
    return 0;
}