# 说明:冒泡排序算法
def bubbleSort(array: list[int]) -> None:
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def main():
    list_a = [1,33,24,6,10,100]
    bubbleSort(list_a)
    print(list_a)

if __name__ == "__main__":
    main()    
