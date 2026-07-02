def reverse_string(input_string: str) -> str:
    res = ""
    for i in reversed(range(0, len(input_string))):
        res+=(input_string[i])
    return res

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
