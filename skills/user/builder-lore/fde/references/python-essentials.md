# Python Essentials
# Only what an FDE needs. No theory, just patterns.
## Variables and types
```python
name = "Ander"          # string
count = 42              # integer
price = 9.99            # float
is_active = True        # boolean
nothing = None          # null equivalent
```
## Functions
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
result = greet("Ander")  # "Hello, Ander"
```
## Loops
```python
items = ["a", "b", "c"]
for item in items:
    print(item)
# Loop with index
for i, item in enumerate(items):
    print(i, item)
```
## List comprehension (filter + transform in one line)
```python
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]   # [2, 4]
doubled = [n * 2 for n in numbers]            # [2, 4, 6, 8, 10]
```
## Dictionaries
```python
user = {"name": "Ander", "role": "designer"}
user["name"]              # "Ander"
user["email"] = "a@b.com" # add key
user.get("missing", "default")  # safe access
# Loop through
for key, value in user.items():
    print(key, value)
```
## Error handling
```python
try:
    result = risky_function()
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    print("Always runs")
```
## Reading and writing files
```python
# Read
with open("file.txt", "r") as f:
    content = f.read()
# Write
with open("output.txt", "w") as f:
    f.write("Hello")
# JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```
## f-strings (string formatting)
```python
name = "Ander"
count = 5
print(f"Hello {name}, you have {count} items")
print(f"Price: {9.99:.2f}")   # 2 decimal places
```
