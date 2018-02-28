import random,sys

print("-- ヒットアンドブロー --")
money = 100

def gen_num():
    nl = [str(i) for i in range(0,9)]
    num = ""
    for i in range(3):
        n = random.choice(nl)
        nl.remove(n)
        num += str(n)
    if num[0] == "0": num = random.choice(nl)+num[1:]
    return num
    
while True:
    atari = gen_num()
    print("所持金: %sクレジット"%(money))
    step = 0
    while True:
        step += 1
        print("\n数字を予想してください")
        while True:
            try:
                inp = int(input('>>'))
                if len(str(inp)) == 3:
                    break
            except:
                pass
        inp = str(inp)
        hit = blow = 0
        for (i,x) in enumerate(atari):
            if inp[i] == x: hit += 1
            elif x in inp: blow+=1
        if hit != 3:
            print("HIT: %s BLOW: %s"%(hit,blow))
        else:
            break
    print("正解! 所要ステップ数: %s"%(step))
    if step < 10:
        print("10ステップ以内のクリア お見事!")
        print("50クレジット 獲得!")
        money += 50