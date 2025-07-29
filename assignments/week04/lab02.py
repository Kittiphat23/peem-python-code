def number_operations():
    numbers = []
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input(f"Insert number[{i}]: "))
        numbers.append(number)

    print(f"\nOriginal numbers: {numbers}")

    even_numbers = []
    odd_numbers = []
    average = sum(numbers) / len(numbers)
    above_average = []

    for i in range(10):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])
        if numbers[i] > average:
            above_average.append(numbers[i])

    print("\nEven Number List:", even_numbers)
    print("Odd Number List:", odd_numbers)
    print("Above Average:", above_average)
    print("Sum:", sum(numbers))
    print("Average:", average)
    print("Min:", min(numbers))
    print("Max:", max(numbers))

if __name__ == "__main__":
    number_operations()
