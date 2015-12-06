import re


with open('input.txt') as input:
    count = 0
    for string in input.readlines():
        double_match = re.compile(r'([a-z][a-z])\w*\1', re.IGNORECASE)
        middle_match = re.compile(r'([a-z])[a-z]\1', re.IGNORECASE)

        if middle_match.search(string) and double_match.search(string):
            count += 1
    print(count)
