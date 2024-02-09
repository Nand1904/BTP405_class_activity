class UnauthorizedError(Exception):
    """Custom exception for unauthorized access."""
    pass

def authorize(username, password):
    """Decorator that authorizes access to a function based on provided credentials."""
    # Define the predefined username and password
    predefined_username = "admin"
    predefined_password = "password123"
    
    def decorator(func):
        """Inner decorator function that checks authorization before executing the function."""
        def wrapper(*args, **kwargs):
            """Wrapper function that verifies credentials and executes the original function if authorized."""
            # Check if provided credentials match predefined values
            if username == predefined_username and password == predefined_password:
                return func(*args, **kwargs)  # Execute the original function
            else:
                raise UnauthorizedError("Unauthorized access")  # Raise UnauthorizedError if credentials are invalid
        return wrapper  # Return the wrapper function
    return decorator  # Return the inner decorator function

# Example usage:
@authorize("admin", "password123")  # Apply the authorize decorator with predefined credentials
def my_authorized_function():
    """Example function requiring authorization."""
    return "Authorized access granted"

# Try executing the authorized function
try:
    result = my_authorized_function()  # Call the authorized function
    print(result)  # Print the result if access is granted
except UnauthorizedError as e:
    print(e)  # Print the error message if access is unauthorized