def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
string1 = "radar"
string2 = "hello"
print(f"Is '{string1}' a palindrome? {is_palindrome(string1)}")
print(f"Is '{string2}' a palindrome? {is_palindrome(string2)}")
