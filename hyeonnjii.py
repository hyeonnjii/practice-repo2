def add_twoNum(num1:int, num2:int) -> int:
    return num1 + num2

if __name__ == '__main__':
    get_nums = input("Enter the integer numbers(using seperator ','): ").replace(' ', '').split(',')
    num1, num2 = map(int, get_nums)
    print(add_twoNum(num1, num2))

    
