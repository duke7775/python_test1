#功能：线性查找
def lineSearch(list_a, target) -> int:
    for i in range(len(list_a)):
        if list_a[i] == target:
            print(f"found target {target} at index {i}")
            return i
    print(f"target {target} not found")
    return -1
def main():
    list_a = [1,888,5,100,33,999]
    target = 33
    lineSearch(list_a, target)
    target = 34
    lineSearch(list_a, target)
if __name__ == "__main__":
    main()    