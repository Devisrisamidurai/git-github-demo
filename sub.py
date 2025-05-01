# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Test the subtraction functionality
if __name__ == "__main__":
    print("Welcome to the Calculator Program!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = subtract(num1, num2)
    
    print(f"The result of {num1} - {num2} is {result}")
