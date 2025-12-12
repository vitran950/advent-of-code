# 🎄 Advent of Code Solutions

**Victor T's Collection of Advent of Code Challenges & Solutions**

## 📝 About

This repository contains solutions and implementations for **Advent of Code** challenges.

## 📂 Structure

```
advert-of-code/
├── 2025/                    # Year folder
│   ├── day1/               # Individual day challenge
│   │   ├── README.md       # Challenge description & notes
│   │   ├── solution.py     # Python solution
│   │   ├── input.txt       # Main puzzle input
│   │   └── input_test.txt  # Test/example input
│   ├── day2/
│   └── ...
├── 2024/
└── README.md               
```

## 🚀 Quick Start

### Prerequisites

- [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
- No other dependencies - just vanilla python libraries

### How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/vitran950/advent-of-code.git
   cd advert-of-code
   ```

2. **Navigate to a specific day and year**
   ```bash
   cd 2025/day1
   ```

3. **Run the solution**
   ```bash
   python solution.py
   ```

### Adding a New Day

1. Create a new folder: `mkdir 2025/dayX`
2. Create `solution.py` with the following template:
   ```python
   def solve(input_file: str):
       with open(input_file) as f:
           lines = f.read().strip().split('\n')
       
       # Part 1
       part1_result = None
       
       # Part 2
       part2_result = None
       
       print(f"Part 1: {part1_result}")
       print(f"Part 2: {part2_result}")
   
   if __name__ == "__main__":
       import sys
       input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
       solve(input_file)
   ```
3. Add `input_test.txt` with the example from the challenge
4. Create a `README.md` with your notes
