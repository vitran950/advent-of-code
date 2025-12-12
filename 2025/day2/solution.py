from typing import List

def parse_input(file_path):
    with open(file_path) as f:
        return [item for line in f for item in line.strip().split(",")]
    
def detect_invalid_id(ids: List[str]) -> int:
    count = 0
    # split by the "," delimiter
    for id in ids:
        ranges = id.split("-")
        # assumption that we'll only have 2 elements
        first = int(ranges[0])
        last = int(ranges[1])
        for i in range(first, last + 1):
            # convert the number to string
            text_num = str(i)
            if len(text_num) % 2 == 0:
                mid = len(text_num) // 2
                first_half = text_num[:mid]
                second_half = text_num[mid:]
                if first_half == second_half:
                    count += i
    return count

def detect_invalid_id2(ids: List[str]) -> int:
    count = 0
    # split by the "," delimiter
    for id in ids:
        ranges = id.split("-")
        # assumption that we'll only have 2 elements
        first = int(ranges[0])
        last = int(ranges[1])
        for i in range(first, last + 1):
            text_num = str(i)
            n = len(text_num)
            # iterate first char -> mid (no point checking the rest)
            for j in range(1, (n // 2) + 1):
                # check if there's any potentials of spaces required to have duplicates
                if n % j == 0:
                    pattern = text_num[:j]
                    # take pattern and take product of the spaces required to create text with same length
                    if pattern * (n // j) == text_num:
                        count += i
                        # need to break out to avoid potentially adding same values
                        break
    return count

if __name__ == "__main__":
    test_data = parse_input("input_test.txt")
    test_ans = detect_invalid_id(test_data)
    print(test_ans)

    data = parse_input("input.txt")
    ans1 = detect_invalid_id(data)
    print(ans1)

    test_ans2 = detect_invalid_id2(test_data)
    print(test_ans2)

    ans2 = detect_invalid_id2(data)
    print(ans2)