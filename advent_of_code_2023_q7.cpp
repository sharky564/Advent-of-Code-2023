#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>

int cmp1(char a) {
    switch (a) {
        case 'A':
            return 14;
        case 'K':
            return 13;
        case 'Q':
            return 12;
        case 'J':
            return 11;
        case 'T':
            return 10;
        default:
            return a - '0';
    }
}

void part1() {
    std::ifstream file("input.txt");
    std::string line;
    std::vector<std::vector<std::pair<std::string, int>>> ranks(7);
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string hand;
        std::string bid;
        ss >> hand >> bid;
        std::pair<std::string, int> hand_bid = {hand, std::stoi(bid)};

        // now get a sorted copy of the hand
        std::vector<char> hand_sorted(hand.begin(), hand.end());
        // get frequency of each card
        std::unordered_map<char, int> freq;
        for (char c : hand_sorted) {
            freq[c]++;
        }
        std::sort(hand_sorted.begin(), hand_sorted.end(), [&freq](char a, char b) {
            if (freq[a] == freq[b]) {
                return cmp1(a) > cmp1(b);
            }
            return freq[a] > freq[b];
        });
        if (hand_sorted[0] == hand_sorted[4]) {
            ranks[0].push_back(hand_bid);
        }
        else if (hand_sorted[0] == hand_sorted[3]) {
            ranks[1].push_back(hand_bid);
        }
        else if (hand_sorted[0] == hand_sorted[2] && hand_sorted[3] == hand_sorted[4]) {
            ranks[2].push_back(hand_bid);
        }
        else if (hand_sorted[0] == hand_sorted[2]) {
            ranks[3].push_back(hand_bid);
        }
        else if (hand_sorted[0] == hand_sorted[1] && hand_sorted[2] == hand_sorted[3]) {
            ranks[4].push_back(hand_bid);
        }
        else if (hand_sorted[0] == hand_sorted[1]) {
            ranks[5].push_back(hand_bid);
        }
        else {
            ranks[6].push_back(hand_bid);
        }
    }

    for (int i = 0; i < 7; i++) {
        std::sort(ranks[i].begin(), ranks[i].end(), [](std::pair<std::string, int> a, std::pair<std::string, int> b) {
            for (int i = 0; i < 5; i++) {
                if (cmp1(a.first[i]) != cmp1(b.first[i])) {
                    return cmp1(a.first[i]) > cmp1(b.first[i]);
                }
            }
            return false;
        });
    }

    std::vector<std::pair<std::string, int>> all_ranks;
    for (int i = 6; i >= 0; i--) {
        for (int j = ranks[i].size() - 1; j >= 0; j--) {
            all_ranks.push_back(ranks[i][j]);
        }
    }

    int total = 0;
    for (int i = 1; i <= all_ranks.size(); i++) {
        total += i * all_ranks[i - 1].second;
    }

    std::cout << total << std::endl;
}

int cmp2(char a) {
    switch (a) {
        case 'A':
            return 14;
        case 'K':
            return 13;
        case 'Q':
            return 12;
        case 'J':
            return 1;
        case 'T':
            return 10;
        default:
            return a - '0';
    }
}

void part2() {
    std::ifstream file("input.txt");
    std::string line;
    std::vector<std::vector<std::pair<std::string, int>>> ranks(7);
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string hand;
        std::string bid;
        ss >> hand >> bid;
        std::pair<std::string, int> hand_bid = {hand, std::stoi(bid)};
        std::string hand_without_jokers = hand;
        hand_without_jokers.erase(std::remove(hand_without_jokers.begin(), hand_without_jokers.end(), 'J'), hand_without_jokers.end());
        int num_jokers = hand.size() - hand_without_jokers.size();
        if (num_jokers == 5) {
            ranks[0].push_back(hand_bid);
            continue;
        }
        else {
            std::vector<char> hand_without_jokers_sorted(hand_without_jokers.begin(), hand_without_jokers.end());
            std::unordered_map<char, int> freq;
            for (char c : hand_without_jokers_sorted) {
                freq[c]++;
            }
            std::sort(hand_without_jokers_sorted.begin(), hand_without_jokers_sorted.end(), [&freq](char a, char b) {
                if (freq[a] == freq[b]) {
                    return cmp2(a) > cmp2(b);
                }
                return freq[a] > freq[b];
            });
            std::vector<char> hand_sorted(num_jokers, hand_without_jokers_sorted[0]);
            hand_sorted.insert(hand_sorted.end(), hand_without_jokers_sorted.begin(), hand_without_jokers_sorted.end());
            if (hand_sorted[0] == hand_sorted[4]) {
                ranks[0].push_back(hand_bid);
            }
            else if (hand_sorted[0] == hand_sorted[3]) {
                ranks[1].push_back(hand_bid);
            }
            else if (hand_sorted[0] == hand_sorted[2] && hand_sorted[3] == hand_sorted[4]) {
                ranks[2].push_back(hand_bid);
            }
            else if (hand_sorted[0] == hand_sorted[2]) {
                ranks[3].push_back(hand_bid);
            }
            else if (hand_sorted[0] == hand_sorted[1] && hand_sorted[2] == hand_sorted[3]) {
                ranks[4].push_back(hand_bid);
            }
            else if (hand_sorted[0] == hand_sorted[1]) {
                ranks[5].push_back(hand_bid);
            }
            else {
                ranks[6].push_back(hand_bid);
            }
        }
    }

    for (int i = 0; i < 7; i++) {
        std::sort(ranks[i].begin(), ranks[i].end(), [](std::pair<std::string, int> a, std::pair<std::string, int> b) {
            for (int i = 0; i < 5; i++) {
                if (cmp2(a.first[i]) != cmp2(b.first[i])) {
                    return cmp2(a.first[i]) > cmp2(b.first[i]);
                }
            }
            return false;
        });
    }

    std::vector<std::pair<std::string, int>> all_ranks;
    for (int i = 6; i >= 0; i--) {
        for (int j = ranks[i].size() - 1; j >= 0; j--) {
            all_ranks.push_back(ranks[i][j]);
        }
    }

    int total = 0;
    for (int i = 1; i <= all_ranks.size(); i++) {
        total += i * all_ranks[i - 1].second;
    }

    std::cout << total << std::endl;
}

int main() {
    part1();
    part2();
    return 0;
}