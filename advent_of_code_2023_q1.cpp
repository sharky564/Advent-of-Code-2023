#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void part1() {
    std::ifstream file("input.txt");
    std::string line;
    int sum = 0;
    while (std::getline(file, line)) {
        int first = 0;
        int last = 0;
        int i = 0;
        while ((i < line.length()) && (!isdigit(line[i]))) {
            i++;
        }
        if (i < line.length()) {
            first = line[i] - '0';
        }
        i = line.length() - 1;
        while ((i >= 0) && (!isdigit(line[i]))) {
            i--;
        }
        if (i >= 0) {
            last = line[i] - '0';
        }
        sum += 10 * first + last;
    }
    std::cout << sum << std::endl;
}

void part2() {
    std::ifstream file("input.txt");
    std::string line;
    int sum = 0;
    std::vector<std::string> numbers = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    while (std::getline(file, line)) {
        int first = 0;
        int last = 0;
        int i = 0;
        while (i < line.length()) {
            if (isdigit(line[i])) {
                first = line[i] - '0';
                break;
            }
            else {
                for (int j = 0; j < numbers.size(); j++) {
                    if (line.substr(i, numbers[j].length()) == numbers[j]) {
                        first = j + 1;
                        i = line.length();
                        break;
                    }
                }
            }
            i++;
        }
        if (first == 0) {
            continue;
        }

        i = line.length() - 1;
        while (i >= 0) {
            if (isdigit(line[i])) {
                last = line[i] - '0';
                break;
            }
            else {
                for (int j = 0; j < numbers.size(); j++) {
                    if (line.substr(i, numbers[j].length()) == numbers[j]) {
                        last = j + 1;
                        i = -1;
                        break;
                    }
                }
            }
            i--;
        }
        sum += 10 * first + last;
    }
    std::cout << sum << std::endl;
}


int main() {
    part1();
    part2();
    return 0;
}