def opentext():
    f = open("C:/essenceofML/chapter2/sample.txt")  #ファイルを開く
    for line in f:  #1行ずつ処理する
        line = line.rstrip()    #末尾の空白と開業を削除
        print(line)

    f.close()

#opentext()

def openwith():
    with open("C:/essenceofML/chapter2/sample.txt") as f:
        for line in f:
            line = line.rstrip()
            print(line)

#openwith()

def writeread():
    with open("C:/essenceofML/chapter2/output.txt","w") as fw:  #書き込み用に開く
        with open("C:/essenceofML/chapter2/sample.txt") as fr:  #読み込み用に開く
            for line in fr:
                print(line, end = "", file=fw)

writeread()