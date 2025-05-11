from pathlib import Path


# Count pairs
def count_valid_pairs(scores, k):
    scores.sort()
    n = len(scores)
    count = 0
    left = 0
    right = n - 1

    while left < right:
        if scores[left] + scores[right] >= k:
            count += right - left
            right -= 1
        else:
            left += 1

    return count


# Read file
def process_file(filename):
    with open(filename, 'r') as f:
        n, k = map(int, f.readline().split())
        ratings = [int(f.readline()) for _ in range(n)]
    return count_valid_pairs(ratings, k)


# Main
if __name__ == "__main__":
    current_folder = Path(__file__).resolve().parent / 'Files'

    result_test = process_file(current_folder / "Test1.txt")
    result_a = process_file(current_folder / "27-169b.txt")
    result_b = process_file(current_folder / "27-169bb.txt")

    print(f"Result Test: {result_test}, Result A: {result_a}, Result B: {result_b}")
