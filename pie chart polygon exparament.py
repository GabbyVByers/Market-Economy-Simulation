import os, pygame.gfxdraw, pygame, math, random, time
pygame.init()

DisplayX, DisplayY = 1440,900
win = pygame.display.set_mode((DisplayX, DisplayY))
pygame.display.set_caption("template")

White = (255,255,255)
Black = (0,0,0)
Blue = (0,0,255)
Green = (0,200,0)
Light_Green = (100,255,100)
Red = (255,0,0)
Dark_Red = (100,0,0)
Light_Blue = (0,255,255)
Purple = (255,0,255)
Yellow = (255,255,0)
Gray = (150,150,150)
Dark_Gray = (40,40,40)
Dark_Gray1 = (100,100,100)
Dark_Gray2 = (80,80,80)
Brown = (139,69,19)

font = pygame.font.SysFont('courier', 20, True) #Bold = True

Supply = 30
Demand = 30
Price = 15
Totalolly = 150
poop, cum, rum = 320, 320, 200

def Game():
    win.fill(Black)

def PieChart(v1, v2, v3, cx, cy, r):
    angle1 = round(v1*720/(v1+v2+v3)) #Increment is every 0.5 degrees
    p1 = [(cx, cy)]
    for n in range(0,angle1):
        x = cx + round(r*math.cos(n*math.pi/360))
        y = cy + round(r*math.sin(n*math.pi/360))
        p1.append((x, y))
    if len(p1) > 2:
        pygame.draw.polygon(win, Blue, p1)
        
    angle2 = round(v2*720/(v1+v2+v3))
    p2 = [(cx, cy)]
    for n in range(angle1,angle1+angle2):
        x = cx + round(r*math.cos(n*math.pi/360))
        y = cy + round(r*math.sin(n*math.pi/360))
        p2.append((x, y))
    if len(p2) > 2:
        pygame.draw.polygon(win, Green, p2)

    angle3 = round(v3*720/(v1+v2+v3))
    p3 = [(cx, cy)]
    for n in range(angle1+angle2,angle1+angle2+angle3):
        x = cx + round(r*math.cos(n*math.pi/360))
        y = cy + round(r*math.sin(n*math.pi/360))
        p3.append((x, y))
    if len(p3) > 2:
        pygame.draw.polygon(win, Yellow, p3)

run = True
while run == True:
    #start_time = time.time()

    MouseX, MouseY = pygame.mouse.get_pos()
    MouseLeft, MouseScroll, MouseRight = pygame.mouse.get_pressed()
    Mouse_RelX, Mouse_RelY = pygame.mouse.get_rel()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    
    Game()
    PieChart(Supply, Demand, Price, poop, cum, rum)
    pygame.display.update()
    #FPS = 1.0 / (time.time() - start_time)
    
pygame.quit()

#TEXT = font.render("Hello World!", 1, Black)
#win.blit(TEXT, (X, Y))





































































