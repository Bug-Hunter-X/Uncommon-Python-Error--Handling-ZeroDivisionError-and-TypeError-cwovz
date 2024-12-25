def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        if isinstance(x,(str,list,dict)):
            return "Invalid input type: String, List, or Dictionary"
        else:
            return "Invalid input type: Unsupported type"

print(function_with_uncommon_error(0))  # Output: Division by zero
print(function_with_uncommon_error(2))  # Output: 5.0
print(function_with_uncommon_error('a')) # Output: Invalid input type: String, List, or Dictionary
print(function_with_uncommon_error([1,2])) # Output: Invalid input type: String, List, or Dictionary
print(function_with_uncommon_error(0.0)) # Output: Division by zero