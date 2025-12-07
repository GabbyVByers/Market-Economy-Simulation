import os, pygame.gfxdraw, pygame, math, random
pygame.init()

DisplayX, DisplayY = 1840,1040
win = pygame.display.set_mode((DisplayX, DisplayY))
pygame.display.set_caption("Simulation of a Market Economy with two Goods")

White = (255,255,255)
Black = (0,0,0)
Blue = (150,150,255)
Green = (0,200,0)
Light_Green = (100,255,100)
Red = (255,80,80)
Dark_Red = (100,0,0)
Light_Blue = (0,255,255)
Purple = (255,0,255)
Yellow = (255,180,0)
Gray = (150,150,150)
Dark_Gray = (40,40,40)
Dark_Gray1 = (100,100,100)
Dark_Gray2 = (80,80,80)
Brown = (139,69,19)
GraphColour = (50,50,50)
NumberColour = (150,150,150)

PrintDebugInformation = False

WageRate = 1000
SupplyLabourInteger = 500
SupplyLabour = SupplyLabourInteger / 100
LabourIncome = 0
AgentSpending = 0
LabourA = 0
LabourB = 0
ProportionLabourA = 500
ProportionLabourB = 500
SupplyA = 0
SupplyB = 0
DemandA = 0
DemandB = 0
PriceA = 500
PriceB = 500
BudgetA = 500
BudgetB = 500
MarginalUtilityA = 0
MarginalUtilityB = 0
ProfitabilityA = 0
ProfitabilityB = 0
MarginalUtilityMoneySpent = 0
MarginalUtilityMoneySpentA = 0
MarginalUtilityMoneySpentB = 0
MarginalDisUtilityMoneyEarned = 0
MarginalWage = 1
RateChangePrice = 1.01
MarginalProductionA = 0
MarginalProductionB = 0
MarginalLabour = 0.01

################################

GraphWidth = 300
GraphHeight = 200
VerticalSpacing = 80
HorizontalSpacing = 80

GraphX1 = HorizontalSpacing
GraphY1 = VerticalSpacing

GraphX2 = HorizontalSpacing
GraphY2 = (2*VerticalSpacing)+GraphHeight

GraphX3 = HorizontalSpacing
GraphY3 = (3*VerticalSpacing)+(2*GraphHeight)

GraphX4 = (2*HorizontalSpacing)+GraphWidth
GraphY4 = VerticalSpacing

GraphX5 = (2*HorizontalSpacing)+GraphWidth
GraphY5 = (2*VerticalSpacing)+GraphHeight

GraphX6 = (2*HorizontalSpacing)+GraphWidth
GraphY6 = (3*VerticalSpacing)+(2*GraphHeight)

GraphX7 = (3*HorizontalSpacing)+(2*GraphWidth)
GraphY7 = (2*VerticalSpacing)+GraphHeight

GraphX8 = (3*HorizontalSpacing)+(2*GraphWidth)
GraphY8 = (3*VerticalSpacing)+(2*GraphHeight)

font = pygame.font.SysFont('times new roman', 30)
font3 = pygame.font.SysFont('times new roman', 25)
font2 = pygame.font.SysFont('courier', 15)
font1 = pygame.font.SysFont('courier', 18)
font4 = pygame.font.SysFont('courier', 25)

PriceATEXT = font.render("Price A", 1, Blue)
PriceBTEXT = font.render("Price B", 1, Red)

SupplyATEXT = font.render("Supply A", 1, Blue)
DemandATEXT = font.render("Demand A", 1, Red)

SupplyBTEXT = font.render("Supply B", 1, Blue)
DemandBTEXT = font.render("Demand B", 1, Red)

SupplyLabourTEXT = font.render("Supply Labour", 1, Blue)

BudgetATEXT = font.render("Budget %A", 1, Blue)
BudgetBTEXT = font.render("Budget %B", 1, Red)

LabourATEXT = font.render("Labour %A", 1, Blue)
LabourBTEXT = font.render("Labour %B", 1, Red)

MarginalUtilityMoneyATEXT = font.render("MU$A", 1, Blue)
MarginalUtilityMoneyBTEXT = font.render("MU$B", 1, Red)
MarginalDisUtilityMoneyWageTEXT = font.render("MDU$", 1, Yellow)

MarginalValueLabourATEXT = font.render("ΔQA*PA", 1, Blue)
MarginalValueLabourBTEXT = font.render("ΔQB*PB", 1, Red)

PriceGraphScale = 800
SupplyDemandAGraphScale = 50
SupplyDemandBGraphScale = 80
SupplyLabourGraphScale = 16
BudgetGraphScale = 100
LabourGraphScale = 100
MarginalUtilityMoneyGraphScale = .15
MarginalValueLabourGraphScale = 20

PriceLable5 = 0
PriceLable4 = int(PriceGraphScale / 4)
PriceLable3 = int(PriceGraphScale / 2)
PriceLable2 = int(3 * PriceGraphScale / 4)
PriceLable1 = PriceGraphScale
PriceLable1TEXT = font2.render(str(PriceLable1), 1, NumberColour)
PriceLable2TEXT = font2.render(str(PriceLable2), 1, NumberColour)
PriceLable3TEXT = font2.render(str(PriceLable3), 1, NumberColour)
PriceLable4TEXT = font2.render(str(PriceLable4), 1, NumberColour)
PriceLable5TEXT = font2.render(str(PriceLable5), 1, NumberColour)

SupplyDemandALable5 = 0
SupplyDemandALable4 = int(SupplyDemandAGraphScale / 4)
SupplyDemandALable3 = int(SupplyDemandAGraphScale / 2)
SupplyDemandALable2 = int(3 * SupplyDemandAGraphScale / 4)
SupplyDemandALable1 = SupplyDemandAGraphScale
SupplyDemandALable1TEXT = font2.render(str(SupplyDemandALable1), 1, NumberColour)
SupplyDemandALable2TEXT = font2.render(str(SupplyDemandALable2), 1, NumberColour)
SupplyDemandALable3TEXT = font2.render(str(SupplyDemandALable3), 1, NumberColour)
SupplyDemandALable4TEXT = font2.render(str(SupplyDemandALable4), 1, NumberColour)
SupplyDemandALable5TEXT = font2.render(str(SupplyDemandALable5), 1, NumberColour)

