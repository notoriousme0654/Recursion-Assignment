def length_of_string(s):
    if s == "":
        return 0
    else:
        return 1 + length_of_string(s[1:])
string = "hello"
print(f"The length of '{string}' is {length_of_string(string)}")
