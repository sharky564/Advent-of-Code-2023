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

void part1() {
    std::ifstream file("input.txt");
    std::string line;
    long long int time;
    long long int distance;
    std::getline(file, line);
    std::stringstream ss(line.substr(line.find(":") + 1));
    std::vector<int> times;
    int value;
    while (ss >> value) {
        times.push_back(value);
    }
    std::getline(file, line);
    ss = std::stringstream(line.substr(line.find(":") + 1));
    std::vector<int> distances;
    while (ss >> value) {
        distances.push_back(value);
    }
    int total = num_sols(times[0], distances[0]);
    for (int i = 1; i < times.size(); i++) {
        total *= num_sols(times[i], distances[i]);
    }
    std::cout << total << std::endl;
}

void part2() {
    std::ifstream file("input.txt");
    std::string line;
    long long int time;
    long long int distance;
    std::getline(file, line);
    std::stringstream ss(line.substr(line.find(":") + 1));
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
}

int main() {
    part1();
    part2();
    return 0;
}