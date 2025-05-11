from pathlib import Path


# Count pairs
def count_valid_pairs(ratings, k):
    ratings.sort()
    left = 0
    right = len(ratings) - 1
    count = 0

    used = [False] * len(ratings)

    while left < right:
        if used[left]:
            left += 1
            continue
        if used[right]:
            right -= 1
            continue
        if ratings[left] + ratings[right] >= k:
            count += 1
            used[left] = True
            used[right] = True
            left += 1
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
