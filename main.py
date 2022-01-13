import re

test_string = '123abc456789abc123ABC'

# a = '\tHello'
# print(a)

# # r before a string is a raw string
# a = r'\tHello'
# print(a)

# matches = re.finditer(r"abc",test_string)
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)
# matches = pattern.findall(test_string)

for match in matches:
    print(match.group())

# match = pattern.match(test_string)
# match = pattern.search(test_string)

# print(match)



