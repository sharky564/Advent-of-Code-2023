#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>

int main() {
    std::ifstream file("aoc_2023_day_5.txt");
    std::string line;
    std::vector<std::string> lines;
    // read each line of input into games
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    std::vector<std::pair<long long int, long long int>> seeds;
    // seeds contains the integers for the first line, after the colon
    std::stringstream ss(lines[0].substr(lines[0].find(":") + 1));
    long long int value;
    while (ss >> value) {
        long long int value1 = value;
        ss >> value;
        long long int value2 = value;
        seeds.push_back({value1, value2});
    }
    int line_ind = 3;
    // print seeds
    std::vector<std::unordered_map<long long int, std::pair<long long int, long long int>>> maps;
    while (line_ind < lines.size()) {
        std::unordered_map<long long int, std::pair<long long int, long long int>> map;
        while ((line_ind < lines.size()) && isdigit(lines[line_ind][0])) {
            std::vector<long long int> line_values;
            std::stringstream ss(lines[line_ind]);
            long long int value;
            while (ss >> value) {
                line_values.push_back(value);
            }
            map[line_values[1]] = {line_values[0], line_values[2]};
            line_ind++;
        }
        line_ind += 2;
        maps.push_back(map);
    }

    std::vector<std::pair<long long int, long long int>> curr_vals = seeds;
    for (int i = 0; i < maps.size(); i++) {
        std::unordered_map<long long int, std::pair<long long int, long long int>> curr_map = maps[i];
        std::vector<std::pair<long long int, long long int>> new_vals;
        while (curr_vals.size() > 0) {
            std::pair<long long int, long long int> curr_pair = curr_vals.front();
            curr_vals.erase(curr_vals.begin());
            bool found = false;
            for (auto it = curr_map.begin(); it != curr_map.end(); it++) {
                if ((curr_pair.first < it->first + it->second.second) && (it->first < curr_pair.first + curr_pair.second)) {
                    long long int left_bound = std::max(curr_pair.first, it->first);
                    long long int right_bound = std::min(curr_pair.first + curr_pair.second, it->first + it->second.second);
                    long long int interval_size = right_bound - left_bound;
                    long long int new_left_bound = left_bound + it->second.first - it->first;
                    new_vals.push_back({new_left_bound, interval_size});
                    if (curr_pair.first < it->first) {
                        curr_vals.push_back({curr_pair.first, it->first - curr_pair.first});
                    }
                    if (it->first + it->second.second < curr_pair.first + curr_pair.second) {
                        curr_vals.push_back({it->first + it->second.second, curr_pair.first + curr_pair.second - it->first - it->second.second});
                    }
                    found = true;
                    break;
                }
            }
            if (!found) {
                new_vals.push_back(curr_pair);
            }
        }
        curr_vals = new_vals;
    }
    long long int min = curr_vals[0].first;
    for (int i = 1; i < curr_vals.size(); i++) {
        if (curr_vals[i].first < min) {
            min = curr_vals[i].first;
        }
    }
    std::cout << min << std::endl;
    return 0;
}