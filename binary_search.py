#说明：二分查找
def binary_search(nums: list,target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2 
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            print(f"found target {target} at index {mid}")
            return mid
        print("i:", i, "j:", j, "mid:", mid, "nums[mid]:", nums[mid])
    print("did not find")    
    return -1

def reverse_string(s: str) -> str:
    new_str = ""
    for i in range(len(s) - 1, -1, -1):
        new_str += s[i]
    print(new_str)

def main():
    list_a = [1,5,10,33,100,999]
    target = 33
    binary_search(list_a, target)
    target = 34
    binary_search(list_a, target)
    str = "hello world"
    reverse_string(str)


if __name__ == "__main__":
    main()    
      