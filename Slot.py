import random,sys

money = 100
jackpot = 1000
pay = 1
out = 1

pattern = ["1","2","3","4","5","6","7","8","9","R","G","B","JP"]

def make_slot():
    slot = ["","",""]
    if out/pay > 2: r = random.randint(1,10)
    elif out/pay > 1 : r = random.randint(1,7)
    else: r = random.randint(1,5)
    #3-10回に1回あたる
    if r == 1:
        if jackpot > 3000: r = random.randint(1,25)
        elif jackpot > 2000: r = random.randint(1,50)
        r = random.randint(1,100)
        if r < 2: slot[0] = "JP"
        elif r < 7: slot[0] = random.choice(["R","G","B"])
        else: slot[0] = random.choice(["1","2","3","4","5","6","7","8","9"])
        slot[1] = slot[0]
        slot[2] = slot[0]
    else:
        slot[0] = random.choice(pattern)
        slot[1] = random.choice(pattern)
        slot[2] = random.choice(pattern)
        if slot[0] == slot[1] == slot[2]: slot[1] = "JP"
    return slot

while True:
    #print("P/O : %s"%(out/pay))
    print("")
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
    print("")
    print(slot)
    print("")
    if slot[0] == slot[1] == slot[2]:
        print("当たり")
        if slot[0] in ["1","2","3","4","5","6","7","8","9"]:
            print("%s x %s = %s獲得!"%(inp,slot[0],inp*int(slot[0])))
            money += inp * int(slot[0])
            out = inp * int(slot[0])
        elif slot[0] in ["R","G","B"]:
            print("%s x %s = %s獲得!"%(inp,15,inp*15))
            money += inp * 15
            out = inp * int(3)
        else:
            print("ジャックポット!!")
            print("%s 獲得!!"%(jackpot))
            money += jackpot
            jackpot = 1000
    else:
        print("はずれ")
        jackpot += inp
    pay += inp