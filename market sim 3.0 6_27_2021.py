import os, pygame.gfxdraw, pygame, math, random, time
pygame.init()

DisplayX, DisplayY = 1840,1040
win = pygame.display.set_mode((DisplayX, DisplayY))
pygame.display.set_caption("Market Simulation Version 3.0")

White = (255,255,255)
White0 = (200,200,200)
Black = (0,0,0)
Blue = (80,80,255)
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
Gold = (255,215,0)
Silver = (200,200,200)

font0 = pygame.font.SysFont('courier', 15, True)
font  = pygame.font.SysFont('courier', 22, True)
font1 = pygame.font.SysFont('courier', 17, True)
font2 = pygame.font.SysFont('courier', 17, True)
font3 = pygame.font.SysFont('courier', 18, True)

WageRate = 0
Income = 10000
SupplyLabour = 8
LabourAPercentage = 33
LabourBPercentage = 33
LabourCPercentage = 34
DemandAPercentage = 33
DemandBPercentage = 33
DemandCPercentage = 34
LabourA = 0
LabourB = 0
LabourC = 0
SupplyA = 0
SupplyB = 0
SupplyC = 0
MoneySpentA = 0
MoneySpentB = 0
MoneySpentC = 0
DemandA = 0
DemandB = 0
DemandC = 0
PriceA = 100
PriceB = 100
PriceC = 100
RateChangePrice = 1.01
RateChangeSupplyLabour = 1.01
Increment = 1
MarginalLabour = 0.01
MarginalMoney = 1
MarginalUtilityA = 0
MarginalUtilityB = 0
MarginalUtilityC = 0
MarginalUtilityMoneySpentA = 0
MarginalUtilityMoneySpentB = 0
MarginalUtilityMoneySpentC = 0
MarginalDisUtilityLabour = 0
MarginalDisUtilityMoneyEarned = 0
MarginalProductionA = 0
MarginalProductionB = 0
MarginalProductionC = 0
MarginalValueProductionA = 0
MarginalValueProductionB = 0
MarginalValueProductionC = 0

GraphColour = (100,100,100)
GraphWidth = 400
GraphHeight = 200
HorizontalGraphSpacing = 55
VerticalGraphSpacing = 55
BaseHorizontalGraphSpacing = 20
BaseVerticalGraphSpacing = VerticalGraphSpacing

GraphOneX,GraphOneY = BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing
GraphTwoX,GraphTwoY = BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing
GraphThreeX,GraphThreeY = BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)
GraphFourX,GraphFourY = BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)
GraphFiveX,GraphFiveY = BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing
GraphSixX,GraphSixY = BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing
GraphSevenX,GraphSevenY = BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)
GraphEightX,GraphEightY = BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)
GraphNineX,GraphNineY = BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing
GraphTenX,GraphTenY = BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing
GraphElevenX,GraphElevenY = BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)
GraphTwelveX,GraphTwelveY = BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)
GraphThirteenX,GraphThirteenY = BaseHorizontalGraphSpacing+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)

PriceGraphHeight = 2000
SupplyDemandAGraphHeight = 15
SupplyDemandBGraphHeight = 15
SupplyDemandCGraphHeight = 15
BudgetPercentGraphHeight = 100
LabourPercentGraphHeight = 100
MarginalUtilityMoneyGraphHeight = .04
MarginalValueProductionGraphHeight = 8
ProductionFunctionGraphHeight,ProductionFunctionGraphWidth = 8,8
MarginalDisUtilityLabourGraphHeight,MarginalDisUtilityLabourGraphWidth = 30,16
MarginalUtilityGraphHeight,MarginalUtilityGraphWidth = 13,30
SupplyLabourGraphHeight = 16
WageRateGraphHeight = 5000

MouseOverGraph = "None"
ScrollStepSizeOne = 100
ScrollStepSizeTwo = 1
ScrollStepSizeThree = 1
ScrollStepSizeFour = 1
ScrollStepSizeFive = 10
ScrollStepSizeSix = 10
ScrollStepSizeSeven = .01
ScrollStepSizeEight = 10
ScrollStepSizeNine = .5
ScrollStepSizeTen = 10
ScrollStepSizeEleven = 1
ScrollStepSizeTwelve = 10
ScrollStepSizeThirteen = 10
ScrollRate = 1.01

OneMin,OneMax = ScrollStepSizeOne,3000
TwoMin,TwoMax = ScrollStepSizeTwo,50
ThreeMin,ThreeMax = ScrollStepSizeThree,50
FourMin,FourMax = ScrollStepSizeFour,50
FiveMin,FiveMax = 100,100
SixMin,SixMax = 100,100
SevenMin,SevenMax = MarginalUtilityMoneyGraphHeight,MarginalUtilityMoneyGraphHeight
EightMin,EightMax = MarginalValueProductionGraphHeight,MarginalValueProductionGraphHeight
NineMin,NineMax = ScrollStepSizeNine,1000
TenMin,TenMax = ScrollStepSizeTen,1000
ElevenMin,ElevenMax = 5,1000
TwelveMin,TwelveMax = 16,16
ThirteenMin,ThirteenMax = 5000,5000

LabelOffsetX = 2
LabelOffsetY = -10

NameLabelOffsetX = 10
NameLabelOffsetY = -30
NumberLabelOffsetX = 10
NumberLabelOffsetY = 2

RoundPrice = 0
RoundSupplyDemand = 3
RoundMarginalUtilityMoney = 6
RoundMarginalValueProduction = 6
RoundSupplyLabour = 2
RoundWageRate = 2

PriceNameLabelTEXT1 = font.render("Price A", 1, Blue)
PriceNameLabelTEXT2 = font.render("Price B", 1, Red)
PriceNameLabelTEXT3 = font.render("Price C", 1, Green)
SupplyDemandATEXT1 = font.render("Supply A", 1, Blue)
SupplyDemandATEXT2 = font.render("Demand A", 1, Red)
SupplyDemandBTEXT1 = font.render("Supply B", 1, Blue)
SupplyDemandBTEXT2 = font.render("Demand B", 1, Red)
SupplyDemandCTEXT1 = font.render("Supply C", 1, Blue)
SupplyDemandCTEXT2 = font.render("Demand C", 1, Red)
BudgetPercentTEXT1 = font.render("Budget A%", 1, Blue)
BudgetPercentTEXT2 = font.render("Budget B%", 1, Red)
BudgetPercentTEXT3 = font.render("Budget C%", 1, Green)
LabourPercentTEXT1 = font.render("Labour A%", 1, Blue)
LabourPercentTEXT2 = font.render("Labour B%", 1, Red)
LabourPercentTEXT3 = font.render("Labour C%", 1, Green)
MarginalUtilityMoneyTEXT1 = font.render("MUΔ$A", 1, Blue)
MarginalUtilityMoneyTEXT2 = font.render("MUΔ$B", 1, Red)
MarginalUtilityMoneyTEXT3 = font.render("MUΔ$C", 1, Green)
MarginalUtilityMoneyTEXT4 = font.render("MDUΔ$", 1, Gold)
MarginalValueProductionTEXT1 = font.render("ΔQA*PA", 1, Blue)
MarginalValueProductionTEXT2 = font.render("ΔQB*PB", 1, Red)
MarginalValueProductionTEXT3 = font.render("ΔQC*PC", 1, Green)
ProductionFunctionTEXT = font.render("Production Function", 1, White)
MarginalDisUtilityLabourFunctionTEXT = font.render("Marginal Dis-Utility Labour", 1, White)
MarginalUtilityFunctionTEXT = font.render("Marginal Utility", 1, White)
SupplyLabourTEXT = font.render("Supply Labour", 1, Blue)
WageRateTEXT = font.render("Wage Rate", 1, Blue)

LineWidth = 1
PriceAList = [(GraphOneX,GraphOneY)]
PriceBList = [(GraphOneX,GraphOneY)]
PriceCList = [(GraphOneX,GraphOneY)]
SupplyAList = [(GraphTwoX,GraphTwoY)]
DemandAList = [(GraphTwoX,GraphTwoY)]
SupplyBList = [(GraphThreeX,GraphThreeY)]
DemandBList = [(GraphThreeX,GraphThreeY)]
SupplyCList = [(GraphFourX,GraphFourY)]
DemandCList = [(GraphFourX,GraphFourY)]
BudgetAList = [(GraphFiveX,GraphFiveY)]
BudgetBList = [(GraphFiveX,GraphFiveY)]
BudgetCList = [(GraphFiveX,GraphFiveY)]
LabourAList = [(GraphSixX,GraphSixY)]
LabourBList = [(GraphSixX,GraphSixY)]
LabourCList = [(GraphSixX,GraphSixY)]
MarginalUtilityMoneyAList = [(GraphSevenX,GraphSevenY)]
MarginalUtilityMoneyBList = [(GraphSevenX,GraphSevenY)]
MarginalUtilityMoneyCList = [(GraphSevenX,GraphSevenY)]
MarginalDisUtilityEarnMoneyList = [(GraphSevenX,GraphSevenY)]
MarginalValueProductionAList = [(GraphEightX,GraphEightY)]
MarginalValueProductionBList = [(GraphEightX,GraphEightY)]
MarginalValueProductionCList = [(GraphEightX,GraphEightY)]
SupplyLabourList = [(GraphTwelveX,GraphTwelveY)]
WageRateList = [(GraphThirteenX,GraphThirteenY)]
ProductionFunctionAList = [(GraphNineX,0)]
ProductionFunctionBList = [(GraphNineX,0)]
ProductionFunctionCList = [(GraphNineX,0)]
MarginalDisUtilityLabourFunctionList = [(GraphTenX,0)]
MarginalUtilityAFunctionList = [(GraphElevenX,0)]
MarginalUtilityBFunctionList = [(GraphElevenX,0)]
MarginalUtilityCFunctionList = [(GraphElevenX,0)]

DropDownThickness = 30
SliderDropDownX = BaseHorizontalGraphSpacing+(3*GraphWidth)+(3*HorizontalGraphSpacing)
SliderDropDownY = BaseVerticalGraphSpacing
SliderDropDownHeight = (3*GraphHeight)+(2*VerticalGraphSpacing)
SliderDropDownWidth = GraphWidth
GraphDropDownX = SliderDropDownX
GraphDropDownY = SliderDropDownY
VariableDropDownX = SliderDropDownX
VariableDropDownY = SliderDropDownY+DropDownThickness-1
MouseHoverOverGraphDropDown = False
MouseHoverOverVariableDropDown = False
DropDownSelected = "Variable"
DropDownGraphTEXT = font.render("Graph", 1, White)
DropDownVariableTEXT = font.render("Variable", 1, White)

VariableMenuTEXT = font.render("Variables", 1, White)
MUASliderTEXT = font.render("MUA", 1, Blue)
MUBSliderTEXT = font.render("MUB", 1, Red)
MUCSliderTEXT = font.render("MUC", 1, Green)
MDULSliderTEXT = font.render("MDUL", 1, Gold)
ProdASliderTEXT = font.render("ProdA", 1, Blue)
ProdBSliderTEXT = font.render("ProdB", 1, Red)
ProdCSliderTEXT = font.render("ProdC", 1, Green)

tempNoneText = font.render("None", 1, White)
tempGraphtext = font.render("Graph", 1, White)

SliderTextOffsetX = -75
SliderTextOffsetY = -10

VariablesMenuX = int(SliderDropDownX+(GraphWidth/2)-(VariableMenuTEXT.get_width()/2))
VariablesMenuY = SliderDropDownY+100
SliderBaseX = SliderDropDownX
SliderBaseY = SliderDropDownY
SliderVerticalSpacing = 50
SliderWidth = 230
SliderThickness = 5
VariableSliderOneX = int(SliderBaseX+(GraphWidth/2)-(SliderWidth/2))
VariableSliderOneY = VariablesMenuY+100
VariableSliderTwoX = VariableSliderOneX
VariableSliderTwoY = VariableSliderOneY+(SliderVerticalSpacing)
VariableSliderThreeX = VariableSliderOneX
VariableSliderThreeY = VariableSliderOneY+(2*SliderVerticalSpacing)
VariableSliderFourX = VariableSliderOneX
VariableSliderFourY = VariableSliderOneY+(3*SliderVerticalSpacing)
VariableSliderFiveX = VariableSliderOneX
VariableSliderFiveY = VariableSliderOneY+(4*SliderVerticalSpacing)
VariableSliderSixX = VariableSliderOneX
VariableSliderSixY = VariableSliderOneY+(5*SliderVerticalSpacing)
VariableSliderSevenX = VariableSliderOneX
VariableSliderSevenY = VariableSliderOneY+(6*SliderVerticalSpacing)

SliderVariableScaleOne = 0
SliderVariableScaleTwo = 0
SliderVariableScaleThree = 0
SliderVariableScaleFour = 0
SliderVariableScaleFive = 0
SliderVariableScaleSix = 0
SliderVariableScaleSeven = 0

SliderDotOneX = VariableSliderOneX
SliderDotOneY = VariableSliderOneY
SliderDotTwoX = VariableSliderTwoX
SliderDotTwoY = VariableSliderTwoY
SliderDotThreeX = VariableSliderThreeX
SliderDotThreeY = VariableSliderThreeY
SliderDotFourX = VariableSliderFourX
SliderDotFourY = VariableSliderFourY
SliderDotFiveX = VariableSliderFiveX
SliderDotFiveY = VariableSliderFiveY
SliderDotSixX = VariableSliderSixX
SliderDotSixY = VariableSliderSixY
SliderDotSevenX = VariableSliderSevenX
SliderDotSevenY = VariableSliderSevenY

VariableSliderSelected = "None"
ShowVariableSliderHitBox = False

