def check_panagram( s2):
    s1 = input("enter string")
    letters = list("abcdefghijklmnopqrstuvwxyz")
    for ch in letters:
        if ch not in list(s1):
            print("not a panagram")
        else:
            print("tis a panagram")
