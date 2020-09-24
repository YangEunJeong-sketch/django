score = 0
mescore = 0
Ascore = 0
while score <= 5 :
    while True : 
        choice = input("가위, 바위, 보 중 하나를 선택하시오.")
        import random
        A = random.randint(1,3)
        if choice == "가위" :
            me = 1
        if choice == "바위" :
            me = 2
        if choice =="보" :
            me = 3
        score += 1
        if A == 1 and me == 3 :
            print("컴퓨터가 승리하였습니다.")
            Ascore += 1
        elif A ==3 and me == 1 :
            print("당신이 승리하였습니다.")
            mescore += 1
        elif A == me :
            print("무승부입니다.")
        else :
            if A > me :
                print("컴퓨터가 승리하였습니다.")
                Ascore += 1
            else :
                print("당신이 승리하였습니다.")
                mescore += 1
        if mescore == 3 :
            print("당신의 최종 승리")
            break
        if Ascore == 3 :
            print("컴퓨터의 최종 승리")
            break
#5판 안에 안 끝남
# break도 안 됨. ㅠ
                
                
      
