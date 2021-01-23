def intersection(arrays):
    dictionary = {}
    result = []
    dictionary_arr = arrays[0]
    
    for value in dictionary_arr:
        if value not in dictionary:
            dictionary[value] = value
    i = 0
    while i < (len(arrays) - 1):
        for value in arrays[i + 1]:
            if value in dictionary and value not in result:
                result.append(value)
        i += 1
    return result
           

if __name__ == "__main__":
    arrays = []
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [12, 7, 2, 9, 1]
    arr3 = [99, 2, 7, 1]

    arrays.append(arr1)
    arrays.append(arr2)
    arrays.append(arr3)
    print(intersection(arrays))
