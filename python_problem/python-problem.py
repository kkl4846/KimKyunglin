
from random import *
num=0
finish='0'
def brGame(user):
        global num,finish
        while True:
            if user=='computer':
                numberOfInput=randint(1,3)
                print('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) :',numberOfInput)
            else:
                numberOfInput=input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) :')
            try:
                numberOfInput=int(numberOfInput)
                it_is=True
            except ValueError:
                it_is=False
            if it_is==False:
                print('정수를 입력하세요')
            else:
                if 1<=numberOfInput<=3:
                    break
                else:
                    print('1,2,3 중 하나를 입력하세요')

        for i in range(numberOfInput):
            num=num+1
            print('{0} :{1}'.format(user,num))
            if num==31:
                if user=='computer':
                    finish='player'
                else:
                    finish='computer'
                break


while True:
    brGame('computer')
    if finish!='0':
        print('{0} win!'.format(finish))
        break
    brGame('player')
    if finish!='0':
        print('{0} win!'.format(finish))
        break
