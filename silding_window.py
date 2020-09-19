# silding window
# Created by Phonratichai

def silding_window(data, window):
    print("=* window : ", window)
    for i in range(window):
        result = data[i:window+i:1]
        if(len(result) == window):
            print("=> ", result)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]
    silding_window(x, 4)
    pass
