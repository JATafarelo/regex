import re

# test_string = '123abc456789abc123ABC'
# test_string = 'hello 123_ heyho hohey'
# test_string = 'helloHELLO 123-_'
# test_string = 'hello_123'

# a = '\tHello'
# print(a)

# # r before a string is a raw string
# a = r'\tHello'
# print(a)

text = """
Hello World!
123456789
2022-01-13

Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T

firsttest@gmail.com
second-test@gmx.de
third-test123@my-domain.org

"""

# pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s\w+')
# pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')

# matches = re.finditer(r"abc",test_string)

# match = pattern.match(test_string)
# match = pattern.search(test_string)

# print(match)

# matches = pattern.finditer(test_string)
# matches = pattern.findall(test_string)

# matches = pattern.finditer(text)

# for match in matches:
    # print(match.group(0))
    # print(match.group(1))
    # print(match.group(2))
    # print(match.group(3))

# test = '123abc456789abc123ABC'

test = 'hello world, you are the best world'

pattern = re.compile(r"world")

# splitted = pattern.split(test)
# print(splitted)

sub = pattern.sub("planet",test)
print(sub)


