def listslicing():
    a = [1,2,3,4,5]
    print(a)
    print(a[2:4])
    print(a[3:])
    print(a[:-1])

#listslicing()

def workingwithlist():
    l = [1,2,3]
    print(l)
    l.append(4) #末尾に追加
    print(l)
    l.insert(1,100) #配列番号1に100を追加する
    print(l)

    a = [[1,2,3]
        ,[4,5,6]]
    a[0].insert(1,100)
    print(a)

    b = [1,2,3]
    c = []
    c.append(4)
    c.append(5)
    print(c)
    b.extend(c) #bとcを連結
    print(b)

    b = [1,2,3]
    print(b+c)

#workingwithlist()