SupplyDemandBLable5 = 0
SupplyDemandBLable4 = int(SupplyDemandBGraphScale / 4)
SupplyDemandBLable3 = int(SupplyDemandBGraphScale / 2)
SupplyDemandBLable2 = int(3 * SupplyDemandBGraphScale / 4)
SupplyDemandBLable1 = SupplyDemandBGraphScale
SupplyDemandBLable1TEXT = font2.render(str(SupplyDemandBLable1), 1, NumberColour)
SupplyDemandBLable2TEXT = font2.render(str(SupplyDemandBLable2), 1, NumberColour)
SupplyDemandBLable3TEXT = font2.render(str(SupplyDemandBLable3), 1, NumberColour)
SupplyDemandBLable4TEXT = font2.render(str(SupplyDemandBLable4), 1, NumberColour)
SupplyDemandBLable5TEXT = font2.render(str(SupplyDemandBLable5), 1, NumberColour)

SupplyLabourLable5 = 0
SupplyLabourLable4 = int(SupplyLabourGraphScale / 4)
SupplyLabourLable3 = int(SupplyLabourGraphScale / 2)
SupplyLabourLable2 = int(3 * SupplyLabourGraphScale / 4)
SupplyLabourLable1 = SupplyLabourGraphScale
SupplyLabourLable1TEXT = font2.render(str(SupplyLabourLable1), 1, NumberColour)
SupplyLabourLable2TEXT = font2.render(str(SupplyLabourLable2), 1, NumberColour)
SupplyLabourLable3TEXT = font2.render(str(SupplyLabourLable3), 1, NumberColour)
SupplyLabourLable4TEXT = font2.render(str(SupplyLabourLable4), 1, NumberColour)
SupplyLabourLable5TEXT = font2.render(str(SupplyLabourLable5), 1, NumberColour)

BudgetLable5 = 0
BudgetLable4 = int(BudgetGraphScale / 4)
BudgetLable3 = int(BudgetGraphScale / 2)
BudgetLable2 = int(3 * BudgetGraphScale / 4)
BudgetLable1 = BudgetGraphScale
BudgetLable1TEXT = font2.render(str(BudgetLable1), 1, NumberColour)
BudgetLable2TEXT = font2.render(str(BudgetLable2), 1, NumberColour)
BudgetLable3TEXT = font2.render(str(BudgetLable3), 1, NumberColour)
BudgetLable4TEXT = font2.render(str(BudgetLable4), 1, NumberColour)
BudgetLable5TEXT = font2.render(str(BudgetLable5), 1, NumberColour)

LabourLable5 = 0
LabourLable4 = int(LabourGraphScale / 4)
LabourLable3 = int(LabourGraphScale / 2)
LabourLable2 = int(3 * LabourGraphScale / 4)
LabourLable1 = LabourGraphScale
LabourLable1TEXT = font2.render(str(LabourLable1), 1, NumberColour)
LabourLable2TEXT = font2.render(str(LabourLable2), 1, NumberColour)
LabourLable3TEXT = font2.render(str(LabourLable3), 1, NumberColour)
LabourLable4TEXT = font2.render(str(LabourLable4), 1, NumberColour)
LabourLable5TEXT = font2.render(str(LabourLable5), 1, NumberColour)

MUMoneyLable5 = 0
MUMoneyLable4 = round(MarginalUtilityMoneyGraphScale / 4,4)
MUMoneyLable3 = round(MarginalUtilityMoneyGraphScale / 2,4)
MUMoneyLable2 = round(3 * MarginalUtilityMoneyGraphScale / 4,4)
MUMoneyLable1 = MarginalUtilityMoneyGraphScale
MUMoneyLable1TEXT = font2.render(str(MUMoneyLable1), 1, NumberColour)
MUMoneyLable2TEXT = font2.render(str(MUMoneyLable2), 1, NumberColour)
MUMoneyLable3TEXT = font2.render(str(MUMoneyLable3), 1, NumberColour)
MUMoneyLable4TEXT = font2.render(str(MUMoneyLable4), 1, NumberColour)
MUMoneyLable5TEXT = font2.render(str(MUMoneyLable5), 1, NumberColour)

LabourValueLable5 = 0
LabourValueLable4 = int(MarginalValueLabourGraphScale / 4)
LabourValueLable3 = int(MarginalValueLabourGraphScale / 2)
LabourValueLable2 = int(3 * MarginalValueLabourGraphScale / 4)
LabourValueLable1 = MarginalValueLabourGraphScale
LabourValueLable1TEXT = font2.render(str(LabourValueLable1), 1, NumberColour)
LabourValueLable2TEXT = font2.render(str(LabourValueLable2), 1, NumberColour)
LabourValueLable3TEXT = font2.render(str(LabourValueLable3), 1, NumberColour)
LabourValueLable4TEXT = font2.render(str(LabourValueLable4), 1, NumberColour)
LabourValueLable5TEXT = font2.render(str(LabourValueLable5), 1, NumberColour)

PriceAPoints = [(GraphX1,GraphY1)]
PriceBPoints = [(GraphX1,GraphY1)]
SupplyAPoints = [(GraphX2,GraphY2)]
DemandAPoints = [(GraphX2,GraphY2)]
SupplyBPoints = [(GraphX3,GraphY3)]
DemandBPoints = [(GraphX3,GraphY3)]
SupplyLabourPoints = [(GraphX4,GraphY4)]
BudgetAPoints = [(GraphX5,GraphY5)]
BudgetBPoints = [(GraphX5,GraphY5)]
LabourAPoints = [(GraphX6,GraphY6)]
LabourBPoints = [(GraphX6,GraphY6)]
MarginalUtilitySpendMoneyAPoints = [(GraphX7,GraphY7)]
MarginalUtilitySpendMoneyBPoints = [(GraphX7,GraphY7)]
MarginalDisUtilityEarnMoneyPoints = [(GraphX7,GraphY7)]
MarginlValueLabourAPoints = [(GraphX8,GraphY8)]
MarginlValueLabourBPoints = [(GraphX8,GraphY8)]

##############################

SliderWidth = 400
SliderHeight = 5
SliderVerticalSpacing = 100
SliderHorizontalDisplacment = SliderWidth + 100
SliderSelectionMargin = 45

SliderPosX1 = DisplayX-SliderHorizontalDisplacment
SliderPosX2 = DisplayX-SliderHorizontalDisplacment
SliderPosX3 = DisplayX-SliderHorizontalDisplacment
SliderPosX4 = DisplayX-SliderHorizontalDisplacment
SliderPosX5 = DisplayX-SliderHorizontalDisplacment

SliderScaler1 = 1
SliderScaler2 = 1
SliderScaler3 = 1
SliderScaler4 = 1
SliderScaler5 = 1

