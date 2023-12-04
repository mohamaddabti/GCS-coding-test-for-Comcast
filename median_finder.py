def sort(numbers):
    # Implementing bubble sort for simplicity
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def sortAndFindMedian(numbers):
    sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

# User interface to input array of numbers
if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by space: ")
    numbers = [int(item) for item in user_input.split()]
    median = sortAndFindMedian(numbers)
    print(f"The median is: {median}")
