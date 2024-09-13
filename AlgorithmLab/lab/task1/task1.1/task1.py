def main():
   
    a, b = map(int, input("Enter two integers (separated by space): ").split())

    
    if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
        
        result = a + b
        
        print("The sum is:", result)
    else:
        
        print("Input is out of the allowed range (-10^9 <= a, b <= 10^9)")


if __name__ == "__main__":
    main()