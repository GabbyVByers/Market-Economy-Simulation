import os, pygame.gfxdraw, pygame, math, random
pygame.init()

DisplayX, DisplayY = 1600,900
win = pygame.display.set_mode((DisplayX, DisplayY))
pygame.display.set_caption("econ sim 2")

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

PrintDebugInformation = True

font = pygame.font.SysFont('courier', 20)
font1 = pygame.font.SysFont('courier', 15)

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
PriceA = 1000
PriceB = 1000
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

def Game():
    win.fill(Black)

def MarginalDisUtilityLabourFunction(x):
    return ((1 / (-x + 16)) - (1/16)) * 300

def MarginalUtilityFunctionA(x):
    return 30 * (0.98 ** x)
def MarginalUtilityFunctionB(x):
    return 20 * (0.975 ** x)

def ProductionFunctionA(x):
    return 12 * (x ** 0.5)
def ProductionFunctionB(x):
    return 9 * (x ** 0.5)

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

    Game()
    pygame.display.update()

    if (PrintDebugInformation == True):
        print(str(DemandA),str(SupplyA),str(DemandB),str(SupplyB),str(PriceA),str(PriceB),str(SupplyLabour),str(BudgetA),str(BudgetB),str(MarginalUtilityMoneySpentA),str(MarginalUtilityMoneySpentB),str(MarginalDisUtilityMoneyEarned),str(LabourIncome),str(MarginalValueProductionA),str(MarginalValueProductionB),str(ProportionLabourA),str(ProportionLabourB))
    
pygame.quit()

#font = pygame.font.SysFont('courier', 30)
#TEXT = font.render("Hello World!", 1, Black)
#win.blit(TEXT, (X, Y))





































































