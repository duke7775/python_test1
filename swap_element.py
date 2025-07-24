#说明：元素对调

def swap_list(list_a, index0, index1) -> list:
    if not isinstance(index0, int) or not isinstance(index1, int):
        raise TypeError("索引必须是整数类型")
    if index0 >= len(list_a) or index1 >= len(list_a):
        raise ValueError(f"索引越界: {index0} or {index1} is out of range for the list.")
    list_a[index0], list_a[index1] = list_a[index1], list_a[index0]
    return list_a

def swap_dict(dict_a, index0, index1) -> dict:
    if not isinstance(index0, int) or not isinstance(index1, int):
        raise TypeError("索引必须是整数类型")
    if index0 >= len(dict_a) or index1 >= len(dict_a):
        raise ValueError(f"索引越界: {index0} or {index1} is out of range for the dictionary.")
    sorted_keys = sorted(dict_a.keys())
    key0 = sorted_keys[index0]
    key1 = sorted_keys[index1]
    dict_a[key0], dict_a[key1] = dict_a[key1], dict_a[key0]
    return dict_a

def main():
    list_a =  [1,33,24,6,10]
    print("Original list:", list_a)
    print("Swapped list:", swap_list(list_a, 3, 4))

    dict_a = {"0":"value0","1":1,"2":"value2","3":"value3","4":"value4"}
    print("Original dict:", dict_a)
    print("Swapped dict:", swap_dict(dict_a, 1, 4))


if __name__ == "__main__":
    main()