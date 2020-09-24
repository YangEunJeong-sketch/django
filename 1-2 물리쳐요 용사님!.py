import random
power = random.randint(1,100)

class Warrior :
    def __init__(self, name, money) :
        self.name = name
        self.money = money

    def store(self, tool) :
        print(" 1) 칼(500원/공격력:500)    2)활(700원/공력력:700)    3)포(1000원/공격력:1000")
        print("{0}원을 이용하여 {1}을 구매하였습니다.".format(self.money, tool)

    def fight(self) :
        import random
        monster = random.randint(500, 999)
        if monster < int(tool) :
            print("Win!")
        else :
            print("TT")


# my = Warrior("양은정", 50000)
# 
