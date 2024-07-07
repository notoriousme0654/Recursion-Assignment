def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
string = "hello"
print(f"The reverse of '{string}' is '{reverse_string(string)}'")
