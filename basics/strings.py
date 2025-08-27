# Python Strings Concepts with Examples

# 1. Creating Strings
str1 = 'Hello'
str2 = "World"
print("String 1:", str1)
print("String 2:", str2)

# 2. String Concatenation
str3 = str1 + " " + str2
print("Concatenated String:", str3)

# 3. String Repetition
print("Repeated String:", str1 * 3)

# 4. Accessing Characters (Indexing)
print("First character of str1:", str1[0])
print("Last character of str2:", str2[-1])

# 5. Slicing Strings
print("First 3 characters of str1:", str1[0:3])
print("Characters from index 1 to end:", str2[1:])

# 6. String Length
print("Length of str3:", len(str3))

# 7. String Methods
sample = "python programming"
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Title Case:", sample.title())
print("Capitalized:", sample.capitalize())
print("Count 'p':", sample.count('p'))
print("Find 'program':", sample.find('program'))
print("Replace 'python' with 'java':", sample.replace('python', 'java'))
print("Check startwith 'py':", sample.startswith('py'))
print("Check endswith 'ing':", sample.endswith('ing'))

# 8. Splitting and Joining
words = sample.split()  # Split into list
print("Split words:", words)
joined = '-'.join(words)  # Join list with '-'
print("Joined words:", joined)

# 9. Stripping Whitespaces
text = "   hello world   "
print("Stripped text:", text.strip())

# 10. Escaping Characters
print("He said, \"Hello\" to me.")
print('It\'s a beautiful day.')

# 11. Raw Strings
path = r"C:\Users\Admin\Documents"
print("Raw path:", path)

# 12. Multiline Strings
multiline = '''This is line 1
This is line 2
This is line 3'''
print("Multiline string:\n", multiline)

# 13. String Formatting
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")  # f-string formatting
print("Name: {}, Age: {}".format(name, age))

# 14. Reversing a String
original = "Python"
reversed_str = original[::-1]
print("Original String:", original)
print("Reversed String:", reversed_str)

# 15. String Comparison and Membership Checks
str_a = "apple"
str_b = "banana"
print("Is str_a equal to str_b?", str_a == str_b)
print("Is str_a not equal to str_b?", str_a != str_b)
print("Is 'a' in str_a?", 'a' in str_a)
print("Is 'z' not in str_b?", 'z' not in str_b)
