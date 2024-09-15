def main():
    a, b = map(int, input("Введите два целых числа (через пробел): ").split())
    if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
        
        result = a + b
        
        print("Сумма:", result)
    else:
        
        print("Ввод вне допустимого диапазона (-10^9 <= a, b <= 10^9)")
        
if __name__ == "__main__":
    main()
