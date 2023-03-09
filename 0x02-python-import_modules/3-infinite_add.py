#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    a_sum = 0
    if total <= 1:
        print("0")
    else:
        if total == 2:
            print("{}".format(sys.argv[1]))
        else:
            for i in range(1, total):
                a_sum += sys.argv[i]
    print("{}".format(a_sum))
