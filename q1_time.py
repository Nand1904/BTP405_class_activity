import time

def timer(func):
  """Decorator function that calculates the time taken for a function to execute and prints the duration."""
  def wrapper(*args, **kwargs):
    start_time = time.time()  # Record the current time before executing the function.
    result = func(*args, **kwargs)  # Execute the function with provided arguments.
    end_time = time.time()  # Record the current time after executing the function.
    duration = end_time - start_time  # Calculate the duration by subtracting start time from end time.
    print(f"Function '{func.__name__}' executed in {duration:.6f} seconds")  # Print the duration of execution.
    return result  # Return the result of the function execution.
  return wrapper  # Return the wrapper function.

@timer  # Apply the timer decorator to the following function.
def my_function(n):
  """Example function that takes some time to execute."""
  result = 0
  for i in range(n):  # Iterate through the range from 0 to n.
    result += i**2  # Add the square of the current number to the result.
  return result  # Return the final result.

# Call the decorated function.
result = my_function(6969)  # Call the function with an argument.
print(f"Result: {result}")  # Print the result returned by the function.