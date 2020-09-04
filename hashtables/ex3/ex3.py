
def intersection(arrays):
    storage = {}
    result = []
    # print(len(arrays))
    for list in arrays:
        # print(item)
        for num in list:
            if num not in storage:
                storage[num] = 0
            storage[num] += 1
            if storage[num] == len(arrays):
                result.append(num)
                print(f"num is {num}")
    print(f"result is {result}")

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
