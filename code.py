#The birthday card that I have created is fully interactable with numerous pages included. 
#The birthday card obtains data inputted by the user which will then utilize it to form the perfect birthday card, with interactable
#shapes and nicely formatted text. If you click on the balloons, 2 balloons will fly out from the sides.
#If you click the star on the second page, stars will fall down from the sky-- and these stars' rotateAngle & fill can be edited!
#Click on an x value greater than or equal to 350 to go to the second page. Click on the x value less than or equal to 50 to go back 
#to the first page.

#Getting the information & data from the user to create the card
response1 = app.getTextInput('How old will the person you are sending this to be?')
response2 = app.getTextInput('Who are you sending this too?')
response3 = app.getTextInput('Type in your name!')

#The design of the first page with all the text and the overall card design (background) coded.
firstPage = Group(
    Rect(50, 0, 300, 400, fill=rgb(255, 229, 180), border='red', borderWidth=10),
    Label('Happy Birthday!', 200, 50, size=40, font='cursive'),
    Label('To:', 100, 300, size=30, font='cursive'),
    Label(response2, 200, 300, size=30, font='cursive'),
    Label('from:', 100, 350, size=30, font='cursive'),
    Label(response3, 200, 350, size=30, font='cursive')
    )
#The design of the second page with all the text and the overall card (background) coded.
secondPage = Group(
    Rect(0, 0 , 400, 400, fill=rgb(255, 229, 180), border='red', borderWidth=10),
    Label(response2, 75, 35, size=30, font='cursive'),
    Label('I hope you have had a great birthday', 200, 75, size=20),
    Label('I hope you enjoy yourself!', 200, 100, size=20),
    Label('Make sure to celebrate turning', 200, 125, size=20),
    Label(response1, 350, 125, size=20),
    Label('Enjoy all the presents you got!', 200, 150, size=20),
    Label('Cheers for this year!', 200, 175, size=20),
    Label('And cheers for many more!', 200, 200, size=20),
    Label('Sincerely,', 225, 350, size=20),
    Label(response3, 315, 350, size=20, font='cursive')
    )

#The different balloons that appear in the code, such as the ones on the first page as well as the ones in the
#sides that fly out when you click the ones on the center.
redBalloon = Oval(200, 150, 35, 50, fill='red')
blueBalloon = Oval(170, 150, 35, 50, fill='blue')
purpleBalloon = Oval(230, 150, 35, 50, fill='purple')
greenBalloon = Oval(185, 180, 35, 50, fill='green')
orangeBalloon = Oval(215, 180, 35, 50, fill='orange')
pinkBalloon = Oval(25, 450, 35, 50, fill='pink', visible=False)
darkGreenBalloon = Oval(375, 450, 35, 50, fill='darkGreen', visible=False)

#A function that allows me to easily create the lines of the balloons that I created on the first page, to make them look neat and
#organized, without overlapping shapes.
def balloonLines(x, y):
    line1 = Line(200, redBalloon.bottom, x, y ,fill='black')
    line2 = Line(170, blueBalloon.bottom, x, y, fill='black')
    line3 = Line(230, purpleBalloon.bottom, x, y, fill='black')
    line4 = Line(185, greenBalloon.bottom, x, y, fill='black')
    line5 = Line(215, orangeBalloon.bottom, x, y, fill='black')
    greenBalloon.toFront()
    orangeBalloon.toFront()
    firstPage.toBack
balloonLines(200, 250)

#Creating the lines for the two balloons that come out from the sides to follow those two specific balloons.
line6 = Line(25, pinkBalloon.bottom, 25, pinkBalloon.bottom+35)
line7 = Line(375, darkGreenBalloon.bottom, 375, darkGreenBalloon.bottom+35)

#The code for the stars on the second page, the one the second page itself as well as the ones that
#appear when you click on the second page.
starOnSecondPage = Star(75, 300, 25, 5, fill='gold', visible=False)
star1 = Star(80, -50, 25, 5, fill='gold')
star2 = Star(160, -50, 25, 5, fill='gold')
star3 = Star(240, -50, 25, 5, fill='gold')
star4 = Star(320, -50, 25, 5, fill='gold')

#A function to avoid repeated code within onMousePress. This is the function that allows for the two side balloons to appear
#when any of the balloons on the front page are clicked. This function could be easily placed into each of the if statements in onMousePress
#to avoid messy code and have clear code. 
def balloonAppear():
        pinkBalloon.visible=True
        darkGreenBalloon.visible=True
        pinkBalloon.centerY-=20
        darkGreenBalloon.centerY-=20
        line6.y1-=20
        line6.y2-=20
        line7.y1-=20
        line7.y2-=20
#Defining Functions to easily change whether the firstPage is visible or secondPage and easily able to switch between them.
def firstPageVisibility(Answer):
    firstPage.visible=Answer
