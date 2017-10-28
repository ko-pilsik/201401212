import turtle as t
import random

t.shape("turtle")
t.pensize(3)
t.speed(6)

t.up()                                           # 거북이가 놀 정사각형 모양의 우리를 그려줍니다.
t.home()
t.goto(-250,-250)
t.down()
t.seth(90)
for x in range(4):
    t.fd(500)
    t.rt(90)

t.up()
t.home()                                         # 거북이가 가운데에서 바라보는 각도를 랜덤으로 해줍니다.
t.setheading(random.randint(0,359))
t.write("스페이스 바를 누르면 거북이가 달립니다!",False,"center",("",10))
t.down()

def Lets_go():                                   # 거북이의 출발 함수를 정의해줍시다.
    while True :
        x1=t.xcor()
        y1=t.ycor()
        h1=t.heading()
        if -250 < x1 < 250 and -250 < y1 < 250 : # 우리 내에서 거북이가 영원히 움직이도록 해줍니다.
            t.fd(2)
        else :                                   # 거북이가 벽에 부딪힐 때 반사되도록 해줍니다.
            x2=t.xcor()
            y2=t.ycor()
            h2=t.heading()
            if x2<=-250:                         # 거북이가 왼쪽 벽에 부딪힐 때 반사되도록 해줍니다.
                t.setheading(180-h2)
                t.fd(3)


            if x2>=250:                          #  거북이가 오른쪽 벽에 부딪힐 때 반사되도록 해줍니다.
                t.setheading(180-h2)
                t.fd(3)

            if y2>=250:                          # 거북이가 위쪽 벽에 부딪힐 때 반사되도록 해줍니다. 
                t.setheading(-h2)
                t.fd(3)

            if y2<=-250:                         # 거북이가 아랫쪽 벽에 부딪힐 때 반사되도록 해줍니다.
                t.setheading(-h2)
                t.fd(3)
            
        

t.onkeypress(Lets_go,"space")                    # 거북이의 출발 함수를 키보드로 지정해줍니다.
t.listen()                                       # 거북이가 우리의 말을 잘 듣도록 조련해줍니다.
