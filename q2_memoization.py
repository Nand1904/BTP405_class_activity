def memoize(func):
  """Decorator that caches function results for specific arguments."""
  cache = {}  # Initialize an empty dictionary to store cached results.

  def wrapper(*args, **kwargs):
    """Wrapper function that checks the cache and calls the original function if needed."""
    key = (args, tuple(kwargs.items()))  # Create a unique key based on function arguments and keyword arguments.
    if key not in cache:  # Check if the key is not present in the cache.
      cache[key] = func(*args, **kwargs)  # Call the original function and store the result in the cache.
    return cache[key]  # Return the cached result.

  return wrapper  # Return the wrapper function.

@memoize  # Apply the memoize decorator to the following function.
def fibonacci(n):
  """Calculates the nth Fibonacci number."""
  if n <= 1:  # Base case: if n is 0 or 1, return n.
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)  # Recursively call fibonacci function for previous numbers and sum them.

# Calculate and print the 40th Fibonacci number
result = fibonacci(69)  # Call the fibonacci function with argument 40.
print(f"The 40th Fibonacci number is: {result}")  # Print the result.