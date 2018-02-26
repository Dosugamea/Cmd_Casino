import random

#カードリストを表示させる
def make_card_txt(cards,hide=False):
    txts = ["","","","","","",""]
    for card in cards:
        txts[0] += "======= "
        if (hide):
            txts[1] += "|     | "
        else:
            txts[1] += "|"+mark_dict[card[0]]+"    | "
        txts[2] += "|     | "
        if (hide):
            txts[3] += "|  ?  | "
        else:
            if len(str(card[1])) != 2:
                txts[3] += "|  "+str(card[1])+"  | "
            else:
                if card[1] == 10:
                    txts[3] += "| "+str(card[1])[0]+" "+str(card[1])[1]+" | "
                else:
                    txts[3] += "|  "+num_dict[str(card[1])]+"  | "
        txts[4] += "|     | "
        txts[5] += "|     | "
        txts[6] += "======= "
    for txt in txts:
        print(txt)

#カードを数える(10以上は10として数える)
def cnt_cards(cards):
    tt = 0
    for card in cards:
        if card[1] < 11:
            tt += card[1]
        else:
            tt += 10
    return tt    

#思ったんだけどこれ初めからマーク入れとけばよかった
marks = ['club', 'diamond', 'heart', 'spade']
mark_dict = {
    "club":"♣",
    "diamond":"♦",
    "heart":"♥",
    "spade":"♠"
}
num_dict = {
    "11":"J",
    "12":"Q",
    "13":"K"
}

#トランプセットを作る
numbers = range(1, 14)
cards = [(m, n) for m in marks for n in numbers]
#ディーラーに引かせる
d_cards = []
for i in range(2):
    c = random.choice(cards)
    d_cards.append(c)
    cards.remove(c)
while True:
    #公式ルールに従い 17以上になるまで引く
    if cnt_cards(d_cards) < 18:
        c = random.choice(cards)
        d_cards.append(c)
        cards.remove(c)
    else:
        break
#プレイヤーに引かせる
p_cards = []
for i in range(2):
    c = random.choice(cards)
    p_cards.append(c)
    cards.remove(c)

#ゲームループ    
while True:
    #メイン画面
    print("ディーラー: Card x"+str(len(d_cards)))
    make_card_txt(d_cards,True)
    print("")
    print("プレイヤー: Card x"+str(len(p_cards)))
    print("トータル:"+str(cnt_cards(p_cards)))
    make_card_txt(p_cards)
    print("ヒットしますか? (1:Hit 2:Stand)")
    while True:
        inp = input(">>>")
        if inp in ["1","2"]:
            break
    #もっかいぴょんぴょん
    if inp == "1":
        c = random.choice(cards)
        p_cards.append(c)
        cards.remove(c)
        if cnt_cards(p_cards) > 21:
            #プレイヤーバスト
            print("\nショーダウン")
            print("ディーラー: Card x"+str(len(d_cards)))
            print("トータル:"+str(cnt_cards(d_cards)))
            make_card_txt(d_cards)
            print("")
            print("プレイヤー: Card x"+str(len(p_cards)))
            print("トータル:"+str(cnt_cards(p_cards)))
            make_card_txt(p_cards)
            print("プレイヤー: バスト")
            print("\nプレイヤーの負け")
            break
    else:
        #ショーダウン
        print("\nショーダウン")
        print("ディーラー: Card x"+str(len(d_cards)))
        print("トータル:"+str(cnt_cards(d_cards)))
        make_card_txt(d_cards)
        print("")
        print("プレイヤー: Card x"+str(len(p_cards)))
        print("トータル:"+str(cnt_cards(p_cards)))
        make_card_txt(p_cards)
        if cnt_cards(d_cards) > 21:
            print("ディーラー: バスト")
            print("\nプレイヤーの勝ち")
        else:
            dtt = cnt_cards(d_cards)
            ptt = cnt_cards(p_cards)
            if dtt > ptt:
                print("\nプレイヤーの負け")
            else:
                print("\nプレイヤーの勝ち")
        break
