import turtle as t
                       # 짱구의 부리부리 댄스를 다 같이 그려봅시다.
  
t.shape("turtle")
t.pensize(3)
t.bgcolor("white")
t.speed(0)
t.fillcolor("bisque")  # 궁둥이 1/2
t.begin_fill()
for x in range(5):
    t.circle(50)
t.up()
t.fd(100) 
t.down()
t.circle(50)           # 궁둥이 2/2
t.fd(40)               # 오른팔 
t.lt(40)
t.fd(50)
t.lt(50)
t.fd(30)
t.lt(90)
t.fd(10)
t.lt(90)
t.fd(7)
t.rt(40)
t.fd(45)
t.end_fill()
t.up()
t.lt(40)
t.fd(23)
t.down()
t.fillcolor("yellow")  # 노랑 바지
t.begin_fill()
t.fd(45)
t.rt(90)
t.fd(80)
t.rt(50)
t.fd(15)
t.lt(140)
t.fd(10)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(45)
t.rt(90)
t.fd(160)
t.end_fill()
t.up()
t.rt(90)
t.fd(45)
t.down()
t.fillcolor("bisque")  # 오른쪽 다리
t.begin_fill()
t.lt(20)
t.fd(20)
t.rt(50)
t.fd(10)
t.rt(85)
t.fd(15)
t.rt(50)
t.fd(20)
t.end_fill()
t.up()
t.back(20)
t.lt(165)
t.down()
t.fd(15)               # 흰 양말 1/2
t.lt(90)
t.fd(15)
t.lt(90)
t.fd(12)
t.up()
t.rt(180)
t.fd(12)
t.lt(50)
t.down()
t.fillcolor("green")  # 초록색 신발 1/2
t.begin_fill()
t.fd(13)
t.rt(140)
t.fd(25)
t.rt(90)
t.fd(10)
t.end_fill()          # 절반 완성했습니다. 나머지 힘내러 퐈이팅!
t.up()
t.fd(35)
t.lt(90)
t.fd(85)
t.down()
t.lt(60)
t.fillcolor("bisque") # 왼쪽 다리
t.begin_fill()
t.fd(16)
t.lt(50)
t.fd(14)
t.rt(110)
t.fd(15)
t.rt(70)
t.fd(20)
t.rt(40)
t.fd(8)
t.rt(70)
t.fd(18)
t.end_fill()
t.up()
t.rt(90)
t.fd(23)
t.down()
t.fd(12)              # 흰 양말 2/2
t.rt(90)
t.fd(10)
t.rt(70)
t.fd(15)
t.back(15)
t.lt(100)
t.fillcolor("green")  # 초록색 신발 2/2
t.begin_fill()
t.fd(15)
t.lt(150)
t.fd(23)
t.lt(90)
t.fd(9)
t.end_fill()
t.up()
t.fd(80)
t.lt(90)
t.fd(50)
t.down()
t.fillcolor("bisque")  # 왼팔
t.begin_fill()
t.rt(50)
t.fd(40)
t.rt(40)
t.fd(15)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(50)
t.fd(55)
t.end_fill()
t.ht()
                      # 감사합니다.
