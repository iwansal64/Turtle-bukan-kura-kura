import random
import turtle
import sys
from pynput import keyboard
sys.path.append(r"D:\Dev\Python\Code")
from Utility import Utility
import racergame1save as save

eventcode = ''
finish = False

def on_press(key):
    eventkey = ''
    try:
        eventkey = key.char
    except AttributeError:
        eventkey = key

    global finish
    if finish:
        finish = False
        global eventcode
        if eventkey == 'r':
            eventcode = 1
        elif eventkey == 's':
            eventcode = 2
        else:
            eventcode = 0


listen = keyboard.Listener(on_press)
listen.start()


load = input("menggunakan save save an terakhir? (y/n)")
if load == "n":
    load = False
else:
    load = True

wasit = turtle

while True:
    if load:
        try:
            bobGroupUnit = save.BobGroupUnit
            bobGroupName = save.BobGroupName
            bobGroup = save.BobGroupName
            break
        except AttributeError:
            print("Tidak ada save save an beralih ke manual konfigurasi.")
            load = False
            continue
        except Exception as e:
            print("ERROR OCCURED : "+e)
    else:
        bobGroupUnit = input("Masukkan Jumlah Grup (kosongkan jika gak ada grup) : ")
        bobGroupName = []
        bobGroup = True
        break

bobArray = []

try:
    bobGroupUnit = int(bobGroupUnit)
except:
    pass

distanceBetweenGroup = 25
if bobGroupUnit == "" or bobGroupUnit == 0:
    bobGroup = False
    if load:
        bobPlayerUnit = save.BobPlayerUnit
    else:
        bobPlayerUnit = int(input("Masukkan Jumlah Player : "))
    
else:
    if load:
        bobPlayerUnit = save.BobPlayerUnit
        distanceBetweenGroup = save.DistanceBetweenGroup
    else:
        bobPlayerUnit = int(input("Masukkan Jumlah Player Per Grup : "))
        distanceBetweenGroup = int(input("Masukkan Jarak Per group : "))

bobName = []
if load:
    if bobGroup:
        bobGroupName = save.BobGroupName
    bobName = save.BobName

else:
    if bobGroup:
        for i in range(bobGroupUnit):
            data = input("Masukkan nama group ke "+str(i + 1)+" : ")
            bobGroupName.append(data)
            bobName.append([])
            for j in range(bobPlayerUnit):
                data = input('Masukkan nama player ke-'+str(j + 1)+" Group ke -"+str(i + 1)+" : ")
                bobName[i].append(data)
    else:
        for i in range(bobPlayerUnit):
            data = input('Masukkan nama player ke-'+str(i + 1)+" : ")
            bobName.append(data)

bobs = []
if not bobGroup:
    for i in range(bobPlayerUnit):
        bobs.append(turtle.Turtle())
else:
    for i in range(0, bobGroupUnit):
        bobs.append([])
        for j in range(0, bobPlayerUnit):
            bobs[i].append(turtle.Turtle())
            bobArray.append(turtle.Turtle())
    


bobPos = {}
width = turtle.window_width() // 2
height = turtle.window_height() // 2

startYPos = -225
finishYPos = 10
startDistance = int(input("Jarak per player dalam group saat mau mulai (default 50): "))

if load:
    timeSpeed = save.TimeSpeed
    minSpeed = save.MinSpeed
    maxSpeed = save.MaxSpeed

else:
    timeSpeed = int(input("Masukkan kecepatan waktu (min 1, max 11): ")) # MAX 10
    minSpeed = int(input("Masukkan min speed : "))
    maxSpeed = int(input("Masukkan max speed : "))

if timeSpeed > 11:
    timeSpeed = 10
elif timeSpeed == 11:
    timeSpeed = 0
elif timeSpeed < 0:
    timeSpeed = 1

if maxSpeed < minSpeed:
    maxSpeed += minSpeed

colors = ["blue", "gray", "purple", "#291053", "#acfc21", "#1ac123"]

if load:
    colors = save.Colors
else:
    data = input('warna?')
    if data == "y":
        colors = []
        while True:
            data = input("Masukkan warna (bisa hex atau nama warna dalam bing)")
            if data == "":
                break
            else:
                colors.append(data)

wasit.color("green")

