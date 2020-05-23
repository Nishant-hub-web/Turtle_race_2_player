from turtle import Screen
import elements
import random
win = Screen()
win.setup(900, 900)
win.bgcolor("black")
win.title("Turtle Race")
win.tracer(0)

obj = elements.Objects()

a_moves=[]
b_moves=[]
n=1
num1=0
running=True
while True:
    win.update()
    if running:
        if n==1:
            print(input("Player one your turn , press Enter:"))
            num1=random.randint(1,6)
            a_moves.append(num1)
            obj.pen.pencolor("cyan")
            obj.pen.goto(-420, -300)
            obj.pen.write(f"Player A moves:{a_moves}", align="left", font=("Courier", 20, "normal"))
            for i in range(num1):
                obj.player_one_move()
            n+=1
        else:
            print(input("Player two your turn , press Enter:"))
            num1 = random.randint(1, 6)
            b_moves.append(num1)
            obj.pen.pencolor("dark green")
            obj.pen.goto(-420, -330)
            obj.pen.write(f"Player B moves:{b_moves}", align="left", font=("Courier", 20, "normal"))
            for i in range(num1):
                obj.player_two_move()
            n -= 1

        if obj.player_one.xcor() >= 200:
            obj.pen.pencolor("purple")
            obj.pen.goto(-420, -385)
            obj.pen.write(f"Player A  Won!!", align="left", font=("Courier", 34, "normal"))
            running = False
        if running:

            if obj.player_two.xcor() >= 200:
                obj.pen.pencolor("purple")
                obj.pen.goto(-420, -385)
                obj.pen.write(f"Player B  Won!!", align="left", font=("Courier", 34, "normal"))

                running = False