def secondPageVisibility(Answer):
    secondPage.visible=Answer
firstPageVisibility(True)
secondPageVisibility(False)

def onMousePress(mouseX, mouseY):
    #If the side balloons reach outside of the canvas, their original position will reset allowing them to reappear.
    if (pinkBalloon.centerY < 0):
        pinkBalloon.centerY=450
        darkGreenBalloon.centerY=450
        line6.y1=475
        line6.y2=500
        line7.y1=475
        line7.y2=500
    #If any of the balloons on the first page are hit, the balloons on the side will fly out from the sides and appear.
    if (redBalloon.hits(mouseX, mouseY)):
        balloonAppear()
    elif (blueBalloon.hits(mouseX, mouseY)):
        balloonAppear()
    elif (purpleBalloon.hits(mouseX, mouseY)):
        balloonAppear()
    elif (greenBalloon.hits(mouseX, mouseY)):
        balloonAppear()
    elif (orangeBalloon.hits(mouseX, mouseY)):
        balloonAppear()
    
    #If you click on an x value greater than 350, the page will switch to the second page and remove the first page.
    if (mouseX >= 350):
        firstPageVisibility(False)
        redBalloon.visible=False
        blueBalloon.visible=False
        greenBalloon.visible=False
        purpleBalloon.visible=False
        orangeBalloon.visible=False
        pinkBalloon.visible=False
        darkGreenBalloon.visible=False
        line6.visible=False
        line7.visible=False
        pinkBalloon.toBack()
        darkGreenBalloon.toBack()
        secondPageVisibility(True)
        secondPage.toFront()
        starOnSecondPage.visible=True
        starOnSecondPage.toFront()
        #If you click on the star on the second page, the stars will fall down from the sky
    if (starOnSecondPage.hits(mouseX, mouseY)):
        star1.visible=True
        star2.visible=True
        star3.visible=True
        star4.visible=True
        star1.toFront()
        star2.toFront()
        star3.toFront()
        star4.toFront()
        star1.centerY+=50
        star2.centerY+=50
        star3.centerY+=50
        star4.centerY+=50
        #If the stars reach a certain Y value greater than 400, the stars' positions will reset and allow for them to reappear again.
        if (star1.centerY>=400):
            star1.centerY=-50
            star2.centerY=-50
            star3.centerY=-50
            star4.centerY=-50
    
    #If you are on the second page and click an x value less than 50, it will switch you back to the first page.    
    if ((mouseX<= 50)):
        redBalloon.visible=True
        blueBalloon.visible=True
        greenBalloon.visible=True
        purpleBalloon.visible=True
        orangeBalloon.visible=True
        pinkBalloon.visible=True
        darkGreenBalloon.visible=True
        line6.visible=True
        line7.visible=True
        pinkBalloon.toFront()
        darkGreenBalloon.toFront()
        secondPageVisibility(False)
        secondPage.toBack()
        starOnSecondPage.visible=False
        starOnSecondPage.toBack()
        balloonLines(200, 250)
        star1.centerY=-50
        star2.centerY=-50
        star3.centerY=-50
        star4.centerY=-50
        star1.fill='gold'
        star2.fill='gold'
        star3.fill='gold'
        star4.fill='gold'
        star1.rotateAngle=0
        star2.rotateAngle=0
        star3.rotateAngle=0
        star4.rotateAngle=0
        firstPageVisibility(True)
        
#If you move your mouse, the stars on the second page will also rotate their angle and rotate whenever you move your mouse.
def onMouseMove(mouseX, mouseY):
    star1.rotateAngle+=15
    star2.rotateAngle+=15
    star3.rotateAngle+=15
    star4.rotateAngle+=15


#Depending on what key you click, the colors of the stars on the second page will also change corresponding to the key you click.
def onKeyPress(key):
    if (key == 'b'):
        star1.fill='blue'
        star2.fill='blue'
        star3.fill='blue'
        star4.fill='blue'
    elif (key == 'r'):
        star1.fill='red'
        star2.fill='red'
        star3.fill='red'
        star4.fill='red'
    elif (key == 'p'):
        star1.fill='purple'
        star2.fill='purple'
        star3.fill='purple'
        star4.fill='purple'
    elif (key =='w'):
        star1.fill='white'
        star2.fill='white'
        star3.fill='white'
        star4.fill='white'
    elif (key =='g'):
        star1.fill='green'
        star2.fill='green'
        star3.fill='green'
        star4.fill='green'
    elif (key =='o'):
        star1.fill='orange'
        star2.fill='orange'
        star3.fill='orange'
        star4.fill='orange'
    else:
        star1.fill='gold'
        star2.fill='gold'
        star3.fill='gold'
        star4.fill='gold'
