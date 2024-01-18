def main(n, mylist):
    def swaps(mylist, o):
        s = 0
        for i in range(len(mylist)):
            for j in range(i + 1, len(mylist)):
                if (o == 'a' and mylist[i] > mylist[j]) or (o == 'd' and mylist[i] < mylist[j]):
                    mylist[i], mylist[j] = mylist[j], mylist[i]
                    s += 1
        return s
    asc, desc = swaps(mylist.copy(), 'a'), swaps(mylist.copy(), 'd')
    return min(asc, desc)
n, mylist = int(input()), list(map(int, input().split())) 
print(main(n, mylist))