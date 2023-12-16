#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>


void part1() {
    std::ifstream file("input.txt");
    std::string line;
    
    std::string sequence;
    std::getline(file, sequence);

    std::unordered_map<std::string, std::vector<std::string>> network;
    while (std::getline(file, line)) {
        std::string node;
        std::string child;
        line.erase(std::remove_if(line.begin(), line.end(), [](char c) { return !(std::isalnum(c) || c == ' '); }), line.end());
        std::stringstream ss(line);
        ss >> node;
        while (ss >> child) {
            network[node].push_back(child);
        }
    }

    std::string curr_node = "AAA";
    int iterations = 0;
    while (curr_node != "ZZZ") {
        iterations++;
        for (char c: sequence) {
            if (c == 'L') {
                curr_node = network[curr_node][0];
            }
            else {
                curr_node = network[curr_node][1];
            }
        }
    }
    std::cout << iterations * sequence.length() << std::endl;
}

template <typename T>
T gcd(T a, T b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

template <typename T>
T lcm(T a, T b) {
    return (a * b) / gcd(a, b);
}


void part2() {
    std::ifstream file("input.txt");
    std::string line;
    std::string sequence;
    std::getline(file, sequence);

    std::unordered_map<std::string, std::vector<std::string>> network;
    while (std::getline(file, line)) {
        std::string node;
        std::string child;
        line.erase(std::remove_if(line.begin(), line.end(), [](char c) { return !(std::isalnum(c) || c == ' '); }), line.end());
        std::stringstream ss(line);
        ss >> node;
        while (ss >> child) {
            network[node].push_back(child);
        }
    }

    std::vector<std::string> nodes;
    for (auto it = network.begin(); it != network.end(); it++) {
        if (it->first.back() == 'A') {
            nodes.push_back(it->first);
        }
    }
    std::vector<int> iterations;
    for (std::string node: nodes) {
        std::string curr_node = node;
        int iter = 0;
        while (curr_node.back() != 'Z') {
            iter++;
            for (char c: sequence) {
                if (c == 'L') {
                    curr_node = network[curr_node][0];
                }
                else {
                    curr_node = network[curr_node][1];
                }
            }
        }
        iterations.push_back(iter);
    }
    long long int iterations_lcm = iterations[0];
    for (int i = 1; i < iterations.size(); i++) {
        long long int val = iterations[i];
        iterations_lcm = lcm(iterations_lcm, val);
    }
    std::cout << iterations_lcm * sequence.length() << std::endl;
}

int main() {
    part1();
    part2();
    return 0;
}