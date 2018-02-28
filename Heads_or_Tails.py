import random,sys

print("-- コイン裏表 --")
money = 100
o_u = ["表","裏"]

def set_bet():
    global money
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
    return inp
    
while True:
    atari = random.choice(o_u)
    bet = set_bet()
    print("コインを投げます...")
    print("結果はどちらでしょうか?")
    print("1 > 表")
    print("2 > 裏")
    while True:
        try:
            c = int(input('>>'))
            if c in [1,2]:
                break
        except:
            pass
    print("結果は %sでした"%(atari))
    if c == 1 and atari == "表":
        print("予想的中です!")
        print("%s x %s = %s獲得!"%(bet,2,bet*2))
        money += bet * 2
    else:
        print("残念ながらはずれです!")
    print("")