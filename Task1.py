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
