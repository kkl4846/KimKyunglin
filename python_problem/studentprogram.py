#함수 이름은 변경 가능합니다.


class NotnumberOfdata(Exception):
    def __init__(self):
        super().__init__('Num of data is not 3!')
class AlreadyExist(Exception):
    def __init__(self):
        super().__init__('Already exist name ')
class NotInteger(Exception):
    def __init__(self):
        super().__init__('Score is not positive integer! ')
class NoNewGradeStudent(Exception):
    def __init__(self):
        super().__init__('학점을 새로 부여할 학생이 존재하지않습니다!')
class NoneStudent(Exception):
    def __init__(self):
        super().__init__('No student data!')
class ExistNoneGradeStudent(Exception):
    def __init__(self):
        super().__init__("There is a student who didn't get grade!")
def Menu1(x) :
        x[1]=int(x[1])
        x[2]=int(x[2])
        name=x[0]
        m_score=x[1]
        f_score=x[2]
        student.append(name)
        studentInfo.insert(student.index(name),{'name':name,'m_score':m_score,'f_score':f_score, 'grade':'none'})

def Menu2(i):
    if (studentInfo[i]['m_score']+studentInfo[i]['f_score'])//2>=90:
        studentInfo[i]['grade']='A'
    elif (studentInfo[i]['m_score']+studentInfo[i]['f_score'])//2>=80:
        studentInfo[i]['grade']='B'
    elif (studentInfo[i]['m_score']+studentInfo[i]['f_score'])//2>=70:
        studentInfo[i]['grade']='C'
        
    else:
        studentInfo[i]['grade']='D'


def Menu3():
    print('---------------------------------')
    print('  name  mid  final  grade')
    print('---------------------------------')
    for i in range(len(student)):
        print('  %5s  %3d  %5d  %5s'%(studentInfo[i]['name'],studentInfo[i]['m_score'],studentInfo[i]['f_score'],studentInfo[i]['grade']))



def Menu4(deleteStd):
    del studentInfo[student.index(deleteStd)]
    del student[student.index(deleteStd)]
    
    

student=[]
studentInfo=[]
it_is=True
count=0
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
   
            try:
                x=list(map(str,input('Enter name mid-score final-score: ').split()))
                if len(x)!=3:
                    raise NotnumberOfdata
                if x[0] in student:
                    raise AlreadyExist

                try:
                    x[1]=int(x[1])
                    x[2]=int(x[2])
                except ValueError:
                    it_is=False
                    print('Score is not positive integer!')
                    continue     
                else:
                    if it_is:
                        if x[1]<0 or x[2]<0:
                            raise NotInteger
            except Exception as e:
                print(e)
            else:
                Menu1(x)

    elif choice == "2":
         count=0
         try:
             if len(student)==0:
                 raise NoneStudent
             for i in range(len(student)):
                 if studentInfo[i]['grade']=='none':
                     count+=1
                     Menu2(i)
             if count==0:
                 raise NoNewGradeStudent
         except Exception as e:
                print(e)
         else:
            print('Grading to all students')
                         
    elif choice == "3" :
         try:
             if len(student)==0:
                 raise NoneStudent
             for i in range(len(student)):
                 if studentInfo[i]['grade']=='none':
                     raise ExistNoneGradeStudent
         except Exception as e:
                print(e)
         else:
             Menu3()
       
 
    elif choice == "4" :
         try:
             if len(student)==0:
                 raise NoneStudent
         except Exception as e:
                print(e)
         else:
             deleteStd=input('Enter the name to delete :')
             if deleteStd not in student:
                 print('Not exist name!')
             else:
                 Menu4(deleteStd)
                 print('%s information is deleted.'%deleteStd)
             
    elif choice == "5" :
        print('Exit Program!')
        break
    else:
        print('Wrong number.Choose again')
        
       
