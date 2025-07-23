#说明：元素对调

def swap_list(list_a, index0, index1) -> list:
    list_a[index0], list_a[index1] = list_a[index1], list_a[index0]
    return list_a

def swap_dict(dict_a,index0 , index1) -> dict:
    dict_a[index0], dict_a[index1] = dict_a[index1], dict_a[index0]
    return dict_a

def main():
    list_a =  [1,33,24,6,10]
    print("Original list:", list_a)
    print("Swapped list:", swap_list(list_a, 2, 4))

    dict_a = {"0":"value0","1":1,"2":"value2","3":"value3","4":"value4"}
    print("Original dict:", dict_a)
    print("Swapped dict:", swap_dict(dict_a, '2', '4'))


if __name__ == "__main__":
    main()