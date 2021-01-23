def get_indices_of_item_weights(weights, length, limit):
    dictionary = {}
    
    for i in range(0, length - 1):
        for j in range(0, length - 1):
            key = (i, j)
            reverseKey = (j, i)
            if key not in dictionary and reverseKey not in dictionary:
                dictionary[key] = weights[i] + weights[j]
                
    for key in dictionary:
        if dictionary[key] == limit:
            if key == (0,0):
                key = (1,0)
                return key
            else:
                return (key[1], key[0])
        
