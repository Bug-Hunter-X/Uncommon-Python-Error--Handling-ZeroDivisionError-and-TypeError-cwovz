def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

print(function_with_uncommon_error(0))  # Output: Division by zero
print(function_with_uncommon_error(2))  # Output: 5.0
print(function_with_uncommon_error('a')) # Output: Invalid input type
print(function_with_uncommon_error(0.0)) # Output:Division by zero