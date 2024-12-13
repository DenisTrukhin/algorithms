def select_goods(goods: list[int], needs: list[int]) -> int:
    goods.sort()
    needs.sort()
    result = 0
    p1 = p2 = 0
    while p1 < len(goods) and p2 < len(needs):
        cur_diff = abs(needs[p2] - goods[p1])
        if p1 + 1 < len(goods) and abs(needs[p2] - goods[p1 + 1]) < cur_diff:
            p1 += 1
        else:
            result += cur_diff
            p2 += 1
    return result


test_cases = [
    ([], [], 0),
    ([8, 3, 5, 7], [5, 6], 1),
    ([8, 3, 5, 7], [4, 6], 2),
    ([8, 3, 5, 7], [10, 9], 3),
    ([8, 3, 5, 7], [20, 30], 34),
    ([8, 4, 5, 7], [2, 1], 5),
    ([18, 11, 15, 17], [2, 1], 19),
    ([8, 4, 5, 7], [5, 4], 0),
]


if __name__ == "__main__":
    for goods, needs, expected in test_cases:
        actual = select_goods(goods, needs)
        assert actual == expected, (goods, needs, expected, actual)
