#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>


void part1() {
    std::ifstream file("input.txt");
    std::string line;
    int sum = 0;
    std::vector<std::vector<char>> grid;
    while (std::getline(file, line)) {
        std::vector<char> row;
        for (int i = 0; i < line.length(); i++) {
            row.push_back(line[i]);
        }
        grid.push_back(row);
    }
    for (int row_ind = 0; row_ind < grid.size(); row_ind++) {
        int col_ind = 0;
        bool num_flag = false;
        int num_start;
        while (col_ind < grid[row_ind].size() + 1) {
            if (col_ind < grid[row_ind].size() && isdigit(grid[row_ind][col_ind]) && !num_flag){
                num_start = col_ind;
                num_flag = true;
            }
            else if (num_flag && ((col_ind < grid[row_ind].size() && !isdigit(grid[row_ind][col_ind])) || (col_ind == grid[row_ind].size()))) {
                int num_end = col_ind;
                num_flag = false;
                for (int i = num_start; i < num_end; i++) {
                    for (int adj_row = std::max(0, row_ind - 1); adj_row <= std::min(row_ind + 1, (int)grid.size() - 1); adj_row++) {
                        for (int adj_col = std::max(0, i - 1); adj_col <= std::min(i + 1, (int)grid[adj_row].size() - 1); adj_col++) {
                            if (!isdigit(grid[adj_row][adj_col]) && (grid[adj_row][adj_col] != '.')) {
                                std::string num_str = "";
                                for (int i = num_start; i < num_end; i++) {
                                    num_str += grid[row_ind][i];
                                }
                                sum += std::stoi(num_str);
                                i = num_end + 1;
                                adj_row = row_ind + 1;
                                adj_col = i + 1;
                            }
                        }
                    }
                }
            }
            col_ind++;
        }
    }
    std::cout << sum << std::endl;
}


void part2() {
    std::ifstream file("input.txt");
    std::string line;
    int sum = 0;
    std::vector<std::vector<char>> grid;
    while (std::getline(file, line)) {
        std::vector<char> row;
        for (int i = 0; i < line.length(); i++) {
            row.push_back(line[i]);
        }
        grid.push_back(row);
    }
    int row_ind = 0;
    while (row_ind < grid.size()) {
        int col_ind = 0;
        std::vector<char> row = grid[row_ind];
        while (col_ind < row.size()) {
            if (row[col_ind] == '*') {
                std::vector<int> adj_nums;
                for (int adj_row = std::max(0, row_ind - 1); adj_row <= std::min(row_ind + 1, (int)grid.size() - 1); adj_row++) {
                    int i = 0;
                    std::vector<char> adj_row_vec = grid[adj_row];
                    bool num_flag = false;
                    int num_start;
                    while (i < adj_row_vec.size() + 1) {
                        if (i < adj_row_vec.size() && isdigit(adj_row_vec[i]) && !num_flag){
                            num_start = i;
                            num_flag = true;
                        }
                        else if (num_flag && ((i < adj_row_vec.size() && !isdigit(adj_row_vec[i])) || (i == adj_row_vec.size()))) {
                            int num_end = i;
                            num_flag = false;
                            if ((num_start <= col_ind + 1) && (num_end >= col_ind)) {
                                int num_length = num_end - num_start;
                                std::string num_str = "";
                                for (int j = num_start; j < num_end; j++) {
                                    num_str += adj_row_vec[j];
                                }
                                int num = std::stoi(num_str);
                                adj_nums.push_back(num);
                                if (adj_nums.size() > 2) {
                                    i = adj_row_vec.size() + 2;
                                    adj_row = row_ind + 2;
                                }
                            }
                        }
                        i++;
                    }
                }
                if (adj_nums.size() == 2) {
                    sum += adj_nums[0] * adj_nums[1];
                }
            }
            col_ind++;
        }
        row_ind++;
    }
    std::cout << sum << std::endl;
}


int main() {
    part1();
    part2();
    return 0;
}