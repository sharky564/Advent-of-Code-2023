#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>

std::vector<std::pair<int, int>> adjacent(std::vector<std::vector<char>>& grid, std::pair<int, int> node) {
    char pipe = grid[node.first][node.second];
    std::vector<std::pair<int, int>> adjacent_nodes;
    switch (pipe) {
        case 'F':
            adjacent_nodes = {{node.first, node.second + 1}, {node.first + 1, node.second}};
            break;
        case '-':
            adjacent_nodes = {{node.first, node.second + 1}, {node.first, node.second - 1}};
            break;
        case '7':
            adjacent_nodes = {{node.first + 1, node.second}, {node.first, node.second - 1}};
            break;
        case '|':
            adjacent_nodes = {{node.first + 1, node.second}, {node.first - 1, node.second}};
            break;
        case 'J':
            adjacent_nodes = {{node.first, node.second - 1}, {node.first - 1, node.second}};
            break;
        case 'L':
            adjacent_nodes = {{node.first, node.second + 1}, {node.first - 1, node.second}};
            break;
        default:
            adjacent_nodes = {};
            break;
    }
    return adjacent_nodes;
}

std::vector<std::pair<int, int>> find_loop(
    std::vector<std::vector<char>>& grid,
    std::pair<int, int> start
) {
    int length = grid.size();
    int height = grid[0].size();
    std::vector<std::pair<int, int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    for (auto &direction : directions) {
        bool valid = true;
        std::vector<std::pair<int, int>> loop = {start};
        if (0 <= start.first + direction.first && start.first + direction.first < length &&
            0 <= start.second + direction.second && start.second + direction.second < height) {
            std::pair<int, int> next = {start.first + direction.first, start.second + direction.second};
            if (find(adjacent(grid, next).begin(), adjacent(grid, next).end(), start) != adjacent(grid, next).end()) {
                loop.push_back(next);
                std::pair<int, int> prev_node = start;
                std::pair<int, int> curr_node = next;
                while (curr_node != start) {
                    std::pair<int, int> next_node;
                    bool found = false;
                    for (auto node : adjacent(grid, curr_node)) {
                        if (node != prev_node) {
                            next_node = node;
                            loop.push_back(next_node);
                            prev_node = curr_node;
                            curr_node = next_node;
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    return loop;
                }
            }
        }
    }
    return {};
}


void part1() {
    std::ifstream file("input.txt");
    std::string line;
    
    std::pair<int, int> start;
    std::vector<std::vector<char>> grid;
    while (std::getline(file, line)) {
        std::vector<char> row;
        for (int i = 0; i < line.size(); i++) {
            row.push_back(line[i]);
            if (line[i] == 'S') {
                start = {grid.size(), i};
            }
        }
        grid.push_back(row);
    }

    std::vector<std::pair<int, int>> loop = find_loop(grid, start);
    std::cout << loop.size()/2 << std::endl;
}


void part2() {
    std::ifstream file("input.txt");
    std::string line;
    
    std::pair<int, int> start;
    std::vector<std::vector<char>> grid;
    while (std::getline(file, line)) {
        std::vector<char> row;
        for (int i = 0; i < line.size(); i++) {
            row.push_back(line[i]);
            if (line[i] == 'S') {
                start = {grid.size(), i};
            }
        }
        grid.push_back(row);
    }

    std::vector<std::pair<int, int>> loop = find_loop(grid, start);
    // replace all non-loop nodes with '.'
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (find(loop.begin(), loop.end(), std::pair<int, int>{i, j}) == loop.end()) {
                grid[i][j] = '.';
            }
        }
    }

    // replace 'S' with appropriate pipe
    std::pair<int, int> prev_node = loop[loop.size() - 2];
    std::pair<int, int> curr_node = loop[0];
    std::pair<int, int> next_node = loop[1];
    std::pair<int, int> next_direction = {next_node.first - curr_node.first, next_node.second - curr_node.second};
    std::pair<int, int> prev_direction = {prev_node.first - curr_node.first, prev_node.second - curr_node.second};
    char pipe;
    if (next_direction.first == 1 && next_direction.second == 0) {
        if (prev_direction.first == 0 && prev_direction.second == 1) {
            pipe = 'F';
        } 
        else if (prev_direction.first == 0 && prev_direction.second == -1) {
            pipe = '7';
        }
        else {
            pipe = '|';
        }
    } 
    else if (next_direction.first == 0 && next_direction.second == 1) {
        if (prev_direction.first == 1 && prev_direction.second == 0) {
            pipe = 'F';
        } 
        else if (prev_direction.first == -1 && prev_direction.second == 0) {
            pipe = 'L';
        }
        else {
            pipe = '-';
        }
    } 
    else if (next_direction.first == -1 && next_direction.second == 0) {
        if (prev_direction.first == 0 && prev_direction.second == 1) {
            pipe = 'L';
        } 
        else if (prev_direction.first == 0 && prev_direction.second == -1) {
            pipe = 'J';
        }
        else {
            pipe = '|';
        }
    } 
    else if (next_direction.first == 0 && next_direction.second == -1) {
        if (prev_direction.first == 1 && prev_direction.second == 0) {
            pipe = '7';
        } 
        else if (prev_direction.first == -1 && prev_direction.second == 0) {
            pipe = 'J';
        }
        else {
            pipe = '-';
        }
    }
    grid[start.first][start.second] = pipe;

    int interior = 0;
    for (auto row : grid) {
        int num_loop_pipes = 0;
        for (auto node : row) {
            if (node == '|' || node == 'L' || node == 'J') {
                num_loop_pipes++;
            }
            if (node == '.' && num_loop_pipes % 2 == 1) {
                interior++;
            }
        }
    }
    std::cout << interior << std::endl;
}

int main() {
    part1();
    part2();
    return 0;
}