import random

#トランプセットを作る
numbers = range(1, 14)
marks = ['club', 'diamond', 'heart', 'spade']
money = 100

def get_card(cnt):
    global cards
    tefudas = []
    for i in range(cnt):
        tefuda = random.choice(cards)
        tefudas.append(tefuda)
        cards.remove(tefuda)
    return tefudas
    
def cnt_card(cards):
    cnt = 0
    for card in cards:
        if card[0] < 10: cnt += card[0]
    cnt = str(cnt)
    if len(cnt) == 2: cnt = cnt[1]
    return int(cnt)

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
    while True:
        try:
            print("1: TIE  2: BANKER  3:PLAYER")
            inpB = input('どこにかけますか?>>')
            if inpB == "1":
                inpB = 1
                break
            elif inpB == "2":
                inpB = 2
                break
            elif inpB == "3":
                inpB = 3
                break
        except:
            pass
    return [inp,inpB]

def bank_draw(banker,player):
    if cnt_card(banker) in [3,4,5,6] and len(player) != 3:
        banker.append(get_card(1))
        print("ヒット")
        return False
    else:
        return True
        
def draw(banker,player):
    #プレイヤーのヒットアンドスタンド
    if cnt_card(player) < 6:
        player.append(get_card(1)[0])
        print("Player: ヒット")
    elif cnt_card(player) > 7:
        if cnt_card(banker) < 8:
            print("Playerの勝ち")
            return 0
    #バンカーのヒットアンドスタンド
    if cnt_card(banker) < 3:
        banker.append(get_card(1)[0])
        print("Banker: ヒット")
    elif cnt_card(banker) == 3:
        if bank_draw(banker,player):
            if player[2][0] != 8:
                banker.append(get_card(1)[0])
                print("Banker: ヒット")
    elif cnt_card(banker) == 4:
        if bank_draw(banker,player):
            if player[2][0] not in [0,1,8,9]:
                banker.append(get_card(1)[0])
                print("Banker: ヒット")
    elif cnt_card(banker) == 5:
        if bank_draw(banker,player):
            if player[2][0] in [4,5,6,7]:
                banker.append(get_card(1)[0])
                print("Banker: ヒット")
    elif cnt_card(banker) == 6:
        if bank_draw(banker,player):
            if player[2][0] in [6,7]:
                banker.append(get_card(1)[0])
                print("Banker: ヒット")
    else:
        if cnt_card(player) not in [8,9]:
            print("Bankerの勝ち")
            return 1
    
while True:
    bet_to = set_bet()

    #カードを引く
    cards = [[n, m] for m in marks for n in numbers]
    player = get_card(2)
    banker = get_card(2)
    print("PLAYER: %s"%(cnt_card(player)))
    print("BANKER: %s"%(cnt_card(banker)))
    print("")

    chk = draw(banker,player)
    print("\nショーダウン")
    print("PLAYER: %s"%(cnt_card(player)))
    print("BANKER: %s"%(cnt_card(banker)))

    if chk == None:
        if cnt_card(player) == cnt_card(banker):
            print("TIE")
            if bet_to[1] == 1:
                print("お見事 x8 獲得")
                money += bet_to[0] * 8
            else:
                print("残念")
        elif cnt_card(player) > cnt_card(banker):
            print("プレイヤーの勝利")
            if bet_to[1] == 2:
                print("お見事 x2 獲得")
                money += bet_to[0] * 2
            else:
                print("残念")
        else:
            print("バンカーの勝利")
            if bet_to[1] == 3:
                print("お見事 x1.95 獲得")
                money += bet_to[0] * 1.95
            else:
                print("残念")