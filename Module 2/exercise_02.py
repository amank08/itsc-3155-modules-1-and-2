user_string = input("Please enter a string: ")

lowercase_letters = [c for c in user_string if c.islower() and c !=' ']
uppercase_letters = [c for c in user_string if c.isupper() or c ==' ']

print(''.join(lowercase_letters) + ''.join(uppercase_letters))