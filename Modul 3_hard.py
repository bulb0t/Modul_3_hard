def inside_data(data_set):
    if isinstance(data_set, dict):
        return dict_data(data_set)
    else:
        return internal_data(*data_set)

def internal_data(*args):
    count = 0
    for arg in args:
        if isinstance(arg, str):
            count += len(arg)
        elif isinstance(arg, int):
            count += arg
        else:
            count += inside_data(arg)
    return count

def dict_data(dict_):
    count = 0
    for keys in dict_.keys():
        count += len(keys)
    for values in dict_.values():
        if isinstance(values, int):
            count += values
        elif isinstance(values, str):
            count += len(values)
        else:
            count += inside_data(values)
    return count

def calculate_structure_sum(data_set):
    if isinstance(data_set[0], str):
        if len(data_set) > 1:
            return len(data_set[0]) + calculate_structure_sum(data_set[1:])
        else:
            len(data_set[0])
    elif isinstance(data_set[0], int):
        if len(data_set) > 1:
            return data_set[0] + calculate_structure_sum(data_set[1:])
        else:
            return data_set[0]
    elif isinstance(data_set[0], dict):
        if len(data_set) > 1:
            return dict_data(data_set[0]) + calculate_structure_sum(data_set[1:])
        else:
            dict_data(data_set[0])
    else:
        if len(data_set) > 1:
            return internal_data(*data_set[0]) + calculate_structure_sum(data_set[1:])
        else:
            return internal_data(*data_set[0])

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))