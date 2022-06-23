from graphics import *
import time
import random
random.seed()

G='Khaki4'
Y='DarkGoldenRod3'
O = 'Tomato2'
B = 'Black'
col_tot = 15

col0_15 = [[0,0,0.75,8,-0.75,G,B,B,B,B,B,B,O],
           [1,1,0.75,8,-0.75,G,B,Y,B,B,B,O,B],
           [2,2,0.75,8,-0.75,G,G,B,Y,B,O,B,B],    #First 2 G blink together
           [3,3,0.75,8,-0.75,G,B,B,B,Y,B,B,O],
           [4,4,0.75,8,-0.75,G,B,Y,B,B,B,O,B],
           [5,5,0.75,8,-0.75,G,B,B,Y,B,O,B,B],
           [6,6,0.75,8,-0.75,G,B,B,B,Y,B,B,O],
           [7,7,0.75,8,-0.75,G,B,Y,B,B,O,B,B],
           [8,8,0.75,8,-0.75,G,B,B,Y,B,O,B,B],
           [9,9,0.75,8,-0.75,G,B,B,B,Y,B,B,O],
           [10,10,0.75,8,-0.75,G,B,Y,B,B,B,O,B],
           [11,11,0.75,8,-0.75,G,B,B,Y,B,O,B,B],
           [12,12,0.75,8,-0.75,G,B,B,O,B,B,B,O],
           [13,13,0.75,8,-0.75,G,B,B,B,O,B,O,B],
           [14,14,0.75,8,-0.75,G,Y,B,Y,B,O,B,B], #(thinner).  GY blink together
           [15,15,15,3,15.35,G,Y,O,B,B,B,B,B]]   #Right most verticals x3

win = GraphWin('Star Trek TOS Computer',1350,400) #Define window OG size 1550,400
win.setBackground('Black') #set background color
win.setCoords(0,-12,16,2) #start (xll,yll,xur,yur) (0,-12,16,1)
prob1=0.6 #probabilities
prob2=0.8
lites_per_col = 18 #rectangles / column
disp = [None]*20#list of rectangle commands/spock's display

def win_setup():
    global d                         #var for far right column
    for x in range(0,20):            #fill list / matrix
        disp[x] = [None]*lites_per_col  #list of lists (lites_per_col)
    for x in range(0,15):         #data down
        for y in range(5,13):          #data across
        #x+q horiz size, y+r vert size. Rectangle command list
            disp[x][y+5] = Rectangle(Point(x,-y+5),Point(x+.75,-y+5+-.75))
            disp[x][y+5].draw(win)  #draw color/display
    d = x+1             #d=x coord for right column
    disp[x+1][5] = Rectangle(Point(15,-1.8),Point(15.35,0.85))
    disp[x+1][5].draw(win)
    disp[x+1][6] = Rectangle(Point(15,-4.7),Point(15.35,-2.1))
    disp[x+1][6].draw(win)
    disp[x+1][7] = Rectangle(Point(15,-8),Point(15.35,-5))
    disp[x+1][7].draw(win)
    return()
def blink_lites2(): #blink lites at random
    global d
    a = int(random.random()*16)     #column col0_15[[x]
    b = int(random.random()*8)+5    #column col0_15[0] is number, skip over
    c = random.random()
    clr = col0_15[a][b]
    #if, elif, else == Case-like statement
    if True:
        if a in (2,14):     #3rd col, top 2 lites blink together
            if a == 2:      #if 2 use green for top pair
                col_a = G; col_b = G
            else:           #if 14 use green/yellow for top pair
                col_a = G; col_b = Y
            if b in (5,6):
                if c > prob1: #if prob > p, blink off
                    disp[a][5+5].setFill('Black')   #blink top pair off
                    disp[a][6+5].setFill('Black')   #blink top pair off
                else:   #if prob < p, blink on
                    disp[a][5+5].setFill(col_a)
                    disp[a][5+5].setFill(col_b)
            elif c > prob2: #if not 5 or 6, different prob
                disp[a][b+5].setFill('Black') #off
            else:
                disp[a][b+5].setFill(clr)   #on
        elif a == 15:   #right most 3 vertical columns
            e = random.randint(5,7)
            clr2 = col0_15[15][e]
            if disp[d][e] != None:
                if c > prob2:
                    disp[d][e].setFill('Black')
                else:
                    disp[d][e].setFill(clr2)
        else: #regular blinking without any exceptions
            if disp[a][b+5] != None:
                if c > prob1:
                    disp[a][b+5].setFill('Black')   #blink off
                else:
                    disp[a][b+5].setFill(clr)   #blink on
        return()
####MAIN####
def visual():
    win_setup()
    for loop in range(0,200000):
        blink_lites2()
        time.sleep(.007)
        blink_lites2()
    win.getMouse()
    win.close()
    print('Done')
visual()