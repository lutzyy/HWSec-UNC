def dict_adder(dict):
    # takes dict input and returns same dict with the sum of values as last index
    total = 0
    for key in dict:
        total += dict[key]
    dict["total"] = total
    print(total)
    print(dict)
    return total

def dict_adder(dict, null_value = None):
    # overlaoded dict_adder for when values are None
    total = 0
    for key in dict:
        if dict[key] is not None:
            total += dict[key]
    dict["total"] = total
    print(total)
    print(dict)
    return total
