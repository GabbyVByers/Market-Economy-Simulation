import os, pygame.gfxdraw, pygame, math, random
pygame.init()

DisplayX, DisplayY = 500,250
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

font = pygame.font.SysFont('courier', 20)
font1 = pygame.font.SysFont('courier', 15)

SupplyLabour = 10
DemandLabour = 0
LabourConsumedA = 0
LabourConsumedB = 0
LabourDemandedA = 10
LabourDemandedB = 10
LabourIncome = 0
WageRate = 1000
SupplyA = 0
SupplyB = 0
DemandA = 0
DemandB = 0
IncomeA = 0
IncomeB = 0
ExpenseA = 0
ExpenseB = 0
ProfitabilityA = 0
ProfitabilityB = 0
PriceA = 1000
PriceB = 1000
BudgetA = 500
BudgetB = 500
SoldA = 0
SoldB = 0
RateChangeLabourSupply = 1.01
RateChangeLabourDemand = 1.01
RateChangeWageRate = 1.01
RateChangePrice = 1.01
MarginalUtilityA = 0
MarginalUtilityB = 0
MarginalDisUtilityMoneyWage = 0
MarginalUtilityMoneyWage = 0
MarginalWage = 1

def Game():
    win.fill(Black)

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

        #Events

    #Calculations

##    #Demand for labour is sum of all demand for labour
##    DemandLabour = LabourDemandedA + LabourDemandedB
##
##    #labour surplus or shortage
##    #allocate labour consumed
##    #calculate labour income
##    #adjust wage rate?
##    if (SupplyLabour > DemandLabour):
##        LabourConsumedA = LabourDemandedA
##        LabourConsumedB = LabourDemandedB
##        LabourIncome = DemandLabour * WageRate
##    if (DemandLabour > SupplyLabour):
##        LabourConsumedA = (LabourDemandedA / DemandLabour) * SupplyLabour
##        LabourConsumedB = (LabourDemandedB / DemandLabour) * SupplyLabour
##        LabourIncome = SupplyLabour * WageRate
##
##    #supply is a function of labour consumed
##    #demand is a function of income and budget
##    SupplyA = LabourConsumedA
##    SupplyB = LabourConsumedB
##    DemandA = (LabourIncome * (BudgetA / 100)) / PriceA
##    DemandB = (LabourIncome * (BudgetB / 100)) / PriceB

    #Labour income, supply, demand
    LabourIncome = SupplyLabour * WageRate
    SupplyA = SupplyLabour * 1
    SupplyB = SupplyLabour * 1
    DemandA = (LabourIncome * (BudgetA / 1000)) / PriceA
    DemandB = (LabourIncome * (BudgetB / 1000)) / PriceB

    #surplus or shortage goods A and B determines amount sold
    if (SupplyA > DemandA):
        SoldA = DemandA
    if (DemandA > SupplyA):
        SoldA = SupplyA
    if (SupplyB > DemandB):
        SoldB = DemandB
    if (DemandB > SupplyB):
        SoldB = SupplyB

    #Income is amount sold times price
    IncomeA = SoldA * PriceA
    IncomeB = SoldB * PriceB

    #expense is laboor consumed times wage rate
    ExpenseA = LabourConsumedA * WageRate
    ExpenseB = LabourConsumedB * WageRate

    #profitiability is difference between income and expenses
    ProfitabilityA = IncomeA - ExpenseA
    ProfitabilityB = IncomeB - ExpenseB

    #adjust demand for labour given profitiability
    if (ProfitabilityA > 0):
        LabourDemandedA = LabourDemandedA * RateChangeLabourDemand
    if (ProfitabilityA < 0):
        LabourDemandedA = LabourDemandedA / RateChangeLabourDemand
    if (ProfitabilityB > 0):
        LabourDemandedB = LabourDemandedB * RateChangeLabourDemand
    if (ProfitabilityB < 0):
        LabourDemandedB = LabourDemandedB / RateChangeLabourDemand

    #marginal utility function
    MarginalUtilityA = 10 / DemandA
    MarginalUtilityB = 10 / (DemandB ** 0.985 )

    #adjust budgeting given marginal utility
    if (MarginalUtilityA > MarginalUtilityB) and (BudgetB > 1):
        BudgetA += 1
        BudgetB += -1
    if (MarginalUtilityB > MarginalUtilityA) and (BudgetA > 1):
        BudgetB += 1
        BudgetA += -1

    #marginal disutility of working for one extra unit of money
    MarginalDisUtilityMoneyWage = (((100 / ((-2 * SupplyLabour) + 32)) - 3.125) * (MarginalWage / WageRate)) * 1.5

    #marginal benefit of working for one extra unit of money
    if (MarginalUtilityA > MarginalUtilityB):
        MarginalUtilityMoneyWage = MarginalUtilityA * (MarginalWage / PriceA)
    if (MarginalUtilityB > MarginalUtilityA):
        MarginalUtilityMoneyWage = MarginalUtilityB * (MarginalWage / PriceB)

    #adjust labour supplied given utility of money vs disutility same amount labour
    if (MarginalDisUtilityMoneyWage > MarginalUtilityMoneyWage):
        SupplyLabour = SupplyLabour / RateChangeLabourSupply
    if (MarginalDisUtilityMoneyWage < MarginalUtilityMoneyWage):
        SupplyLabour = SupplyLabour * RateChangeLabourSupply
    if (SupplyLabour > 15.99):
        SupplyLabour = 15.99
    if (SupplyLabour < 1):
        SupplyLabour = 1
    
    #price and wage adjustments
    if (DemandA > SupplyA):
        PriceA = PriceA * RateChangePrice
    if (DemandA < SupplyA):
        PriceA = PriceA / RateChangePrice
    
    if (DemandB > SupplyB):
        PriceB = PriceB * RateChangePrice
    if (DemandB < SupplyB):
        PriceB = PriceB / RateChangePrice

    WageRate = 1000

##    if (DemandLabour > SupplyLabour):
##        WageRate = WageRate * RateChangeWageRate
##    if (DemandLabour < SupplyLabour):
##        WageRate = WageRate / RateChangeWageRate

    Game()
    pygame.display.update()

    print(str(DemandA),str(SupplyA),str(PriceA),str(DemandB),str(SupplyB),str(PriceB),str(SupplyLabour),str(MarginalDisUtilityMoneyWage),str(MarginalUtilityMoneyWage),str(BudgetA),str(BudgetB),str(BudgetA + BudgetB))
    #print(str(BudgetA),str(BudgetB))
    
pygame.quit()

#font = pygame.font.SysFont('courier', 30)
#TEXT = font.render("Hello World!", 1, Black)
#win.blit(TEXT, (X, Y))





































































