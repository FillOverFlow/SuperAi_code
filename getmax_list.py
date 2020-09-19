# created by Phonratichai
# in python has function max already => max()
# get_max_in_list => hand make :)

def get_max_in_list(list_item):
    maxN = -999999999999999
    for i in list_item:
        if(i > maxN):
            maxN = i
        else:
            continue
    return maxN


if __name__ == "__main__":
    some_list = [-11, -2, -3, -4]
    print(get_max_in_list(some_list))  # use my function
    print(max(some_list))  # use default in python
