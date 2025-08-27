# Python Dictionary Concepts with Examples

# Dictionary is an unordered collection of key-value pairs

# 1. Creating a Dictionary
details = {"name": "Alice", "age": 25, "city": "Paris"}
print("Dictionary:", details)

# 2. Accessing Elements
print("Name:", details["name"])  # Access value using key
print("Age using get():", details.get("age"))  # safer way

# 3. Adding/Updating Elements
details["email"] = "alice@example.com"  # Add new key-value
print("After adding email:", details)
details["age"] = 26  # Update value
print("After updating age:", details)

# 4. Removing Elements
removed = details.pop("city")  # Remove key and return value
print("Removed city:", removed)
print("After removing city:", details)

popped_item = details.popitem()  # Removes last inserted item
print("Popped item:", popped_item)

# 5. Checking Membership
if "name" in details:
    print("Name key exists")

# 6. Dictionary Methods
keys = details.keys()
values = details.values()
items = details.items()
print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# 7. Iterating Over Dictionary
for key, value in details.items():
    print(f"{key}: {value}")

# 8. Copying Dictionary
copy_details = details.copy()
print("Copy of dictionary:", copy_details)

# 9. Clearing Dictionary
# details.clear()
# print("After clearing:", details)

# 10. Nested Dictionary
students = {
    "student1": {"name": "Bob", "age": 20},
    "student2": {"name": "Carol", "age": 22}
}
print("Nested Dictionary:", students)

# 11. Using fromkeys()
keys_list = ["a", "b", "c"]
new_dict = dict.fromkeys(keys_list, 0)  # all values set to 0
print("Dictionary from keys:", new_dict)

# 12. Using setdefault()
details.setdefault("phone", "1234567890")  # add key if not exists
print("After setdefault:", details)