VariableSliderHitBoxOneX = int(VariableSliderOneX-(SliderVerticalSpacing/2))
VariableSliderHitBoxOneY = int(VariableSliderOneY-(SliderVerticalSpacing/2))
VariableSliderHitBoxWidthOne = SliderWidth+SliderVerticalSpacing
VariableSliderHitBoxHeightOne = SliderVerticalSpacing
VariableSliderHitBoxTwoX = int(VariableSliderTwoX-(SliderVerticalSpacing/2))
VariableSliderHitBoxTwoY = int(VariableSliderTwoY-(SliderVerticalSpacing/2))
VariableSliderHitBoxWidthTwo = SliderWidth+SliderVerticalSpacing
VariableSliderHitBoxHeightTwo = SliderVerticalSpacing
VariableSliderHitBoxThreeX = int(VariableSliderThreeX-(SliderVerticalSpacing/2))
VariableSliderHitBoxThreeY = int(VariableSliderThreeY-(SliderVerticalSpacing/2))
VariableSliderHitBoxWidthThree = SliderWidth+SliderVerticalSpacing
VariableSliderHitBoxHeightThree = SliderVerticalSpacing
VariableSliderHitBoxFourX = int(VariableSliderFourX-(SliderVerticalSpacing/2))
VariableSliderHitBoxFourY = int(VariableSliderFourY-(SliderVerticalSpacing/2))
VariableSliderHitBoxWidthFour = SliderWidth+SliderVerticalSpacing
VariableSliderHitBoxHeightFour = SliderVerticalSpacing
VariableSliderHitBoxFiveX = int(VariableSliderFiveX-(SliderVerticalSpacing/2))
VariableSliderHitBoxFiveY = int(VariableSliderFiveY-(SliderVerticalSpacing/2))
VariableSliderHitBoxWidthFive = SliderWidth+SliderVerticalSpacing
VariableSliderHitBoxHeightFive = SliderVerticalSpacing
VariableSliderHitBoxSixX = int(VariableSliderSixX-(SliderVerticalSpacing/2))
VariableSliderHitBoxSixY = int(VariableSliderSixY-(SliderVerticalSpacing/2))
VariableSliderHitBoxWidthSix = SliderWidth+SliderVerticalSpacing
VariableSliderHitBoxHeightSix = SliderVerticalSpacing
VariableSliderHitBoxSevenX = int(VariableSliderSevenX-(SliderVerticalSpacing/2))
VariableSliderHitBoxSevenY = int(VariableSliderSevenY-(SliderVerticalSpacing/2))
VariableSliderHitBoxWidthSeven = SliderWidth+SliderVerticalSpacing
VariableSliderHitBoxHeightSeven = SliderVerticalSpacing

VariableSliderValueOne = 200
VariableSliderValueTwo = 200
VariableSliderValueThree = 200
VariableSliderValueFour = 600
VariableSliderValueFive = 200
VariableSliderValueSix = 200
VariableSliderValueSeven = 200

VariableSliderHitBoxButtonTEXT = font0.render("ENABLE/DISABLE Slider Hit Boxes", 1, Black)
VariableSliderHitboxButtonWidth = VariableSliderHitBoxButtonTEXT.get_width()+20
VariableSliderHitboxButtonHeight = VariableSliderHitBoxButtonTEXT.get_height()
VariableSliderHitboxButtonX = int(SliderDropDownX+(GraphWidth/2)-(VariableSliderHitboxButtonWidth/2))
VariableSliderHitboxButtonY = SliderDropDownY+600

PAUSE = False
STEPPING = False

PauseTEXT = font0.render("PAUSE", 1, Black)
PlayTEXT = font0.render("PLAY", 1, Black)
PauseButtonWidth = PauseTEXT.get_width()+20
PauseButtonHeight = PauseTEXT.get_height()
PauseButtonX = int(SliderDropDownX+(GraphWidth/2)-(PauseButtonWidth/2))
PauseButtonY = SliderDropDownY+630

StepTEXT = font0.render("STEP", 1, Black)
StepButtonWidth = StepTEXT.get_width()+20
StepButtonHeight = StepTEXT.get_height()
StepButtonX = int(SliderDropDownX+(GraphWidth/2)-(StepButtonWidth/2))
StepButtonY = SliderDropDownY+660

FPS = 0
start_time = 0

def Game():
    win.fill(Black)

def DrawGridLines():
    #horizontal grid lines
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.25)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.5)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.75)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+GraphHeight+VerticalGraphSpacing), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+GraphHeight+VerticalGraphSpacing), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(2*GraphHeight)+(2*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(2*GraphHeight)+(2*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.25)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.5)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), (BaseHorizontalGraphSpacing+GraphWidth-1+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+int(GraphHeight*0.75)+(3*GraphHeight)+(3*VerticalGraphSpacing)), 1)
    #vertical grid lines
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+GraphWidth+HorizontalGraphSpacing,BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+VerticalGraphSpacing),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+GraphHeight+VerticalGraphSpacing-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(2*GraphHeight)+(2*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(2*GraphHeight)+(2*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(2*GraphWidth)+(2*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.25)+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.5)+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)
    pygame.draw.line(win, GraphColour, (BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+(3*GraphHeight)+(3*VerticalGraphSpacing)),(BaseHorizontalGraphSpacing+int(GraphWidth*0.75)+(3*GraphWidth)+(3*HorizontalGraphSpacing),BaseVerticalGraphSpacing+GraphHeight+(3*GraphHeight)+(3*VerticalGraphSpacing)-1), 1)

