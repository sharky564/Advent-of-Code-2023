#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>

int num_sols(long long int time, long long int dist) {
    long long int min_val = std::floor((time - std::sqrt(time * time - 4 * dist)) / 2) + 1;
    long long int max_val = std::ceil((time + std::sqrt(time * time - 4 * dist)) / 2) - 1;
    return max_val - min_val + 1;
}

int main() {
    std::ifstream file("input.txt");
    std::string line;
    long long int time;
    long long int distance;
    std::getline(file, line);
    std::stringstream ss(line.substr(line.find(":") + 1));
    // concatenate the numbers into a string
    std::string num_str;
    std::string value;
    while (ss >> value) {
        num_str += value;
    }
    time = std::stoll(num_str);
    std::getline(file, line);
    ss = std::stringstream(line.substr(line.find(":") + 1));
    num_str = "";
    while (ss >> value) {
        num_str += value;
    }
    distance = std::stoll(num_str);
    std::cout << num_sols(time, distance) << std::endl;
    return 0;
}