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

def Referencingandcopyinglists():
    l = [1,2,3]
    m = l   #これは参照をコピーするだけ
    m.append(4)
    print(m)
    print(l)    #mを変更するとlも変更される
    l = [1,2,3]
    m = l[:]    #新しいリストが作られて値がコピーされる
    m.append(4)
    print(m)
    print(l)

#Referencingandcopyinglists()

def listoflists():
    l = [[],[],[]]
    l[1].append(1)
    print(l)
    l[2].append(2)
    l[2].append(3)
    print(l)
    l[2].insert(1,100)
    print(l)

#listoflists()

def listcomprehension():
    l = [i**2 for i in range(5)]
    print(l)
    
    m = [[i*10+j for j in range(5)] for i in range(5)]
    print(m)

#listcomprehension()

def ManipulatingTuples():
    t = 1,"a",1.5   #タプルの作成
    print(t)
    u = t,(1,2,3)
    print(u)    #タプルを要素として持つタプルの作成
    print(t[1])
    #t[1] = 1   #tapleは内容を変更できない
    s = ()
    k = 1,
    print(s,k)
#ManipulatingTuples()

def sequence():
    for i in range(3):  #rangeを使った繰り返し
        print(i)

    print("next")

    l = [2,4,6]
    for x in l:
        print(x)

    print("next")

    m = [x * 2 for x in l]  #lの内容を2倍した値を持つリスト
    print(m)

    print("next")

    s = "abcd"
    for x in s:
        print(x)

    print("next")
    
    t = ["*" + x + "*" for x in s]
    print(t)

    print("next")

    k = list(s) #リスト関数で文字列をリスト化
    print(k)

#sequence()

def dictionary():
    d = {"a":1, #辞書の作成
         "b":2,
         "c":3}
    print(d["a"])   #キーを指定して値を取得
    
    print("b" in d)

#dictionary()

def keyandvalue():
    d = {}  #空の辞書を作成
    d["x"] = 1
    d["y"] = 2
    d["z"] = 3
    print(d)

    for k in d: #全てのキーを取り出す
        print(k)

    for x in d.items(): #キーと値を組にしたタプルを取り出す
        print(x)

#keyandvalue()

#集合は重複を許さず順番に意味を持たない
def syugou():
    a = set()   #空の集合を作成
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(3)
    print("a = ",a)

    print(2 in a)
    print(5 in a)
    b = {2,3,4}
    print("b = ",b)
    print("論理積 = ",a & b)    #論理積
    print("論理和 = ",a | b)    #論理和
    print("差 = ",a-b)  #集合同士の演算

    for x in a:
        print(x)

#syugou()