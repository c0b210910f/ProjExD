from random import randint, sample, shuffle
import copy
import datetime
tmozisuu = 10
kmozisuu = 2
alphallist = list("QWERTYUIOPASDFGHJKLZXCVBNM")
def quiz():
    
    shuffle(alphallist)
    tmozi = sample(alphallist,tmozisuu)
    print("対象文字")
    print(tmozi)
    hmozi = copy.copy(tmozi)
    for i in range(kmozisuu):
        shuffle(hmozi)
        del hmozi[0]
    kmozi = list(set(tmozi) - set(hmozi))
    print("欠損文字")
    print(kmozi)
    print("表示文字")
    print(hmozi)
    print(tmozi)

    p_ans = int(input("欠損文字はいくつあるでしょうか？："))
    ans = kmozisuu
    
    if p_ans == ans:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        for i in range(int(ans)):
            a = input(str(i+1) + "つ目の文字を入力してください：")
            if a not in kmozi:
                print("不正解です。")
                if __name__ == "__main__":

                    quiz()

                


            
            

    else:
        print("不正解")
        if __name__ == "__main__":

            quiz()


    

if __name__ == "__main__":
    st = datetime.datetime.now()

    quiz()
    ed = datetime.datetime.now()
    print("完答するのにかかった時間")
    print((ed-st).seconds)