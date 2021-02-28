intList = []


def siz():
    return len(intList)


def Add(v):
    return intList.append(v)


def head():
    if siz() == 0:
        return 'null'
    return intList[0]


def tail():
    if siz() == 0:
        return 'null'
    return intList[siz() - 1]


def take():
    if siz() == 0:
        return 'null'
    r = intList[0]
    intList.remove(intList[0])

    return r


Add(1)
Add(2)
Add(3)

print(intList)
print(head())
print(tail())
print(take())
print(take())
print(take())
print(intList)
