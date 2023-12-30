#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>

long long int solve(int expansion_coeff, 
                    std::vector<int>& expansion_rows, 
                    std::vector<int>& expansion_cols, 
                    std::vector<std::pair<int, int>>& galaxies) {
    long long int total = 0;
    for (int i = 0; i < galaxies.size(); i++) {
        std::pair<int, int> galaxy1 = galaxies[i];
        for (int j = i + 1; j < galaxies.size(); j++) {
            std::pair<int, int> galaxy2 = galaxies[j];
            int row_diff = std::abs(galaxy1.first - galaxy2.first);
            int x_min = std::min(galaxy1.first, galaxy2.first);
            int x_max = std::max(galaxy1.first, galaxy2.first);
            int row_count = 0;
            int k = 0;
            while (expansion_rows[k] < x_min) {
                k++;
            }
            while ((k < expansion_rows.size()) && (expansion_rows[k] <= x_max)) {
                row_count++;
                k++;
            }
            int dist_x = row_diff + row_count * (expansion_coeff - 1);

            int col_diff = std::abs(galaxy1.second - galaxy2.second);
            int y_min = std::min(galaxy1.second, galaxy2.second);
            int y_max = std::max(galaxy1.second, galaxy2.second);
            int col_count = 0;
            k = 0;
            while (expansion_cols[k] < y_min) {
                k++;
            }
            while ((k < expansion_cols.size()) && (expansion_cols[k] <= y_max)) {
                col_count++;
                k++;
            }
            int dist_y = col_diff + col_count * (expansion_coeff - 1);
            total += dist_x + dist_y;
        }
    }
    return total;
}

void part1() {
    std::ifstream file("input.txt");
    std::string line;
    
    std::vector<std::vector<char>> grid;
    while (std::getline(file, line)) {
        std::vector<char> row;
        for (int i = 0; i < line.size(); i++) {
            row.push_back(line[i]);
        }
        grid.push_back(row);
    }
    int rows = grid.size();
    int cols = grid[0].size();

    std::vector<int> expansion_rows;
    for (int i = 0; i < rows; i++) {
        bool is_expansion_row = true;
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '#') {
                is_expansion_row = false;
                break;
            }
        }
        if (is_expansion_row) {
            expansion_rows.push_back(i);
        }
    }

    std::vector<int> expansion_cols;
    for (int j = 0; j < cols; j++) {
        bool is_expansion_col = true;
        for (int i = 0; i < rows; i++) {
            if (grid[i][j] == '#') {
                is_expansion_col = false;
                break;
            }
        }
        if (is_expansion_col) {
            expansion_cols.push_back(j);
        }
    }

    std::vector<std::pair<int, int>> galaxies;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++){
            if (grid[i][j] == '#') {
                galaxies.push_back(std::make_pair(i, j));
            }
        }
    }

    int expansion_coeff = 2;
    long long int total = solve(expansion_coeff, expansion_rows, expansion_cols, galaxies);
    std::cout << total << std::endl;
}


void part2() {
    std::ifstream file("input.txt");
    std::string line;
    
    std::vector<std::vector<char>> grid;
    while (std::getline(file, line)) {
        std::vector<char> row;
        for (int i = 0; i < line.size(); i++) {
            row.push_back(line[i]);
        }
        grid.push_back(row);
    }
    int rows = grid.size();
    int cols = grid[0].size();

    std::vector<int> expansion_rows;
    for (int i = 0; i < rows; i++) {
        bool is_expansion_row = true;
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '#') {
                is_expansion_row = false;
                break;
            }
        }
        if (is_expansion_row) {
            expansion_rows.push_back(i);
        }
    }

    std::vector<int> expansion_cols;
    for (int j = 0; j < cols; j++) {
        bool is_expansion_col = true;
        for (int i = 0; i < rows; i++) {
            if (grid[i][j] == '#') {
                is_expansion_col = false;
                break;
            }
        }
        if (is_expansion_col) {
            expansion_cols.push_back(j);
        }
    }

    std::vector<std::pair<int, int>> galaxies;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++){
            if (grid[i][j] == '#') {
                galaxies.push_back(std::make_pair(i, j));
            }
        }
    }

    int expansion_coeff = 1000000;
    long long int total = solve(expansion_coeff, expansion_rows, expansion_cols, galaxies);
    std::cout << total << std::endl;
}

int main() {
    part1();
    part2();
    return 0;
}