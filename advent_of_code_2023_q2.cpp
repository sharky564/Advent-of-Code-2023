#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

int main() {
    std::ifstream file("aoc_2023_day_2.txt");
    std::string line;
    int sum = 0;
    while (std::getline(file, line)) {
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == ':' || line[i] == ',' || line[i] == ';') {
                line[i] = ' ';
            }
        }
        // split the line into words
        std::vector<std::string> words;
        std::stringstream ss(line);
        std::string word;
        while (ss >> word) {
            words.push_back(word);
        }
        int id = std::stoi(words[1]);
        int red = 0;
        int green = 0;
        int blue = 0;
        for (int i = 2; i < words.size(); i++) {
            if (words[i] == "red") {
                red = std::max(red, std::stoi(words[i-1]));
            } else if (words[i] == "green") {
                green = std::max(green, std::stoi(words[i-1]));
            } else if (words[i] == "blue") {
                blue = std::max(blue, std::stoi(words[i-1]));
            }
        }
        sum += red * green * blue;
    }
    std::cout << sum << std::endl;
    return 0;
}