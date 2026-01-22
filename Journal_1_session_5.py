import math

def main():
    n = 1000
    for i in range(n):
        x = 2 * i / (n - 1)
        print(x, math.sin(x))

main()