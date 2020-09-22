# code: 22p22c0398-พรระติชัย
# crated by Phonratichai
# 19/09/63 14:40
nameList = ['winn', 'thanarak', 'somchai',
            'ricky', 'tao', 'wanida', 'peerapol']


def countname_with_alphabet(alphabet):
    count = 0
    for name in nameList:
        if alphabet in name:
            count += 1
    return count


def findname_with_alphabet(alphabet):
    subnameList = []
    for name in nameList:
        if alphabet in name:
            subnameList.append(name)
    return subnameList


if __name__ == "__main__":
    print(countname_with_alphabet('a'))
    print(countname_with_alphabet('n'))
    print(findname_with_alphabet('a'))
    print(findname_with_alphabet('n'))
