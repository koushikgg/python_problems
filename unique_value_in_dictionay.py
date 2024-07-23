def unique_values(dict):
    unique_value_set = set()
    for d in dict:
        for value in d.values():
            unique_value_set.add(value)
    return unique_value_set

if __name__ == '__main__':
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                   {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    result = unique_values(sample_data)
    print("Unique Values:", result)