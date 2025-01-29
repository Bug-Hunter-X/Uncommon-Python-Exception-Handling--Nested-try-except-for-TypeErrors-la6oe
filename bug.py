def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            print("Type Error Occurred")
        else:
            raise
    else:
        return result

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Division by zero!
print(function_with_uncommon_error(10, "hello")) # Output: Type Error Occurred
print(function_with_uncommon_error("hello",2)) # Raises TypeError
