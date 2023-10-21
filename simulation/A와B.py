S = list(input())

p = list(input())


def ps():
    while p:
        if p[-1] == "A":
            p.pop()
        elif p[-1] == "B":
            p.pop()
            p.reverse()

        if S == p:
            return 1

    return 0


print(ps())
