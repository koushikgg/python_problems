def max_min_values(set):
    maxi_value = max(set)
    mini_value = min(set)

    return maxi_value, mini_value

if __name__ == '__main__':
    sample_set = {1,4,2,6,8,9}

    maxi, mini = max_min_values(sample_set)
    print(f"Max value in set: {maxi}")
    print(f"Min value in set: {mini}")