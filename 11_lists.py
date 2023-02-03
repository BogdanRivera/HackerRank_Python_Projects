if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        opc = list(input().split())
        if 'insert' in opc[0]:
            arr.insert(int(opc[1]), int(opc[2]))
        elif 'print' in opc[0]:
            print(arr)
        elif 'remove' in opc[0]:
            arr.remove(int(opc[1]))
        elif 'append' in opc[0]:
            arr.append(int(opc[1]))
        elif 'sort' in opc[0]:
            arr.sort()
        elif 'pop' in opc[0]:
            arr.pop()
        elif 'reverse' in opc[0]:
            arr.reverse()
