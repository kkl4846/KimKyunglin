num=0
while True:
    numberOfInput=input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) :')
    if numberOfInput.isdigit():
        if numberOfInput.isdigit():
            if numberOfInput!=1 or numberOfInput!=2 or numberOfInput!=3:
                print('1,2,3 중 하나를 입력하세요')
            else:
                break
        else:
            print('정수를 입력하세요')
    else:
         print('정수를 입력하세요')
