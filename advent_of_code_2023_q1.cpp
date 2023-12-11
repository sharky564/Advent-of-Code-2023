#include <iostream>
#include <fstream>
#include <string>

int main() {
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
    return 0;
}