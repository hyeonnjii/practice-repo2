def adder_twoNum(num1:int, num2:int) -> int:
    return num1 + num2

if __name__ == '__main__':
    get_nums = input("Enter the integer numbers(using seperator ','): ").replace(' ', '').split(',')
    
    # strip은 인자 1개를 주로 사용, replace 는 여러개로 사용가능!
    num1, num2 = map(int, get_nums)
    print(add_twoNum(num1, num2))

    