while True:
    shape = input("Bentuk Player (circle, square, turtle, arrow, triangle) : ")
    if shape == "arrow" or shape == "":
        shape = "classic"

    eventcode = ''
    finish = False
    wasit.penup()
    random.shuffle(colors)

    # SETUP

    # Start Positioning
    groupIndex = 0
    if not bobGroup:
        for index in range(bobPlayerUnit):
            item = bobs[index]

            item.penup()
            try:
                item.color(colors[index])
            except:
                item.color("red")

            item.speed(timeSpeed)
            item.goto(((-bobPlayerUnit * startDistance) + startDistance * index, startYPos))
            item.setheading(90)
            item.pendown()
    else:
        xPlusPos = 0
        h = 0
        for index, item in enumerate(bobArray):
            item.shape(shape)
            if (h + 1) > bobPlayerUnit:
                xPlusPos += distanceBetweenGroup
                h = 0

            item.penup()
            try:
                item.color(colors[index])
            except:
                item.color("red")
            item.speed(timeSpeed)
            item.goto(((-bobPlayerUnit * startDistance) + xPlusPos + startDistance * index, startYPos))
            item.setheading(90)
            item.pendown()
            h += 1


    # Wasit Line
    wasit.goto((-width, height - finishYPos))
    wasit.pendown()
    wasit.goto((width, height - finishYPos))
    wasit.penup()
    wasit.goto((240, -200))

    randomPlayerNum = 1

    # GAME YO
    run = True
    while run:
        groupIndex = 0
        h = 0
        for index, bob in enumerate(bobArray):
            if bobGroup:
                if (h + 1) > bobPlayerUnit:
                    h -= bobPlayerUnit
                    groupIndex += 1


            speed = random.randint(minSpeed, maxSpeed)
            bob.forward(speed)
            if not bobGroup:
                try:
                    bobName[index]
                except:
                    bobName.append("RandomPlayer"+str(randomPlayerNum))
                    randomPlayerNum += 1
            else:
                try:
                    bobName[groupIndex][h]
                except:
                    bobName.append("RandomPlayer"+str(randomPlayerNum))
                    randomPlayerNum += 1


            if not bobGroup:
                Utility.addListInList(bobPos, bobName[index], 1, -speed, "Add")
            else:
                Utility.addListInList(bobPos, bobName[groupIndex][h], 1, -speed, "Add")

            finished = False
            if not bobGroup:
                if bobPos[bobName[index]][1] + height + -startYPos <= finishYPos:
                    finished = True
            else:
                if bobPos[bobName[groupIndex][h]][1] + height + -startYPos <= finishYPos:
                    finished = True

            if finished:
                finish = True
                if not bobGroup:
                    print("Winner is : "+bobName[index])
                    run = False
                    break
                else:
                    for i in bobName:
                        for j in i:
                            if not bobGroup:
                                if j == bobName[index]:
                                    championNames = j

                                    print("winner is : "+championNames)
                                    break
                            else:
                                if j == bobName[groupIndex][h]:
                                    championNames = ''
                                    for index, name in enumerate(i):
                                        if index == len(i) - 1:
                                            break
                                        championNames += name
                                        championNames += ", "
                                    championNames += i[len(i) - 1]

                                    print("winner is : "+championNames)
                                    print("MVP : "+bobName[groupIndex][h])
                                    break
            
            h += 1
            
            while finish:
                continue
    
            if eventcode == 0:
                turtle.bye()
                run = False
                break
            elif eventcode == 1:
                bobPos = {}
                break
            elif eventcode == 2:
                with open("racergame1save.py", "w+") as f:
                    f.write(f"""BobGroupUnit = {bobGroupUnit}
BobGroupName = {bobGroupName}
BobGroup = {bobGroup}
BobPlayerUnit = {bobPlayerUnit}
BobName = {bobName}
Colors = {colors}
DistanceBetweenGroup = {distanceBetweenGroup}
TimeSpeed = {timeSpeed}
MinSpeed = {minSpeed}
MaxSpeed = {maxSpeed}
                    """)
                turtle.bye()
                run = False
                break

        if eventcode == 1:
            break

    if eventcode == 0 or eventcode == 2:
        break

    elif eventcode == 1:
        turtle.reset()
        continue

