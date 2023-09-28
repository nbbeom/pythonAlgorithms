import sys

input = sys.stdin.readline

lines = []
point = [0] * 1001


n = int(input())
for _ in range(n):
    i, j = map(int, input().split())
    lines.append((i, j))
