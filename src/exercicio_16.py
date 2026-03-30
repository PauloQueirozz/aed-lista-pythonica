def odd_numbers(n: int) -> list[int]:
    list = []
    for i in range(n + 1):
        if i % 2 != 0:
            list.append(i)
    return list
