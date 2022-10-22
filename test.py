import sys

if __debug__:
    sys.stdin = open("input.txt", 'r')
    sys.stdout = open("output.txt", 'w')

print(f"Hello {input()}!")