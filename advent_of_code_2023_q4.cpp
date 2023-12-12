#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

void part1() {
    std::ifstream file("input.txt");
    std::string line;
    std::vector<std::string> games;
    while (std::getline(file, line)) {
        games.push_back(line);
    }
    int sum = 0;
    int curr_card = 0;
    for (std::string line: games) {
        line = line.substr(line.find(":") + 1);
        std::string first_half = line.substr(0, line.find("|"));
        std::string second_half = line.substr(line.find("|") + 1);
        std::vector<int> wins = std::vector<int>();
        std::vector<int> plays = std::vector<int>();
        std::stringstream ss(first_half);
        int value;
        while (ss >> value) {
            wins.push_back(value);
        }
        std::stringstream ss2(second_half);
        while (ss2 >> value) {
            plays.push_back(value);
        }
        int j = 0;
        for (int i = 0; i < plays.size(); i++) {
            if (std::find(wins.begin(), wins.end(), plays[i]) != wins.end()) {
                j++;
            }
        }
        if (j > 0) {
            sum += 1 << (j - 1);
        }
        curr_card++;
    }
    std::cout << sum << std::endl;
}


void part2() {
    std::ifstream file("input.txt");
    std::string line;
    std::vector<std::string> games;
    while (std::getline(file, line)) {
        games.push_back(line);
    }
    std::vector<int> num_cards = std::vector(games.size(), 1);
    int sum = 0;
    int curr_card = 0;
    for (std::string line: games) {
        line = line.substr(line.find(":") + 1);
        std::string first_half = line.substr(0, line.find("|"));
        std::string second_half = line.substr(line.find("|") + 1);
        std::vector<int> wins = std::vector<int>();
        std::vector<int> plays = std::vector<int>();
        std::stringstream ss(first_half);
        int value;
        while (ss >> value) {
            wins.push_back(value);
        }
        std::stringstream ss2(second_half);
        while (ss2 >> value) {
            plays.push_back(value);
        }
        int j = 0;
        for (int i = 0; i < plays.size(); i++) {
            if (std::find(wins.begin(), wins.end(), plays[i]) != wins.end()) {
                j++;
                num_cards[curr_card + j] += num_cards[curr_card];
            }
        }
        sum += num_cards[curr_card];
        curr_card++;
    }
    std::cout << sum << std::endl;
}

int main() {
    part1();
    part2();
    return 0;
}