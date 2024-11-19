# Python Code
def calculate_stats(numbers):
    """
    Calculate the mean and standard deviation of a list of numbers.
    Returns a dictionary with mean and standard deviation.
    """
    from statistics import mean, stdev  # Import required modules
    mean_value = mean(numbers)
    std_dev = stdev(numbers)
    return {"mean": mean_value, "std_dev": std_dev}

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = calculate_stats(numbers)
print(f"Python Result: {stats}")

