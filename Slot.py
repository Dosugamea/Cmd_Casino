import random,sys

money = 100
jackpot = 1000

pattern = ["1","2","3","4","5","6","7","8","9","R","G","B","JP"]

#13 * 13 * 13 = 2197
#2197 / 5:

def make_slot():
    return random.sample(pattern, 3)

while True:
    print("JACKPOT: %s"%(jackpot))
    print("所持金: %sクレジット"%(money))
    if money <= 0:
        print("GAME OVER")
        sys.exit()
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
    slot = make_slot()
    atari = False
    if slot[0] != slot[1] and slot[1] != slot[2]:
        r = random.randint(1,20)
        if r == 1:
            atari = True
            slot[0] = slot[1] = slot[2] = random.choice(pattern)
    else:
        atari = True
    print(slot)
    if atari:
        print("当たり")
        if slot[0] in ["1","2","3","4","5","6","7","8","9"]:
            print("%s x %s = %s獲得!"%(inp,slot[0],inp*int(slot[0])))
            money += inp * int(slot[0])
        elif slot[0] in ["R","G","B"]:
            print("%s x %s = %s獲得!"%(inp,15,inp*15))
            money += inp * 15
        else:
            print("ジャックポット!!")
            print("%s 獲得!!"%(jackpot))
            money += jackpot
            jackpot = 1000
    else:
        print("はずれ")
        jackpot += inp