def DrawGraphs():
    #rectangles
    pygame.draw.rect(win, GraphColour, (GraphOneX,GraphOneY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphTwoX,GraphTwoY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphThreeX,GraphThreeY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphFourX,GraphFourY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphFiveX,GraphFiveY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphSixX,GraphSixY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphSevenX,GraphSevenY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphEightX,GraphEightY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphNineX,GraphNineY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphTenX,GraphTenY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphElevenX,GraphElevenY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphTwelveX,GraphTwelveY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, GraphColour, (GraphThirteenX,GraphThirteenY,GraphWidth,GraphHeight), 1)

    if (MouseOverGraph == "One"):
        pygame.draw.rect(win, White0, (GraphOneX,GraphOneY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Two"):
        pygame.draw.rect(win, White0, (GraphTwoX,GraphTwoY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Three"):
        pygame.draw.rect(win, White0, (GraphThreeX,GraphThreeY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Four"):
        pygame.draw.rect(win, White0, (GraphFourX,GraphFourY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Five"):
        pygame.draw.rect(win, White0, (GraphFiveX,GraphFiveY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Six"):
        pygame.draw.rect(win, White0, (GraphSixX,GraphSixY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Seven"):
        pygame.draw.rect(win, White0, (GraphSevenX,GraphSevenY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Eight"):
        pygame.draw.rect(win, White0, (GraphEightX,GraphEightY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Nine"):
        pygame.draw.rect(win, White0, (GraphNineX,GraphNineY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Ten"):
        pygame.draw.rect(win, White0, (GraphTenX,GraphTenY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Eleven"):
        pygame.draw.rect(win, White0, (GraphElevenX,GraphElevenY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Twelve"):
        pygame.draw.rect(win, White0, (GraphTwelveX,GraphTwelveY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == "Thirteen"):
        pygame.draw.rect(win, White0, (GraphThirteenX,GraphThirteenY,GraphWidth,GraphHeight), 1)

    #axis lable
    VerticalLabelTEXTZero = font1.render("0", 1, GraphColour)
    PriceGraphVerticalLabelTEXT1 = font1.render(str(PriceGraphHeight), 1, GraphColour)
    PriceGraphVerticalLabelTEXT2 = font1.render(str(int(PriceGraphHeight*.75)), 1, GraphColour)
    PriceGraphVerticalLabelTEXT3 = font1.render(str(int(PriceGraphHeight*.5)), 1, GraphColour)
    PriceGraphVerticalLabelTEXT4 = font1.render(str(int(PriceGraphHeight*.25)), 1, GraphColour)
    SupplyDemandAGraphVerticalLabelTEXT1 = font1.render(str(SupplyDemandAGraphHeight), 1, GraphColour)
    SupplyDemandAGraphVerticalLabelTEXT2 = font1.render(str(int(SupplyDemandAGraphHeight*.75)), 1, GraphColour)
    SupplyDemandAGraphVerticalLabelTEXT3 = font1.render(str(int(SupplyDemandAGraphHeight*.5)), 1, GraphColour)
    SupplyDemandAGraphVerticalLabelTEXT4 = font1.render(str(int(SupplyDemandAGraphHeight*.25)), 1, GraphColour)
    SupplyDemandBGraphVerticalLabelTEXT1 = font1.render(str(SupplyDemandBGraphHeight), 1, GraphColour)
    SupplyDemandBGraphVerticalLabelTEXT2 = font1.render(str(int(SupplyDemandBGraphHeight*.75)), 1, GraphColour)
    SupplyDemandBGraphVerticalLabelTEXT3 = font1.render(str(int(SupplyDemandBGraphHeight*.5)), 1, GraphColour)
    SupplyDemandBGraphVerticalLabelTEXT4 = font1.render(str(int(SupplyDemandBGraphHeight*.25)), 1, GraphColour)
    SupplyDemandCGraphVerticalLabelTEXT1 = font1.render(str(SupplyDemandCGraphHeight), 1, GraphColour)
    SupplyDemandCGraphVerticalLabelTEXT2 = font1.render(str(int(SupplyDemandCGraphHeight*.75)), 1, GraphColour)
    SupplyDemandCGraphVerticalLabelTEXT3 = font1.render(str(int(SupplyDemandCGraphHeight*.5)), 1, GraphColour)
    SupplyDemandCGraphVerticalLabelTEXT4 = font1.render(str(int(SupplyDemandCGraphHeight*.25)), 1, GraphColour)
    BudgetPercentGraphVerticalLabelTEXT1 = font1.render(str(BudgetPercentGraphHeight), 1, GraphColour)
    BudgetPercentGraphVerticalLabelTEXT2 = font1.render(str(int(BudgetPercentGraphHeight*.75)), 1, GraphColour)
    BudgetPercentGraphVerticalLabelTEXT3 = font1.render(str(int(BudgetPercentGraphHeight*.5)), 1, GraphColour)
    BudgetPercentGraphVerticalLabelTEXT4 = font1.render(str(int(BudgetPercentGraphHeight*.25)), 1, GraphColour)
    LabourPercentGraphVerticalLabelTEXT1 = font1.render(str(LabourPercentGraphHeight), 1, GraphColour)
    LabourPercentGraphVerticalLabelTEXT2 = font1.render(str(int(LabourPercentGraphHeight*.75)), 1, GraphColour)
    LabourPercentGraphVerticalLabelTEXT3 = font1.render(str(int(LabourPercentGraphHeight*.5)), 1, GraphColour)
    LabourPercentGraphVerticalLabelTEXT4 = font1.render(str(int(LabourPercentGraphHeight*.25)), 1, GraphColour)
    MarginalUtilityMoneyGraphVerticalLabelTEXT1 = font1.render(str(MarginalUtilityMoneyGraphHeight), 1, GraphColour)
    MarginalUtilityMoneyGraphVerticalLabelTEXT2 = font1.render(str(MarginalUtilityMoneyGraphHeight*.75), 1, GraphColour)
    MarginalUtilityMoneyGraphVerticalLabelTEXT3 = font1.render(str(MarginalUtilityMoneyGraphHeight*.5), 1, GraphColour)
    MarginalUtilityMoneyGraphVerticalLabelTEXT4 = font1.render(str(MarginalUtilityMoneyGraphHeight*.25), 1, GraphColour)
    MarginalValueProductionGraphVerticalLabelTEXT1 = font1.render(str(MarginalValueProductionGraphHeight), 1, GraphColour)
    MarginalValueProductionGraphVerticalLabelTEXT2 = font1.render(str(int(MarginalValueProductionGraphHeight*.75)), 1, GraphColour)
    MarginalValueProductionGraphVerticalLabelTEXT3 = font1.render(str(int(MarginalValueProductionGraphHeight*.5)), 1, GraphColour)
    MarginalValueProductionGraphVerticalLabelTEXT4 = font1.render(str(int(MarginalValueProductionGraphHeight*.25)), 1, GraphColour)
    ProductionFunctionGraphVerticalLabelTEXT1 = font1.render(str(ProductionFunctionGraphHeight), 1, GraphColour)
    ProductionFunctionGraphVerticalLabelTEXT2 = font1.render(str(int(ProductionFunctionGraphHeight*.75)), 1, GraphColour)
    ProductionFunctionGraphVerticalLabelTEXT3 = font1.render(str(int(ProductionFunctionGraphHeight*.5)), 1, GraphColour)
    ProductionFunctionGraphVerticalLabelTEXT4 = font1.render(str(int(ProductionFunctionGraphHeight*.25)), 1, GraphColour)
    ProductionFunctionGraphHorizontalLabelTEXT1 = font1.render(str(ProductionFunctionGraphWidth), 1, GraphColour)
    ProductionFunctionGraphHorizontalLabelTEXT2 = font1.render(str(round(ProductionFunctionGraphWidth*.75,2)), 1, GraphColour)
    ProductionFunctionGraphHorizontalLabelTEXT3 = font1.render(str(round(ProductionFunctionGraphWidth*.5,2)), 1, GraphColour)
    ProductionFunctionGraphHorizontalLabelTEXT4 = font1.render(str(round(ProductionFunctionGraphWidth*.25,2)), 1, GraphColour)
    MarginalDisUtilityLabourGraphVerticalLabelTEXT1 = font1.render(str(MarginalDisUtilityLabourGraphHeight), 1, GraphColour)
    MarginalDisUtilityLabourGraphVerticalLabelTEXT2 = font1.render(str(int(MarginalDisUtilityLabourGraphHeight*.75)), 1, GraphColour)
    MarginalDisUtilityLabourGraphVerticalLabelTEXT3 = font1.render(str(int(MarginalDisUtilityLabourGraphHeight*.5)), 1, GraphColour)
    MarginalDisUtilityLabourGraphVerticalLabelTEXT4 = font1.render(str(int(MarginalDisUtilityLabourGraphHeight*.25)), 1, GraphColour)
    MarginalDisUtilityLabourGraphHorizontalLabelTEXT1 = font1.render(str(MarginalDisUtilityLabourGraphWidth), 1, GraphColour)
    MarginalDisUtilityLabourGraphHorizontalLabelTEXT2 = font1.render(str(round(MarginalDisUtilityLabourGraphWidth*.75,2)), 1, GraphColour)
    MarginalDisUtilityLabourGraphHorizontalLabelTEXT3 = font1.render(str(round(MarginalDisUtilityLabourGraphWidth*.5,2)), 1, GraphColour)
    MarginalDisUtilityLabourGraphHorizontalLabelTEXT4 = font1.render(str(round(MarginalDisUtilityLabourGraphWidth*.25,2)), 1, GraphColour)
    MarginalUtilityGraphVerticalLabelTEXT1 = font1.render(str(MarginalUtilityGraphHeight), 1, GraphColour)
    MarginalUtilityGraphVerticalLabelTEXT2 = font1.render(str(int(MarginalUtilityGraphHeight*.75)), 1, GraphColour)
    MarginalUtilityGraphVerticalLabelTEXT3 = font1.render(str(int(MarginalUtilityGraphHeight*.5)), 1, GraphColour)
    MarginalUtilityGraphVerticalLabelTEXT4 = font1.render(str(int(MarginalUtilityGraphHeight*.25)), 1, GraphColour)
    MarginalUtilityGraphHorizontalLabelTEXT1 = font1.render(str(MarginalUtilityGraphWidth), 1, GraphColour)
    MarginalUtilityGraphHorizontalLabelTEXT2 = font1.render(str(round(MarginalUtilityGraphWidth*.75,2)), 1, GraphColour)
    MarginalUtilityGraphHorizontalLabelTEXT3 = font1.render(str(round(MarginalUtilityGraphWidth*.5,2)), 1, GraphColour)
    MarginalUtilityGraphHorizontalLabelTEXT4 = font1.render(str(round(MarginalUtilityGraphWidth*.25,2)), 1, GraphColour)
    SupplyLabourGraphVerticalLabelTEXT1 = font1.render(str(SupplyLabourGraphHeight), 1, GraphColour)
    SupplyLabourGraphVerticalLabelTEXT2 = font1.render(str(int(SupplyLabourGraphHeight*.75)), 1, GraphColour)
    SupplyLabourGraphVerticalLabelTEXT3 = font1.render(str(int(SupplyLabourGraphHeight*.5)), 1, GraphColour)
    SupplyLabourGraphVerticalLabelTEXT4 = font1.render(str(int(SupplyLabourGraphHeight*.25)), 1, GraphColour)
    WageRateGraphVerticalLabelTEXT1 = font1.render(str(WageRateGraphHeight), 1, GraphColour)
    WageRateGraphVerticalLabelTEXT2 = font1.render(str(int(WageRateGraphHeight*.75)), 1, GraphColour)
    WageRateGraphVerticalLabelTEXT3 = font1.render(str(int(WageRateGraphHeight*.5)), 1, GraphColour)
    WageRateGraphVerticalLabelTEXT4 = font1.render(str(int(WageRateGraphHeight*.25)), 1, GraphColour)
    win.blit(VerticalLabelTEXTZero, (GraphOneX+GraphWidth+LabelOffsetX,GraphOneY+GraphHeight+LabelOffsetY))    
    win.blit(PriceGraphVerticalLabelTEXT1, (GraphOneX+GraphWidth+LabelOffsetX,GraphOneY+LabelOffsetY))
    win.blit(PriceGraphVerticalLabelTEXT2, (GraphOneX+GraphWidth+LabelOffsetX,GraphOneY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(PriceGraphVerticalLabelTEXT3, (GraphOneX+GraphWidth+LabelOffsetX,GraphOneY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(PriceGraphVerticalLabelTEXT4, (GraphOneX+GraphWidth+LabelOffsetX,GraphOneY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphTwoX+GraphWidth+LabelOffsetX,GraphTwoY+GraphHeight+LabelOffsetY))
    win.blit(SupplyDemandAGraphVerticalLabelTEXT1, (GraphTwoX+GraphWidth+LabelOffsetX,GraphTwoY+LabelOffsetY))
    win.blit(SupplyDemandAGraphVerticalLabelTEXT2, (GraphTwoX+GraphWidth+LabelOffsetX,GraphTwoY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(SupplyDemandAGraphVerticalLabelTEXT3, (GraphTwoX+GraphWidth+LabelOffsetX,GraphTwoY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(SupplyDemandAGraphVerticalLabelTEXT4, (GraphTwoX+GraphWidth+LabelOffsetX,GraphTwoY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphThreeX+GraphWidth+LabelOffsetX,GraphThreeY+GraphHeight+LabelOffsetY))
    win.blit(SupplyDemandBGraphVerticalLabelTEXT1, (GraphThreeX+GraphWidth+LabelOffsetX,GraphThreeY+LabelOffsetY))
    win.blit(SupplyDemandBGraphVerticalLabelTEXT2, (GraphThreeX+GraphWidth+LabelOffsetX,GraphThreeY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(SupplyDemandBGraphVerticalLabelTEXT3, (GraphThreeX+GraphWidth+LabelOffsetX,GraphThreeY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(SupplyDemandBGraphVerticalLabelTEXT4, (GraphThreeX+GraphWidth+LabelOffsetX,GraphThreeY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphFourX+GraphWidth+LabelOffsetX,GraphFourY+GraphHeight+LabelOffsetY))
    win.blit(SupplyDemandCGraphVerticalLabelTEXT1, (GraphFourX+GraphWidth+LabelOffsetX,GraphFourY+LabelOffsetY))
    win.blit(SupplyDemandCGraphVerticalLabelTEXT2, (GraphFourX+GraphWidth+LabelOffsetX,GraphFourY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(SupplyDemandCGraphVerticalLabelTEXT3, (GraphFourX+GraphWidth+LabelOffsetX,GraphFourY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(SupplyDemandCGraphVerticalLabelTEXT4, (GraphFourX+GraphWidth+LabelOffsetX,GraphFourY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphFiveX+GraphWidth+LabelOffsetX,GraphFiveY+GraphHeight+LabelOffsetY))
    win.blit(BudgetPercentGraphVerticalLabelTEXT1, (GraphFiveX+GraphWidth+LabelOffsetX,GraphFiveY+LabelOffsetY))
    win.blit(BudgetPercentGraphVerticalLabelTEXT2, (GraphFiveX+GraphWidth+LabelOffsetX,GraphFiveY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(BudgetPercentGraphVerticalLabelTEXT3, (GraphFiveX+GraphWidth+LabelOffsetX,GraphFiveY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(BudgetPercentGraphVerticalLabelTEXT4, (GraphFiveX+GraphWidth+LabelOffsetX,GraphFiveY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphSixX+GraphWidth+LabelOffsetX,GraphSixY+GraphHeight+LabelOffsetY))
    win.blit(LabourPercentGraphVerticalLabelTEXT1, (GraphSixX+GraphWidth+LabelOffsetX,GraphSixY+LabelOffsetY))
    win.blit(LabourPercentGraphVerticalLabelTEXT2, (GraphSixX+GraphWidth+LabelOffsetX,GraphSixY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(LabourPercentGraphVerticalLabelTEXT3, (GraphSixX+GraphWidth+LabelOffsetX,GraphSixY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(LabourPercentGraphVerticalLabelTEXT4, (GraphSixX+GraphWidth+LabelOffsetX,GraphSixY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphSevenX+GraphWidth+LabelOffsetX,GraphSevenY+GraphHeight+LabelOffsetY))
    win.blit(MarginalUtilityMoneyGraphVerticalLabelTEXT1, (GraphSevenX+GraphWidth+LabelOffsetX,GraphSevenY+LabelOffsetY))
    win.blit(MarginalUtilityMoneyGraphVerticalLabelTEXT2, (GraphSevenX+GraphWidth+LabelOffsetX,GraphSevenY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(MarginalUtilityMoneyGraphVerticalLabelTEXT3, (GraphSevenX+GraphWidth+LabelOffsetX,GraphSevenY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(MarginalUtilityMoneyGraphVerticalLabelTEXT4, (GraphSevenX+GraphWidth+LabelOffsetX,GraphSevenY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphEightX+GraphWidth+LabelOffsetX,GraphEightY+GraphHeight+LabelOffsetY))
    win.blit(MarginalValueProductionGraphVerticalLabelTEXT1, (GraphEightX+GraphWidth+LabelOffsetX,GraphEightY+LabelOffsetY))
    win.blit(MarginalValueProductionGraphVerticalLabelTEXT2, (GraphEightX+GraphWidth+LabelOffsetX,GraphEightY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(MarginalValueProductionGraphVerticalLabelTEXT3, (GraphEightX+GraphWidth+LabelOffsetX,GraphEightY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(MarginalValueProductionGraphVerticalLabelTEXT4, (GraphEightX+GraphWidth+LabelOffsetX,GraphEightY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphNineX+GraphWidth+LabelOffsetX,GraphNineY+GraphHeight+LabelOffsetY))
    win.blit(ProductionFunctionGraphVerticalLabelTEXT1, (GraphNineX+GraphWidth+LabelOffsetX,GraphNineY+LabelOffsetY))
    win.blit(ProductionFunctionGraphVerticalLabelTEXT2, (GraphNineX+GraphWidth+LabelOffsetX,GraphNineY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(ProductionFunctionGraphVerticalLabelTEXT3, (GraphNineX+GraphWidth+LabelOffsetX,GraphNineY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(ProductionFunctionGraphVerticalLabelTEXT4, (GraphNineX+GraphWidth+LabelOffsetX,GraphNineY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphNineX,GraphNineY+GraphHeight))
    win.blit(ProductionFunctionGraphHorizontalLabelTEXT1, (GraphNineX+int(GraphWidth*1)-(ProductionFunctionGraphHorizontalLabelTEXT1.get_width()),GraphNineY+GraphHeight)) # -20
    win.blit(ProductionFunctionGraphHorizontalLabelTEXT2, (GraphNineX+int(GraphWidth*0.75),GraphNineY+GraphHeight))
    win.blit(ProductionFunctionGraphHorizontalLabelTEXT3, (GraphNineX+int(GraphWidth*0.5),GraphNineY+GraphHeight))
    win.blit(ProductionFunctionGraphHorizontalLabelTEXT4, (GraphNineX+int(GraphWidth*0.25),GraphNineY+GraphHeight))
    win.blit(VerticalLabelTEXTZero, (GraphTenX+GraphWidth+LabelOffsetX,GraphTenY+GraphHeight+LabelOffsetY))
    win.blit(MarginalDisUtilityLabourGraphVerticalLabelTEXT1, (GraphTenX+GraphWidth+LabelOffsetX,GraphTenY+LabelOffsetY))
    win.blit(MarginalDisUtilityLabourGraphVerticalLabelTEXT2, (GraphTenX+GraphWidth+LabelOffsetX,GraphTenY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(MarginalDisUtilityLabourGraphVerticalLabelTEXT3, (GraphTenX+GraphWidth+LabelOffsetX,GraphTenY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(MarginalDisUtilityLabourGraphVerticalLabelTEXT4, (GraphTenX+GraphWidth+LabelOffsetX,GraphTenY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphTenX,GraphTenY+GraphHeight))
    win.blit(MarginalDisUtilityLabourGraphHorizontalLabelTEXT1, (GraphTenX+int(GraphWidth*1)-(MarginalDisUtilityLabourGraphHorizontalLabelTEXT1.get_width()),GraphTenY+GraphHeight))
    win.blit(MarginalDisUtilityLabourGraphHorizontalLabelTEXT2, (GraphTenX+int(GraphWidth*0.75),GraphTenY+GraphHeight))
    win.blit(MarginalDisUtilityLabourGraphHorizontalLabelTEXT3, (GraphTenX+int(GraphWidth*0.5),GraphTenY+GraphHeight))
    win.blit(MarginalDisUtilityLabourGraphHorizontalLabelTEXT4, (GraphTenX+int(GraphWidth*0.25),GraphTenY+GraphHeight))
    win.blit(VerticalLabelTEXTZero, (GraphElevenX+GraphWidth+LabelOffsetX,GraphElevenY+GraphHeight+LabelOffsetY))
    win.blit(MarginalUtilityGraphVerticalLabelTEXT1, (GraphElevenX+GraphWidth+LabelOffsetX,GraphElevenY+LabelOffsetY))
    win.blit(MarginalUtilityGraphVerticalLabelTEXT2, (GraphElevenX+GraphWidth+LabelOffsetX,GraphElevenY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(MarginalUtilityGraphVerticalLabelTEXT3, (GraphElevenX+GraphWidth+LabelOffsetX,GraphElevenY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(MarginalUtilityGraphVerticalLabelTEXT4, (GraphElevenX+GraphWidth+LabelOffsetX,GraphElevenY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphElevenX,GraphElevenY+GraphHeight))
    win.blit(MarginalUtilityGraphHorizontalLabelTEXT1, (GraphElevenX+int(GraphWidth*1)-(MarginalUtilityGraphHorizontalLabelTEXT1.get_width()),GraphElevenY+GraphHeight))
    win.blit(MarginalUtilityGraphHorizontalLabelTEXT2, (GraphElevenX+int(GraphWidth*0.75),GraphElevenY+GraphHeight))
    win.blit(MarginalUtilityGraphHorizontalLabelTEXT3, (GraphElevenX+int(GraphWidth*0.5),GraphElevenY+GraphHeight))
    win.blit(MarginalUtilityGraphHorizontalLabelTEXT4, (GraphElevenX+int(GraphWidth*0.25),GraphElevenY+GraphHeight))
    win.blit(VerticalLabelTEXTZero, (GraphTwelveX+GraphWidth+LabelOffsetX,GraphTwelveY+GraphHeight+LabelOffsetY))
    win.blit(SupplyLabourGraphVerticalLabelTEXT1, (GraphTwelveX+GraphWidth+LabelOffsetX,GraphTwelveY+LabelOffsetY))
    win.blit(SupplyLabourGraphVerticalLabelTEXT2, (GraphTwelveX+GraphWidth+LabelOffsetX,GraphTwelveY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(SupplyLabourGraphVerticalLabelTEXT3, (GraphTwelveX+GraphWidth+LabelOffsetX,GraphTwelveY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(SupplyLabourGraphVerticalLabelTEXT4, (GraphTwelveX+GraphWidth+LabelOffsetX,GraphTwelveY+int(GraphHeight*0.75)+LabelOffsetY))
    win.blit(VerticalLabelTEXTZero, (GraphThirteenX+GraphWidth+LabelOffsetX,GraphThirteenY+GraphHeight+LabelOffsetY))
    win.blit(WageRateGraphVerticalLabelTEXT1, (GraphThirteenX+GraphWidth+LabelOffsetX,GraphThirteenY+LabelOffsetY))
    win.blit(WageRateGraphVerticalLabelTEXT2, (GraphThirteenX+GraphWidth+LabelOffsetX,GraphThirteenY+int(GraphHeight*0.25)+LabelOffsetY))
    win.blit(WageRateGraphVerticalLabelTEXT3, (GraphThirteenX+GraphWidth+LabelOffsetX,GraphThirteenY+int(GraphHeight*0.5)+LabelOffsetY))
    win.blit(WageRateGraphVerticalLabelTEXT4, (GraphThirteenX+GraphWidth+LabelOffsetX,GraphThirteenY+int(GraphHeight*0.75)+LabelOffsetY))
    #graph name
    win.blit(PriceNameLabelTEXT1, (GraphOneX+NameLabelOffsetX,GraphOneY+NameLabelOffsetY))
    win.blit(PriceNameLabelTEXT2, (GraphOneX+NameLabelOffsetX+int((1/3)*GraphWidth),GraphOneY+NameLabelOffsetY))
    win.blit(PriceNameLabelTEXT3, (GraphOneX+NameLabelOffsetX+int((2/3)*GraphWidth),GraphOneY+NameLabelOffsetY))
    win.blit(SupplyDemandATEXT1, (GraphTwoX+NameLabelOffsetX,GraphTwoY+NameLabelOffsetY))
    win.blit(SupplyDemandATEXT2, (GraphTwoX+NameLabelOffsetX+int((1/2)*GraphWidth),GraphTwoY+NameLabelOffsetY))
    win.blit(SupplyDemandBTEXT1, (GraphThreeX+NameLabelOffsetX,GraphThreeY+NameLabelOffsetY))
    win.blit(SupplyDemandBTEXT2, (GraphThreeX+NameLabelOffsetX+int((1/2)*GraphWidth),GraphThreeY+NameLabelOffsetY))
    win.blit(SupplyDemandCTEXT1, (GraphFourX+NameLabelOffsetX,GraphFourY+NameLabelOffsetY))
    win.blit(SupplyDemandCTEXT2, (GraphFourX+NameLabelOffsetX+int((1/2)*GraphWidth),GraphFourY+NameLabelOffsetY))
    win.blit(BudgetPercentTEXT1, (GraphFiveX+NameLabelOffsetX,GraphFiveY+NameLabelOffsetY))
    win.blit(BudgetPercentTEXT2, (GraphFiveX+int((1/3)*GraphWidth)+NameLabelOffsetX,GraphFiveY+NameLabelOffsetY))
    win.blit(BudgetPercentTEXT3, (GraphFiveX+int((2/3)*GraphWidth)+NameLabelOffsetX,GraphFiveY+NameLabelOffsetY))
    win.blit(LabourPercentTEXT1, (GraphSixX+NameLabelOffsetX,GraphSixY+NameLabelOffsetY))
    win.blit(LabourPercentTEXT2, (GraphSixX+int((1/3)*GraphWidth)+NameLabelOffsetX,GraphSixY+NameLabelOffsetY))
    win.blit(LabourPercentTEXT3, (GraphSixX+int((2/3)*GraphWidth)+NameLabelOffsetX,GraphSixY+NameLabelOffsetY))
    win.blit(MarginalUtilityMoneyTEXT1, (GraphSevenX+NameLabelOffsetX,GraphSevenY+NameLabelOffsetY))
    win.blit(MarginalUtilityMoneyTEXT2, (GraphSevenX+NameLabelOffsetX+int((1/4)*GraphWidth),GraphSevenY+NameLabelOffsetY))
    win.blit(MarginalUtilityMoneyTEXT3, (GraphSevenX+NameLabelOffsetX+int((2/4)*GraphWidth),GraphSevenY+NameLabelOffsetY))
    win.blit(MarginalUtilityMoneyTEXT4, (GraphSevenX+NameLabelOffsetX+int((3/4)*GraphWidth),GraphSevenY+NameLabelOffsetY))
    win.blit(MarginalValueProductionTEXT1, (GraphEightX+NameLabelOffsetX,GraphEightY+NameLabelOffsetY))
    win.blit(MarginalValueProductionTEXT2, (GraphEightX+NameLabelOffsetX+int((1/3)*GraphWidth),GraphEightY+NameLabelOffsetY))
    win.blit(MarginalValueProductionTEXT3, (GraphEightX+NameLabelOffsetX+int((2/3)*GraphWidth),GraphEightY+NameLabelOffsetY))
    win.blit(ProductionFunctionTEXT, (GraphNineX+NameLabelOffsetX,GraphNineY+NameLabelOffsetY))
    win.blit(MarginalDisUtilityLabourFunctionTEXT, (GraphTenX+NameLabelOffsetX,GraphTenY+NameLabelOffsetY))
    win.blit(MarginalUtilityFunctionTEXT, (GraphElevenX+NameLabelOffsetX,GraphElevenY+NameLabelOffsetY))
    win.blit(SupplyLabourTEXT,(GraphTwelveX+NameLabelOffsetX,GraphTwelveY+NameLabelOffsetY))
    win.blit(WageRateTEXT,((GraphThirteenX+NameLabelOffsetX,GraphThirteenY+NameLabelOffsetY)))
    #graph numbers
    PriceNumberLabelTEXT1 = font2.render("$"+str(round(PriceA)), 1, Blue)
    PriceNumberLabelTEXT2 = font2.render("$"+str(round(PriceB)), 1, Red)
    PriceNumberLabelTEXT3 = font2.render("$"+str(round(PriceC)), 1, Green)
    win.blit(PriceNumberLabelTEXT1, (GraphOneX+NumberLabelOffsetX,GraphOneY+NumberLabelOffsetY))
    win.blit(PriceNumberLabelTEXT2, (GraphOneX+int((1/3)*GraphWidth)+NumberLabelOffsetX,GraphOneY+NumberLabelOffsetY))
    win.blit(PriceNumberLabelTEXT3, (GraphOneX+int((2/3)*GraphWidth)+NumberLabelOffsetX,GraphOneY+NumberLabelOffsetY))
    SupplyDemandANumberTEXT1 = font2.render(str(round(SupplyA,RoundSupplyDemand)), 1, Blue)
    SupplyDemandANumberTEXT2 = font2.render(str(round(DemandA,RoundSupplyDemand)), 1, Red)
    win.blit(SupplyDemandANumberTEXT1, (GraphTwoX+NumberLabelOffsetX,GraphTwoY+NumberLabelOffsetY))
    win.blit(SupplyDemandANumberTEXT2, (GraphTwoX+NumberLabelOffsetX+int((1/2)*GraphWidth),GraphTwoY+NumberLabelOffsetY))
    SupplyDemandBNumberTEXT1 = font2.render(str(round(SupplyB,RoundSupplyDemand)), 1, Blue)
    SupplyDemandBNumberTEXT2 = font2.render(str(round(DemandB,RoundSupplyDemand)), 1, Red)
    win.blit(SupplyDemandBNumberTEXT1, (GraphThreeX+NumberLabelOffsetX,GraphThreeY+NumberLabelOffsetY))
    win.blit(SupplyDemandBNumberTEXT2, (GraphThreeX+NumberLabelOffsetX+int((1/2)*GraphWidth),GraphThreeY+NumberLabelOffsetY))
    SupplyDemandCNumberTEXT1 = font2.render(str(round(SupplyC,RoundSupplyDemand)), 1, Blue)
    SupplyDemandCNumberTEXT2 = font2.render(str(round(DemandC,RoundSupplyDemand)), 1, Red)
    win.blit(SupplyDemandCNumberTEXT1, (GraphFourX+NumberLabelOffsetX,GraphFourY+NumberLabelOffsetY))
    win.blit(SupplyDemandCNumberTEXT2, (GraphFourX+NumberLabelOffsetX+int((1/2)*GraphWidth),GraphFourY+NumberLabelOffsetY))
    BudgetPercentNumberTEXT1 = font2.render(str(round(DemandAPercentage))+"%", 1, Blue)
    BudgetPercentNumberTEXT2 = font2.render(str(round(DemandBPercentage))+"%", 1, Red)
    BudgetPercentNumberTEXT3 = font2.render(str(round(DemandCPercentage))+"%", 1, Green)
    win.blit(BudgetPercentNumberTEXT1, (GraphFiveX+NumberLabelOffsetX,GraphFiveY+NumberLabelOffsetY))
    win.blit(BudgetPercentNumberTEXT2, (GraphFiveX+int((1/3)*GraphWidth)+NumberLabelOffsetX,GraphFiveY+NumberLabelOffsetY))
    win.blit(BudgetPercentNumberTEXT3, (GraphFiveX+int((2/3)*GraphWidth)+NumberLabelOffsetX,GraphFiveY+NumberLabelOffsetY))
    LabourPercentNumberTEXT1 = font2.render(str(round(LabourAPercentage))+"%", 1, Blue)
    LabourPercentNumberTEXT2 = font2.render(str(round(LabourBPercentage))+"%", 1, Red)
    LabourPercentNumberTEXT3 = font2.render(str(round(LabourCPercentage))+"%", 1, Green)
    win.blit(LabourPercentNumberTEXT1, (GraphSixX+NumberLabelOffsetX,GraphSixY+NumberLabelOffsetY))
    win.blit(LabourPercentNumberTEXT2, (GraphSixX+int((1/3)*GraphWidth)+NumberLabelOffsetX,GraphSixY+NumberLabelOffsetY))
    win.blit(LabourPercentNumberTEXT3, (GraphSixX+int((2/3)*GraphWidth)+NumberLabelOffsetX,GraphSixY+NumberLabelOffsetY))
    MarginalUtilityMoneyNumberTEXT1 = font2.render(str(round(MarginalUtilityMoneySpentA,RoundMarginalUtilityMoney)), 1, Blue)
    MarginalUtilityMoneyNumberTEXT2 = font2.render(str(round(MarginalUtilityMoneySpentB,RoundMarginalUtilityMoney)), 1, Red)
    MarginalUtilityMoneyNumberTEXT3 = font2.render(str(round(MarginalUtilityMoneySpentC,RoundMarginalUtilityMoney)), 1, Green)
    MarginalUtilityMoneyNumberTEXT4 = font2.render(str(round(MarginalDisUtilityMoneyEarned,RoundMarginalUtilityMoney)), 1, Gold)
    win.blit(MarginalUtilityMoneyNumberTEXT1, (GraphSevenX+NumberLabelOffsetX,GraphSevenY+NumberLabelOffsetY))
    win.blit(MarginalUtilityMoneyNumberTEXT2, (GraphSevenX+NumberLabelOffsetX+int((1/4)*GraphWidth),GraphSevenY+NumberLabelOffsetY))
    win.blit(MarginalUtilityMoneyNumberTEXT3, (GraphSevenX+NumberLabelOffsetX+int((2/4)*GraphWidth),GraphSevenY+NumberLabelOffsetY))
    win.blit(MarginalUtilityMoneyNumberTEXT4, (GraphSevenX+NumberLabelOffsetX+int((3/4)*GraphWidth),GraphSevenY+NumberLabelOffsetY))
    MarginalValueProductionNumberTEXT1 = font2.render(str(round(MarginalValueProductionA,RoundMarginalValueProduction)), 1, Blue)
    MarginalValueProductionNumberTEXT2 = font2.render(str(round(MarginalValueProductionB,RoundMarginalValueProduction)), 1, Red)
    MarginalValueProductionNumberTEXT3 = font2.render(str(round(MarginalValueProductionC,RoundMarginalValueProduction)), 1, Green)
    win.blit(MarginalValueProductionNumberTEXT1, (GraphEightX+NumberLabelOffsetX,GraphEightY+NumberLabelOffsetY))
    win.blit(MarginalValueProductionNumberTEXT2, (GraphEightX+NumberLabelOffsetX+int((1/3)*GraphWidth),GraphEightY+NumberLabelOffsetY))
    win.blit(MarginalValueProductionNumberTEXT3, (GraphEightX+NumberLabelOffsetX+int((2/3)*GraphWidth),GraphEightY+NumberLabelOffsetY))
    SupplyLabourNumberTEXT = font2.render(str(round(SupplyLabour,RoundSupplyLabour)), 1, Blue)
    win.blit(SupplyLabourNumberTEXT, (GraphTwelveX+NumberLabelOffsetX,GraphTwelveY+NumberLabelOffsetY))
    WageRateNumberTEXT = font2.render("$"+str(round(WageRate,RoundWageRate)), 1, Blue)
    win.blit(WageRateNumberTEXT, (GraphThirteenX+NumberLabelOffsetX,GraphThirteenY+NumberLabelOffsetY))

def DrawLines():
    pygame.draw.lines(win, Blue, False, PriceAList, LineWidth)
    pygame.draw.lines(win, Red, False, PriceBList, LineWidth)
    pygame.draw.lines(win, Green, False, PriceCList, LineWidth)
    pygame.draw.lines(win, Blue, False, SupplyAList, LineWidth)
    pygame.draw.lines(win, Red, False, DemandAList, LineWidth)
    pygame.draw.lines(win, Blue, False, SupplyBList, LineWidth)
    pygame.draw.lines(win, Red, False, DemandBList, LineWidth)
    pygame.draw.lines(win, Blue, False, SupplyCList, LineWidth)
    pygame.draw.lines(win, Red, False, DemandCList, LineWidth)
    pygame.draw.lines(win, Blue, False, BudgetAList, LineWidth)
    pygame.draw.lines(win, Red, False, BudgetBList, LineWidth)
    pygame.draw.lines(win, Green, False, BudgetCList, LineWidth)
    pygame.draw.lines(win, Blue, False, LabourAList, LineWidth)
    pygame.draw.lines(win, Red, False, LabourBList, LineWidth)
    pygame.draw.lines(win, Green, False, LabourCList, LineWidth)
    pygame.draw.lines(win, Blue, False, MarginalUtilityMoneyAList, LineWidth)
    pygame.draw.lines(win, Red, False, MarginalUtilityMoneyBList, LineWidth)
    pygame.draw.lines(win, Green, False, MarginalUtilityMoneyCList, LineWidth)
    pygame.draw.lines(win, Gold, False, MarginalDisUtilityEarnMoneyList, LineWidth)
    pygame.draw.lines(win, Blue, False, MarginalValueProductionAList, LineWidth)
    pygame.draw.lines(win, Red, False, MarginalValueProductionBList, LineWidth)
    pygame.draw.lines(win, Green, False, MarginalValueProductionCList, LineWidth)
    pygame.draw.lines(win, Blue, False, SupplyLabourList, LineWidth)
    pygame.draw.lines(win, Blue, False, WageRateList, LineWidth)
    pygame.draw.lines(win, Blue, False, ProductionFunctionAList, LineWidth)
    pygame.draw.lines(win, Red, False, ProductionFunctionBList, LineWidth)
    pygame.draw.lines(win, Green, False, ProductionFunctionCList, LineWidth)
    pygame.draw.lines(win, White, False, MarginalDisUtilityLabourFunctionList, LineWidth)
    pygame.draw.lines(win, Blue, False, MarginalUtilityAFunctionList, LineWidth)
    pygame.draw.lines(win, Red, False, MarginalUtilityBFunctionList, LineWidth)
    pygame.draw.lines(win, Green, False, MarginalUtilityCFunctionList, LineWidth)
    
def DrawConnections():
    pygame.draw.line(win, White, (int(GraphTenX+((SupplyLabour/MarginalDisUtilityLabourGraphWidth)*GraphWidth)), GraphTenY+GraphHeight-1), (int(GraphTenX+((SupplyLabour/MarginalDisUtilityLabourGraphWidth)*GraphWidth)), int((GraphTenY+GraphHeight)- MDULList(int(GraphTenX+((SupplyLabour/MarginalDisUtilityLabourGraphWidth)*GraphWidth))))), 1)                                                                                       
    pygame.draw.line(win, White, (int(GraphTenX+((SupplyLabour/MarginalDisUtilityLabourGraphWidth)*GraphWidth)), int((GraphTenY+GraphHeight)- MDULList(int(GraphTenX+((SupplyLabour/MarginalDisUtilityLabourGraphWidth)*GraphWidth))))), (GraphTenX+GraphWidth-1, int((GraphTenY+GraphHeight)- MDULList(int(GraphTenX+((SupplyLabour/MarginalDisUtilityLabourGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Blue, (int(GraphNineX+((LabourA/ProductionFunctionGraphWidth)*GraphWidth)), GraphNineY+GraphHeight-1), (int(GraphNineX+((LabourA/ProductionFunctionGraphWidth)*GraphWidth)), int(GraphNineY+GraphHeight-ProdFuncAList(int(GraphNineX+((LabourA/ProductionFunctionGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Blue, (int(GraphNineX+((LabourA/ProductionFunctionGraphWidth)*GraphWidth)), int(GraphNineY+GraphHeight-ProdFuncAList(int(GraphNineX+((LabourA/ProductionFunctionGraphWidth)*GraphWidth))))), (GraphNineX+GraphWidth-1, int(GraphNineY+GraphHeight-ProdFuncAList(int(GraphNineX+((LabourA/ProductionFunctionGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Red, (int(GraphNineX+((LabourB/ProductionFunctionGraphWidth)*GraphWidth)), GraphNineY+GraphHeight-1), (int(GraphNineX+((LabourB/ProductionFunctionGraphWidth)*GraphWidth)), int(GraphNineY+GraphHeight-ProdFuncBList(int(GraphNineX+((LabourB/ProductionFunctionGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Red, (int(GraphNineX+((LabourB/ProductionFunctionGraphWidth)*GraphWidth)), int(GraphNineY+GraphHeight-ProdFuncBList(int(GraphNineX+((LabourB/ProductionFunctionGraphWidth)*GraphWidth))))), (GraphNineX+GraphWidth-1, int(GraphNineY+GraphHeight-ProdFuncBList(int(GraphNineX+((LabourB/ProductionFunctionGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Green, (int(GraphNineX+((LabourC/ProductionFunctionGraphWidth)*GraphWidth)), GraphNineY+GraphHeight-1), (int(GraphNineX+((LabourC/ProductionFunctionGraphWidth)*GraphWidth)), int(GraphNineY+GraphHeight-ProdFuncCList(int(GraphNineX+((LabourC/ProductionFunctionGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Green, (int(GraphNineX+((LabourC/ProductionFunctionGraphWidth)*GraphWidth)), int(GraphNineY+GraphHeight-ProdFuncCList(int(GraphNineX+((LabourC/ProductionFunctionGraphWidth)*GraphWidth))))), (GraphNineX+GraphWidth-1, int(GraphNineY+GraphHeight-ProdFuncCList(int(GraphNineX+((LabourC/ProductionFunctionGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Blue, (int(GraphElevenX+((DemandA/MarginalUtilityGraphWidth)*GraphWidth)), GraphElevenY+GraphHeight-1), (int(GraphElevenX+((DemandA/MarginalUtilityGraphWidth)*GraphWidth)), int(GraphElevenY+GraphHeight-MUAList(int(GraphElevenX+((DemandA/MarginalUtilityGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Blue, (int(GraphElevenX+((DemandA/MarginalUtilityGraphWidth)*GraphWidth)), int(GraphElevenY+GraphHeight-MUAList(int(GraphElevenX+((DemandA/MarginalUtilityGraphWidth)*GraphWidth))))), (GraphElevenX+GraphWidth-1, int(GraphElevenY+GraphHeight-MUAList(int(GraphElevenX+((DemandA/MarginalUtilityGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Red, (int(GraphElevenX+((DemandB/MarginalUtilityGraphWidth)*GraphWidth)), GraphElevenY+GraphHeight-1), (int(GraphElevenX+((DemandB/MarginalUtilityGraphWidth)*GraphWidth)), int(GraphElevenY+GraphHeight-MUBList(int(GraphElevenX+((DemandB/MarginalUtilityGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Red, (int(GraphElevenX+((DemandB/MarginalUtilityGraphWidth)*GraphWidth)), int(GraphElevenY+GraphHeight-MUBList(int(GraphElevenX+((DemandB/MarginalUtilityGraphWidth)*GraphWidth))))), (GraphElevenX+GraphWidth-1, int(GraphElevenY+GraphHeight-MUBList(int(GraphElevenX+((DemandB/MarginalUtilityGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Green, (int(GraphElevenX+((DemandC/MarginalUtilityGraphWidth)*GraphWidth)), GraphElevenY+GraphHeight-1), (int(GraphElevenX+((DemandC/MarginalUtilityGraphWidth)*GraphWidth)), int(GraphElevenY+GraphHeight-MUCList(int(GraphElevenX+((DemandC/MarginalUtilityGraphWidth)*GraphWidth))))), 1)
    pygame.draw.line(win, Green, (int(GraphElevenX+((DemandC/MarginalUtilityGraphWidth)*GraphWidth)), int(GraphElevenY+GraphHeight-MUCList(int(GraphElevenX+((DemandC/MarginalUtilityGraphWidth)*GraphWidth))))), (GraphElevenX+GraphWidth-1, int(GraphElevenY+GraphHeight-MUCList(int(GraphElevenX+((DemandC/MarginalUtilityGraphWidth)*GraphWidth))))), 1)

def DrawDropDown():
    pygame.draw.rect(win, GraphColour, (SliderDropDownX,SliderDropDownY,SliderDropDownWidth,SliderDropDownHeight), 1)
    
    if (MouseHoverOverGraphDropDown == False):
        pygame.draw.rect(win, Dark_Gray, (GraphDropDownX,GraphDropDownY,SliderDropDownWidth,DropDownThickness), 0)
        pygame.draw.rect(win, Gray, (GraphDropDownX,GraphDropDownY,SliderDropDownWidth,DropDownThickness), 1)
    if (MouseHoverOverGraphDropDown == True):
        pygame.draw.rect(win, Dark_Gray1, (GraphDropDownX,GraphDropDownY,SliderDropDownWidth,DropDownThickness), 0)
        pygame.draw.rect(win, Gray, (GraphDropDownX,GraphDropDownY,SliderDropDownWidth,DropDownThickness), 1)
    win.blit(DropDownGraphTEXT, (GraphDropDownX+8, GraphDropDownY+2))

    if (MouseHoverOverVariableDropDown == False):
        pygame.draw.rect(win, Dark_Gray, (VariableDropDownX,VariableDropDownY,SliderDropDownWidth,DropDownThickness), 0)
        pygame.draw.rect(win, Gray, (VariableDropDownX,VariableDropDownY,SliderDropDownWidth,DropDownThickness), 1)
    if (MouseHoverOverVariableDropDown == True):
        pygame.draw.rect(win, Dark_Gray1, (VariableDropDownX,VariableDropDownY,SliderDropDownWidth,DropDownThickness), 0)
        pygame.draw.rect(win, Gray, (VariableDropDownX,VariableDropDownY,SliderDropDownWidth,DropDownThickness), 1)
    win.blit(DropDownVariableTEXT, (VariableDropDownX+8, VariableDropDownY+2))

def DrawSliders():
    if (DropDownSelected == "Variable"):

        if (ShowVariableSliderHitBox == True):
            pygame.draw.rect(win, Red, (VariableSliderHitBoxOneX,VariableSliderHitBoxOneY,VariableSliderHitBoxWidthOne,VariableSliderHitBoxHeightOne), 1)
            pygame.draw.rect(win, Red, (VariableSliderHitBoxTwoX,VariableSliderHitBoxTwoY,VariableSliderHitBoxWidthTwo,VariableSliderHitBoxHeightTwo), 1)
            pygame.draw.rect(win, Red, (VariableSliderHitBoxThreeX,VariableSliderHitBoxThreeY,VariableSliderHitBoxWidthThree,VariableSliderHitBoxHeightThree), 1)
            pygame.draw.rect(win, Red, (VariableSliderHitBoxFourX,VariableSliderHitBoxFourY,VariableSliderHitBoxWidthFour,VariableSliderHitBoxHeightFour), 1)
            pygame.draw.rect(win, Red, (VariableSliderHitBoxFiveX,VariableSliderHitBoxFiveY,VariableSliderHitBoxWidthFive,VariableSliderHitBoxHeightFive), 1)
            pygame.draw.rect(win, Red, (VariableSliderHitBoxSixX,VariableSliderHitBoxSixY,VariableSliderHitBoxWidthSix,VariableSliderHitBoxHeightSix), 1)
            pygame.draw.rect(win, Red, (VariableSliderHitBoxSevenX,VariableSliderHitBoxSevenY,VariableSliderHitBoxWidthSeven,VariableSliderHitBoxHeightSeven), 1)

        win.blit(VariableMenuTEXT, (VariablesMenuX,VariablesMenuY))
        
        pygame.draw.rect(win, Gray, (VariableSliderOneX,VariableSliderOneY,SliderWidth,SliderThickness))
        pygame.draw.rect(win, Gray, (VariableSliderTwoX,VariableSliderTwoY,SliderWidth,SliderThickness))
        pygame.draw.rect(win, Gray, (VariableSliderThreeX,VariableSliderThreeY,SliderWidth,SliderThickness))
        pygame.draw.rect(win, Gray, (VariableSliderFourX,VariableSliderFourY,SliderWidth,SliderThickness))
        pygame.draw.rect(win, Gray, (VariableSliderFiveX,VariableSliderFiveY,SliderWidth,SliderThickness))
        pygame.draw.rect(win, Gray, (VariableSliderSixX,VariableSliderSixY,SliderWidth,SliderThickness))
        pygame.draw.rect(win, Gray, (VariableSliderSevenX,VariableSliderSevenY,SliderWidth,SliderThickness))
        
        win.blit(MUASliderTEXT, (VariableSliderOneX+SliderTextOffsetX,VariableSliderOneY+SliderTextOffsetY))
        win.blit(MUBSliderTEXT, (VariableSliderTwoX+SliderTextOffsetX,VariableSliderTwoY+SliderTextOffsetY))
        win.blit(MUCSliderTEXT, (VariableSliderThreeX+SliderTextOffsetX,VariableSliderThreeY+SliderTextOffsetY))
        win.blit(MDULSliderTEXT, (VariableSliderFourX+SliderTextOffsetX,VariableSliderFourY+SliderTextOffsetY))
        win.blit(ProdASliderTEXT, (VariableSliderFiveX+SliderTextOffsetX,VariableSliderFiveY+SliderTextOffsetY))
        win.blit(ProdBSliderTEXT, (VariableSliderSixX+SliderTextOffsetX,VariableSliderSixY+SliderTextOffsetY))
        win.blit(ProdCSliderTEXT, (VariableSliderSevenX+SliderTextOffsetX,VariableSliderSevenY+SliderTextOffsetY))

        pygame.draw.rect(win, Red, (SliderDotOneX,SliderDotOneY,SliderThickness,SliderThickness))
        pygame.draw.rect(win, Red, (SliderDotTwoX,SliderDotTwoY,SliderThickness,SliderThickness))
        pygame.draw.rect(win, Red, (SliderDotThreeX,SliderDotThreeY,SliderThickness,SliderThickness))
        pygame.draw.rect(win, Red, (SliderDotFourX,SliderDotFourY,SliderThickness,SliderThickness))
        pygame.draw.rect(win, Red, (SliderDotFiveX,SliderDotFiveY,SliderThickness,SliderThickness))
        pygame.draw.rect(win, Red, (SliderDotSixX,SliderDotSixY,SliderThickness,SliderThickness))
        pygame.draw.rect(win, Red, (SliderDotSevenX,SliderDotSevenY,SliderThickness,SliderThickness))
        if (VariableSliderSelected == "One"):
            pygame.draw.rect(win, White, (SliderDotOneX,SliderDotOneY,SliderThickness,SliderThickness))
        if (VariableSliderSelected == "Two"):
            pygame.draw.rect(win, White, (SliderDotTwoX,SliderDotTwoY,SliderThickness,SliderThickness))
        if (VariableSliderSelected == "Three"):
            pygame.draw.rect(win, White, (SliderDotThreeX,SliderDotThreeY,SliderThickness,SliderThickness))
        if (VariableSliderSelected == "Four"):
            pygame.draw.rect(win, White, (SliderDotFourX,SliderDotFourY,SliderThickness,SliderThickness))
        if (VariableSliderSelected == "Five"):
            pygame.draw.rect(win, White, (SliderDotFiveX,SliderDotFiveY,SliderThickness,SliderThickness))
        if (VariableSliderSelected == "Six"):
            pygame.draw.rect(win, White, (SliderDotSixX,SliderDotSixY,SliderThickness,SliderThickness))
        if (VariableSliderSelected == "Seven"):
            pygame.draw.rect(win, White, (SliderDotSevenX,SliderDotSevenY,SliderThickness,SliderThickness))
            
        TEXT1 = font.render("+"+str(round(SliderVariableScaleOne*VariableSliderValueOne))+"%", 1, Green)
        TEXT2 = font.render("+"+str(round(SliderVariableScaleTwo*VariableSliderValueTwo))+"%", 1, Green)
        TEXT3 = font.render("+"+str(round(SliderVariableScaleThree*VariableSliderValueThree))+"%", 1, Green)
        TEXT4 = font.render("+"+str(round(SliderVariableScaleFour*VariableSliderValueFour))+"%", 1, Green)
        TEXT5 = font.render("+"+str(round(SliderVariableScaleFive*VariableSliderValueFive))+"%", 1, Green)
        TEXT6 = font.render("+"+str(round(SliderVariableScaleSix*VariableSliderValueSix))+"%", 1, Green)
        TEXT7 = font.render("+"+str(round(SliderVariableScaleSeven*VariableSliderValueSeven))+"%", 1, Green)
        win.blit(TEXT1, (VariableSliderOneX+SliderWidth+10,VariableSliderOneY+SliderTextOffsetY))
        win.blit(TEXT2, (VariableSliderTwoX+SliderWidth+10,VariableSliderTwoY+SliderTextOffsetY))
        win.blit(TEXT3, (VariableSliderThreeX+SliderWidth+10,VariableSliderThreeY+SliderTextOffsetY))
        win.blit(TEXT4, (VariableSliderFourX+SliderWidth+10,VariableSliderFourY+SliderTextOffsetY))
        win.blit(TEXT5, (VariableSliderFiveX+SliderWidth+10,VariableSliderFiveY+SliderTextOffsetY))
        win.blit(TEXT6, (VariableSliderSixX+SliderWidth+10,VariableSliderSixY+SliderTextOffsetY))
        win.blit(TEXT7, (VariableSliderSevenX+SliderWidth+10,VariableSliderSevenY+SliderTextOffsetY))

        pygame.draw.rect(win, White, (VariableSliderHitboxButtonX,VariableSliderHitboxButtonY,VariableSliderHitboxButtonWidth,VariableSliderHitboxButtonHeight))
        win.blit(VariableSliderHitBoxButtonTEXT, (VariableSliderHitboxButtonX+10,VariableSliderHitboxButtonY))

        if (PAUSE == False):
            pygame.draw.rect(win, White, (PauseButtonX,PauseButtonY,PauseButtonWidth,PauseButtonHeight))
            win.blit(PauseTEXT, (PauseButtonX+10,PauseButtonY))
        if (PAUSE == True):
            pygame.draw.rect(win, White, (PauseButtonX,PauseButtonY,PauseButtonWidth,PauseButtonHeight))
            win.blit(PlayTEXT, (PauseButtonX+10,PauseButtonY))
        
        pygame.draw.rect(win, White, (StepButtonX,StepButtonY,StepButtonWidth,StepButtonHeight))
        win.blit(StepTEXT, (StepButtonX+10,StepButtonY))

    if (DropDownSelected == "Graph"):
        win.blit(tempGraphtext, (VariablesMenuX,VariablesMenuY))
        pass
    if (DropDownSelected == "None"):
        win.blit(tempNoneText, (VariablesMenuX,VariablesMenuY))
        pass

def DrawFPS():
    FPSText = font3.render("FPS/UPS: "+str(round(FPS)), 1, White)
    win.blit(FPSText, (DisplayX-134,0))

def MarginalDisUtilityLabourFunction(x):
    return ((1/((-1*x)+16))-(1/16))*400*(1+(SliderVariableScaleFour*(VariableSliderValueFour/100)))

def ProductionFunctionA(x):
    return (x**0.5)*3*(1+(SliderVariableScaleFive*(VariableSliderValueFive/100)))
def ProductionFunctionB(x):
    return (x**0.5)*4*(1+(SliderVariableScaleSix*(VariableSliderValueSix/100)))
def ProductionFunctionC(x):
    return (x**0.5)*6*(1+(SliderVariableScaleSeven*(VariableSliderValueSeven/100)))

def MarginalUtilityFunctionA(x):
    return (0.9**x)*17*(1+(SliderVariableScaleOne*(VariableSliderValueOne/100)))
def MarginalUtilityFunctionB(x):
    return (0.9**x)*10*(1+(SliderVariableScaleTwo*(VariableSliderValueTwo/100)))
def MarginalUtilityFunctionC(x):
    return (0.9**x)*6*(1+(SliderVariableScaleThree*(VariableSliderValueThree/100)))

def IncrementPercentage(a,b,c):
    a = a + Increment
    x = a+b+c
    a = (a/x)*100
    b = (b/x)*100
    c = (c/x)*100
    return a,b,c

def ProdFuncAList(x):
    a = ((GraphHeight*(ProductionFunctionA(((x-GraphNineX)/GraphWidth)*ProductionFunctionGraphWidth)))/ProductionFunctionGraphHeight)+1
    if (a > GraphHeight):
        return GraphHeight
    else:
        return a

def ProdFuncBList(x):
    a = ((GraphHeight*(ProductionFunctionB(((x-GraphNineX)/GraphWidth)*ProductionFunctionGraphWidth)))/ProductionFunctionGraphHeight)+1
    if (a > GraphHeight):
        return GraphHeight
    else:
        return a

def ProdFuncCList(x):
    a = ((GraphHeight*(ProductionFunctionC(((x-GraphNineX)/GraphWidth)*ProductionFunctionGraphWidth)))/ProductionFunctionGraphHeight)+1
    if (a > GraphHeight):
        return GraphHeight
    else:
        return a

def MDULList(x):
    a = ((GraphHeight*(MarginalDisUtilityLabourFunction(((x-GraphTenX)/GraphWidth)*MarginalDisUtilityLabourGraphWidth)))/MarginalDisUtilityLabourGraphHeight)+1
    if (a > GraphHeight):
        return GraphHeight
    else:
        return a

def MUAList(x):
    a = ((GraphHeight*(MarginalUtilityFunctionA(((x-GraphElevenX)/GraphWidth)*MarginalUtilityGraphWidth)))/MarginalUtilityGraphHeight)+1
    if (a > GraphHeight):
        return GraphHeight
    else:
        return a

def MUBList(x):
    a = ((GraphHeight*(MarginalUtilityFunctionB(((x-GraphElevenX)/GraphWidth)*MarginalUtilityGraphWidth)))/MarginalUtilityGraphHeight)+1
    if (a > GraphHeight):
        return GraphHeight
    else:
        return a

def MUCList(x):
    a = ((GraphHeight*(MarginalUtilityFunctionC(((x-GraphElevenX)/GraphWidth)*MarginalUtilityGraphWidth)))/MarginalUtilityGraphHeight)+1
    if (a > GraphHeight):
        return GraphHeight
    else:
        return a

while (len(ProductionFunctionAList) < GraphWidth):
    ProductionFunctionAList.append((GraphNineX+len(ProductionFunctionAList),0))
    
while (len(ProductionFunctionBList) < GraphWidth):
    ProductionFunctionBList.append((GraphNineX+len(ProductionFunctionBList),0))
    
while (len(ProductionFunctionCList) < GraphWidth):
    ProductionFunctionCList.append((GraphNineX+len(ProductionFunctionCList),0))

while (len(MarginalDisUtilityLabourFunctionList) < GraphWidth):
    MarginalDisUtilityLabourFunctionList.append((GraphTenX+len(MarginalDisUtilityLabourFunctionList),0))

while (len(MarginalUtilityAFunctionList) < GraphWidth):
    MarginalUtilityAFunctionList.append((GraphElevenX+len(MarginalUtilityAFunctionList),0))

while (len(MarginalUtilityBFunctionList) < GraphWidth):
    MarginalUtilityBFunctionList.append((GraphElevenX+len(MarginalUtilityBFunctionList),0))

while (len(MarginalUtilityCFunctionList) < GraphWidth):
    MarginalUtilityCFunctionList.append((GraphElevenX+len(MarginalUtilityCFunctionList),0))

run = True
while run == True:
    start_time = time.time()

    MouseX, MouseY = pygame.mouse.get_pos()
    MouseLeft, MouseScroll, MouseRight = pygame.mouse.get_pressed()
    Mouse_RelX, Mouse_RelY = pygame.mouse.get_rel()
    keys = pygame.key.get_pressed()

    if (GraphDropDownX < MouseX < GraphDropDownX+SliderDropDownWidth) and (GraphDropDownY < MouseY < GraphDropDownY+DropDownThickness):
        MouseHoverOverGraphDropDown = True
    else:
        MouseHoverOverGraphDropDown = False

    if (VariableDropDownX < MouseX < VariableDropDownX+SliderDropDownWidth) and (VariableDropDownY < MouseY < VariableDropDownY+DropDownThickness):
        MouseHoverOverVariableDropDown = True
    else:
        MouseHoverOverVariableDropDown = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if (MouseHoverOverGraphDropDown == True) and (event.type == pygame.MOUSEBUTTONUP) and (DropDownSelected == "None"):
            DropDownSelected = "Graph"
        elif (MouseHoverOverGraphDropDown == True) and (event.type == pygame.MOUSEBUTTONUP) and (DropDownSelected == "Graph"):
            DropDownSelected = "None"
        elif (MouseHoverOverGraphDropDown == True) and (event.type == pygame.MOUSEBUTTONUP) and (DropDownSelected == "Variable"):
            DropDownSelected = "Graph"

        if (MouseHoverOverVariableDropDown == True) and (event.type == pygame.MOUSEBUTTONUP) and (DropDownSelected == "None"):
            DropDownSelected = "Variable"
        elif (MouseHoverOverVariableDropDown == True) and (event.type == pygame.MOUSEBUTTONUP) and (DropDownSelected == "Graph"):
            DropDownSelected = "Variable"
        elif (MouseHoverOverVariableDropDown == True) and (event.type == pygame.MOUSEBUTTONUP) and (DropDownSelected == "Variable"):
            DropDownSelected = "None"

        if (DropDownSelected == "Variable"):
            if (event.type == pygame.MOUSEBUTTONDOWN) and (VariableSliderHitBoxOneX < MouseX < VariableSliderHitBoxOneX+VariableSliderHitBoxWidthOne) and (VariableSliderHitBoxOneY < MouseY < VariableSliderHitBoxOneY+VariableSliderHitBoxHeightOne):
                VariableSliderSelected = "One"
            if (event.type == pygame.MOUSEBUTTONDOWN) and (VariableSliderHitBoxTwoX < MouseX < VariableSliderHitBoxTwoX+VariableSliderHitBoxWidthTwo) and (VariableSliderHitBoxTwoY < MouseY < VariableSliderHitBoxTwoY+VariableSliderHitBoxHeightTwo):
                VariableSliderSelected = "Two"
            if (event.type == pygame.MOUSEBUTTONDOWN) and (VariableSliderHitBoxThreeX < MouseX < VariableSliderHitBoxThreeX+VariableSliderHitBoxWidthThree) and (VariableSliderHitBoxThreeY < MouseY < VariableSliderHitBoxThreeY+VariableSliderHitBoxHeightThree):
                VariableSliderSelected = "Three"
            if (event.type == pygame.MOUSEBUTTONDOWN) and (VariableSliderHitBoxFourX < MouseX < VariableSliderHitBoxFourX+VariableSliderHitBoxWidthFour) and (VariableSliderHitBoxFourY < MouseY < VariableSliderHitBoxFourY+VariableSliderHitBoxHeightFour):
                VariableSliderSelected = "Four"
            if (event.type == pygame.MOUSEBUTTONDOWN) and (VariableSliderHitBoxFiveX < MouseX < VariableSliderHitBoxFiveX+VariableSliderHitBoxWidthFive) and (VariableSliderHitBoxFiveY < MouseY < VariableSliderHitBoxFiveY+VariableSliderHitBoxHeightFive):
                VariableSliderSelected = "Five"
            if (event.type == pygame.MOUSEBUTTONDOWN) and (VariableSliderHitBoxSixX < MouseX < VariableSliderHitBoxSixX+VariableSliderHitBoxWidthSix) and (VariableSliderHitBoxSixY < MouseY < VariableSliderHitBoxSixY+VariableSliderHitBoxHeightSix):
                VariableSliderSelected = "Six"
            if (event.type == pygame.MOUSEBUTTONDOWN) and (VariableSliderHitBoxSevenX < MouseX < VariableSliderHitBoxSevenX+VariableSliderHitBoxWidthSeven) and (VariableSliderHitBoxSevenY < MouseY < VariableSliderHitBoxSevenY+VariableSliderHitBoxHeightSeven):
                VariableSliderSelected = "Seven"
            if (event.type == pygame.MOUSEBUTTONUP):
                VariableSliderSelected = "None"
            if (VariableSliderHitboxButtonX < MouseX < VariableSliderHitboxButtonX+VariableSliderHitboxButtonWidth) and (VariableSliderHitboxButtonY < MouseY < VariableSliderHitboxButtonY+VariableSliderHitboxButtonHeight) and (event.type == pygame.MOUSEBUTTONUP) and (ShowVariableSliderHitBox == True):
                ShowVariableSliderHitBox = False
            elif (VariableSliderHitboxButtonX < MouseX < VariableSliderHitboxButtonX+VariableSliderHitboxButtonWidth) and (VariableSliderHitboxButtonY < MouseY < VariableSliderHitboxButtonY+VariableSliderHitboxButtonHeight) and (event.type == pygame.MOUSEBUTTONUP) and (ShowVariableSliderHitBox == False):
                ShowVariableSliderHitBox = True
            if (PauseButtonX < MouseX < PauseButtonX+PauseButtonWidth) and (PauseButtonY < MouseY < PauseButtonY+PauseButtonHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
                if (PAUSE == True):
                    PAUSE = False
                elif (PAUSE == False):
                    PAUSE = True
            if (StepButtonX < MouseX < StepButtonX+StepButtonWidth) and (StepButtonY < MouseY < StepButtonY+StepButtonHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
                STEPPING = True

        if (DropDownSelected == "Graph"):
            pass

        if (DropDownSelected == "None"):
            pass

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "One"):
            if event.button == 4:
                PriceGraphHeight += ScrollStepSizeOne
                if (PriceGraphHeight > OneMax):
                    PriceGraphHeight = OneMax
            elif event.button == 5:
                PriceGraphHeight += -ScrollStepSizeOne
                if (PriceGraphHeight < OneMin):
                    PriceGraphHeight = OneMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Two"):
            if event.button == 4:
                SupplyDemandAGraphHeight += ScrollStepSizeTwo
                if (SupplyDemandAGraphHeight > TwoMax):
                    SupplyDemandAGraphHeight = TwoMax
            elif event.button == 5:
                SupplyDemandAGraphHeight += -ScrollStepSizeTwo
                if (SupplyDemandAGraphHeight < TwoMin):
                    SupplyDemandAGraphHeight = TwoMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Three"):
            if event.button == 4:
                SupplyDemandBGraphHeight += ScrollStepSizeThree
                if (SupplyDemandBGraphHeight > ThreeMax):
                    SupplyDemandBGraphHeight = ThreeMax
            elif event.button == 5:
                SupplyDemandBGraphHeight += -ScrollStepSizeThree
                if (SupplyDemandBGraphHeight < ThreeMin):
                    SupplyDemandBGraphHeight = ThreeMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Four"):
            if event.button == 4:
                SupplyDemandCGraphHeight += ScrollStepSizeFour
                if (SupplyDemandCGraphHeight > FourMax):
                    SupplyDemandCGraphHeight = FourMax
            elif event.button == 5:
                SupplyDemandCGraphHeight += -ScrollStepSizeFour
                if (SupplyDemandCGraphHeight < FourMin):
                    SupplyDemandCGraphHeight = FourMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Five"):
            if event.button == 4:
                BudgetPercentGraphHeight += ScrollStepSizeFive
                if (BudgetPercentGraphHeight > FiveMax):
                    BudgetPercentGraphHeight = FiveMax
            elif event.button == 5:
                BudgetPercentGraphHeight += -ScrollStepSizeFive
                if (BudgetPercentGraphHeight < FiveMin):
                    BudgetPercentGraphHeight = FiveMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Six"):
            if event.button == 4:
                LabourPercentGraphHeight += ScrollStepSizeSix
                if (LabourPercentGraphHeight > SixMax):
                    LabourPercentGraphHeight = SixMax
            elif event.button == 5:
                LabourPercentGraphHeight += -ScrollStepSizeSix
                if (LabourPercentGraphHeight < SixMin):
                    LabourPercentGraphHeight = SixMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Seven"):
            if event.button == 4:
                MarginalUtilityMoneyGraphHeight += ScrollStepSizeSeven
                if (MarginalUtilityMoneyGraphHeight > SevenMax):
                    MarginalUtilityMoneyGraphHeight = SevenMax
            elif event.button == 5:
                MarginalUtilityMoneyGraphHeight += -ScrollStepSizeSeven
                if (MarginalUtilityMoneyGraphHeight < SevenMin):
                    MarginalUtilityMoneyGraphHeight = SevenMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Eight"):
            if event.button == 4:
                MarginalValueProductionGraphHeight += ScrollStepSizeEight
                if (MarginalValueProductionGraphHeight > EightMax):
                    MarginalValueProductionGraphHeight = EightMax
            elif event.button == 5:
                MarginalValueProductionGraphHeight += -ScrollStepSizeEight
                if (MarginalValueProductionGraphHeight < EightMin):
                    MarginalValueProductionGraphHeight = EightMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Nine"):
            if event.button == 4:
                ProductionFunctionGraphHeight += ScrollStepSizeNine
                if (ProductionFunctionGraphHeight > NineMax):
                    ProductionFunctionGraphHeight = NineMax
            elif event.button == 5:
                ProductionFunctionGraphHeight += -ScrollStepSizeNine
                if (ProductionFunctionGraphHeight < NineMin):
                    ProductionFunctionGraphHeight = NineMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Ten"):
            if event.button == 4:
                MarginalDisUtilityLabourGraphHeight += ScrollStepSizeTen
                if (MarginalDisUtilityLabourGraphHeight > TenMax):
                    MarginalDisUtilityLabourGraphHeight = TenMax
            elif event.button == 5:
                MarginalDisUtilityLabourGraphHeight += -ScrollStepSizeTen
                if (MarginalDisUtilityLabourGraphHeight < TenMin):
                    MarginalDisUtilityLabourGraphHeight = TenMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Eleven"):
            if event.button == 4:
                MarginalUtilityGraphHeight += ScrollStepSizeEleven
                if (MarginalUtilityGraphHeight > ElevenMax):
                    MarginalUtilityGraphHeight = ElevenMax
            elif event.button == 5:
                MarginalUtilityGraphHeight += -ScrollStepSizeEleven
                if (MarginalUtilityGraphHeight < ElevenMin):
                    MarginalUtilityGraphHeight = ElevenMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Twelve"):
            if event.button == 4:
                SupplyLabourGraphHeight += ScrollStepSizeTwelve
                if (SupplyLabourGraphHeight > TwelveMax):
                    SupplyLabourGraphHeight = TwelveMax
            elif event.button == 5:
                SupplyLabourGraphHeight += -ScrollStepSizeTwelve
                if (SupplyLabourGraphHeight < TwelveMin):
                    SupplyLabourGraphHeight = TwelveMin

        if (event.type == pygame.MOUSEBUTTONDOWN) and (MouseOverGraph == "Thirteen"):
            if event.button == 4:
                WageRateGraphHeight += ScrollStepSizeThirteen
                if (WageRateGraphHeight > ThirteenMax):
                    WageRateGraphHeight = ThirteenMax
            elif event.button == 5:
                WageRateGraphHeight += -ScrollStepSizeThirteen
                if (WageRateGraphHeight < ThirteenMin):
                    WageRateGraphHeight = ThirteenMin

    if (PAUSE == False) or (STEPPING == True):
        WageRate = Income / SupplyLabour

        LabourA = SupplyLabour * (LabourAPercentage / 100)
        LabourB = SupplyLabour * (LabourBPercentage / 100)
        LabourC = SupplyLabour * (LabourCPercentage / 100)

        SupplyA = ProductionFunctionA(LabourA)
        SupplyB = ProductionFunctionB(LabourB)
        SupplyC = ProductionFunctionC(LabourC)

        MoneySpentA = Income * (DemandAPercentage / 100)
        MoneySpentB = Income * (DemandBPercentage / 100)
        MoneySpentC = Income * (DemandCPercentage / 100)

        DemandA = MoneySpentA / PriceA
        DemandB = MoneySpentB / PriceB
        DemandC = MoneySpentC / PriceC

        MarginalUtilityA = MarginalUtilityFunctionA(DemandA)
        MarginalUtilityB = MarginalUtilityFunctionB(DemandB)
        MarginalUtilityC = MarginalUtilityFunctionC(DemandC)

        MarginalUtilityMoneySpentA = MarginalUtilityA * (MarginalMoney / PriceA)
        MarginalUtilityMoneySpentB = MarginalUtilityB * (MarginalMoney / PriceB)
        MarginalUtilityMoneySpentC = MarginalUtilityC * (MarginalMoney / PriceC)

        MarginalDisUtilityLabour = MarginalDisUtilityLabourFunction(SupplyLabour)
        MarginalDisUtilityMoneyEarned = MarginalDisUtilityLabour * (MarginalMoney / WageRate)

        if (MarginalUtilityMoneySpentA > MarginalUtilityMoneySpentB) and (MarginalUtilityMoneySpentA > MarginalUtilityMoneySpentC):
            DemandAPercentage,DemandBPercentage,DemandCPercentage = IncrementPercentage(DemandAPercentage,DemandBPercentage,DemandCPercentage)
        if (MarginalUtilityMoneySpentB > MarginalUtilityMoneySpentA) and (MarginalUtilityMoneySpentB > MarginalUtilityMoneySpentC):
            DemandBPercentage,DemandAPercentage,DemandCPercentage = IncrementPercentage(DemandBPercentage,DemandAPercentage,DemandCPercentage)
        if (MarginalUtilityMoneySpentC > MarginalUtilityMoneySpentA) and (MarginalUtilityMoneySpentC > MarginalUtilityMoneySpentB):
            DemandCPercentage,DemandBPercentage,DemandAPercentage = IncrementPercentage(DemandCPercentage,DemandBPercentage,DemandAPercentage)

        if (MarginalDisUtilityMoneyEarned > max(MarginalUtilityMoneySpentA,MarginalUtilityMoneySpentB,MarginalUtilityMoneySpentC)):
            SupplyLabour = SupplyLabour / RateChangeSupplyLabour
        if (MarginalDisUtilityMoneyEarned < max(MarginalUtilityMoneySpentA,MarginalUtilityMoneySpentB,MarginalUtilityMoneySpentC)):
            SupplyLabour = SupplyLabour * RateChangeSupplyLabour

        MarginalProductionA = ProductionFunctionA(LabourA + (SupplyLabour/1000)) - ProductionFunctionA(LabourA)
        MarginalProductionB = ProductionFunctionB(LabourB + (SupplyLabour/1000)) - ProductionFunctionB(LabourB)
        MarginalProductionC = ProductionFunctionC(LabourC + (SupplyLabour/1000)) - ProductionFunctionC(LabourC)

        MarginalValueProductionA = MarginalProductionA * PriceA
        MarginalValueProductionB = MarginalProductionB * PriceB
        MarginalValueProductionC = MarginalProductionC * PriceC

        if (max(MarginalValueProductionA,MarginalValueProductionB,MarginalValueProductionC) == MarginalValueProductionA):
            LabourAPercentage,LabourBPercentage,LabourCPercentage = IncrementPercentage(LabourAPercentage,LabourBPercentage,LabourCPercentage)
        if (max(MarginalValueProductionA,MarginalValueProductionB,MarginalValueProductionC) == MarginalValueProductionB):
            LabourBPercentage,LabourAPercentage,LabourCPercentage = IncrementPercentage(LabourBPercentage,LabourAPercentage,LabourCPercentage)
        if (max(MarginalValueProductionA,MarginalValueProductionB,MarginalValueProductionC) == MarginalValueProductionC):
            LabourCPercentage,LabourBPercentage,LabourAPercentage = IncrementPercentage(LabourCPercentage,LabourBPercentage,LabourAPercentage)

        PriceA = MoneySpentA / SupplyA
        PriceB = MoneySpentB / SupplyB
        PriceC = MoneySpentC / SupplyC

        IncomeMarketA = MoneySpentA
        IncomeMarketB = MoneySpentB
        IncomeMarketC = MoneySpentC

        Income = round(IncomeMarketA + IncomeMarketB + IncomeMarketC)

        PriceAList.append((GraphOneX+len(PriceAList),(GraphOneY+GraphHeight)-int((GraphHeight*PriceA)/PriceGraphHeight)))
        if (len(PriceAList) > (GraphWidth)):
            PriceAList.pop(0)
            PriceAList = [(x-1,y) for (x,y) in PriceAList]
        PriceBList.append((GraphOneX+len(PriceBList),(GraphOneY+GraphHeight)-int((GraphHeight*PriceB)/PriceGraphHeight)))
        if (len(PriceBList) > (GraphWidth)):
            PriceBList.pop(0)
            PriceBList = [(x-1,y) for (x,y) in PriceBList]
        PriceCList.append((GraphOneX+len(PriceCList),(GraphOneY+GraphHeight)-int((GraphHeight*PriceC)/PriceGraphHeight)))
        if (len(PriceCList) > (GraphWidth)):
            PriceCList.pop(0)
            PriceCList = [(x-1,y) for (x,y) in PriceCList]

        SupplyAList.append((GraphTwoX+len(SupplyAList),(GraphTwoY+GraphHeight)-int((GraphHeight*SupplyA)/SupplyDemandAGraphHeight)))
        if (len(SupplyAList) > (GraphWidth)):
            SupplyAList.pop(0)
            SupplyAList = [(x-1,y) for (x,y) in SupplyAList]
        DemandAList.append((GraphTwoX+len(DemandAList),(GraphTwoY+GraphHeight)-int((GraphHeight*DemandA)/SupplyDemandAGraphHeight)))
        if (len(DemandAList) > (GraphWidth)):
            DemandAList.pop(0)
            DemandAList = [(x-1,y) for (x,y) in DemandAList]

        SupplyBList.append((GraphThreeX+len(SupplyBList),(GraphThreeY+GraphHeight)-int((GraphHeight*SupplyB)/SupplyDemandBGraphHeight)))
        if (len(SupplyBList) > (GraphWidth)):
            SupplyBList.pop(0)
            SupplyBList = [(x-1,y) for (x,y) in SupplyBList]
        DemandBList.append((GraphThreeX+len(DemandBList),(GraphThreeY+GraphHeight)-int((GraphHeight*DemandB)/SupplyDemandBGraphHeight)))
        if (len(DemandBList) > (GraphWidth)):
            DemandBList.pop(0)
            DemandBList = [(x-1,y) for (x,y) in DemandBList]

        SupplyCList.append((GraphFourX+len(SupplyCList),(GraphFourY+GraphHeight)-int((GraphHeight*SupplyC)/SupplyDemandCGraphHeight)))
        if (len(SupplyCList) > (GraphWidth)):
            SupplyCList.pop(0)
            SupplyCList = [(x-1,y) for (x,y) in SupplyCList]
        DemandCList.append((GraphFourX+len(DemandCList),(GraphFourY+GraphHeight)-int((GraphHeight*DemandC)/SupplyDemandCGraphHeight)))
        if (len(DemandCList) > (GraphWidth)):
            DemandCList.pop(0)
            DemandCList = [(x-1,y) for (x,y) in DemandCList]

        BudgetAList.append((GraphFiveX+len(BudgetAList),(GraphFiveY+GraphHeight)-int((GraphHeight*DemandAPercentage)/BudgetPercentGraphHeight)))
        if (len(BudgetAList) > (GraphWidth)):
            BudgetAList.pop(0)
            BudgetAList = [(x-1,y) for (x,y) in BudgetAList]
        BudgetBList.append((GraphFiveX+len(BudgetBList),(GraphFiveY+GraphHeight)-int((GraphHeight*DemandBPercentage)/BudgetPercentGraphHeight)))
        if (len(BudgetBList) > (GraphWidth)):
            BudgetBList.pop(0)
            BudgetBList = [(x-1,y) for (x,y) in BudgetBList]
        BudgetCList.append((GraphFiveX+len(BudgetCList),(GraphFiveY+GraphHeight)-int((GraphHeight*DemandCPercentage)/BudgetPercentGraphHeight)))
        if (len(BudgetCList) > (GraphWidth)):
            BudgetCList.pop(0)
            BudgetCList = [(x-1,y) for (x,y) in BudgetCList]

        LabourAList.append((GraphSixX+len(LabourAList),(GraphSixY+GraphHeight)-int((GraphHeight*LabourAPercentage)/LabourPercentGraphHeight)))
        if (len(LabourAList) > (GraphWidth)):
            LabourAList.pop(0)
            LabourAList = [(x-1,y) for (x,y) in LabourAList]
        LabourBList.append((GraphSixX+len(LabourBList),(GraphSixY+GraphHeight)-int((GraphHeight*LabourBPercentage)/LabourPercentGraphHeight)))
        if (len(LabourBList) > (GraphWidth)):
            LabourBList.pop(0)
            LabourBList = [(x-1,y) for (x,y) in LabourBList]
        LabourCList.append((GraphSixX+len(LabourCList),(GraphSixY+GraphHeight)-int((GraphHeight*LabourCPercentage)/LabourPercentGraphHeight)))
        if (len(LabourCList) > (GraphWidth)):
            LabourCList.pop(0)
            LabourCList = [(x-1,y) for (x,y) in LabourCList]

        MarginalUtilityMoneyAList.append((GraphSevenX+len(MarginalUtilityMoneyAList),(GraphSevenY+GraphHeight)-int((GraphHeight*MarginalUtilityMoneySpentA)/MarginalUtilityMoneyGraphHeight)))
        if (len(MarginalUtilityMoneyAList) > (GraphWidth)):
            MarginalUtilityMoneyAList.pop(0)
            MarginalUtilityMoneyAList = [(x-1,y) for (x,y) in MarginalUtilityMoneyAList]
        MarginalUtilityMoneyBList.append((GraphSevenX+len(MarginalUtilityMoneyBList),(GraphSevenY+GraphHeight)-int((GraphHeight*MarginalUtilityMoneySpentB)/MarginalUtilityMoneyGraphHeight)))
        if (len(MarginalUtilityMoneyBList) > (GraphWidth)):
            MarginalUtilityMoneyBList.pop(0)
            MarginalUtilityMoneyBList = [(x-1,y) for (x,y) in MarginalUtilityMoneyBList]
        MarginalUtilityMoneyCList.append((GraphSevenX+len(MarginalUtilityMoneyCList),(GraphSevenY+GraphHeight)-int((GraphHeight*MarginalUtilityMoneySpentC)/MarginalUtilityMoneyGraphHeight)))
        if (len(MarginalUtilityMoneyCList) > (GraphWidth)):
            MarginalUtilityMoneyCList.pop(0)
            MarginalUtilityMoneyCList = [(x-1,y) for (x,y) in MarginalUtilityMoneyCList]
        MarginalDisUtilityEarnMoneyList.append((GraphSevenX+len(MarginalDisUtilityEarnMoneyList),(GraphSevenY+GraphHeight)-int((GraphHeight*MarginalDisUtilityMoneyEarned)/MarginalUtilityMoneyGraphHeight)))
        if (len(MarginalDisUtilityEarnMoneyList) > (GraphWidth)):
            MarginalDisUtilityEarnMoneyList.pop(0)
            MarginalDisUtilityEarnMoneyList = [(x-1,y) for (x,y) in MarginalDisUtilityEarnMoneyList]

        MarginalValueProductionAList.append((GraphEightX+len(MarginalValueProductionAList),(GraphEightY+GraphHeight)-int((GraphHeight*MarginalValueProductionA)/MarginalValueProductionGraphHeight)))
        if (len(MarginalValueProductionAList) > (GraphWidth)):
            MarginalValueProductionAList.pop(0)
            MarginalValueProductionAList = [(x-1,y) for (x,y) in MarginalValueProductionAList]
        MarginalValueProductionBList.append((GraphEightX+len(MarginalValueProductionBList),(GraphEightY+GraphHeight)-int((GraphHeight*MarginalValueProductionB)/MarginalValueProductionGraphHeight)))
        if (len(MarginalValueProductionBList) > (GraphWidth)):
            MarginalValueProductionBList.pop(0)
            MarginalValueProductionBList = [(x-1,y) for (x,y) in MarginalValueProductionBList]
        MarginalValueProductionCList.append((GraphEightX+len(MarginalValueProductionCList),(GraphEightY+GraphHeight)-int((GraphHeight*MarginalValueProductionC)/MarginalValueProductionGraphHeight)))
        if (len(MarginalValueProductionCList) > (GraphWidth)):
            MarginalValueProductionCList.pop(0)
            MarginalValueProductionCList = [(x-1,y) for (x,y) in MarginalValueProductionCList]

        SupplyLabourList.append((GraphTwelveX+len(SupplyLabourList),(GraphTwelveY+GraphHeight)-int((GraphHeight*SupplyLabour)/SupplyLabourGraphHeight)))
        if (len(SupplyLabourList) > (GraphWidth)):
            SupplyLabourList.pop(0)
            SupplyLabourList = [(x-1,y) for (x,y) in SupplyLabourList]

        WageRateList.append((GraphThirteenX+len(WageRateList),(GraphThirteenY+GraphHeight)-int((GraphHeight*WageRate)/WageRateGraphHeight)))
        if (len(WageRateList) > (GraphWidth)):
            WageRateList.pop(0)
            WageRateList = [(x-1,y) for (x,y) in WageRateList]

    ProductionFunctionAList = [(x,int((GraphNineY+GraphHeight)-ProdFuncAList(x))) for (x,y) in ProductionFunctionAList]
    ProductionFunctionBList = [(x,int((GraphNineY+GraphHeight)-ProdFuncBList(x))) for (x,y) in ProductionFunctionBList]
    ProductionFunctionCList = [(x,int((GraphNineY+GraphHeight)-ProdFuncCList(x))) for (x,y) in ProductionFunctionCList]
    MarginalDisUtilityLabourFunctionList = [(x,int((GraphTenY+GraphHeight)-MDULList(x))) for (x,y) in MarginalDisUtilityLabourFunctionList]
    MarginalUtilityAFunctionList = [(x,int((GraphElevenY+GraphHeight)-MUAList(x))) for (x,y) in MarginalUtilityAFunctionList]
    MarginalUtilityBFunctionList = [(x,int((GraphElevenY+GraphHeight)-MUBList(x))) for (x,y) in MarginalUtilityBFunctionList]
    MarginalUtilityCFunctionList = [(x,int((GraphElevenY+GraphHeight)-MUCList(x))) for (x,y) in MarginalUtilityCFunctionList]

    if (VariableSliderSelected == "One"):
        SliderDotOneX = MouseX
        if (SliderDotOneX < VariableSliderOneX):
            SliderDotOneX = VariableSliderOneX
        if (SliderDotOneX > VariableSliderOneX+SliderWidth-SliderThickness):
            SliderDotOneX = VariableSliderOneX+SliderWidth-SliderThickness
            
    if (VariableSliderSelected == "Two"):
        SliderDotTwoX = MouseX
        if (SliderDotTwoX < VariableSliderTwoX):
            SliderDotTwoX = VariableSliderTwoX
        if (SliderDotTwoX > VariableSliderTwoX+SliderWidth-SliderThickness):
            SliderDotTwoX = VariableSliderTwoX+SliderWidth-SliderThickness
            
    if (VariableSliderSelected == "Three"):
        SliderDotThreeX = MouseX
        if (SliderDotThreeX < VariableSliderThreeX):
            SliderDotThreeX = VariableSliderThreeX
        if (SliderDotThreeX > VariableSliderThreeX+SliderWidth-SliderThickness):
            SliderDotThreeX = VariableSliderThreeX+SliderWidth-SliderThickness

    if (VariableSliderSelected == "Four"):
        SliderDotFourX = MouseX
        if (SliderDotFourX < VariableSliderFourX):
            SliderDotFourX = VariableSliderFourX
        if (SliderDotFourX > VariableSliderFourX+SliderWidth-SliderThickness):
            SliderDotFourX = VariableSliderFourX+SliderWidth-SliderThickness

    if (VariableSliderSelected == "Five"):
        SliderDotFiveX = MouseX
        if (SliderDotFiveX < VariableSliderFiveX):
            SliderDotFiveX = VariableSliderFiveX
        if (SliderDotFiveX > VariableSliderFiveX+SliderWidth-SliderThickness):
            SliderDotFiveX = VariableSliderFiveX+SliderWidth-SliderThickness

    if (VariableSliderSelected == "Six"):
        SliderDotSixX = MouseX
        if (SliderDotSixX < VariableSliderSixX):
            SliderDotSixX = VariableSliderSixX
        if (SliderDotSixX > VariableSliderSixX+SliderWidth-SliderThickness):
            SliderDotSixX = VariableSliderSixX+SliderWidth-SliderThickness

    if (VariableSliderSelected == "Seven"):
        SliderDotSevenX = MouseX
        if (SliderDotSevenX < VariableSliderSevenX):
            SliderDotSevenX = VariableSliderSevenX
        if (SliderDotSevenX > VariableSliderSevenX+SliderWidth-SliderThickness):
            SliderDotSevenX = VariableSliderSevenX+SliderWidth-SliderThickness

    SliderVariableScaleOne = (SliderDotOneX-VariableSliderOneX)/(SliderWidth-SliderThickness)
    SliderVariableScaleTwo = (SliderDotTwoX-VariableSliderTwoX)/(SliderWidth-SliderThickness)
    SliderVariableScaleThree = (SliderDotThreeX-VariableSliderThreeX)/(SliderWidth-SliderThickness)
    SliderVariableScaleFour = (SliderDotFourX-VariableSliderFourX)/(SliderWidth-SliderThickness)
    SliderVariableScaleFive = (SliderDotFiveX-VariableSliderFiveX)/(SliderWidth-SliderThickness)
    SliderVariableScaleSix = (SliderDotSixX-VariableSliderSixX)/(SliderWidth-SliderThickness)
    SliderVariableScaleSeven = (SliderDotSevenX-VariableSliderSevenX)/(SliderWidth-SliderThickness)

    if (GraphOneX < MouseX < GraphOneX+GraphWidth) and (GraphOneY < MouseY < GraphOneY+GraphHeight):
        MouseOverGraph = "One"

    elif (GraphTwoX < MouseX < GraphTwoX+GraphWidth) and (GraphTwoY < MouseY < GraphTwoY+GraphHeight):
        MouseOverGraph = "Two"

    elif (GraphThreeX < MouseX < GraphThreeX+GraphWidth) and (GraphThreeY < MouseY < GraphThreeY+GraphHeight):
        MouseOverGraph = "Three"

    elif (GraphFourX < MouseX < GraphFourX+GraphWidth) and (GraphFourY < MouseY < GraphFourY+GraphHeight):
        MouseOverGraph = "Four"

    elif (GraphFiveX < MouseX < GraphFiveX+GraphWidth) and (GraphFiveY < MouseY < GraphFiveY+GraphHeight):
        MouseOverGraph = "Five"

    elif (GraphSixX < MouseX < GraphSixX+GraphWidth) and (GraphSixY < MouseY < GraphSixY+GraphHeight):
        MouseOverGraph = "Six"

    elif (GraphSevenX < MouseX < GraphSevenX+GraphWidth) and (GraphSevenY < MouseY < GraphSevenY+GraphHeight):
        MouseOverGraph = "Seven"

    elif (GraphEightX < MouseX < GraphEightX+GraphWidth) and (GraphEightY < MouseY < GraphEightY+GraphHeight):
        MouseOverGraph = "Eight"

    elif (GraphNineX < MouseX < GraphNineX+GraphWidth) and (GraphNineY < MouseY < GraphNineY+GraphHeight):
        MouseOverGraph = "Nine"

    elif (GraphTenX < MouseX < GraphTenX+GraphWidth) and (GraphTenY < MouseY < GraphTenY+GraphHeight):
        MouseOverGraph = "Ten"

    elif (GraphElevenX < MouseX < GraphElevenX+GraphWidth) and (GraphElevenY < MouseY < GraphElevenY+GraphHeight):
        MouseOverGraph = "Eleven"

    elif (GraphTwelveX < MouseX < GraphTwelveX+GraphWidth) and (GraphTwelveY < MouseY < GraphTwelveY+GraphHeight):
        MouseOverGraph = "Twelve"

    elif (GraphThirteenX < MouseX < GraphThirteenX+GraphWidth) and (GraphThirteenY < MouseY < GraphThirteenY+GraphHeight):
        MouseOverGraph = "Thirteen"

    else:
        MouseOverGraph = "None"

    STEPPING = False
    Game()
    DrawGridLines()
    DrawConnections()
    DrawLines()
    DrawGraphs()
    DrawDropDown()
    DrawSliders()
    DrawFPS()
    pygame.display.update()

    FPS = 1.0 / (time.time() - start_time)

pygame.quit()
