# R Code
calculate_stats <- function(numbers) {
  # Calculate the mean and standard deviation of a vector
  mean_value <- mean(numbers)
  std_dev <- sd(numbers)
  return(list(mean = mean_value, std_dev = std_dev))
}

# Example usage
numbers <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
stats <- calculate_stats(numbers)
cat("R Result:\n")
print(stats)
