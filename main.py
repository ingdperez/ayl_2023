# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


import re


def longest_repetition(chars):
    if not chars: return ("", 0)
    longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return longest[1], len(longest[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(longest_repetition("555555555555"))


