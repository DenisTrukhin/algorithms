def chanceOfMeatballPrecipitations(gene: str, k: int) -> float:
    if k > len(gene):
        return 0

    all_substrings_count = len(gene) - k + 1
    unique_count = 0
    chars_count = [0] * 26
    for c in gene[:k - 1]:
        chars_count[ord(c) - ord("a")] += 1
    i = k - 1
    while i < len(gene):
        chars_count[ord(gene[i]) - ord("a")] += 1
        if all(c in {0, 1} for c in chars_count):
            unique_count += 1
        chars_count[ord(gene[i - (k - 1)]) - ord("a")] -= 1
        i += 1
    return unique_count / all_substrings_count


test_cases = [
    ("aaaaaa", 4, 0),
    ("ababcdaa", 3, 0.5),
    ("ab", 5, 0),
    ("ab", 1, 1),
]

if __name__ == "__main__":
    for gene, k, expected in test_cases:
        actual = chanceOfMeatballPrecipitations(gene, k)
        assert actual == expected, (gene, k, expected, actual)