MDULSliderTEXT = font3.render("Scale Marginal Dis-Utility of Labour", 1, White)
MUASliderTEXT = font3.render("Scale Marginal Utility Commodity 'A'", 1, White)
MUBSliderTEXT = font3.render("Scale Marginal Utility Commodity 'B'", 1, White)
PFASliderTEXT = font3.render("Scale Production Function 'A'", 1, White)
PFBSliderTEXT = font3.render("Scale Production Function 'B'", 1, White)

SliderTextDisplacement = -35

def Game():
    win.fill(Black)

def DrawSliders():
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment,SliderVerticalSpacing,SliderWidth,SliderHeight), 0)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment,2*SliderVerticalSpacing,SliderWidth,SliderHeight), 0)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment,3*SliderVerticalSpacing,SliderWidth,SliderHeight), 0)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment,4*SliderVerticalSpacing,SliderWidth,SliderHeight), 0)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment,5*SliderVerticalSpacing,SliderWidth,SliderHeight), 0)
    pygame.draw.rect(win, White, (SliderPosX1,SliderVerticalSpacing,SliderHeight,SliderHeight), 0)
    pygame.draw.rect(win, White, (SliderPosX2,2*SliderVerticalSpacing,SliderHeight,SliderHeight), 0)
    pygame.draw.rect(win, White, (SliderPosX3,3*SliderVerticalSpacing,SliderHeight,SliderHeight), 0)
    pygame.draw.rect(win, White, (SliderPosX4,4*SliderVerticalSpacing,SliderHeight,SliderHeight), 0)
    pygame.draw.rect(win, White, (SliderPosX5,5*SliderVerticalSpacing,SliderHeight,SliderHeight), 0)
    win.blit(MDULSliderTEXT, (DisplayX-SliderHorizontalDisplacment,SliderVerticalSpacing+SliderTextDisplacement))
    win.blit(MUASliderTEXT, (DisplayX-SliderHorizontalDisplacment,2*SliderVerticalSpacing+SliderTextDisplacement))
    win.blit(MUBSliderTEXT, (DisplayX-SliderHorizontalDisplacment,3*SliderVerticalSpacing+SliderTextDisplacement))
    win.blit(PFASliderTEXT, (DisplayX-SliderHorizontalDisplacment,4*SliderVerticalSpacing+SliderTextDisplacement))
    win.blit(PFBSliderTEXT, (DisplayX-SliderHorizontalDisplacment,5*SliderVerticalSpacing+SliderTextDisplacement))

    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin,   SliderVerticalSpacing-SliderSelectionMargin, 2*SliderSelectionMargin+SliderWidth, 2*SliderSelectionMargin), 1)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin, 2*SliderVerticalSpacing-SliderSelectionMargin, 2*SliderSelectionMargin+SliderWidth, 2*SliderSelectionMargin), 1)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin, 3*SliderVerticalSpacing-SliderSelectionMargin, 2*SliderSelectionMargin+SliderWidth, 2*SliderSelectionMargin), 1)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin, 4*SliderVerticalSpacing-SliderSelectionMargin, 2*SliderSelectionMargin+SliderWidth, 2*SliderSelectionMargin), 1)
    pygame.draw.rect(win, GraphColour, (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin, 5*SliderVerticalSpacing-SliderSelectionMargin, 2*SliderSelectionMargin+SliderWidth, 2*SliderSelectionMargin), 1)

    SliderNumber1TEXT = font4.render("+"+str(round(500*SliderScaler1))+"%", 1, Green)
    SliderNumber2TEXT = font4.render("+"+str(round(500*SliderScaler2))+"%", 1, Green)
    SliderNumber3TEXT = font4.render("+"+str(round(500*SliderScaler3))+"%", 1, Green)
    SliderNumber4TEXT = font4.render("+"+str(round(300*SliderScaler4))+"%", 1, Green)
    SliderNumber5TEXT = font4.render("+"+str(round(300*SliderScaler5))+"%", 1, Green)

    win.blit(SliderNumber1TEXT, (SliderPosX1,SliderVerticalSpacing+10))
    win.blit(SliderNumber2TEXT, (SliderPosX2,2*SliderVerticalSpacing+10))
    win.blit(SliderNumber3TEXT, (SliderPosX3,3*SliderVerticalSpacing+10))
    win.blit(SliderNumber4TEXT, (SliderPosX4,4*SliderVerticalSpacing+10))
    win.blit(SliderNumber5TEXT, (SliderPosX5,5*SliderVerticalSpacing+10))
    

