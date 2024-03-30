while True:
    a = int(input())
    if a in [1, 9, 17, 25]:
        print("1 этаж")
    elif a in [2, 10, 18, 26]:
        print("2 этаж")
    elif a in [3, 11, 19, 27]:
        print("3 этаж")
    elif a in [4, 12, 20, 28]:
        print("4 этаж")
    elif a in [5, 13, 21, 29]:
        print("5 этаж")
    elif a in [6, 14, 22, 30]:
        print("6 этаж")
    elif a in [7, 15, 23, 31]:
        print("7 этаж")
    elif a in [8, 16, 24, 32]:
        print("8 этаж")
    if a in [1, 2, 3, 4, 5, 6, 7, 8]:
        print("1 подъезд")
    elif a in [9, 10, 11, 12, 13, 14, 15, 16]:
        print("2 подъезд")
    elif a in [17, 18, 19, 20, 21, 22, 23, 24]:
        print("3 подъезд")
    elif a in [25, 26, 27, 28, 29, 30, 31, 32]:
        print("4 подъезд")
