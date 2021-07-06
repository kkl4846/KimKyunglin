num=0
while True:
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