def DrawGraphs():
    #draw price graph
    pygame.draw.rect(win, GraphColour, (GraphX1,GraphY1,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX1,GraphY1+int(GraphHeight/4)), (GraphX1+GraphWidth-1,GraphY1+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX1,GraphY1+int(2*GraphHeight/4)), (GraphX1+GraphWidth-1,GraphY1+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX1,GraphY1+int(3*GraphHeight/4)), (GraphX1+GraphWidth-1,GraphY1+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX1+int(GraphWidth/4),GraphY1), (GraphX1+int(GraphWidth/4),GraphY1+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX1+int(2*GraphWidth/4),GraphY1), (GraphX1+int(2*GraphWidth/4),GraphY1+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX1+int(3*GraphWidth/4),GraphY1), (GraphX1+int(3*GraphWidth/4),GraphY1+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, PriceAPoints, 1)
    pygame.draw.lines(win, Red, False, PriceBPoints, 1)
    win.blit(PriceATEXT, (GraphX1, GraphY1-35))
    win.blit(PriceBTEXT, (GraphX1+150, GraphY1-35))
    win.blit(PriceLable1TEXT, (GraphX1+GraphWidth+3,-7+GraphY1))
    win.blit(PriceLable2TEXT, (GraphX1+GraphWidth+3,-7+GraphY1+int(GraphHeight/4)))
    win.blit(PriceLable3TEXT, (GraphX1+GraphWidth+3,-7+GraphY1+int(GraphHeight/2)))
    win.blit(PriceLable4TEXT, (GraphX1+GraphWidth+3,-7+GraphY1+int(3*GraphHeight/4)))
    win.blit(PriceLable5TEXT, (GraphX1+GraphWidth+3,-7+GraphY1+GraphHeight))
    NumberPriceAText = font1.render("$"+str(round(PriceA,2)), 1, Blue)
    win.blit(NumberPriceAText, (GraphX1,GraphY1))
    NumberPriceBText = font1.render("$"+str(round(PriceB,2)), 1, Red)
    win.blit(NumberPriceBText, (GraphX1+150,GraphY1))
    #draw supply and demand A
    pygame.draw.rect(win, GraphColour, (GraphX2,GraphY2,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX2,GraphY2+int(GraphHeight/4)), (GraphX2+GraphWidth-1,GraphY2+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX2,GraphY2+int(2*GraphHeight/4)), (GraphX2+GraphWidth-1,GraphY2+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX2,GraphY2+int(3*GraphHeight/4)), (GraphX2+GraphWidth-1,GraphY2+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX2+int(GraphWidth/4),GraphY2), (GraphX2+int(GraphWidth/4),GraphY2+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX2+int(2*GraphWidth/4),GraphY2), (GraphX2+int(2*GraphWidth/4),GraphY2+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX2+int(3*GraphWidth/4),GraphY2), (GraphX2+int(3*GraphWidth/4),GraphY2+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, SupplyAPoints, 1)
    pygame.draw.lines(win, Red, False, DemandAPoints, 1)
    win.blit(SupplyATEXT, (GraphX2, GraphY2-35))
    win.blit(DemandATEXT, (GraphX2+150, GraphY2-35))
    win.blit(SupplyDemandALable1TEXT, (GraphX2+GraphWidth+3,-7+GraphY2))
    win.blit(SupplyDemandALable2TEXT, (GraphX2+GraphWidth+3,-7+GraphY2+int(GraphHeight/4)))
    win.blit(SupplyDemandALable3TEXT, (GraphX2+GraphWidth+3,-7+GraphY2+int(GraphHeight/2)))
    win.blit(SupplyDemandALable4TEXT, (GraphX2+GraphWidth+3,-7+GraphY2+int(3*GraphHeight/4)))
    win.blit(SupplyDemandALable5TEXT, (GraphX2+GraphWidth+3,-7+GraphY2+GraphHeight))
    NumberSupplyAText = font1.render(str(round(SupplyA,2)), 1, Blue)
    win.blit(NumberSupplyAText, (GraphX2,GraphY2))
    NumberDemandAText = font1.render(str(round(DemandA,2)), 1, Red)
    win.blit(NumberDemandAText, (GraphX2+150,GraphY2))
    #draw supply and demand B
    pygame.draw.rect(win, GraphColour, (GraphX3,GraphY3,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX3,GraphY3+int(GraphHeight/4)), (GraphX3+GraphWidth-1,GraphY3+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX3,GraphY3+int(2*GraphHeight/4)), (GraphX3+GraphWidth-1,GraphY3+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX3,GraphY3+int(3*GraphHeight/4)), (GraphX3+GraphWidth-1,GraphY3+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX3+int(GraphWidth/4),GraphY3), (GraphX3+int(GraphWidth/4),GraphY3+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX3+int(2*GraphWidth/4),GraphY3), (GraphX3+int(2*GraphWidth/4),GraphY3+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX3+int(3*GraphWidth/4),GraphY3), (GraphX3+int(3*GraphWidth/4),GraphY3+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, SupplyBPoints, 1)
    pygame.draw.lines(win, Red, False, DemandBPoints, 1)
    win.blit(SupplyBTEXT, (GraphX3, GraphY3-35))
    win.blit(DemandBTEXT, (GraphX3+150, GraphY3-35))
    win.blit(SupplyDemandBLable1TEXT, (GraphX3+GraphWidth+3,-7+GraphY3))
    win.blit(SupplyDemandBLable2TEXT, (GraphX3+GraphWidth+3,-7+GraphY3+int(GraphHeight/4)))
    win.blit(SupplyDemandBLable3TEXT, (GraphX3+GraphWidth+3,-7+GraphY3+int(GraphHeight/2)))
    win.blit(SupplyDemandBLable4TEXT, (GraphX3+GraphWidth+3,-7+GraphY3+int(3*GraphHeight/4)))
    win.blit(SupplyDemandBLable5TEXT, (GraphX3+GraphWidth+3,-7+GraphY3+GraphHeight))
    NumberSupplyBText = font1.render(str(round(SupplyB,2)), 1, Blue)
    win.blit(NumberSupplyBText, (GraphX3,GraphY3))
    NumberDemandBText = font1.render(str(round(DemandB,2)), 1, Red)
    win.blit(NumberDemandBText, (GraphX3+150,GraphY3))
    #draw supply labour
    pygame.draw.rect(win, GraphColour, (GraphX4,GraphY4,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX4,GraphY4+int(GraphHeight/4)), (GraphX4+GraphWidth-1,GraphY4+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX4,GraphY4+int(2*GraphHeight/4)), (GraphX4+GraphWidth-1,GraphY4+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX4,GraphY4+int(3*GraphHeight/4)), (GraphX4+GraphWidth-1,GraphY4+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX4+int(GraphWidth/4),GraphY4), (GraphX4+int(GraphWidth/4),GraphY4+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX4+int(2*GraphWidth/4),GraphY4), (GraphX4+int(2*GraphWidth/4),GraphY4+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX4+int(3*GraphWidth/4),GraphY4), (GraphX4+int(3*GraphWidth/4),GraphY4+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, SupplyLabourPoints, 1)
    win.blit(SupplyLabourTEXT, (GraphX4, GraphY4-35))
    win.blit(SupplyLabourLable1TEXT, (GraphX4+GraphWidth+3,-7+GraphY4))
    win.blit(SupplyLabourLable2TEXT, (GraphX4+GraphWidth+3,-7+GraphY4+int(GraphHeight/4)))
    win.blit(SupplyLabourLable3TEXT, (GraphX4+GraphWidth+3,-7+GraphY4+int(GraphHeight/2)))
    win.blit(SupplyLabourLable4TEXT, (GraphX4+GraphWidth+3,-7+GraphY4+int(3*GraphHeight/4)))
    win.blit(SupplyLabourLable5TEXT, (GraphX4+GraphWidth+3,-7+GraphY4+GraphHeight))
    NumberSupplyLabourText = font1.render(str(round(SupplyLabour,2)), 1, Blue)
    win.blit(NumberSupplyLabourText, (GraphX4,GraphY4))
    #draw budget allocation
    pygame.draw.rect(win, GraphColour, (GraphX5,GraphY5,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX5,GraphY5+int(GraphHeight/4)), (GraphX5+GraphWidth-1,GraphY5+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX5,GraphY5+int(2*GraphHeight/4)), (GraphX5+GraphWidth-1,GraphY5+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX5,GraphY5+int(3*GraphHeight/4)), (GraphX5+GraphWidth-1,GraphY5+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX5+int(GraphWidth/4),GraphY5), (GraphX5+int(GraphWidth/4),GraphY5+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX5+int(2*GraphWidth/4),GraphY5), (GraphX5+int(2*GraphWidth/4),GraphY5+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX5+int(3*GraphWidth/4),GraphY5), (GraphX5+int(3*GraphWidth/4),GraphY5+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, BudgetAPoints, 1)
    pygame.draw.lines(win, Red, False, BudgetBPoints, 1)
    win.blit(BudgetATEXT, (GraphX5, GraphY5-35))
    win.blit(BudgetBTEXT, (GraphX5+160, GraphY5-35))
    win.blit(BudgetLable1TEXT, (GraphX5+GraphWidth+3,-7+GraphY5))
    win.blit(BudgetLable2TEXT, (GraphX5+GraphWidth+3,-7+GraphY5+int(GraphHeight/4)))
    win.blit(BudgetLable3TEXT, (GraphX5+GraphWidth+3,-7+GraphY5+int(GraphHeight/2)))
    win.blit(BudgetLable4TEXT, (GraphX5+GraphWidth+3,-7+GraphY5+int(3*GraphHeight/4)))
    win.blit(BudgetLable5TEXT, (GraphX5+GraphWidth+3,-7+GraphY5+GraphHeight))
    NumberBudgetAText = font1.render("%"+str(round(BudgetA/10,2)), 1, Blue)
    win.blit(NumberBudgetAText, (GraphX5,GraphY5))
    NumberBudgetBText = font1.render("%"+str(round(BudgetB/10,2)), 1, Red)
    win.blit(NumberBudgetBText, (GraphX5+160,GraphY5))
    #draw labour allocation
    pygame.draw.rect(win, GraphColour, (GraphX6,GraphY6,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX6,GraphY6+int(GraphHeight/4)), (GraphX6+GraphWidth-1,GraphY6+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX6,GraphY6+int(2*GraphHeight/4)), (GraphX6+GraphWidth-1,GraphY6+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX6,GraphY6+int(3*GraphHeight/4)), (GraphX6+GraphWidth-1,GraphY6+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX6+int(GraphWidth/4),GraphY6), (GraphX6+int(GraphWidth/4),GraphY6+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX6+int(2*GraphWidth/4),GraphY6), (GraphX6+int(2*GraphWidth/4),GraphY6+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX6+int(3*GraphWidth/4),GraphY6), (GraphX6+int(3*GraphWidth/4),GraphY6+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, LabourAPoints, 1)
    pygame.draw.lines(win, Red, False, LabourBPoints, 1)
    win.blit(LabourATEXT, (GraphX6, GraphY6-35))
    win.blit(LabourBTEXT, (GraphX6+160, GraphY6-35))
    win.blit(LabourLable1TEXT, (GraphX6+GraphWidth+3,-7+GraphY6))
    win.blit(LabourLable2TEXT, (GraphX6+GraphWidth+3,-7+GraphY6+int(GraphHeight/4)))
    win.blit(LabourLable3TEXT, (GraphX6+GraphWidth+3,-7+GraphY6+int(GraphHeight/2)))
    win.blit(LabourLable4TEXT, (GraphX6+GraphWidth+3,-7+GraphY6+int(3*GraphHeight/4)))
    win.blit(LabourLable5TEXT, (GraphX6+GraphWidth+3,-7+GraphY6+GraphHeight))
    NumberLabourAText = font1.render("%"+str(round(ProportionLabourA/10,2)), 1, Blue)
    win.blit(NumberLabourAText, (GraphX6,GraphY6))
    NumberLabourBText = font1.render("%"+str(round(ProportionLabourB/10,2)), 1, Red)
    win.blit(NumberLabourBText, (GraphX6+160,GraphY6))
    #draw marginal utility moneyA, moneyB, money-wage
    pygame.draw.rect(win, GraphColour, (GraphX7,GraphY7,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX7,GraphY7+int(GraphHeight/4)), (GraphX7+GraphWidth-1,GraphY7+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX7,GraphY7+int(2*GraphHeight/4)), (GraphX7+GraphWidth-1,GraphY7+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX7,GraphY7+int(3*GraphHeight/4)), (GraphX7+GraphWidth-1,GraphY7+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX7+int(GraphWidth/4),GraphY7), (GraphX7+int(GraphWidth/4),GraphY7+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX7+int(2*GraphWidth/4),GraphY7), (GraphX7+int(2*GraphWidth/4),GraphY7+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX7+int(3*GraphWidth/4),GraphY7), (GraphX7+int(3*GraphWidth/4),GraphY7+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, MarginalUtilitySpendMoneyAPoints, 1)
    pygame.draw.lines(win, Red, False, MarginalUtilitySpendMoneyBPoints, 1)
    pygame.draw.lines(win, Yellow, False, MarginalDisUtilityEarnMoneyPoints, 1)
    win.blit(MarginalUtilityMoneyATEXT, (GraphX7, GraphY7-35))
    win.blit(MarginalUtilityMoneyBTEXT, (GraphX7+100, GraphY7-35))
    win.blit(MarginalDisUtilityMoneyWageTEXT, (GraphX7+196, GraphY7-35))
    win.blit(MUMoneyLable1TEXT, (GraphX7+GraphWidth+3,-7+GraphY7))
    win.blit(MUMoneyLable2TEXT, (GraphX7+GraphWidth+3,-7+GraphY7+int(GraphHeight/4)))
    win.blit(MUMoneyLable3TEXT, (GraphX7+GraphWidth+3,-7+GraphY7+int(GraphHeight/2)))
    win.blit(MUMoneyLable4TEXT, (GraphX7+GraphWidth+3,-7+GraphY7+int(3*GraphHeight/4)))
    win.blit(MUMoneyLable5TEXT, (GraphX7+GraphWidth+3,-7+GraphY7+GraphHeight))
    NumberMUMoneyAText = font1.render(str(round(MarginalUtilityMoneySpentA,6)), 1, Blue)
    win.blit(NumberMUMoneyAText, (GraphX7,GraphY7))
    NumberMUMoneyBText = font1.render(str(round(MarginalUtilityMoneySpentB,6)), 1, Red)
    win.blit(NumberMUMoneyBText, (GraphX7+100,GraphY7))
    NumberMDUEMoneyText = font1.render(str(round(MarginalDisUtilityMoneyEarned,6)), 1, Yellow)
    win.blit(NumberMDUEMoneyText, (GraphX7+196,GraphY7))
    #draw marginal value of labour per market
    pygame.draw.rect(win, GraphColour, (GraphX8,GraphY8,GraphWidth,GraphHeight), 1)
    pygame.draw.line(win, GraphColour, (GraphX8,GraphY8+int(GraphHeight/4)), (GraphX8+GraphWidth-1,GraphY8+int(GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX8,GraphY8+int(2*GraphHeight/4)), (GraphX8+GraphWidth-1,GraphY8+int(2*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX8,GraphY8+int(3*GraphHeight/4)), (GraphX8+GraphWidth-1,GraphY8+int(3*GraphHeight/4)), 1)
    pygame.draw.line(win, GraphColour, (GraphX8+int(GraphWidth/4),GraphY8), (GraphX8+int(GraphWidth/4),GraphY8+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX8+int(2*GraphWidth/4),GraphY8), (GraphX8+int(2*GraphWidth/4),GraphY8+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (GraphX8+int(3*GraphWidth/4),GraphY8), (GraphX8+int(3*GraphWidth/4),GraphY8+GraphHeight-1), 1)
    pygame.draw.lines(win, Blue, False, MarginlValueLabourAPoints, 1)
    pygame.draw.lines(win, Red, False, MarginlValueLabourBPoints, 1)
    win.blit(MarginalValueLabourATEXT, (GraphX8, GraphY8-35))
    win.blit(MarginalValueLabourBTEXT, (GraphX8+150, GraphY8-35))
    win.blit(LabourValueLable1TEXT, (GraphX8+GraphWidth+3,-7+GraphY8))
    win.blit(LabourValueLable2TEXT, (GraphX8+GraphWidth+3,-7+GraphY8+int(GraphHeight/4)))
    win.blit(LabourValueLable3TEXT, (GraphX8+GraphWidth+3,-7+GraphY8+int(GraphHeight/2)))
    win.blit(LabourValueLable4TEXT, (GraphX8+GraphWidth+3,-7+GraphY8+int(3*GraphHeight/4)))
    win.blit(LabourValueLable5TEXT, (GraphX8+GraphWidth+3,-7+GraphY8+GraphHeight))
    NumberLabourValueAText = font1.render("$"+str(round(MarginalValueProductionA,4)), 1, Blue)
    win.blit(NumberLabourValueAText, (GraphX8,GraphY8))
    NumberLabourValueBText = font1.render("$"+str(round(MarginalValueProductionB,4)), 1, Red)
    win.blit(NumberLabourValueBText, (GraphX8+150,GraphY8))

def MarginalDisUtilityLabourFunction(x):
    return ((1 / (-x + 16)) - (1/16)) * 300 * (1 + (5*SliderScaler1))

def MarginalUtilityFunctionA(x):
    return 30 * (0.9 ** x) * (1 + (5*SliderScaler2))
def MarginalUtilityFunctionB(x):
    return 20 * (0.93 ** x) * (1 + (5*SliderScaler3))

def ProductionFunctionA(x):
    return 5 * (x ** 0.5) * (1 + (3*SliderScaler4))
def ProductionFunctionB(x):
    return 9 * (x ** 0.5) * (1 + (3*SliderScaler5))

run = True
while run == True:

    MouseX, MouseY = pygame.mouse.get_pos()
    MouseLeft, MouseScroll, MouseRight = pygame.mouse.get_pressed()
    Mouse_RelX, Mouse_RelY = pygame.mouse.get_rel()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        #Exit Game
        if event.type == pygame.QUIT:
            run = False

    #allocate the supply of labour between A and B
    LabourA = SupplyLabour * (ProportionLabourA / 1000)
    LabourB = SupplyLabour * (ProportionLabourB / 1000)

    #put labour through production function for A and B
    SupplyA = ProductionFunctionA(LabourA)
    SupplyB = ProductionFunctionB(LabourB)

    #labour income
    LabourIncome = SupplyLabour * WageRate

    #demand from budget
    DemandA = (LabourIncome * (BudgetA / 1000)) / PriceA
    DemandB = (LabourIncome * (BudgetB / 1000)) / PriceB

    #marginal utility and disutility
    MarginalUtilityA = MarginalUtilityFunctionA(DemandA)
    MarginalUtilityB = MarginalUtilityFunctionB(DemandB)
    MarginalDisUtilityLabour = MarginalDisUtilityLabourFunction(SupplyLabour)

    #Marginal DisUtility and Utility of Earning and Spending "marginal wage" of Money
    MarginalUtilityMoneySpentA = MarginalUtilityA * (MarginalWage / PriceA)
    MarginalUtilityMoneySpentB = MarginalUtilityB * (MarginalWage / PriceB)
    if (MarginalUtilityMoneySpentA > MarginalUtilityMoneySpentB):
        MarginalUtilityMoneySpent = MarginalUtilityMoneySpentA
    if (MarginalUtilityMoneySpentA < MarginalUtilityMoneySpentB):
        MarginalUtilityMoneySpent = MarginalUtilityMoneySpentB
    MarginalDisUtilityMoneyEarned = MarginalDisUtilityLabour * (MarginalWage / WageRate)

    #Budget Adjustment                                                                                 <------ this changes a lot
    if (MarginalUtilityMoneySpentA > MarginalUtilityMoneySpentB) and (BudgetB > 1):
        BudgetA += 1
        BudgetB += -1
    if (MarginalUtilityMoneySpentA < MarginalUtilityMoneySpentB) and (BudgetA > 1):
        BudgetA += -1
        BudgetB += 1

    #Labour Supply Adjust
    if (MarginalUtilityMoneySpent > MarginalDisUtilityMoneyEarned) and (SupplyLabourInteger < 1598): #highest is 1598 (15.98 hours)
        SupplyLabourInteger += 1
    if (MarginalUtilityMoneySpent < MarginalDisUtilityMoneyEarned) and (SupplyLabourInteger > 2): #lowest is 2 (.02 hours)
        SupplyLabourInteger -= 1
    SupplyLabour = SupplyLabourInteger / 100

    #marginal production: f(x+dx) - f(x)
    MarginalProductionA = ProductionFunctionA(LabourA + MarginalLabour) - ProductionFunctionA(LabourA)
    MarginalProductionB = ProductionFunctionB(LabourB + MarginalLabour) - ProductionFunctionB(LabourB)
    #value of marginal production, [ f(x+dx) - f(x) ] * price
    MarginalValueProductionA = MarginalProductionA * PriceA
    MarginalValueProductionB = MarginalProductionB * PriceB
    #adjust labour allocation to A and B
    if (MarginalValueProductionA > MarginalValueProductionB) and (ProportionLabourB > 2): #lowest is 2 or 0.2%
        ProportionLabourA += 1
        ProportionLabourB += -1
    if (MarginalValueProductionA < MarginalValueProductionB) and (ProportionLabourA > 2): #lowest is 2 or 0.2%
        ProportionLabourA += -1
        ProportionLabourB += 1

    #agent spending should be equal to labour income
    AgentSpending = (DemandA * PriceA) + (DemandB * PriceB)

    #price adjustment
    if (DemandA > SupplyA):
        PriceA = PriceA * RateChangePrice
    if (DemandA < SupplyA) and (PriceA > 2):
        PriceA = PriceA / RateChangePrice
        if (PriceA < 2): #price cannot go below 2
            PriceA = 2
        
    if (DemandB > SupplyB):
        PriceB = PriceB * RateChangePrice
    if (DemandB < SupplyB) and (PriceB > 2):
        PriceB = PriceB / RateChangePrice
        if (PriceB < 2): #price cannot go below 2
            PriceB = 2

###################################################################################

    #Price A B
    PriceAPoints.append((len(PriceAPoints)+HorizontalSpacing,GraphHeight+VerticalSpacing-int(200*PriceA/PriceGraphScale)))
    if (len(PriceAPoints) > 299):
        PriceAPoints.pop(0)
        PriceAPoints = [(x-1,y) for (x,y) in PriceAPoints] 

    PriceBPoints.append((len(PriceBPoints)+HorizontalSpacing,GraphHeight+VerticalSpacing-int(200*PriceB/PriceGraphScale)))
    if (len(PriceBPoints) > 299):
        PriceBPoints.pop(0)
        PriceBPoints = [(x-1,y) for (x,y) in PriceBPoints] 

    #Supply Demand A
    SupplyAPoints.append((len(SupplyAPoints)+HorizontalSpacing,(2*VerticalSpacing)+(2*GraphHeight)-int(200*SupplyA/SupplyDemandAGraphScale)))
    if (len(SupplyAPoints) > 299):
        SupplyAPoints.pop(0)
        SupplyAPoints = [(x-1,y) for (x,y) in SupplyAPoints]

    DemandAPoints.append((len(DemandAPoints)+HorizontalSpacing,(2*VerticalSpacing)+(2*GraphHeight)-int(200*DemandA/SupplyDemandAGraphScale)))
    if (len(DemandAPoints) > 299):
        DemandAPoints.pop(0)
        DemandAPoints = [(x-1,y) for (x,y) in DemandAPoints]

    #Supply Demand B
    SupplyBPoints.append((len(SupplyBPoints)+HorizontalSpacing,(3*VerticalSpacing)+(3*GraphHeight)-int(200*SupplyB/SupplyDemandBGraphScale)))
    if (len(SupplyBPoints) > 299):
        SupplyBPoints.pop(0)
        SupplyBPoints = [(x-1,y) for (x,y) in SupplyBPoints]

    DemandBPoints.append((len(DemandBPoints)+HorizontalSpacing,(3*VerticalSpacing)+(3*GraphHeight)-int(200*DemandB/SupplyDemandBGraphScale)))
    if (len(DemandBPoints) > 299):
        DemandBPoints.pop(0)
        DemandBPoints = [(x-1,y) for (x,y) in DemandBPoints]

    #Supply Labour
    SupplyLabourPoints.append((len(SupplyLabourPoints)+GraphWidth+(2*HorizontalSpacing),GraphHeight+VerticalSpacing-int(200*SupplyLabour/SupplyLabourGraphScale)))
    if (len(SupplyLabourPoints) > 299):
        SupplyLabourPoints.pop(0)
        SupplyLabourPoints = [(x-1,y) for (x,y) in SupplyLabourPoints]

    #Budget A B
    BudgetAPoints.append((len(BudgetAPoints)+GraphWidth+(2*HorizontalSpacing),(2*VerticalSpacing)+(2*GraphHeight)-int(200*(BudgetA/10)/BudgetGraphScale)))
    if (len(BudgetAPoints) > 299):
        BudgetAPoints.pop(0)
        BudgetAPoints = [(x-1,y) for (x,y) in BudgetAPoints]
        
    BudgetBPoints.append((len(BudgetBPoints)+GraphWidth+(2*HorizontalSpacing),(2*VerticalSpacing)+(2*GraphHeight)-int(200*(BudgetB/10)/BudgetGraphScale)))
    if (len(BudgetBPoints) > 299):
        BudgetBPoints.pop(0)
        BudgetBPoints = [(x-1,y) for (x,y) in BudgetBPoints]

    #Labour A B
    LabourAPoints.append((len(LabourAPoints)+GraphWidth+(2*HorizontalSpacing),(3*VerticalSpacing)+(3*GraphHeight)-int(200*(ProportionLabourA/10)/LabourGraphScale)))
    if (len(LabourAPoints) > 299):
        LabourAPoints.pop(0)
        LabourAPoints = [(x-1,y) for (x,y) in LabourAPoints]
        
    LabourBPoints.append((len(LabourBPoints)+GraphWidth+(2*HorizontalSpacing),(3*VerticalSpacing)+(3*GraphHeight)-int(200*(ProportionLabourB/10)/LabourGraphScale)))
    if (len(LabourBPoints) > 299):
        LabourBPoints.pop(0)
        LabourBPoints = [(x-1,y) for (x,y) in LabourBPoints]

    #Marginal Utility Money
    MarginalUtilitySpendMoneyAPoints.append((len(MarginalUtilitySpendMoneyAPoints)+(2*GraphWidth)+(3*HorizontalSpacing),(2*VerticalSpacing)+(2*GraphHeight)-int(200*MarginalUtilityMoneySpentA/MarginalUtilityMoneyGraphScale)))
    if (len(MarginalUtilitySpendMoneyAPoints) > 299):
        MarginalUtilitySpendMoneyAPoints.pop(0)
        MarginalUtilitySpendMoneyAPoints = [(x-1,y) for (x,y) in MarginalUtilitySpendMoneyAPoints]

    MarginalUtilitySpendMoneyBPoints.append((len(MarginalUtilitySpendMoneyBPoints)+(2*GraphWidth)+(3*HorizontalSpacing),(2*VerticalSpacing)+(2*GraphHeight)-int(200*MarginalUtilityMoneySpentB/MarginalUtilityMoneyGraphScale)))
    if (len(MarginalUtilitySpendMoneyBPoints) > 299):
        MarginalUtilitySpendMoneyBPoints.pop(0)
        MarginalUtilitySpendMoneyBPoints = [(x-1,y) for (x,y) in MarginalUtilitySpendMoneyBPoints]

    MarginalDisUtilityEarnMoneyPoints.append((len(MarginalDisUtilityEarnMoneyPoints)+(2*GraphWidth)+(3*HorizontalSpacing),(2*VerticalSpacing)+(2*GraphHeight)-int(200*MarginalDisUtilityMoneyEarned/MarginalUtilityMoneyGraphScale)))
    if (len(MarginalDisUtilityEarnMoneyPoints) > 299):
        MarginalDisUtilityEarnMoneyPoints.pop(0)
        MarginalDisUtilityEarnMoneyPoints = [(x-1,y) for (x,y) in MarginalDisUtilityEarnMoneyPoints]

    #Marginal Value Labour
    MarginlValueLabourAPoints.append((len(MarginlValueLabourAPoints)+(2*GraphWidth)+(3*HorizontalSpacing),(3*VerticalSpacing)+(3*GraphHeight)-int((200*MarginalValueProductionA)/MarginalValueLabourGraphScale)))
    if (len(MarginlValueLabourAPoints) > 299):
        MarginlValueLabourAPoints.pop(0)
        MarginlValueLabourAPoints = [(x-1,y) for (x,y) in MarginlValueLabourAPoints]

    MarginlValueLabourBPoints.append((len(MarginlValueLabourBPoints)+(2*GraphWidth)+(3*HorizontalSpacing),(3*VerticalSpacing)+(3*GraphHeight)-int((200*MarginalValueProductionB)/MarginalValueLabourGraphScale)))
    if (len(MarginlValueLabourBPoints) > 299):
        MarginlValueLabourBPoints.pop(0)
        MarginlValueLabourBPoints = [(x-1,y) for (x,y) in MarginlValueLabourBPoints]

################################################################################################################

    if (MouseLeft == 1) and ((DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin) < MouseX < (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin)+(2*SliderSelectionMargin+SliderWidth)) and ((1*SliderVerticalSpacing-SliderSelectionMargin) < MouseY < (1*SliderVerticalSpacing-SliderSelectionMargin)+(2*SliderSelectionMargin)):
        SliderPosX1 = MouseX
        if (SliderPosX1 < DisplayX-SliderHorizontalDisplacment):
            SliderPosX1 = DisplayX-SliderHorizontalDisplacment
        if (SliderPosX1 > DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight):
            SliderPosX1 = DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight

    if (MouseLeft == 1) and ((DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin) < MouseX < (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin)+(2*SliderSelectionMargin+SliderWidth)) and ((2*SliderVerticalSpacing-SliderSelectionMargin) < MouseY < (2*SliderVerticalSpacing-SliderSelectionMargin)+(2*SliderSelectionMargin)):
        SliderPosX2 = MouseX
        if (SliderPosX2 < DisplayX-SliderHorizontalDisplacment):
            SliderPosX2 = DisplayX-SliderHorizontalDisplacment
        if (SliderPosX2 > DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight):
            SliderPosX2 = DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight

    if (MouseLeft == 1) and ((DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin) < MouseX < (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin)+(2*SliderSelectionMargin+SliderWidth)) and ((3*SliderVerticalSpacing-SliderSelectionMargin) < MouseY < (3*SliderVerticalSpacing-SliderSelectionMargin)+(2*SliderSelectionMargin)):
        SliderPosX3 = MouseX
        if (SliderPosX3 < DisplayX-SliderHorizontalDisplacment):
            SliderPosX3 = DisplayX-SliderHorizontalDisplacment
        if (SliderPosX3 > DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight):
            SliderPosX3 = DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight

    if (MouseLeft == 1) and ((DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin) < MouseX < (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin)+(2*SliderSelectionMargin+SliderWidth)) and ((4*SliderVerticalSpacing-SliderSelectionMargin) < MouseY < (4*SliderVerticalSpacing-SliderSelectionMargin)+(2*SliderSelectionMargin)):
        SliderPosX4 = MouseX
        if (SliderPosX4 < DisplayX-SliderHorizontalDisplacment):
            SliderPosX4 = DisplayX-SliderHorizontalDisplacment
        if (SliderPosX4 > DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight):
            SliderPosX4 = DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight

    if (MouseLeft == 1) and ((DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin) < MouseX < (DisplayX-SliderHorizontalDisplacment-SliderSelectionMargin)+(2*SliderSelectionMargin+SliderWidth)) and ((5*SliderVerticalSpacing-SliderSelectionMargin) < MouseY < (5*SliderVerticalSpacing-SliderSelectionMargin)+(2*SliderSelectionMargin)):
        SliderPosX5 = MouseX
        if (SliderPosX5 < DisplayX-SliderHorizontalDisplacment):
            SliderPosX5 = DisplayX-SliderHorizontalDisplacment
        if (SliderPosX5 > DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight):
            SliderPosX5 = DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight

    SliderScaler1 = (SliderPosX1 - (DisplayX-SliderHorizontalDisplacment)) / ((DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight)-(DisplayX-SliderHorizontalDisplacment))
    SliderScaler2 = (SliderPosX2 - (DisplayX-SliderHorizontalDisplacment)) / ((DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight)-(DisplayX-SliderHorizontalDisplacment))
    SliderScaler3 = (SliderPosX3 - (DisplayX-SliderHorizontalDisplacment)) / ((DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight)-(DisplayX-SliderHorizontalDisplacment))
    SliderScaler4 = (SliderPosX4 - (DisplayX-SliderHorizontalDisplacment)) / ((DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight)-(DisplayX-SliderHorizontalDisplacment))
    SliderScaler5 = (SliderPosX5 - (DisplayX-SliderHorizontalDisplacment)) / ((DisplayX-SliderHorizontalDisplacment+SliderWidth-SliderHeight)-(DisplayX-SliderHorizontalDisplacment))

    Game()
    DrawGraphs()
    DrawSliders()
    pygame.display.update()

    if (PrintDebugInformation == True):
        print(str(DemandA),str(SupplyA),str(DemandB),str(SupplyB),str(PriceA),str(PriceB),str(SupplyLabour),str(BudgetA),str(BudgetB),str(MarginalUtilityMoneySpentA),str(MarginalUtilityMoneySpentB),str(MarginalDisUtilityMoneyEarned),str(LabourIncome),str(MarginalValueProductionA),str(MarginalValueProductionB),str(ProportionLabourA),str(ProportionLabourB))
        #print(str(MarginalValueProductionA))

pygame.quit()

#font = pygame.font.SysFont('courier', 30)
#TEXT = font.render("Hello World!", 1, Black)
#win.blit(TEXT, (X, Y))


