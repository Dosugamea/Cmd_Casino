import random,sys

money = 100


class Slot():
    jackpot = 1000
    pay = 1
    out = 1
    pattern = ["1","2","3","4","5","6","7","8","9","R","G","B","JP"]

    def make_slot(self):
        slot = ["","",""]
        if self.out/self.pay > 2: r = random.randint(1,10)
        elif self.out/self.pay > 1 : r = random.randint(1,7)
        else: r = random.randint(1,5)
        #3-10回に1回あたる
        if r == 1:
            if self.jackpot > 3000: r = random.randint(1,25)
            elif self.jackpot > 2000: r = random.randint(1,50)
            r = random.randint(1,100)
            if r < 2: slot[0] = "JP"
            elif r < 7: slot[0] = random.choice(["R","G","B"])
            else: slot[0] = random.choice(["1","2","3","4","5","6","7","8","9"])
            slot[1] = slot[0]
            slot[2] = slot[0]
        else:
            slot[0] = random.choice(self.pattern)
            slot[1] = random.choice(self.pattern)
            slot[2] = random.choice(self.pattern)
            if slot[0] == slot[1] == slot[2]: slot[1] = "JP"
        return slot
        
    def roll(self,inp):
        print("P/O : %s"%(self.out/self.pay))
        out = 0
        slot = self.make_slot()
        print("")
        print(slot)
        print("")
        if slot[0] == slot[1] == slot[2]:
            print("当たり")
            if slot[0] in ["1","2","3","4","5","6","7","8","9"]:
                print("%s x %s = %s獲得!"%(inp,slot[0],inp*int(slot[0])))
                out = inp * int(slot[0])
                self.out += inp * int(slot[0])
            elif slot[0] in ["R","G","B"]:
                print("%s x %s = %s獲得!"%(inp,15,inp*15))
                out = inp * 15 
                self.out += inp * int(3)
            else:
                print("ジャックポット!!")
                jp = self.jackpot
                print("%s 獲得!!"%(jp))
                out = jp
                self.out += jp
                self.jackpot = 1000
        else:
            print("はずれ")
            self.jackpot += inp
        self.pay += inp
        return out

slotter = Slot()
      
print("所持金: %s"%(money))      
while True:
    try:
        inp = input('いくらかけますか?>>')
        if inp == "ALL":
            inp = money
            break
        elif inp == "HALF":
            inp = int(money/2)
            break
        elif int(inp) > 0 and int(inp) <= money:
            inp = int(inp)
            break
    except:
        pass
print(str(inp)+"クレジット かけます")
money -= inp
money += slotter.roll(inp)
print(money)