import datetime

def date():
    d = datetime.date(2017,1,1) #dateクラスのインスタンスを作成
    print(d.year)   #データ属性year

    print(d.weekday())  #weekdayメソッド

#date()

class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + "," + self.last_name

person1 = Person(first_name="John",last_name="Smith")
print(person1.first_name,person1.last_name)
person2 = Person()
person2.first_name = "Robert"
person2.last_name = "Johnson"
print(person2.first_name,person2.last_name)
print(person1.get_name())
print(person1)
