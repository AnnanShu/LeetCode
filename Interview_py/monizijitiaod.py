import sys

the_line = sys.stdin.readline()

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ans = list(map(int, sys.stdin.readline().split()))
    bns = list(map(int, sys.stdin.readline().split()))
    sorted(zip(bns, range(n)))

