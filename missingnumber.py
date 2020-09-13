def Algorithm(n, list):
    for i in range(1, n+1):
        if i in list:
            None

        else:
            print(i)
            break

n = eval(input(""))
list = [int(i) for i in input().split()]

Algorithm(n, list)
