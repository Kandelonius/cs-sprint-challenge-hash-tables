def get_indices_of_item_weights(weights, length, limit):
    totals = {}
    count = 0
    # What if we store each weight in the input list as keys? What would be a
    # useful thing to store as the value for each key?
    for num in weights:
        # if num == limit:
        #     return num
        if (limit - num) in totals:
            result = (count, (totals[limit - num]))
            return result
        totals[num] = count
        count += 1
    # print(totals)
    return None
weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))