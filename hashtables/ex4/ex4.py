
def has_negatives(a):
    values = {}
    result = []
    # print(a)
    for num in a:
        if abs(num) not in values:
            values[abs(num)] = 0
        values[abs(num)] += 1
        if values[abs(num)] > 1:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
