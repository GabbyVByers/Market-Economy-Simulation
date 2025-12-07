import os, pygame.gfxdraw, pygame, math, random, time
pygame.init()

DisplayX, DisplayY = 1700,900
win = pygame.display.set_mode((DisplayX, DisplayY))
pygame.display.set_caption("Market Simulation Version 4.2")

#General Variables
start_time = time.time()
xxx = .1 # displays the frame rate every xxx second
FPS = 1
counter = 0
White = (255,255,255)
Black = (0,0,0)
Blue = (100,100,255)
French_Blue = (0,0,255)
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
Lime = (190, 255, 0)

font  = pygame.font.SysFont('courier', 20, True) #Bold = True
font1 = pygame.font.SysFont('courier', 17, True) #Fluid Variable
font2 = pygame.font.SysFont('courier', 15, True) #Axis Text
font3 = pygame.font.SysFont('courier', 25, True) #Name

#Simulation Variables
Increment = 1
Percent = 100
ImportPercent = 100 #possibly change
MarginalLabour = 0.1
RateChangeSupplyLabour = 1.01
GermanySupplyLabour = 8
FranceSupplyLabour = 8
GermanyLabourA = 0
GermanyLabourB = 0
GermanyLabourC = 0
FranceLabourA = 0
FranceLabourB = 0
FranceLabourC = 0
GermanyLabourPercentA = Percent/3
GermanyLabourPercentB = Percent/3
GermanyLabourPercentC = Percent/3
FranceLabourPercentA = Percent/3
FranceLabourPercentB = Percent/3
FranceLabourPercentC = Percent/3
GermanyBudgetPercentA = Percent/3
GermanyBudgetPercentB = Percent/3
GermanyBudgetPercentC = Percent/3
FranceBudgetPercentA = Percent/3
FranceBudgetPercentB = Percent/3
FranceBudgetPercentC = Percent/3
GermanySupplyA = 0
GermanySupplyB = 0
GermanySupplyC = 0
FranceSupplyA = 0
FranceSupplyB = 0
FranceSupplyC = 0
GermanyIncome = 10000
FranceIncome = 10000
GermanyMoneyDemandA = 0
GermanyMoneyDemandB = 0
GermanyMoneyDemandC = 0
FranceMoneyDemandA = 0
FranceMoneyDemandB = 0
FranceMoneyDemandC = 0
GermanyMoneyDemandForeignA = 0
GermanyMoneyDemandDomesticA = 0
GermanyMoneyDemandForeignB = 0
GermanyMoneyDemandDomesticB = 0
GermanyMoneyDemandForeignC = 0
GermanyMoneyDemandDomesticC = 0
FranceMoneyDemandForeignA = 0
FranceMoneyDemandDomesticA = 0
FranceMoneyDemandForeignB = 0
FranceMoneyDemandDomesticB = 0
FranceMoneyDemandForeignC = 0
FranceMoneyDemandDomesticC = 0

GermanyImportPercentA = 0
GermanyImportPercentB = 0
GermanyImportPercentC = 0
GermanyDomesticPercentA = ImportPercent
GermanyDomesticPercentB = ImportPercent
GermanyDomesticPercentC = ImportPercent
FranceImportPercentA = 0
FranceImportPercentB = 0
FranceImportPercentC = 0
FranceDomesticPercentA = ImportPercent
FranceDomesticPercentB = ImportPercent
FranceDomesticPercentC = ImportPercent

GermanyWageRate = 0
FranceWageRate = 0
GermanyPriceA = 100
GermanyPriceB = 100
GermanyPriceC = 100
FrancePriceA = 100
FrancePriceB = 100
FrancePriceC = 100
GermanyAnticipatedDemandA = 0
GermanyAnticipatedDemandB = 0
GermanyAnticipatedDemandC = 0
FranceAnticipatedDemandA = 0
FranceAnticipatedDemandB = 0
FranceAnticipatedDemandC = 0
GermanyMarginalUtilityMoneySpentA = 0
GermanyMarginalUtilityMoneySpentB = 0
GermanyMarginalUtilityMoneySpentC = 0
FranceMarginalUtilityMoneySpentA = 0
FranceMarginalUtilityMoneySpentB = 0
FranceMarginalUtilityMoneySpentC = 0
GermanyMarginalDisUtilityMoneyEarned = 0
FranceMarginalDisUtilityMoneyEarned = 0
GermanyMarginalValueProductionA = 0
GermanyMarginalValueProductionB = 0
GermanyMarginalValueProductionC = 0
FranceMarginalValueProductionA = 0
FranceMarginalValueProductionB = 0
FranceMarginalValueProductionC = 0

#MouseOver Variables
MouseOver = "None"
MouseOverGraph = 0

#Graph Variables
GraphWidth = 360
GraphHeight = 160
GraphHorizontalSpacing = 50
GraphVerticalSpacing = 50
GraphBaseX = 50
GraphBaseY = 65

SliderBoxX = GraphBaseX
SliderBoxY = GraphBaseY
SliderBoxHeight = (4*GraphHeight) + (3*GraphVerticalSpacing)
GraphOneX = GraphBaseX + GraphWidth + GraphHorizontalSpacing
GraphOneY = GraphBaseY
GraphTwoX = GraphBaseX + (2*GraphWidth) + (2*GraphHorizontalSpacing)
GraphTwoY = GraphBaseY
GraphThreeX = GraphBaseX + (3*GraphWidth) + (3*GraphHorizontalSpacing)
GraphThreeY = GraphBaseY
GraphFourX = GraphBaseX + GraphWidth + GraphHorizontalSpacing
GraphFourY = GraphBaseY + GraphVerticalSpacing + GraphHeight
GraphFiveX = GraphBaseX + (2*GraphWidth) + (2*GraphHorizontalSpacing)
GraphFiveY = GraphBaseY + GraphVerticalSpacing + GraphHeight
GraphSixX = GraphBaseX + (3*GraphWidth) + (3*GraphHorizontalSpacing)
GraphSixY = GraphBaseY + GraphVerticalSpacing + GraphHeight
GraphSevenX = GraphBaseX + GraphWidth + GraphHorizontalSpacing
GraphSevenY = GraphBaseY + (2*GraphVerticalSpacing) + (2*GraphHeight)
GraphEightX = GraphBaseX + (2*GraphWidth) + (2*GraphHorizontalSpacing)
GraphEightY = GraphBaseY + (2*GraphVerticalSpacing) + (2*GraphHeight)
GraphNineX = GraphBaseX + (3*GraphWidth) + (3*GraphHorizontalSpacing)
GraphNineY = GraphBaseY + (2*GraphVerticalSpacing) + (2*GraphHeight)
GraphTenX = GraphBaseX + GraphWidth + GraphHorizontalSpacing
GraphTenY = GraphBaseY + (3*GraphVerticalSpacing) + (3*GraphHeight)
GraphElevenX = GraphBaseX + (2*GraphWidth) + (2*GraphHorizontalSpacing)
GraphElevenY = GraphBaseY + (3*GraphVerticalSpacing) + (3*GraphHeight)
GraphTwelveX = GraphBaseX + (3*GraphWidth) + (3*GraphHorizontalSpacing)
GraphTwelveY = GraphBaseY + (3*GraphVerticalSpacing) + (3*GraphHeight)

#Backround Variables
MenuSelection = "Germany" #Default
MenuBorderWidth = 5
GermanyMenuTEXT = font.render("Germany", 1, White)
FranceMenuTEXT = font.render("France", 1, White)
GlobeMenuTEXT = font.render("Globe", 1, White)

GermanyMenuWidth = GermanyMenuTEXT.get_width() + (2*MenuBorderWidth)
GermanyMenuHeight = GermanyMenuTEXT.get_height() + (2*MenuBorderWidth)
GermanyMenuButtonX = int(GraphBaseX + (GraphWidth/2) - (((6*MenuBorderWidth)+GermanyMenuTEXT.get_width()+FranceMenuTEXT.get_width())/2))
GermanyMenuButtonY = int((GraphBaseY/2) - (GermanyMenuHeight/2))

FranceMenuButtonWidth = FranceMenuTEXT.get_width() + (2*MenuBorderWidth)
FranceMenuButtonHeight = FranceMenuTEXT.get_height() + (2*MenuBorderWidth)
FranceMenuButtonX = int(GraphBaseX + GermanyMenuWidth + (GraphWidth/2) - (((6*MenuBorderWidth)+GermanyMenuTEXT.get_width()+FranceMenuTEXT.get_width())/2))
FranceMenuButtonY = int((GraphBaseY/2) - (FranceMenuButtonHeight/2))

#Graph Top Text
MiniTextBase = 6
MiniTextSpacing = 5
TextDisplacementX = 10
TextDisplacementY = -25
VariableTextDisplacementX = 10
VariableTextDisplacementY = 5
VerticalLabelTextDisplacementX = 3
VerticalLabelTextDisplacementY = -10
HorizontalLabelTextDisplacementX = 0
HorizontalLabelTextDisplacementY = 0
ProductionFunction_TEXT = font.render("Production Function", 1, White)
PFA_TEXT = font.render("ProdF A", 1, Blue)
PFB_TEXT = font.render("ProdF B", 1, Red)
PFC_TEXT = font.render("ProdF C", 1, Green)
MDUL_TEXT = font.render("Marginal DisUtility Labour", 1, White)
MU_TEXT = font.render("Marginal Utility", 1, White)
MUA_TEXT = font.render("MUA", 1, Blue)
MUB_TEXT = font.render("MUB", 1, Red)
MUC_TEXT = font.render("MUC", 1, Green)
PriceA_TEXT = font.render("Price A", 1, Blue)
PriceB_TEXT = font.render("Price B", 1, Red)
PriceC_TEXT = font.render("Price C", 1, Green)
LabourPercent_TEXT = font.render("Labour Allocation", 1, White)
Export_TEXT = font.render("Exports", 1, White)
ExportA_TEXT = font.render("$A", 1, Blue)
ExportB_TEXT = font.render("$B", 1, Red)
ExportC_TEXT = font.render("$C", 1, Green)
SupplyLabour_TEXT = font.render("Supply Labour", 1, White)
BudgetPercent_TEXT = font.render("Budget Allocation", 1, White)
Import_TEXT = font.render("Imports", 1, White)
ImportA_TEXT = font.render("$A", 1, Blue)
ImportB_TEXT = font.render("$B", 1, Red)
ImportC_TEXT = font.render("$C", 1, Green)
WageRate_TEXT = font.render("Wage Rate", 1, White)
MUMoneyA_TEXT = font.render("MUΔ$A", 1, Blue)
MUMoneyB_TEXT = font.render("MUΔ$B", 1, Red)
MUMoneyC_TEXT = font.render("MUΔ$C", 1, Green)
MDUEarnMoney_TEXT = font.render("MDUΔ$", 1, Gold)
MVPA_TEXT = font.render("ΔQA*PA", 1, Blue)
MVPB_TEXT = font.render("ΔQA*PB", 1, Red)
MVPC_TEXT = font.render("ΔQA*PC", 1, Green)

#Pie Chart Mini Text
LabourPercentA_Mini_Text = font1.render("Labour A ", 1, Blue)
LabourPercentB_Mini_Text = font1.render("Labour B ", 1, Red)
LabourPercentC_Mini_Text = font1.render("Labour C ", 1, Green)
BudgetPercentA_Mini_Text = font1.render("Budget A ", 1, Blue)
BudgetPercentB_Mini_Text = font1.render("Budget B ", 1, Red)
BudgetPercentC_Mini_Text = font1.render("Budget C ", 1, Green)

#Graph Vertical Labels
GraphHeightZero_TEXT = font2.render(str(0), 1, Dark_Gray1)

GermanyGraphOneHeight = 25 #Production
GermanyGraphTwoHeight = 100 #MDUL
GermanyGraphThreeHeight = 20 #MUABC
GermanyGraphFourHeight = 700 #Prices
GermanyGraphSixHeight = 7000 #Exports
GermanyGraphSevenHeight = 16 #Supply Labour
GermanyGraphNineHeight = 7000 #Imports
GermanyGraphTenHeight = 10000 #Wage Rate
GermanyGraphElevenHeight = 0.02 #MUΔ$ABC
GermanyGraphTwelveHeight = 200 #ΔQABC*PABC

FranceGraphOneHeight = 25 #Production
FranceGraphTwoHeight = 100 #MDUL
FranceGraphThreeHeight = 20 #MUABC
FranceGraphFourHeight = 700 #Prices
FranceGraphSixHeight = 7000 #Exports
FranceGraphSevenHeight = 16 #Supply Labour
FranceGraphNineHeight = 7000 #Imports
FranceGraphTenHeight = 10000 #Wage Rate
FranceGraphElevenHeight = 0.02 #MUΔ$ABC
FranceGraphTwelveHeight = 200 #ΔQABC*PABC

GraphOneHeightStepSize = 5
GraphTwoHeightStepSize = 50
GraphThreeHeightStepSize = 5
GraphFourHeightStepSize = 50
GraphFiveHeightStepSize = 1
GraphSixHeightStepSize = 500
GraphSevenHeightStepSize = 1
GraphEightHeightStepSize = 1
GraphNineHeightStepSize = 500
GraphTenHeightStepSize = 1
GraphElevenHeightStepSize = .005
GraphTwelveHeightStepSize = 20

GraphOneHeightMax = 200
GraphTwoHeightMax = 800
GraphThreeHeightMax = 50
GraphFourHeightMax = 1000
GraphFiveHeightMax = 999999
GraphSixHeightMax = 10000
GraphSevenHeightMax = 16
GraphEightHeightMax = 999999
GraphNineHeightMax = 10000
GraphTenHeightMax = 10000
GraphElevenHeightMax = 0.08
GraphTwelveHeightMax = 500

GraphOneHeightMin = 5
GraphTwoHeightMin = 50
GraphThreeHeightMin = 5
GraphFourHeightMin = 200
GraphFiveHeightMin = 0
GraphSixHeightMin = 1000
GraphSevenHeightMin = 16
GraphEightHeightMin = 0
GraphNineHeightMin = 1000
GraphTenHeightMin = 10000
GraphElevenHeightMin = 0.01
GraphTwelveHeightMin = 100

#Graph Horizontal Label (hard coded or maybe shift + scroll)
GermanyGraphOneWidth = 10
GermanyGraphTwoWidth = 15
GermanyGraphThreeWidth = 20

FranceGraphOneWidth = 10
FranceGraphTwoWidth = 15
FranceGraphThreeWidth = 20

#Raw Function Lists
GermanyProductionFunctionAList = [(GraphOneX,0)]
GermanyProductionFunctionBList = [(GraphOneX,0)]
GermanyProductionFunctionCList = [(GraphOneX,0)]
GermanyMarginalDisUtilityLabourList = [(GraphTwoX,0)]
GermanyMarginalUtilityAList = [(GraphThreeX,0)]
GermanyMarginalUtilityBList = [(GraphThreeX,0)]
GermanyMarginalUtilityCList = [(GraphThreeX,0)]
FranceProductionFunctionAList = [(GraphOneX,0)]
FranceProductionFunctionBList = [(GraphOneX,0)]
FranceProductionFunctionCList = [(GraphOneX,0)]
FranceMarginalDisUtilityLabourList = [(GraphTwoX,0)]
FranceMarginalUtilityAList = [(GraphThreeX,0)]
FranceMarginalUtilityBList = [(GraphThreeX,0)]
FranceMarginalUtilityCList = [(GraphThreeX,0)]

#Germany Raw Data List
GermanyRawPriceAList = [(GraphFourX,0)]
GermanyRawPriceBList = [(GraphFourX,0)]
GermanyRawPriceCList = [(GraphFourX,0)]
GermanyRawExportABCList = [(GraphSixX,0)]
GermanyRawExportBCList = [(GraphSixX,0)]
GermanyRawExportCList = [(GraphSixX,0)]
GermanyRawSupplyLabourList = [(GraphSevenX,0)]
GermanyRawImportABCList = [(GraphNineX,0)]
GermanyRawImportBCList = [(GraphNineX,0)]
GermanyRawImportCList = [(GraphNineX,0)]
GermanyRawWageRateList = [(GraphTenX,0)]
GermanyRawMUMoneyAList = [(GraphElevenX,0)]
GermanyRawMUMoneyBList = [(GraphElevenX,0)]
GermanyRawMUMoneyCList = [(GraphElevenX,0)]
GermanyRawMDUMoneyList = [(GraphElevenX,0)]
GermanyRawMPVAList = [(GraphTwelveX,0)]
GermanyRawMPVBList = [(GraphTwelveX,0)]
GermanyRawMPVCList = [(GraphTwelveX,0)]

#Germany Raw Data List
FranceRawPriceAList = [(GraphFourX,0)]
FranceRawPriceBList = [(GraphFourX,0)]
FranceRawPriceCList = [(GraphFourX,0)]
FranceRawExportABCList = [(GraphSixX,0)]
FranceRawExportBCList = [(GraphSixX,0)]
FranceRawExportCList = [(GraphSixX,0)]
FranceRawSupplyLabourList = [(GraphSevenX,0)]
FranceRawImportABCList = [(GraphNineX,0)]
FranceRawImportBCList = [(GraphNineX,0)]
FranceRawImportCList = [(GraphNineX,0)]
FranceRawWageRateList = [(GraphTenX,0)]
FranceRawMUMoneyAList = [(GraphElevenX,0)]
FranceRawMUMoneyBList = [(GraphElevenX,0)]
FranceRawMUMoneyCList = [(GraphElevenX,0)]
FranceRawMDUMoneyList = [(GraphElevenX,0)]
FranceRawMPVAList = [(GraphTwelveX,0)]
FranceRawMPVBList = [(GraphTwelveX,0)]
FranceRawMPVCList = [(GraphTwelveX,0)]

#Flag and Country Name
FlagBorder = 1
FlagTranslateX = -20
FlagTranslateY = 20
FlagWidth = 200
FlagHeight = 60
FlagX = SliderBoxX + GraphWidth + FlagTranslateX - FlagWidth
FlagY = SliderBoxY + FlagTranslateY
GermanyTEXT = font3.render("Germany", 1, White)
FranceTEXT = font3.render("France", 1, White)
GermanyTEXT_X = FlagX - GermanyTEXT.get_width() - 18 #TODO center it perfectly
GermanyTEXT_Y = FlagY + round(FlagHeight/2) - round(GermanyTEXT.get_height()/2)
FranceTEXT_X = FlagX - FranceTEXT.get_width() - 24 #TODO center it perfectly
FranceTEXT_Y = FlagY + round(FlagHeight/2) - round(FranceTEXT.get_height()/2)

#Slider
SliderRangeWidth = GraphWidth
SliderRangeHeight = SliderBoxHeight - ((2*FlagTranslateY) + FlagHeight) - 200
SliderRangeX = GraphBaseX
SliderRangeY = SliderBoxY + (2*FlagTranslateY) + FlagHeight

SliderWidth = 280
SliderThickness = 5
SliderVerticalSpacing = round((SliderRangeHeight - (13*SliderThickness)) / 14)
SliderX = round(GraphBaseX + (GraphWidth/2) - (SliderWidth/2))

SliderNameDisplacementX = 0
SliderNameDisplacementY = 5

SliderOneY = SliderVerticalSpacing + SliderRangeY
SliderTwoY = (2*SliderVerticalSpacing) + SliderThickness + SliderRangeY
SliderThreeY = (3*SliderVerticalSpacing) + (2*SliderThickness) + SliderRangeY
SliderFourY = (4*SliderVerticalSpacing) + (3*SliderThickness) + SliderRangeY
SliderFiveY = (5*SliderVerticalSpacing) + (4*SliderThickness) + SliderRangeY
SliderSixY = (6*SliderVerticalSpacing) + (5*SliderThickness) + SliderRangeY
SliderSevenY = (7*SliderVerticalSpacing) + (6*SliderThickness) + SliderRangeY
SliderEightY = (8*SliderVerticalSpacing) + (7*SliderThickness) + SliderRangeY
SliderNineY = (9*SliderVerticalSpacing) + (8*SliderThickness) + SliderRangeY
SliderTenY = (10*SliderVerticalSpacing) + (9*SliderThickness) + SliderRangeY
SliderElevenY = (11*SliderVerticalSpacing) + (10*SliderThickness) + SliderRangeY
SliderTwelveY = (12*SliderVerticalSpacing) + (11*SliderThickness) + SliderRangeY
SliderThirteenY = (13*SliderVerticalSpacing) + (12*SliderThickness) + SliderRangeY

HalfSliderVerticalSpacing = round(SliderVerticalSpacing/2)

SliderHitboxX = SliderX - HalfSliderVerticalSpacing
SliderHitboxWidth = SliderWidth + SliderVerticalSpacing
SliderHitboxHeight = SliderThickness + SliderVerticalSpacing

SliderOneHitboxY = SliderOneY - HalfSliderVerticalSpacing
SliderTwoHitboxY = SliderTwoY - HalfSliderVerticalSpacing
SliderThreeHitboxY = SliderThreeY - HalfSliderVerticalSpacing
SliderFourHitboxY = SliderFourY - HalfSliderVerticalSpacing
SliderFiveHitboxY = SliderFiveY - HalfSliderVerticalSpacing
SliderSixHitboxY = SliderSixY - HalfSliderVerticalSpacing
SliderSevenHitboxY = SliderSevenY - HalfSliderVerticalSpacing
SliderEightHitboxY = SliderEightY - HalfSliderVerticalSpacing
SliderNineHitboxY = SliderNineY - HalfSliderVerticalSpacing
SliderTenHitboxY = SliderTenY - HalfSliderVerticalSpacing
SliderElevenHitboxY = SliderElevenY - HalfSliderVerticalSpacing
SliderTwelveHitboxY = SliderTwelveY - HalfSliderVerticalSpacing
SliderThirteenHitboxY = SliderThirteenY - HalfSliderVerticalSpacing

MUASliderText = font1.render("MUA", 1 ,Blue)
MUBSliderText = font1.render("MUB", 1 ,Red)
MUCSliderText = font1.render("MUC", 1 ,Green)
MDULSliderText = font1.render("MDUL", 1, White)
PFASliderText = font1.render("PFA", 1 ,Blue)
PFBSliderText = font1.render("PFB", 1 ,Red)
PFCSliderText = font1.render("PFC", 1 ,Green)
TarrifAText = font1.render("Tariff A", 1, Blue)
TarrifBText = font1.render("Tariff B", 1, Red)
TarrifCText = font1.render("Tariff C", 1, Green)
SubsidyAText = font1.render("Subsidy A", 1, Blue)
SubsidyBText = font1.render("Subsidy B", 1, Red)
SubsidyCText = font1.render("Subsidy C", 1, Green)

SliderValueOne = 0 #Zero to One
SliderValueTwo = 0
SliderValueThree = 0
SliderValueFour = 0
SliderValueFive = 0
SliderValueSix = 0
SliderValueSeven = 0
SliderValueEight = 0
SliderValueNine = 0
SliderValueTen = 0
SliderValueEleven = 0
SliderValueTwelve = 0
SliderValueThirteen = 0

GermanySliderDotOneX = SliderX
GermanySliderDotTwoX = SliderX
GermanySliderDotThreeX = SliderX
GermanySliderDotFourX = SliderX
GermanySliderDotFiveX = SliderX
GermanySliderDotSixX = SliderX
GermanySliderDotSevenX = SliderX
GermanySliderDotEightX = SliderX
GermanySliderDotNineX = SliderX
GermanySliderDotTenX = SliderX
GermanySliderDotElevenX = SliderX
GermanySliderDotTwelveX = SliderX
GermanySliderDotThirteenX = SliderX

FranceSliderDotOneX = SliderX
FranceSliderDotTwoX = SliderX
FranceSliderDotThreeX = SliderX
FranceSliderDotFourX = SliderX
FranceSliderDotFiveX = SliderX
FranceSliderDotSixX = SliderX
FranceSliderDotSevenX = SliderX
FranceSliderDotEightX = SliderX
FranceSliderDotNineX = SliderX
FranceSliderDotTenX = SliderX
FranceSliderDotElevenX = SliderX
FranceSliderDotTwelveX = SliderX
FranceSliderDotThirteenX = SliderX

SliderSelection = "None"

GermanySliderNormalizedValueOne = 0
GermanySliderNormalizedValueTwo = 0
GermanySliderNormalizedValueThree = 0
GermanySliderNormalizedValueFour = 0
GermanySliderNormalizedValueFive = 0
GermanySliderNormalizedValueSix = 0
GermanySliderNormalizedValueSeven = 0
GermanySliderNormalizedValueEight = 0
GermanySliderNormalizedValueNine = 0
GermanySliderNormalizedValueTen = 0
GermanySliderNormalizedValueEleven = 0
GermanySliderNormalizedValueTwelve = 0
GermanySliderNormalizedValueThirteen = 0

FranceSliderNormalizedValueOne = 0
FranceSliderNormalizedValueTwo = 0
FranceSliderNormalizedValueThree = 0
FranceSliderNormalizedValueFour = 0
FranceSliderNormalizedValueFive = 0
FranceSliderNormalizedValueSix = 0
FranceSliderNormalizedValueSeven = 0
FranceSliderNormalizedValueEight = 0
FranceSliderNormalizedValueNine = 0
FranceSliderNormalizedValueTen = 0
FranceSliderNormalizedValueEleven = 0
FranceSliderNormalizedValueTwelve = 0
FranceSliderNormalizedValueThirteen = 0

#Slider Max Values
SliderMaxPercentValueOne = 300
SliderMaxPercentValueTwo = 300
SliderMaxPercentValueThree = 300
SliderMaxPercentValueFour = 300
SliderMaxPercentValueFive = 300
SliderMaxPercentValueSix = 300
SliderMaxPercentValueSeven = 300
SliderMaxPercentValueEight = 100
SliderMaxPercentValueNine = 100
SliderMaxPercentValueTen = 100
SliderMaxPercentValueEleven = 100
SliderMaxPercentValueTwelve = 100
SliderMaxPercentValueThirteen = 100

#Debug Buttons
ButtonRangeWidth = GraphWidth
ButtonRangeHeight = (SliderBoxHeight + SliderBoxY) - (SliderRangeY + SliderRangeHeight)
ButtonRangeX = GraphBaseX
ButtonRangeY = SliderRangeY + SliderRangeHeight

ButtonTextMarginX = 10
ButtonTextDisplacementY = 1
ButtonVerticalSpacing = 20

PAUSE = False
Pause_Text = font1.render("Pause", 1, Black)
Play_Text = font1.render("Play", 1, Black)
PauseButtonWidth = Pause_Text.get_width()+(ButtonTextMarginX * 2)
PauseButtonHeight = Pause_Text.get_height()
PauseButtonX = GraphBaseX + round(GraphWidth/2) - round(PauseButtonWidth/2)
PauseButtonY = ButtonRangeY + ButtonVerticalSpacing

STEP = False
Step_Text = font1.render("Step", 1, Black)
StepButtonWidth = Step_Text.get_width()+(ButtonTextMarginX * 2)
StepButtonHeight = Step_Text.get_height()
StepButtonX = GraphBaseX + round(GraphWidth/2) - round(StepButtonWidth/2)
StepButtonY = ButtonRangeY + (2*ButtonVerticalSpacing) + Pause_Text.get_height()

ShowSliderHitbox = False
SliderHitbox_Text = font1.render("Enable/Disable Slider Hit Boxes", 1, Black)
SliderHitboxButtonWidth = SliderHitbox_Text.get_width()+(ButtonTextMarginX * 2)
SliderHitboxButtonHeight = SliderHitbox_Text.get_height()
SliderHitboxButtonX = GraphBaseX + round(GraphWidth/2) - round(SliderHitboxButtonWidth/2)
SliderHitboxButtonY = ButtonRangeY + (3*ButtonVerticalSpacing) + (2*Pause_Text.get_height())

DebugWindow = False
DebugWindow_Text = font1.render("Toggle Debugger", 1, Black)
DebugWindowButtonWidth = DebugWindow_Text.get_width()+(ButtonTextMarginX * 2)
DebugWindowButtonHeight = DebugWindow_Text.get_height()
DebugWindowButtonX = GraphBaseX + round(GraphWidth/2) - round(DebugWindowButtonWidth/2)
DebugWindowButtonY = ButtonRangeY + (4*ButtonVerticalSpacing) + (3*Pause_Text.get_height())

ButtonMouseOver = "None"

#Tariff
GermanyTariffRateA = 0
GermanyTariffRateB = 0
GermanyTariffRateC = 0
FranceTariffRateA = 0
FranceTariffRateB = 0
FranceTariffRateC = 0

#Debug Menu
MouseOverDebugWindow = False
MouseDragDebugWindow = False
DebugWindowX = 600
DebugWindowY = 200
DebugWindowWidth = 400
DebugWindowHeight = 600
DebugWindowTextVerticalSpacing = 20
DebugWindowTextBaseX = 5
DebugWindowTextBaseY = 0

#Tool Tips
tt1_text = font2.render(" shortcut: P", 1, Black)
tt2_text = font2.render(" shortcut: S", 1, Black)
tt3_text = font2.render(" no shortcut", 1, Black)
tt4_text = font2.render(" shortcut: D", 1, Black)

#Dummy Text
DummyTextGlobe = font.render("WIP Globe Menu", 1, White)

def MouseToolTips():
    if (ButtonMouseOver == "Pause"):
        pygame.draw.rect(win, Gray, (MouseX,MouseY,tt1_text.get_width()+(2*ButtonTextMarginX),tt1_text.get_height()))
        pygame.draw.rect(win, White, (MouseX,MouseY,tt1_text.get_width()+(2*ButtonTextMarginX),tt1_text.get_height()), 1)
        win.blit(tt1_text, (MouseX+ButtonTextMarginX,MouseY))
    if (ButtonMouseOver == "Step"):
        pygame.draw.rect(win, Gray, (MouseX,MouseY,tt2_text.get_width()+(2*ButtonTextMarginX),tt2_text.get_height()))
        pygame.draw.rect(win, White, (MouseX,MouseY,tt2_text.get_width()+(2*ButtonTextMarginX),tt2_text.get_height()), 1)
        win.blit(tt2_text, (MouseX+ButtonTextMarginX,MouseY))
    if (ButtonMouseOver == "SliderHitbox"):
        pygame.draw.rect(win, Gray, (MouseX,MouseY,tt3_text.get_width()+(2*ButtonTextMarginX),tt3_text.get_height()))
        pygame.draw.rect(win, White, (MouseX,MouseY,tt3_text.get_width()+(2*ButtonTextMarginX),tt3_text.get_height()), 1)
        win.blit(tt3_text, (MouseX+ButtonTextMarginX,MouseY))
    if (ButtonMouseOver == "DebugWindow"):
        pygame.draw.rect(win, Gray, (MouseX,MouseY,tt4_text.get_width()+(2*ButtonTextMarginX),tt4_text.get_height()))
        pygame.draw.rect(win, White, (MouseX,MouseY,tt4_text.get_width()+(2*ButtonTextMarginX),tt4_text.get_height()), 1)
        win.blit(tt4_text, (MouseX+ButtonTextMarginX,MouseY))

def DebugWindowFunction():
    pygame.draw.rect(win, White, (DebugWindowX,DebugWindowY,DebugWindowWidth,DebugWindowHeight))
    if (MouseOverDebugWindow == True):
        pygame.draw.rect(win, Blue, (DebugWindowX,DebugWindowY,DebugWindowWidth,DebugWindowHeight), 3)
    if (MouseDragDebugWindow == True):
        pygame.draw.rect(win, Red, (DebugWindowX,DebugWindowY,DebugWindowWidth,DebugWindowHeight), 3)

    a = font.render("DEBUGGER    'D' key to toggle", 1, Black)
    if (GermanyPriceA > FrancePriceA):
        b = font.render("GA $"+str(round(GermanyPriceA))+" +%"+str(round(100*((GermanyPriceA - FrancePriceA)/FrancePriceA),2))+" rel F", 1, Black)
    if (GermanyPriceA < FrancePriceA):
        b = font.render("GA $"+str(round(GermanyPriceA))+" -%"+str(round(100*((FrancePriceA - GermanyPriceA)/FrancePriceA),2))+" rel F", 1, Black)
    if (GermanyPriceB > FrancePriceB):
        c = font.render("GB $"+str(round(GermanyPriceB))+" +%"+str(round(100*((GermanyPriceB - FrancePriceB)/FrancePriceB),2))+" rel F", 1, Black)
    if (GermanyPriceB < FrancePriceB):
        c = font.render("GB $"+str(round(GermanyPriceB))+" -%"+str(round(100*((FrancePriceB - GermanyPriceB)/FrancePriceB),2))+" rel F", 1, Black)
    if (GermanyPriceC > FrancePriceC):
        d = font.render("GC $"+str(round(GermanyPriceC))+" +%"+str(round(100*((GermanyPriceC - FrancePriceC)/FrancePriceC),2))+" rel F", 1, Black)
    if (GermanyPriceC < FrancePriceC):
        d = font.render("GC $"+str(round(GermanyPriceC))+" -%"+str(round(100*((FrancePriceC - GermanyPriceC)/FrancePriceC),2))+" rel F", 1, Black)

    if (FrancePriceA > GermanyPriceA):
        e = font.render("FA $"+str(round(FrancePriceA))+" +%"+str(round(100*((FrancePriceA - GermanyPriceA)/GermanyPriceA),2))+" rel G", 1, Black)
    if (FrancePriceA < GermanyPriceA):
        e = font.render("FA $"+str(round(FrancePriceA))+" -%"+str(round(100*((GermanyPriceA - FrancePriceA)/GermanyPriceA),2))+" rel G", 1, Black)
    if (FrancePriceB > GermanyPriceB):
        f = font.render("FB $"+str(round(FrancePriceB))+" +%"+str(round(100*((FrancePriceB - GermanyPriceB)/GermanyPriceB),2))+" rel G", 1, Black)
    if (FrancePriceB < GermanyPriceB):
        f = font.render("FB $"+str(round(FrancePriceB))+" -%"+str(round(100*((GermanyPriceB - FrancePriceB)/GermanyPriceB),2))+" rel G", 1, Black)
    if (FrancePriceC > GermanyPriceC):
        g = font.render("FC $"+str(round(FrancePriceC))+" +%"+str(round(100*((FrancePriceC - GermanyPriceC)/GermanyPriceC),2))+" rel G", 1, Black)
    if (FrancePriceC < GermanyPriceC):
        g = font.render("FC $"+str(round(FrancePriceC))+" -%"+str(round(100*((GermanyPriceC - FrancePriceC)/GermanyPriceC),2))+" rel G", 1, Black)

    h = font.render("Tariff Revenue (Demand - Spent)", 1, Black)
    i = font.render("GTA "+str(round(GermanyTariffRateA*100))+"% $"+str(round(GermanyTariffRevenueA))+" ($"+str(round(GermanyMoneyDemandForeignA))+" - $"+str(round(GermanyMoneySpentForeignA))+")", 1, Black)
    j = font.render("GTB "+str(round(GermanyTariffRateB*100))+"% $"+str(round(GermanyTariffRevenueB))+" ($"+str(round(GermanyMoneyDemandForeignB))+" - $"+str(round(GermanyMoneySpentForeignB))+")", 1, Black)
    k = font.render("GTC "+str(round(GermanyTariffRateC*100))+"% $"+str(round(GermanyTariffRevenueC))+" ($"+str(round(GermanyMoneyDemandForeignC))+" - $"+str(round(GermanyMoneySpentForeignC))+")", 1, Black)
    l = font.render("FTA "+str(round(FranceTariffRateA*100))+"% $"+str(round(FranceTariffRevenueA))+" ($"+str(round(FranceMoneyDemandForeignA))+" - $"+str(round(FranceMoneySpentForeignA))+")", 1, Black)
    m = font.render("FTB "+str(round(FranceTariffRateB*100))+"% $"+str(round(FranceTariffRevenueB))+" ($"+str(round(FranceMoneyDemandForeignB))+" - $"+str(round(FranceMoneySpentForeignB))+")", 1, Black)
    n = font.render("FTC "+str(round(FranceTariffRateC*100))+"% $"+str(round(FranceTariffRevenueC))+" ($"+str(round(FranceMoneyDemandForeignC))+" - $"+str(round(FranceMoneySpentForeignC))+")", 1, Black)

    o = font.render("TARIFF_GermanyA $"+str(round(TARIFF_GermanyPriceA))+" rel F", 1, Black)
    p = font.render("TARIFF_GermanyB $"+str(round(TARIFF_GermanyPriceB))+" rel F", 1, Black)
    q = font.render("TARIFF_GermanyC $"+str(round(TARIFF_GermanyPriceC))+" rel F", 1, Black)
    r = font.render("TARIFF_FranceA $"+str(round(TARIFF_FrancePriceA))+" rel G", 1, Black)
    s = font.render("TARIFF_FranceB $"+str(round(TARIFF_FrancePriceB))+" rel G", 1, Black)
    t = font.render("TARIFF_FranceC $"+str(round(TARIFF_FrancePriceC))+" rel G", 1, Black)

    win.blit(a, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(0*DebugWindowTextVerticalSpacing)))
    win.blit(b, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(2*DebugWindowTextVerticalSpacing)))
    win.blit(c, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(3*DebugWindowTextVerticalSpacing)))
    win.blit(d, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(4*DebugWindowTextVerticalSpacing)))
    win.blit(e, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(5*DebugWindowTextVerticalSpacing)))
    win.blit(f, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(6*DebugWindowTextVerticalSpacing)))
    win.blit(g, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(7*DebugWindowTextVerticalSpacing)))
    win.blit(h, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(8*DebugWindowTextVerticalSpacing)))
    win.blit(i, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(9*DebugWindowTextVerticalSpacing)))
    win.blit(j, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(10*DebugWindowTextVerticalSpacing)))
    win.blit(k, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(11*DebugWindowTextVerticalSpacing)))
    win.blit(l, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(12*DebugWindowTextVerticalSpacing)))
    win.blit(m, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(13*DebugWindowTextVerticalSpacing)))
    win.blit(n, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(14*DebugWindowTextVerticalSpacing)))
    win.blit(o, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(15*DebugWindowTextVerticalSpacing)))
    win.blit(p, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(16*DebugWindowTextVerticalSpacing)))
    win.blit(q, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(17*DebugWindowTextVerticalSpacing)))
    win.blit(r, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(18*DebugWindowTextVerticalSpacing)))
    win.blit(s, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(19*DebugWindowTextVerticalSpacing)))
    win.blit(t, (DebugWindowX+DebugWindowTextBaseX,DebugWindowY+DebugWindowTextBaseY+(20*DebugWindowTextVerticalSpacing)))

def PieChart2(v1, v2, cx, cy, r):
    pygame.draw.circle(win, Dark_Gray1, (cx, cy), r+2)

    angle1 = round(v1*720/100) #Increment is every 0.5 degrees
    p1 = [(cx, cy)]
    for n in range(0,angle1):
        x = cx + round(r*math.cos(n*math.pi/360))
        y = cy + round(r*math.sin(n*math.pi/360))
        p1.append((x, y))
    if len(p1) > 2:
        pygame.draw.polygon(win, Blue, p1)

    angle2 = round(v2*720/100)
    p2 = [(cx, cy)]
    for n in range(angle1,angle1+angle2):
        x = cx + round(r*math.cos(n*math.pi/360))
        y = cy + round(r*math.sin(n*math.pi/360))
        p2.append((x, y))
    if len(p2) > 2:
        pygame.draw.polygon(win, Red, p2)

def PieChart3(v1, v2, v3, cx, cy, r):
    pygame.draw.circle(win, Dark_Gray1, (cx, cy), r)

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
        pygame.draw.polygon(win, Red, p2)

    angle3 = round(v3*720/(v1+v2+v3))
    p3 = [(cx, cy)]
    for n in range(angle1+angle2,angle1+angle2+angle3):
        x = cx + round(r*math.cos(n*math.pi/360))
        y = cy + round(r*math.sin(n*math.pi/360))
        p3.append((x, y))
    if len(p3) > 2:
        pygame.draw.polygon(win, Green, p3)

def Game():
    #Backround
    win.fill(Black)

    #Draw Button
    pygame.draw.rect(win, Dark_Gray2, (GermanyMenuButtonX,GermanyMenuButtonY,GermanyMenuWidth,GermanyMenuHeight))
    pygame.draw.rect(win, Dark_Gray2, (FranceMenuButtonX,FranceMenuButtonY,FranceMenuButtonWidth,FranceMenuButtonHeight))

    #Draw Button Text
    win.blit(GermanyMenuTEXT, (GermanyMenuButtonX+MenuBorderWidth,GermanyMenuButtonY+MenuBorderWidth))
    win.blit(FranceMenuTEXT, (FranceMenuButtonX+MenuBorderWidth,FranceMenuButtonY+MenuBorderWidth))

    #Draw White Outline if Mouse Over
    if (MouseOver == "GermanyMenuButton"):
        pygame.draw.rect(win, White, (GermanyMenuButtonX,GermanyMenuButtonY,GermanyMenuWidth,GermanyMenuHeight), 1)
    if (MouseOver == "FranceMenuButton"):
        pygame.draw.rect(win, White, (FranceMenuButtonX,FranceMenuButtonY,FranceMenuButtonWidth,FranceMenuButtonHeight), 1)

    #FPS
    FPS_TEXT = font1.render("FPS/UPS: "+str(round(FPS)), 1, White)
    win.blit(FPS_TEXT, (DisplayX-130,0))

def DrawButtons():
    #Pause
    pygame.draw.rect(win, White, (PauseButtonX,PauseButtonY,PauseButtonWidth,PauseButtonHeight))
    if (ButtonMouseOver == "Pause"):
        pygame.draw.rect(win, Red, (PauseButtonX,PauseButtonY,PauseButtonWidth,PauseButtonHeight), 2)
    if (PAUSE == False):
        win.blit(Pause_Text, (PauseButtonX+ButtonTextMarginX,PauseButtonY+ButtonTextDisplacementY))
    if (PAUSE == True):
        win.blit(Play_Text, (PauseButtonX+ButtonTextMarginX,PauseButtonY+ButtonTextDisplacementY))
    #Step
    pygame.draw.rect(win, White, (StepButtonX,StepButtonY,StepButtonWidth,StepButtonHeight))
    if (ButtonMouseOver == "Step"):
        pygame.draw.rect(win, Red, (StepButtonX,StepButtonY,StepButtonWidth,StepButtonHeight), 2)
    win.blit(Step_Text, (StepButtonX+ButtonTextMarginX,StepButtonY+ButtonTextDisplacementY))
    #Slider Hit Box
    pygame.draw.rect(win, White, (SliderHitboxButtonX,SliderHitboxButtonY,SliderHitboxButtonWidth,SliderHitboxButtonHeight))
    if (ButtonMouseOver == "SliderHitbox"):
        pygame.draw.rect(win, Red, (SliderHitboxButtonX,SliderHitboxButtonY,SliderHitboxButtonWidth,SliderHitboxButtonHeight), 2)
    win.blit(SliderHitbox_Text, (SliderHitboxButtonX+ButtonTextMarginX,SliderHitboxButtonY+ButtonTextDisplacementY))
    #Debug Button
    pygame.draw.rect(win, White, (DebugWindowButtonX,DebugWindowButtonY,DebugWindowButtonWidth,DebugWindowButtonHeight))
    if (ButtonMouseOver == "DebugWindow"):
        pygame.draw.rect(win, Red, (DebugWindowButtonX,DebugWindowButtonY,DebugWindowButtonWidth,DebugWindowButtonHeight), 2)
    win.blit(DebugWindow_Text, (DebugWindowButtonX+ButtonTextMarginX,DebugWindowButtonY+ButtonTextDisplacementY))

def DrawBoxesLast():
    #Boxes
    pygame.draw.rect(win, Dark_Gray1, (SliderBoxX,SliderBoxY,GraphWidth,SliderBoxHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphOneX,GraphOneY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphTwoX,GraphTwoY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphThreeX,GraphThreeY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphFourX,GraphFourY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphSixX,GraphSixY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphSevenX,GraphSevenY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphNineX,GraphNineY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphTenX,GraphTenY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphElevenX,GraphElevenY,GraphWidth,GraphHeight), 1)
    pygame.draw.rect(win, Dark_Gray1, (GraphTwelveX,GraphTwelveY,GraphWidth,GraphHeight), 1)

    if (MouseOverGraph == 1):
        pygame.draw.rect(win, White, (GraphOneX,GraphOneY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 2):
        pygame.draw.rect(win, White, (GraphTwoX,GraphTwoY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 3):
        pygame.draw.rect(win, White, (GraphThreeX,GraphThreeY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 4):
        pygame.draw.rect(win, White, (GraphFourX,GraphFourY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 6):
        pygame.draw.rect(win, White, (GraphSixX,GraphSixY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 7):
        pygame.draw.rect(win, White, (GraphSevenX,GraphSevenY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 9):
        pygame.draw.rect(win, White, (GraphNineX,GraphNineY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 10):
        pygame.draw.rect(win, White, (GraphTenX,GraphTenY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 11):
        pygame.draw.rect(win, White, (GraphElevenX,GraphElevenY,GraphWidth,GraphHeight), 1)
    if (MouseOverGraph == 12):
        pygame.draw.rect(win, White, (GraphTwelveX,GraphTwelveY,GraphWidth,GraphHeight), 1)

def DrawCountryGraphs():
    #Horizontal Lines
    pygame.draw.line(win, Dark_Gray1, (GraphOneX,GraphOneY+int(GraphHeight*(1/4))),(GraphOneX+GraphWidth-1,GraphOneY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphOneX,GraphOneY+int(GraphHeight*(2/4))),(GraphOneX+GraphWidth-1,GraphOneY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphOneX,GraphOneY+int(GraphHeight*(3/4))),(GraphOneX+GraphWidth-1,GraphOneY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwoX,GraphTwoY+int(GraphHeight*(1/4))),(GraphTwoX+GraphWidth-1,GraphTwoY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwoX,GraphTwoY+int(GraphHeight*(2/4))),(GraphTwoX+GraphWidth-1,GraphTwoY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwoX,GraphTwoY+int(GraphHeight*(3/4))),(GraphTwoX+GraphWidth-1,GraphTwoY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphThreeX,GraphThreeY+int(GraphHeight*(1/4))),(GraphThreeX+GraphWidth-1,GraphThreeY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphThreeX,GraphThreeY+int(GraphHeight*(2/4))),(GraphThreeX+GraphWidth-1,GraphThreeY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphThreeX,GraphThreeY+int(GraphHeight*(3/4))),(GraphThreeX+GraphWidth-1,GraphThreeY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphFourX,GraphFourY+int(GraphHeight*(1/4))),(GraphFourX+GraphWidth-1,GraphFourY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphFourX,GraphFourY+int(GraphHeight*(2/4))),(GraphFourX+GraphWidth-1,GraphFourY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphFourX,GraphFourY+int(GraphHeight*(3/4))),(GraphFourX+GraphWidth-1,GraphFourY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSixX,GraphSixY+int(GraphHeight*(1/4))),(GraphSixX+GraphWidth-1,GraphSixY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSixX,GraphSixY+int(GraphHeight*(2/4))),(GraphSixX+GraphWidth-1,GraphSixY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSixX,GraphSixY+int(GraphHeight*(3/4))),(GraphSixX+GraphWidth-1,GraphSixY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSevenX,GraphSevenY+int(GraphHeight*(1/4))),(GraphSevenX+GraphWidth-1,GraphSevenY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSevenX,GraphSevenY+int(GraphHeight*(2/4))),(GraphSevenX+GraphWidth-1,GraphSevenY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSevenX,GraphSevenY+int(GraphHeight*(3/4))),(GraphSevenX+GraphWidth-1,GraphSevenY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphNineX,GraphNineY+int(GraphHeight*(1/4))),(GraphNineX+GraphWidth-1,GraphNineY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphNineX,GraphNineY+int(GraphHeight*(2/4))),(GraphNineX+GraphWidth-1,GraphNineY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphNineX,GraphNineY+int(GraphHeight*(3/4))),(GraphNineX+GraphWidth-1,GraphNineY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTenX,GraphTenY+int(GraphHeight*(1/4))),(GraphTenX+GraphWidth-1,GraphTenY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTenX,GraphTenY+int(GraphHeight*(2/4))),(GraphTenX+GraphWidth-1,GraphTenY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTenX,GraphTenY+int(GraphHeight*(3/4))),(GraphTenX+GraphWidth-1,GraphTenY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphElevenX,GraphElevenY+int(GraphHeight*(1/4))),(GraphElevenX+GraphWidth-1,GraphElevenY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphElevenX,GraphElevenY+int(GraphHeight*(2/4))),(GraphElevenX+GraphWidth-1,GraphElevenY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphElevenX,GraphElevenY+int(GraphHeight*(3/4))),(GraphElevenX+GraphWidth-1,GraphElevenY+int(GraphHeight*(3/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwelveX,GraphTwelveY+int(GraphHeight*(1/4))),(GraphTwelveX+GraphWidth-1,GraphTwelveY+int(GraphHeight*(1/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwelveX,GraphTwelveY+int(GraphHeight*(2/4))),(GraphTwelveX+GraphWidth-1,GraphTwelveY+int(GraphHeight*(2/4))), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwelveX,GraphTwelveY+int(GraphHeight*(3/4))),(GraphTwelveX+GraphWidth-1,GraphTwelveY+int(GraphHeight*(3/4))), 1)

    #Vertical Lines
    pygame.draw.line(win, Dark_Gray1, (GraphOneX+int(GraphWidth*(1/4)),GraphOneY),(GraphOneX+int(GraphWidth*(1/4)),GraphOneY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphOneX+int(GraphWidth*(2/4)),GraphOneY),(GraphOneX+int(GraphWidth*(2/4)),GraphOneY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphOneX+int(GraphWidth*(3/4)),GraphOneY),(GraphOneX+int(GraphWidth*(3/4)),GraphOneY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwoX+int(GraphWidth*(1/4)),GraphTwoY),(GraphTwoX+int(GraphWidth*(1/4)),GraphTwoY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwoX+int(GraphWidth*(2/4)),GraphTwoY),(GraphTwoX+int(GraphWidth*(2/4)),GraphTwoY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwoX+int(GraphWidth*(3/4)),GraphTwoY),(GraphTwoX+int(GraphWidth*(3/4)),GraphTwoY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphThreeX+int(GraphWidth*(1/4)),GraphThreeY),(GraphThreeX+int(GraphWidth*(1/4)),GraphThreeY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphThreeX+int(GraphWidth*(2/4)),GraphThreeY),(GraphThreeX+int(GraphWidth*(2/4)),GraphThreeY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphThreeX+int(GraphWidth*(3/4)),GraphThreeY),(GraphThreeX+int(GraphWidth*(3/4)),GraphThreeY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphFourX+int(GraphWidth*(1/4)),GraphFourY),(GraphFourX+int(GraphWidth*(1/4)),GraphFourY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphFourX+int(GraphWidth*(2/4)),GraphFourY),(GraphFourX+int(GraphWidth*(2/4)),GraphFourY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphFourX+int(GraphWidth*(3/4)),GraphFourY),(GraphFourX+int(GraphWidth*(3/4)),GraphFourY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSixX+int(GraphWidth*(1/4)),GraphSixY),(GraphSixX+int(GraphWidth*(1/4)),GraphSixY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSixX+int(GraphWidth*(2/4)),GraphSixY),(GraphSixX+int(GraphWidth*(2/4)),GraphSixY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSixX+int(GraphWidth*(3/4)),GraphSixY),(GraphSixX+int(GraphWidth*(3/4)),GraphSixY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSevenX+int(GraphWidth*(1/4)),GraphSevenY),(GraphSevenX+int(GraphWidth*(1/4)),GraphSevenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSevenX+int(GraphWidth*(2/4)),GraphSevenY),(GraphSevenX+int(GraphWidth*(2/4)),GraphSevenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphSevenX+int(GraphWidth*(3/4)),GraphSevenY),(GraphSevenX+int(GraphWidth*(3/4)),GraphSevenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphNineX+int(GraphWidth*(1/4)),GraphNineY),(GraphNineX+int(GraphWidth*(1/4)),GraphNineY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphNineX+int(GraphWidth*(2/4)),GraphNineY),(GraphNineX+int(GraphWidth*(2/4)),GraphNineY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphNineX+int(GraphWidth*(3/4)),GraphNineY),(GraphNineX+int(GraphWidth*(3/4)),GraphNineY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTenX+int(GraphWidth*(1/4)),GraphTenY),(GraphTenX+int(GraphWidth*(1/4)),GraphTenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTenX+int(GraphWidth*(2/4)),GraphTenY),(GraphTenX+int(GraphWidth*(2/4)),GraphTenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTenX+int(GraphWidth*(3/4)),GraphTenY),(GraphTenX+int(GraphWidth*(3/4)),GraphTenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphElevenX+int(GraphWidth*(1/4)),GraphElevenY),(GraphElevenX+int(GraphWidth*(1/4)),GraphElevenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphElevenX+int(GraphWidth*(2/4)),GraphElevenY),(GraphElevenX+int(GraphWidth*(2/4)),GraphElevenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphElevenX+int(GraphWidth*(3/4)),GraphElevenY),(GraphElevenX+int(GraphWidth*(3/4)),GraphElevenY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwelveX+int(GraphWidth*(1/4)),GraphTwelveY),(GraphTwelveX+int(GraphWidth*(1/4)),GraphTwelveY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwelveX+int(GraphWidth*(2/4)),GraphTwelveY),(GraphTwelveX+int(GraphWidth*(2/4)),GraphTwelveY+GraphHeight-1), 1)
    pygame.draw.line(win, Dark_Gray1, (GraphTwelveX+int(GraphWidth*(3/4)),GraphTwelveY),(GraphTwelveX+int(GraphWidth*(3/4)),GraphTwelveY+GraphHeight-1), 1)

    #Draw Graph Top Text
    win.blit(ProductionFunction_TEXT, (GraphOneX+TextDisplacementX,GraphOneY+(2*TextDisplacementY)))
    win.blit(PFA_TEXT, (GraphOneX+TextDisplacementX,GraphOneY+TextDisplacementY))
    win.blit(PFB_TEXT, (GraphOneX+int(GraphWidth*(1/3))+TextDisplacementX,GraphOneY+TextDisplacementY))
    win.blit(PFC_TEXT, (GraphOneX+int(GraphWidth*(2/3))+TextDisplacementX,GraphOneY+TextDisplacementY))
    win.blit(MDUL_TEXT, (GraphTwoX+TextDisplacementX,GraphTwoY+TextDisplacementY))
    win.blit(MU_TEXT, (GraphThreeX+TextDisplacementX,GraphThreeY+(2*TextDisplacementY)))
    win.blit(MUA_TEXT, (GraphThreeX+TextDisplacementX,GraphThreeY+TextDisplacementY))
    win.blit(MUB_TEXT, (GraphThreeX+TextDisplacementX+int(GraphWidth*(1/3)),GraphThreeY+TextDisplacementY))
    win.blit(MUC_TEXT, (GraphThreeX+TextDisplacementX+int(GraphWidth*(2/3)),GraphThreeY+TextDisplacementY))
    win.blit(PriceA_TEXT, (GraphFourX+TextDisplacementX,GraphFourY+TextDisplacementY))
    win.blit(PriceB_TEXT, (GraphFourX+TextDisplacementX+int(GraphWidth*(1/3)),GraphFourY+TextDisplacementY))
    win.blit(PriceC_TEXT, (GraphFourX+TextDisplacementX+int(GraphWidth*(2/3)),GraphFourY+TextDisplacementY))
    win.blit(LabourPercent_TEXT, (GraphFiveX+TextDisplacementX,GraphFiveY+TextDisplacementY))#############################
    win.blit(Export_TEXT, (GraphSixX+TextDisplacementX,GraphSixY+TextDisplacementY))
    a = GraphWidth - (Export_TEXT.get_width() + (2*TextDisplacementX))
    win.blit(ExportA_TEXT, (GraphSixX+TextDisplacementX+Export_TEXT.get_width()+40,GraphSixY+TextDisplacementY))
    win.blit(ExportB_TEXT, (GraphSixX+TextDisplacementX+Export_TEXT.get_width()+int(a*(1/3))+40,GraphSixY+TextDisplacementY))
    win.blit(ExportC_TEXT, (GraphSixX+TextDisplacementX+Export_TEXT.get_width()+int(a*(2/3))+40,GraphSixY+TextDisplacementY))
    win.blit(SupplyLabour_TEXT, (GraphSevenX+TextDisplacementX,GraphSevenY+TextDisplacementY))
    win.blit(BudgetPercent_TEXT, (GraphEightX+TextDisplacementX,GraphEightY+TextDisplacementY))#############################
    win.blit(Import_TEXT, (GraphNineX+TextDisplacementX,GraphNineY+TextDisplacementY))
    b = GraphWidth - (Import_TEXT.get_width() + (2*TextDisplacementX))
    win.blit(ImportA_TEXT, (GraphNineX+TextDisplacementX+Export_TEXT.get_width()+40,GraphNineY+TextDisplacementY))
    win.blit(ImportB_TEXT, (GraphNineX+TextDisplacementX+Export_TEXT.get_width()+int(b*(1/3))+40,GraphNineY+TextDisplacementY))
    win.blit(ImportC_TEXT, (GraphNineX+TextDisplacementX+Export_TEXT.get_width()+int(b*(2/3))+40,GraphNineY+TextDisplacementY))
    win.blit(WageRate_TEXT, (GraphTenX+TextDisplacementX,GraphTenY+TextDisplacementY))
    win.blit(MUMoneyA_TEXT, (GraphElevenX+TextDisplacementX,GraphElevenY+TextDisplacementY))
    win.blit(MUMoneyB_TEXT, (GraphElevenX+TextDisplacementX+int(GraphWidth*(1/4)),GraphElevenY+TextDisplacementY))
    win.blit(MUMoneyC_TEXT, (GraphElevenX+TextDisplacementX+int(GraphWidth*(2/4)),GraphElevenY+TextDisplacementY))
    win.blit(MDUEarnMoney_TEXT, (GraphElevenX+TextDisplacementX+int(GraphWidth*(3/4)),GraphElevenY+TextDisplacementY))
    win.blit(MVPA_TEXT, (GraphTwelveX+TextDisplacementX,GraphTwelveY+TextDisplacementY))
    win.blit(MVPB_TEXT, (GraphTwelveX+TextDisplacementX+int(GraphWidth*(1/3)),GraphTwelveY+TextDisplacementY))
    win.blit(MVPC_TEXT, (GraphTwelveX+TextDisplacementX+int(GraphWidth*(2/3)),GraphTwelveY+TextDisplacementY))

    #Draw Fluid Graph Variables
    win.blit(VariableSupplyA_TEXT, (GraphOneX+VariableTextDisplacementX,GraphOneY+VariableTextDisplacementY))
    win.blit(VariableSupplyB_TEXT, (GraphOneX+VariableTextDisplacementX+int(GraphWidth*(1/3)),GraphOneY+VariableTextDisplacementY))
    win.blit(VariableSupplyC_TEXT, (GraphOneX+VariableTextDisplacementX+int(GraphWidth*(2/3)),GraphOneY+VariableTextDisplacementY))
    win.blit(VariablePriceA_TEXT, (GraphFourX+VariableTextDisplacementX,GraphFourY+VariableTextDisplacementY))
    win.blit(VariablePriceB_TEXT, (GraphFourX+VariableTextDisplacementX+int(GraphWidth*(1/3)),GraphFourY+VariableTextDisplacementY))
    win.blit(VariablePriceC_TEXT, (GraphFourX+VariableTextDisplacementX+int(GraphWidth*(2/3)),GraphFourY+VariableTextDisplacementY))
    win.blit(VariableSupplyLabour_TEXT, (GraphSevenX+VariableTextDisplacementX,GraphSevenY+VariableTextDisplacementY))
    win.blit(VariableIncome_TEXT, (GraphSevenX+VariableTextDisplacementX+int(GraphWidth/2),GraphSevenY+VariableTextDisplacementY))
    win.blit(VariableTotalExports_TEXT, (GraphSixX+VariableTextDisplacementX,GraphSixY+VariableTextDisplacementY))
    win.blit(VariableExportsA, (GraphSixX+VariableTextDisplacementX+Export_TEXT.get_width()+40,GraphSixY+VariableTextDisplacementY))
    win.blit(VariableExportsB, (GraphSixX+VariableTextDisplacementX+Export_TEXT.get_width()+int(a*(1/3))+40,GraphSixY+VariableTextDisplacementY))
    win.blit(VariableExportsC, (GraphSixX+VariableTextDisplacementX+Export_TEXT.get_width()+int(a*(2/3))+40,GraphSixY+VariableTextDisplacementY))
    win.blit(VariableTotalImports_TEXT, (GraphNineX+VariableTextDisplacementX,GraphNineY+VariableTextDisplacementY))
    win.blit(VariableImportsA, (GraphNineX+VariableTextDisplacementX+Export_TEXT.get_width()+40,GraphNineY+VariableTextDisplacementY))
    win.blit(VariableImportsB, (GraphNineX+VariableTextDisplacementX+Export_TEXT.get_width()+int(a*(1/3))+40,GraphNineY+VariableTextDisplacementY))
    win.blit(VariableImportsC, (GraphNineX+VariableTextDisplacementX+Export_TEXT.get_width()+int(a*(2/3))+40,GraphNineY+VariableTextDisplacementY))
    win.blit(VariableWageRate, (GraphTenX+VariableTextDisplacementX,GraphTenY+VariableTextDisplacementY))
    win.blit(VariableMUSpendMoneyA, (GraphElevenX+VariableTextDisplacementX,GraphElevenY+VariableTextDisplacementY))
    win.blit(VariableMUSpendMoneyB, (GraphElevenX+VariableTextDisplacementX+int(GraphWidth*(1/4)),GraphElevenY+VariableTextDisplacementY))
    win.blit(VariableMUSpendMoneyC, (GraphElevenX+VariableTextDisplacementX+int(GraphWidth*(2/4)),GraphElevenY+VariableTextDisplacementY))
    win.blit(VariableMDUEarnMoney, (GraphElevenX+VariableTextDisplacementX+int(GraphWidth*(3/4)),GraphElevenY+VariableTextDisplacementY))
    win.blit(VariableMVPA_TEXT, (GraphTwelveX+VariableTextDisplacementX,GraphTwelveY+VariableTextDisplacementY))
    win.blit(VariableMVPB_TEXT, (GraphTwelveX+VariableTextDisplacementX+int(GraphWidth*(1/3)),GraphTwelveY+VariableTextDisplacementY))
    win.blit(VariableMVPC_TEXT, (GraphTwelveX+VariableTextDisplacementX+int(GraphWidth*(2/3)),GraphTwelveY+VariableTextDisplacementY))

    win.blit(LabourPercentA_Mini_Text, (GraphFiveX+VariableTextDisplacementX,GraphFiveY+MiniTextBase))
    win.blit(LabourPercentB_Mini_Text, (GraphFiveX+VariableTextDisplacementX,GraphFiveY+(MiniTextSpacing*1)+(LabourPercentA_Text.get_height()*1)+MiniTextBase))
    win.blit(LabourPercentC_Mini_Text, (GraphFiveX+VariableTextDisplacementX,GraphFiveY+(MiniTextSpacing*2)+(LabourPercentA_Text.get_height()*2)+MiniTextBase))
    win.blit(LabourPercentA_Text, (GraphFiveX+VariableTextDisplacementX+10+LabourPercentA_Mini_Text.get_width(),GraphFiveY+MiniTextBase))
    win.blit(LabourPercentB_Text, (GraphFiveX+VariableTextDisplacementX+10+LabourPercentB_Mini_Text.get_width(),GraphFiveY+(MiniTextSpacing*1)+(LabourPercentA_Text.get_height()*1)+MiniTextBase))
    win.blit(LabourPercentC_Text, (GraphFiveX+VariableTextDisplacementX+10+LabourPercentC_Mini_Text.get_width(),GraphFiveY+(MiniTextSpacing*2)+(LabourPercentA_Text.get_height()*2)+MiniTextBase))

    win.blit(BudgetPercentA_Mini_Text, (GraphEightX+VariableTextDisplacementX,GraphEightY+MiniTextBase))
    win.blit(BudgetPercentB_Mini_Text, (GraphEightX+VariableTextDisplacementX,GraphEightY+(MiniTextSpacing*1)+(LabourPercentA_Text.get_height()*1)+MiniTextBase))
    win.blit(BudgetPercentC_Mini_Text, (GraphEightX+VariableTextDisplacementX,GraphEightY+(MiniTextSpacing*2)+(LabourPercentA_Text.get_height()*2)+MiniTextBase))
    win.blit(BudgetPercentA_Text, (GraphEightX+VariableTextDisplacementX+10+LabourPercentA_Mini_Text.get_width(),GraphEightY+MiniTextBase))
    win.blit(BudgetPercentB_Text, (GraphEightX+VariableTextDisplacementX+10+LabourPercentB_Mini_Text.get_width(),GraphEightY+(MiniTextSpacing*1)+(LabourPercentA_Text.get_height()*1)+MiniTextBase))
    win.blit(BudgetPercentC_Text, (GraphEightX+VariableTextDisplacementX+10+LabourPercentC_Mini_Text.get_width(),GraphEightY+(MiniTextSpacing*2)+(LabourPercentA_Text.get_height()*2)+MiniTextBase))



    #Draw Fluid Vertical Labels
    win.blit(GraphOneHeightLabel0_TEXT, (GraphOneX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphOneY))
    win.blit(GraphOneHeightLabel3_TEXT, (GraphOneX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphOneY+int(GraphHeight*(1/4))))
    win.blit(GraphOneHeightLabel2_TEXT, (GraphOneX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphOneY+int(GraphHeight*(2/4))))
    win.blit(GraphOneHeightLabel1_TEXT, (GraphOneX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphOneY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphOneX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphOneY+GraphHeight))
    win.blit(GraphTwoHeightLabel0_TEXT, (GraphTwoX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwoY))
    win.blit(GraphTwoHeightLabel3_TEXT, (GraphTwoX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwoY+int(GraphHeight*(1/4))))
    win.blit(GraphTwoHeightLabel2_TEXT, (GraphTwoX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwoY+int(GraphHeight*(2/4))))
    win.blit(GraphTwoHeightLabel1_TEXT, (GraphTwoX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwoY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphTwoX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwoY+GraphHeight))
    win.blit(GraphThreeHeightLabel0_TEXT, (GraphThreeX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphThreeY))
    win.blit(GraphThreeHeightLabel3_TEXT, (GraphThreeX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphThreeY+int(GraphHeight*(1/4))))
    win.blit(GraphThreeHeightLabel2_TEXT, (GraphThreeX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphThreeY+int(GraphHeight*(2/4))))
    win.blit(GraphThreeHeightLabel1_TEXT, (GraphThreeX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphThreeY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphThreeX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphThreeY+GraphHeight))
    win.blit(GraphFourHeightLabel0_TEXT, (GraphFourX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphFourY))
    win.blit(GraphFourHeightLabel3_TEXT, (GraphFourX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphFourY+int(GraphHeight*(1/4))))
    win.blit(GraphFourHeightLabel2_TEXT, (GraphFourX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphFourY+int(GraphHeight*(2/4))))
    win.blit(GraphFourHeightLabel1_TEXT, (GraphFourX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphFourY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphFourX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphFourY+GraphHeight))
    win.blit(GraphSixHeightLabel0_TEXT, (GraphSixX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSixY))
    win.blit(GraphSixHeightLabel3_TEXT, (GraphSixX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSixY+int(GraphHeight*(1/4))))
    win.blit(GraphSixHeightLabel2_TEXT, (GraphSixX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSixY+int(GraphHeight*(2/4))))
    win.blit(GraphSixHeightLabel1_TEXT, (GraphSixX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSixY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphSixX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSixY+GraphHeight))
    win.blit(GraphSevenHeightLabel0_TEXT, (GraphSevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSevenY))
    win.blit(GraphSevenHeightLabel3_TEXT, (GraphSevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSevenY+int(GraphHeight*(1/4))))
    win.blit(GraphSevenHeightLabel2_TEXT, (GraphSevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSevenY+int(GraphHeight*(2/4))))
    win.blit(GraphSevenHeightLabel1_TEXT, (GraphSevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSevenY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphSevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphSevenY+GraphHeight))
    win.blit(GraphNineHeightLabel0_TEXT, (GraphNineX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphNineY))
    win.blit(GraphNineHeightLabel3_TEXT, (GraphNineX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphNineY+int(GraphHeight*(1/4))))
    win.blit(GraphNineHeightLabel2_TEXT, (GraphNineX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphNineY+int(GraphHeight*(2/4))))
    win.blit(GraphNineHeightLabel1_TEXT, (GraphNineX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphNineY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphNineX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphNineY+GraphHeight))
    win.blit(GraphTenHeightLabel0_TEXT, (GraphTenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTenY))
    win.blit(GraphTenHeightLabel3_TEXT, (GraphTenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTenY+int(GraphHeight*(1/4))))
    win.blit(GraphTenHeightLabel2_TEXT, (GraphTenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTenY+int(GraphHeight*(2/4))))
    win.blit(GraphTenHeightLabel1_TEXT, (GraphTenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTenY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphTenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTenY+GraphHeight))
    win.blit(GraphElevenHeightLabel0_TEXT, (GraphElevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphElevenY))
    win.blit(GraphElevenHeightLabel3_TEXT, (GraphElevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphElevenY+int(GraphHeight*(1/4))))
    win.blit(GraphElevenHeightLabel2_TEXT, (GraphElevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphElevenY+int(GraphHeight*(2/4))))
    win.blit(GraphElevenHeightLabel1_TEXT, (GraphElevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphElevenY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphElevenX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphElevenY+GraphHeight))
    win.blit(GraphTwelveHeightLabel0_TEXT, (GraphTwelveX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwelveY))
    win.blit(GraphTwelveHeightLabel3_TEXT, (GraphTwelveX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwelveY+int(GraphHeight*(1/4))))
    win.blit(GraphTwelveHeightLabel2_TEXT, (GraphTwelveX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwelveY+int(GraphHeight*(2/4))))
    win.blit(GraphTwelveHeightLabel1_TEXT, (GraphTwelveX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwelveY+int(GraphHeight*(3/4))))
    win.blit(GraphHeightZero_TEXT, (GraphTwelveX+GraphWidth-1+VerticalLabelTextDisplacementX,VerticalLabelTextDisplacementY+GraphTwelveY+GraphHeight))

    #Draw Fluid Horizontal Labels
    win.blit(GraphOneWidthLabel0_TEXT, (GraphOneX+GraphWidth-GraphOneWidthLabel0_TEXT.get_width(),GraphOneY+GraphHeight))
    win.blit(GraphOneWidthLabel1_TEXT, (GraphOneX+int(GraphWidth*(1/4)),GraphOneY+GraphHeight))
    win.blit(GraphOneWidthLabel2_TEXT, (GraphOneX+int(GraphWidth*(2/4)),GraphOneY+GraphHeight))
    win.blit(GraphOneWidthLabel3_TEXT, (GraphOneX+int(GraphWidth*(3/4)),GraphOneY+GraphHeight))
    win.blit(GraphHeightZero_TEXT, (GraphOneX,GraphOneY+GraphHeight))
    win.blit(GraphTwoWidthLabel0_TEXT, (GraphTwoX+GraphWidth-GraphTwoWidthLabel0_TEXT.get_width(),GraphTwoY+GraphHeight))
    win.blit(GraphTwoWidthLabel1_TEXT, (GraphTwoX+int(GraphWidth*(1/4)),GraphTwoY+GraphHeight))
    win.blit(GraphTwoWidthLabel2_TEXT, (GraphTwoX+int(GraphWidth*(2/4)),GraphTwoY+GraphHeight))
    win.blit(GraphTwoWidthLabel3_TEXT, (GraphTwoX+int(GraphWidth*(3/4)),GraphTwoY+GraphHeight))
    win.blit(GraphHeightZero_TEXT, (GraphTwoX,GraphTwoY+GraphHeight))
    win.blit(GraphThreeWidthLabel0_TEXT, (GraphThreeX+GraphWidth-GraphThreeWidthLabel0_TEXT.get_width(),GraphThreeY+GraphHeight))
    win.blit(GraphThreeWidthLabel1_TEXT, (GraphThreeX+int(GraphWidth*(1/4)),GraphThreeY+GraphHeight))
    win.blit(GraphThreeWidthLabel2_TEXT, (GraphThreeX+int(GraphWidth*(2/4)),GraphThreeY+GraphHeight))
    win.blit(GraphThreeWidthLabel3_TEXT, (GraphThreeX+int(GraphWidth*(3/4)),GraphThreeY+GraphHeight))
    win.blit(GraphHeightZero_TEXT, (GraphThreeX,GraphThreeY+GraphHeight))

#Graph Lines
def DrawGermanyGraphLines():
    #Functions
    pygame.draw.lines(win, Blue, False, GermanyProductionFunctionAList, 1)
    pygame.draw.lines(win, Red, False, GermanyProductionFunctionBList, 1)
    pygame.draw.lines(win, Green, False, GermanyProductionFunctionCList, 1)
    pygame.draw.lines(win, White, False, GermanyMarginalDisUtilityLabourList, 1)
    pygame.draw.lines(win, Blue, False, GermanyMarginalUtilityAList, 1)
    pygame.draw.lines(win, Red, False, GermanyMarginalUtilityBList, 1)
    pygame.draw.lines(win, Green, False, GermanyMarginalUtilityCList, 1)
    #Data
    pygame.draw.lines(win, Blue, False, GermanyBakePriceAList, 1)
    pygame.draw.lines(win, Red, False, GermanyBakePriceBList, 1)
    pygame.draw.lines(win, Green, False, GermanyBakePriceCList, 1)
    pygame.draw.polygon(win, Blue, GermanyBakeExportABCList, 0)
    pygame.draw.polygon(win, Red, GermanyBakeExportBCList, 0)
    pygame.draw.polygon(win, Green, GermanyBakeExportCList, 0)
    pygame.draw.lines(win, White, False, GermanyBakeSupplyLabourList, 1)
    pygame.draw.polygon(win, Blue, GermanyBakeImportABCList, 0)
    pygame.draw.polygon(win, Red, GermanyBakeImportBCList, 0)
    pygame.draw.polygon(win, Green, GermanyBakeImportCList, 0)
    pygame.draw.lines(win, White, False, GermanyBakeWageRateList, 1)
    pygame.draw.lines(win, Blue, False, GermanyBakeMUMoneyAList, 1)
    pygame.draw.lines(win, Red, False, GermanyBakeMUMoneyBList, 1)
    pygame.draw.lines(win, Green, False, GermanyBakeMUMoneyCList, 1)
    pygame.draw.lines(win, Gold, False, GermanyBakeMDUMoneyList, 1)
    pygame.draw.lines(win, Blue, False, GermanyBakeMPVAList, 1)
    pygame.draw.lines(win, Red, False, GermanyBakeMPVBList, 1)
    pygame.draw.lines(win, Green, False, GermanyBakeMPVCList, 1)

def DrawFranceGraphLines():
    #Functions
    pygame.draw.lines(win, Blue, False, FranceProductionFunctionAList, 1)
    pygame.draw.lines(win, Red, False, FranceProductionFunctionBList, 1)
    pygame.draw.lines(win, Green, False, FranceProductionFunctionCList, 1)
    pygame.draw.lines(win, White, False, FranceMarginalDisUtilityLabourList, 1)
    pygame.draw.lines(win, Blue, False, FranceMarginalUtilityAList, 1)
    pygame.draw.lines(win, Red, False, FranceMarginalUtilityBList, 1)
    pygame.draw.lines(win, Green, False, FranceMarginalUtilityCList, 1)
    #Data
    pygame.draw.lines(win, Blue, False, FranceBakePriceAList, 1)
    pygame.draw.lines(win, Red, False, FranceBakePriceBList, 1)
    pygame.draw.lines(win, Green, False, FranceBakePriceCList, 1)
    pygame.draw.polygon(win, Blue, FranceBakeExportABCList, 0)
    pygame.draw.polygon(win, Red, FranceBakeExportBCList, 0)
    pygame.draw.polygon(win, Green, FranceBakeExportCList, 0)
    pygame.draw.lines(win, White, False, FranceBakeSupplyLabourList, 1)
    pygame.draw.polygon(win, Blue, FranceBakeImportABCList, 0)
    pygame.draw.polygon(win, Red, FranceBakeImportBCList, 0)
    pygame.draw.polygon(win, Green, FranceBakeImportCList, 0)
    pygame.draw.lines(win, White, False, FranceBakeWageRateList, 1)
    pygame.draw.lines(win, Blue, False, FranceBakeMUMoneyAList, 1)
    pygame.draw.lines(win, Red, False, FranceBakeMUMoneyBList, 1)
    pygame.draw.lines(win, Green, False, FranceBakeMUMoneyCList, 1)
    pygame.draw.lines(win, Gold, False, FranceBakeMDUMoneyList, 1)
    pygame.draw.lines(win, Blue, False, FranceBakeMPVAList, 1)
    pygame.draw.lines(win, Red, False, FranceBakeMPVBList, 1)
    pygame.draw.lines(win, Green, False, FranceBakeMPVCList, 1)

#Draw Sliders
def DrawGermanySliders():
    #Flag
    pygame.draw.rect(win, Dark_Gray1, (FlagX-FlagBorder,FlagY-FlagBorder,FlagWidth+(2*FlagBorder),FlagHeight+(2*FlagBorder)))
    pygame.draw.rect(win, Gold, (FlagX,FlagY,FlagWidth,FlagHeight))
    pygame.draw.rect(win, Red, (FlagX,FlagY,FlagWidth,round(FlagHeight*(2/3))))
    pygame.draw.rect(win, Black, (FlagX,FlagY,FlagWidth,round(FlagHeight*(1/3))))
    win.blit(GermanyTEXT, (GermanyTEXT_X,GermanyTEXT_Y))

    #Slider Bar
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderOneY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderTwoY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderThreeY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderFourY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderFiveY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderSixY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderSevenY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderEightY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderNineY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderTenY,SliderWidth,SliderThickness))

    #Slider Name
    win.blit(MUASliderText, (SliderX+SliderNameDisplacementX,SliderOneY+SliderNameDisplacementY))
    win.blit(MUBSliderText, (SliderX+SliderNameDisplacementX,SliderTwoY+SliderNameDisplacementY))
    win.blit(MUCSliderText, (SliderX+SliderNameDisplacementX,SliderThreeY+SliderNameDisplacementY))
    win.blit(MDULSliderText, (SliderX+SliderNameDisplacementX,SliderFourY+SliderNameDisplacementY))
    win.blit(PFASliderText, (SliderX+SliderNameDisplacementX,SliderFiveY+SliderNameDisplacementY))
    win.blit(PFBSliderText, (SliderX+SliderNameDisplacementX,SliderSixY+SliderNameDisplacementY))
    win.blit(PFCSliderText, (SliderX+SliderNameDisplacementX,SliderSevenY+SliderNameDisplacementY))
    win.blit(TarrifAText, (SliderX+SliderNameDisplacementX,SliderEightY+SliderNameDisplacementY))
    win.blit(TarrifBText, (SliderX+SliderNameDisplacementX,SliderNineY+SliderNameDisplacementY))
    win.blit(TarrifCText, (SliderX+SliderNameDisplacementX,SliderTenY+SliderNameDisplacementY))

    #Slider Name Percent Variable
    win.blit(GermanySliderPercentValueTextOne, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderOneY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextTwo, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderTwoY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextThree, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderThreeY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextFour, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderFourY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextFive, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderFiveY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextSix, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderSixY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextSeven, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderSevenY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextEight, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderEightY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextNine, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderNineY+SliderNameDisplacementY))
    win.blit(GermanySliderPercentValueTextTen, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderTenY+SliderNameDisplacementY))

    #Slider Hit Box
    if (ShowSliderHitbox == True):
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderOneHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderTwoHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderThreeHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderFourHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderFiveHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderSixHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderSevenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderEightHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderNineHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderTenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderElevenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderTwelveHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderThirteenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)

    #Slider Dot
    pygame.draw.rect(win, Red, (GermanySliderDotOneX,SliderOneY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotTwoX,SliderTwoY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotThreeX,SliderThreeY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotFourX,SliderFourY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotFiveX,SliderFiveY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotSixX,SliderSixY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotSevenX,SliderSevenY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotEightX,SliderEightY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotNineX,SliderNineY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (GermanySliderDotTenX,SliderTenY,SliderThickness,SliderThickness))

    if (SliderSelection == "One"):
        pygame.draw.rect(win, White, (GermanySliderDotOneX,SliderOneY,SliderThickness,SliderThickness))
    if (SliderSelection == "Two"):
        pygame.draw.rect(win, White, (GermanySliderDotTwoX,SliderTwoY,SliderThickness,SliderThickness))
    if (SliderSelection == "Three"):
        pygame.draw.rect(win, White, (GermanySliderDotThreeX,SliderThreeY,SliderThickness,SliderThickness))
    if (SliderSelection == "Four"):
        pygame.draw.rect(win, White, (GermanySliderDotFourX,SliderFourY,SliderThickness,SliderThickness))
    if (SliderSelection == "Five"):
        pygame.draw.rect(win, White, (GermanySliderDotFiveX,SliderFiveY,SliderThickness,SliderThickness))
    if (SliderSelection == "Six"):
        pygame.draw.rect(win, White, (GermanySliderDotSixX,SliderSixY,SliderThickness,SliderThickness))
    if (SliderSelection == "Seven"):
        pygame.draw.rect(win, White, (GermanySliderDotSevenX,SliderSevenY,SliderThickness,SliderThickness))
    if (SliderSelection == "Eight"):
        pygame.draw.rect(win, White, (GermanySliderDotEightX,SliderEightY,SliderThickness,SliderThickness))
    if (SliderSelection == "Nine"):
        pygame.draw.rect(win, White, (GermanySliderDotNineX,SliderNineY,SliderThickness,SliderThickness))
    if (SliderSelection == "Ten"):
        pygame.draw.rect(win, White, (GermanySliderDotTenX,SliderTenY,SliderThickness,SliderThickness))

def DrawFranceSliders():
    #Flag
    pygame.draw.rect(win, Dark_Gray1, (FlagX-FlagBorder,FlagY-FlagBorder,FlagWidth+(2*FlagBorder),FlagHeight+(2*FlagBorder)))
    pygame.draw.rect(win, Red, (FlagX,FlagY,FlagWidth,FlagHeight))
    pygame.draw.rect(win, White, (FlagX,FlagY,round(FlagWidth*(2/3)),FlagHeight))
    pygame.draw.rect(win, French_Blue, (FlagX,FlagY,round(FlagWidth*(1/3)),FlagHeight))
    win.blit(FranceTEXT, (FranceTEXT_X,FranceTEXT_Y))

    #Slider Bar
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderOneY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderTwoY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderThreeY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderFourY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderFiveY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderSixY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderSevenY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderEightY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderNineY,SliderWidth,SliderThickness))
    pygame.draw.rect(win, Dark_Gray1, (SliderX,SliderTenY,SliderWidth,SliderThickness))

    #Slider Name
    win.blit(MUASliderText, (SliderX+SliderNameDisplacementX,SliderOneY+SliderNameDisplacementY))
    win.blit(MUBSliderText, (SliderX+SliderNameDisplacementX,SliderTwoY+SliderNameDisplacementY))
    win.blit(MUCSliderText, (SliderX+SliderNameDisplacementX,SliderThreeY+SliderNameDisplacementY))
    win.blit(MDULSliderText, (SliderX+SliderNameDisplacementX,SliderFourY+SliderNameDisplacementY))
    win.blit(PFASliderText, (SliderX+SliderNameDisplacementX,SliderFiveY+SliderNameDisplacementY))
    win.blit(PFBSliderText, (SliderX+SliderNameDisplacementX,SliderSixY+SliderNameDisplacementY))
    win.blit(PFCSliderText, (SliderX+SliderNameDisplacementX,SliderSevenY+SliderNameDisplacementY))
    win.blit(TarrifAText, (SliderX+SliderNameDisplacementX,SliderEightY+SliderNameDisplacementY))
    win.blit(TarrifBText, (SliderX+SliderNameDisplacementX,SliderNineY+SliderNameDisplacementY))
    win.blit(TarrifCText, (SliderX+SliderNameDisplacementX,SliderTenY+SliderNameDisplacementY))

    #Slider Name Percent Variable
    win.blit(FranceSliderPercentValueTextOne, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderOneY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextTwo, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderTwoY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextThree, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderThreeY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextFour, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderFourY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextFive, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderFiveY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextSix, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderSixY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextSeven, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderSevenY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextEight, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderEightY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextNine, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderNineY+SliderNameDisplacementY))
    win.blit(FranceSliderPercentValueTextTen, (SliderX+round(SliderWidth/2)+SliderNameDisplacementX,SliderTenY+SliderNameDisplacementY))

    #Slider Hit Box
    if (ShowSliderHitbox == True):
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderOneHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderTwoHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderThreeHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderFourHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderFiveHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderSixHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderSevenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderEightHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderNineHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderTenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderElevenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderTwelveHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)
        pygame.draw.rect(win, Red, (SliderHitboxX,SliderThirteenHitboxY,SliderHitboxWidth,SliderHitboxHeight), 1)

    #Slider Dot
    pygame.draw.rect(win, Red, (FranceSliderDotOneX,SliderOneY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotTwoX,SliderTwoY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotThreeX,SliderThreeY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotFourX,SliderFourY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotFiveX,SliderFiveY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotSixX,SliderSixY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotSevenX,SliderSevenY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotEightX,SliderEightY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotNineX,SliderNineY,SliderThickness,SliderThickness))
    pygame.draw.rect(win, Red, (FranceSliderDotTenX,SliderTenY,SliderThickness,SliderThickness))

    if (SliderSelection == "One"):
        pygame.draw.rect(win, White, (FranceSliderDotOneX,SliderOneY,SliderThickness,SliderThickness))
    if (SliderSelection == "Two"):
        pygame.draw.rect(win, White, (FranceSliderDotTwoX,SliderTwoY,SliderThickness,SliderThickness))
    if (SliderSelection == "Three"):
        pygame.draw.rect(win, White, (FranceSliderDotThreeX,SliderThreeY,SliderThickness,SliderThickness))
    if (SliderSelection == "Four"):
        pygame.draw.rect(win, White, (FranceSliderDotFourX,SliderFourY,SliderThickness,SliderThickness))
    if (SliderSelection == "Five"):
        pygame.draw.rect(win, White, (FranceSliderDotFiveX,SliderFiveY,SliderThickness,SliderThickness))
    if (SliderSelection == "Six"):
        pygame.draw.rect(win, White, (FranceSliderDotSixX,SliderSixY,SliderThickness,SliderThickness))
    if (SliderSelection == "Seven"):
        pygame.draw.rect(win, White, (FranceSliderDotSevenX,SliderSevenY,SliderThickness,SliderThickness))
    if (SliderSelection == "Eight"):
        pygame.draw.rect(win, White, (FranceSliderDotEightX,SliderEightY,SliderThickness,SliderThickness))
    if (SliderSelection == "Nine"):
        pygame.draw.rect(win, White, (FranceSliderDotNineX,SliderNineY,SliderThickness,SliderThickness))
    if (SliderSelection == "Ten"):
        pygame.draw.rect(win, White, (FranceSliderDotTenX,SliderTenY,SliderThickness,SliderThickness))

#Germany Production
def GermanyProductionFunctionA(x):
    return (x**0.5)*12*(1+(round(SliderMaxPercentValueFive*GermanySliderNormalizedValueFive)/100))
def GermanyProductionFunctionB(x):
    return (x**0.5)*6*(1+(round(SliderMaxPercentValueSix*GermanySliderNormalizedValueSix)/100))
def GermanyProductionFunctionC(x):
    return (x**0.5)*8*(1+(round(SliderMaxPercentValueSeven*GermanySliderNormalizedValueSeven)/100))

#France Production
def FranceProductionFunctionA(x):
    return (x**0.5)*4*(1+(round(SliderMaxPercentValueFive*FranceSliderNormalizedValueFive)/100))
def FranceProductionFunctionB(x):
    return (x**0.5)*5*(1+(round(SliderMaxPercentValueSix*FranceSliderNormalizedValueSix)/100))
def FranceProductionFunctionC(x):
    return (x**0.5)*6*(1+(round(SliderMaxPercentValueSeven*FranceSliderNormalizedValueSeven)/100))

#Germany Marginal Utility
def GermanyMarginalUtilityFunctionA(x):
    return (0.9**x)*12*(1+(round(SliderMaxPercentValueOne*GermanySliderNormalizedValueOne)/100))
def GermanyMarginalUtilityFunctionB(x):
    return (0.9**x)*10*(1+(round(SliderMaxPercentValueTwo*GermanySliderNormalizedValueTwo)/100))
def GermanyMarginalUtilityFunctionC(x):
    return (0.9**x)*8*(1+(round(SliderMaxPercentValueThree*GermanySliderNormalizedValueThree)/100))

#France Marginal Utility
def FranceMarginalUtilityFunctionA(x):
    return (0.9**x)*12*(1+(round(SliderMaxPercentValueOne*FranceSliderNormalizedValueOne)/100))
def FranceMarginalUtilityFunctionB(x):
    return (0.9**x)*10*(1+(round(SliderMaxPercentValueTwo*FranceSliderNormalizedValueTwo)/100))
def FranceMarginalUtilityFunctionC(x):
    return (0.9**x)*8*(1+(round(SliderMaxPercentValueThree*FranceSliderNormalizedValueThree)/100))

#Marginal Dis Utility Labour
def GermanyMarginalDisUtilityLabourFunction(x):
    return ((1/((-1*x)+16))-(1/16))*400*(1+(round(SliderMaxPercentValueFour*GermanySliderNormalizedValueFour)/100))
def FranceMarginalDisUtilityLabourFunction(x):
    return ((1/((-1*x)+16))-(1/16))*400*(1+(round(SliderMaxPercentValueFour*FranceSliderNormalizedValueFour)/100))

def IncrementPercentage(a,b,c):
    a = a + Increment
    x = a + b + c
    a = (a/x) * Percent
    b = (b/x) * Percent
    c = (c/x) * Percent
    return a, b, c

def IncrementTwo(a,b):
    a = a + Increment
    x = a + b
    a = (a/x) * ImportPercent
    b = (b/x) * ImportPercent
    return a, b

#Germany Pixel Functions
def PixelGermanyProductionFunctionA(x):
    a = 1+int((GermanyProductionFunctionA(((x-GraphOneX)/GraphWidth)*GermanyGraphOneWidth)/GermanyGraphOneHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelGermanyProductionFunctionB(x):
    a = 1+int((GermanyProductionFunctionB(((x-GraphOneX)/GraphWidth)*GermanyGraphOneWidth)/GermanyGraphOneHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelGermanyProductionFunctionC(x):
    a = 1+int((GermanyProductionFunctionC(((x-GraphOneX)/GraphWidth)*GermanyGraphOneWidth)/GermanyGraphOneHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelGermanyMarginalDisUtilityLabourFunction(x):
    a = 1+int((GermanyMarginalDisUtilityLabourFunction(((x-GraphTwoX)/GraphWidth)*GermanyGraphTwoWidth)/GermanyGraphTwoHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelGermanyMarginalUtilityFunctionA(x):
    a = 1+int((GermanyMarginalUtilityFunctionA(((x-GraphThreeX)/GraphWidth)*GermanyGraphThreeWidth)/GermanyGraphThreeHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelGermanyMarginalUtilityFunctionB(x):
    a = 1+int((GermanyMarginalUtilityFunctionB(((x-GraphThreeX)/GraphWidth)*GermanyGraphThreeWidth)/GermanyGraphThreeHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelGermanyMarginalUtilityFunctionC(x):
    a = 1+int((GermanyMarginalUtilityFunctionC(((x-GraphThreeX)/GraphWidth)*GermanyGraphThreeWidth)/GermanyGraphThreeHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a

#France Pixel Functions
def PixelFranceProductionFunctionA(x):
    a = 1+int((FranceProductionFunctionA(((x-GraphOneX)/GraphWidth)*FranceGraphOneWidth)/FranceGraphOneHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelFranceProductionFunctionB(x):
    a = 1+int((FranceProductionFunctionB(((x-GraphOneX)/GraphWidth)*FranceGraphOneWidth)/FranceGraphOneHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelFranceProductionFunctionC(x):
    a = 1+int((FranceProductionFunctionC(((x-GraphOneX)/GraphWidth)*FranceGraphOneWidth)/FranceGraphOneHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelFranceMarginalDisUtilityLabourFunction(x):
    a = 1+int((FranceMarginalDisUtilityLabourFunction(((x-GraphTwoX)/GraphWidth)*FranceGraphTwoWidth)/FranceGraphTwoHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelFranceMarginalUtilityFunctionA(x):
    a = 1+int((FranceMarginalUtilityFunctionA(((x-GraphThreeX)/GraphWidth)*FranceGraphThreeWidth)/FranceGraphThreeHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelFranceMarginalUtilityFunctionB(x):
    a = 1+int((FranceMarginalUtilityFunctionB(((x-GraphThreeX)/GraphWidth)*FranceGraphThreeWidth)/FranceGraphThreeHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a
def PixelFranceMarginalUtilityFunctionC(x):
    a = 1+int((FranceMarginalUtilityFunctionC(((x-GraphThreeX)/GraphWidth)*FranceGraphThreeWidth)/FranceGraphThreeHeight)*GraphHeight)
    if (a > GraphHeight):
        a = GraphHeight
    return a

#Germany Function Lists
while (len(GermanyProductionFunctionAList) < GraphWidth):
    GermanyProductionFunctionAList.append((GraphOneX+len(GermanyProductionFunctionAList),0))
while (len(GermanyProductionFunctionBList) < GraphWidth):
    GermanyProductionFunctionBList.append((GraphOneX+len(GermanyProductionFunctionBList),0))
while (len(GermanyProductionFunctionCList) < GraphWidth):
    GermanyProductionFunctionCList.append((GraphOneX+len(GermanyProductionFunctionCList),0))
while (len(GermanyMarginalDisUtilityLabourList) < GraphWidth):
    GermanyMarginalDisUtilityLabourList.append((GraphTwoX+len(GermanyMarginalDisUtilityLabourList),0))
while (len(GermanyMarginalUtilityAList) < GraphWidth):
    GermanyMarginalUtilityAList.append((GraphThreeX+len(GermanyMarginalUtilityAList),0))
while (len(GermanyMarginalUtilityBList) < GraphWidth):
    GermanyMarginalUtilityBList.append((GraphThreeX+len(GermanyMarginalUtilityBList),0))
while (len(GermanyMarginalUtilityCList) < GraphWidth):
    GermanyMarginalUtilityCList.append((GraphThreeX+len(GermanyMarginalUtilityCList),0))

#France Function Lists
while (len(FranceProductionFunctionAList) < GraphWidth):
    FranceProductionFunctionAList.append((GraphOneX+len(FranceProductionFunctionAList),0))
while (len(FranceProductionFunctionBList) < GraphWidth):
    FranceProductionFunctionBList.append((GraphOneX+len(FranceProductionFunctionBList),0))
while (len(FranceProductionFunctionCList) < GraphWidth):
    FranceProductionFunctionCList.append((GraphOneX+len(FranceProductionFunctionCList),0))
while (len(FranceMarginalDisUtilityLabourList) < GraphWidth):
    FranceMarginalDisUtilityLabourList.append((GraphTwoX+len(FranceMarginalDisUtilityLabourList),0))
while (len(FranceMarginalUtilityAList) < GraphWidth):
    FranceMarginalUtilityAList.append((GraphThreeX+len(FranceMarginalUtilityAList),0))
while (len(FranceMarginalUtilityBList) < GraphWidth):
    FranceMarginalUtilityBList.append((GraphThreeX+len(FranceMarginalUtilityBList),0))
while (len(FranceMarginalUtilityCList) < GraphWidth):
    FranceMarginalUtilityCList.append((GraphThreeX+len(FranceMarginalUtilityCList),0))

run = True
while run == True:

    MouseX, MouseY = pygame.mouse.get_pos()
    MouseLeft, MouseScroll, MouseRight = pygame.mouse.get_pressed()
    Mouse_RelX, Mouse_RelY = pygame.mouse.get_rel()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            run = False

        #Menu Button Click
        if (GermanyMenuButtonX < MouseX < GermanyMenuButtonX+GermanyMenuWidth) and (GermanyMenuButtonY < MouseY < GermanyMenuButtonY+GermanyMenuHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
            MenuSelection = "Germany"
        if (FranceMenuButtonX < MouseX < FranceMenuButtonX+FranceMenuButtonWidth) and (FranceMenuButtonY < MouseY < FranceMenuButtonY+FranceMenuButtonHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
            MenuSelection = "France"

        #Button Click
        if (PauseButtonX < MouseX < PauseButtonX+PauseButtonWidth) and (PauseButtonY < MouseY < PauseButtonY+PauseButtonHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
            if (PAUSE == True):
                PAUSE = False
            elif (PAUSE == False):
                PAUSE = True

        if (StepButtonX < MouseX < StepButtonX+StepButtonWidth) and (StepButtonY < MouseY < StepButtonY+StepButtonHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
            STEP = True

        if (SliderHitboxButtonX < MouseX < SliderHitboxButtonX+SliderHitboxButtonWidth) and (SliderHitboxButtonY < MouseY < SliderHitboxButtonY+SliderHitboxButtonHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
            if (ShowSliderHitbox == False):
                ShowSliderHitbox = True
            elif (ShowSliderHitbox == True):
                ShowSliderHitbox = False

        if (DebugWindowButtonX < MouseX < DebugWindowButtonX+DebugWindowButtonWidth) and (DebugWindowButtonY < MouseY < DebugWindowButtonY+DebugWindowButtonHeight) and (event.type == pygame.MOUSEBUTTONDOWN):
            if (DebugWindow == False):
                DebugWindow = True
            elif (DebugWindow == True):
                DebugWindow = False

        #keyboard shortcuts
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_p) and (PAUSE == True):
                PAUSE = False
            elif (event.key == pygame.K_p) and (PAUSE == False):
                PAUSE = True

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_s):
                STEP = True

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_d) and (DebugWindow == False):
                DebugWindow = True
            elif (event.key == pygame.K_d) and (DebugWindow == True):
                DebugWindow = False

        #Click on Slider
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderOneHitboxY < MouseY < SliderOneHitboxY + SliderHitboxHeight):
            SliderSelection = "One"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderTwoHitboxY < MouseY < SliderTwoHitboxY + SliderHitboxHeight):
            SliderSelection = "Two"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderThreeHitboxY < MouseY < SliderThreeHitboxY + SliderHitboxHeight):
            SliderSelection = "Three"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderFourHitboxY < MouseY < SliderFourHitboxY + SliderHitboxHeight):
            SliderSelection = "Four"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderFiveHitboxY < MouseY < SliderFiveHitboxY + SliderHitboxHeight):
            SliderSelection = "Five"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderSixHitboxY < MouseY < SliderSixHitboxY + SliderHitboxHeight):
            SliderSelection = "Six"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderSevenHitboxY < MouseY < SliderSevenHitboxY + SliderHitboxHeight):
            SliderSelection = "Seven"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderEightHitboxY < MouseY < SliderEightHitboxY + SliderHitboxHeight):
            SliderSelection = "Eight"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderNineHitboxY < MouseY < SliderNineHitboxY + SliderHitboxHeight):
            SliderSelection = "Nine"
        if (MouseOverDebugWindow == False) and (event.type == pygame.MOUSEBUTTONDOWN) and (SliderHitboxX < MouseX < SliderHitboxX + SliderHitboxWidth) and (SliderTenHitboxY < MouseY < SliderTenHitboxY + SliderHitboxHeight):
            SliderSelection = "Ten"

        #Click on debug window
        if (MouseOverDebugWindow == True) and (event.type == pygame.MOUSEBUTTONDOWN):
            MouseDragDebugWindow = True

        #Click Track Resolution
        if (event.type == pygame.MOUSEBUTTONUP):
            SliderSelection = "None"
            MouseDragDebugWindow = False

        #Mouse Over Graph
        MouseOverGraph = 0
        if ((MenuSelection == "Germany") or (MenuSelection == "France")) and (MouseOverDebugWindow == False):
            if (GraphOneX < MouseX < GraphOneX+GraphWidth) and (GraphOneY < MouseY < GraphOneY+GraphHeight):
                MouseOverGraph = 1
            if (GraphTwoX < MouseX < GraphTwoX+GraphWidth) and (GraphTwoY < MouseY < GraphTwoY+GraphHeight):
                MouseOverGraph = 2
            if (GraphThreeX < MouseX < GraphThreeX+GraphWidth) and (GraphThreeY < MouseY < GraphThreeY+GraphHeight):
                MouseOverGraph = 3
            if (GraphFourX < MouseX < GraphFourX+GraphWidth) and (GraphFourY < MouseY < GraphFourY+GraphHeight):
                MouseOverGraph = 4
            if (GraphSixX < MouseX < GraphSixX+GraphWidth) and (GraphSixY < MouseY < GraphSixY+GraphHeight):
                MouseOverGraph = 6
            if (GraphSevenX < MouseX < GraphSevenX+GraphWidth) and (GraphSevenY < MouseY < GraphSevenY+GraphHeight):
                MouseOverGraph = 7
            if (GraphNineX < MouseX < GraphNineX+GraphWidth) and (GraphNineY < MouseY < GraphNineY+GraphHeight):
                MouseOverGraph = 9
            if (GraphTenX < MouseX < GraphTenX+GraphWidth) and (GraphTenY < MouseY < GraphTenY+GraphHeight):
                MouseOverGraph = 10
            if (GraphElevenX < MouseX < GraphElevenX+GraphWidth) and (GraphElevenY < MouseY < GraphElevenY+GraphHeight):
                MouseOverGraph = 11
            if (GraphTwelveX < MouseX < GraphTwelveX+GraphWidth) and (GraphTwelveY < MouseY < GraphTwelveY+GraphHeight):
                MouseOverGraph = 12

        #Scroll Vertical Graph Scale Germany
        if (MenuSelection == "Germany") and (MouseOverGraph == 1) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphOneHeight += GraphOneHeightStepSize
                if (GermanyGraphOneHeight > GraphOneHeightMax):
                    GermanyGraphOneHeight = GraphOneHeightMax
            if event.button == 5:
                GermanyGraphOneHeight -= GraphOneHeightStepSize
                if (GermanyGraphOneHeight < GraphOneHeightMin):
                    GermanyGraphOneHeight = GraphOneHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 2) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphTwoHeight += GraphTwoHeightStepSize
                if (GermanyGraphTwoHeight > GraphTwoHeightMax):
                    GermanyGraphTwoHeight = GraphTwoHeightMax
            if event.button == 5:
                GermanyGraphTwoHeight -= GraphTwoHeightStepSize
                if (GermanyGraphTwoHeight < GraphTwoHeightMin):
                    GermanyGraphTwoHeight = GraphTwoHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 3) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphThreeHeight += GraphThreeHeightStepSize
                if (GermanyGraphThreeHeight > GraphThreeHeightMax):
                    GermanyGraphThreeHeight = GraphThreeHeightMax
            if event.button == 5:
                GermanyGraphThreeHeight -= GraphThreeHeightStepSize
                if (GermanyGraphThreeHeight < GraphThreeHeightMin):
                    GermanyGraphThreeHeight = GraphThreeHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 4) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphFourHeight += GraphFourHeightStepSize
                if (GermanyGraphFourHeight > GraphFourHeightMax):
                    GermanyGraphFourHeight = GraphFourHeightMax
            if event.button == 5:
                GermanyGraphFourHeight -= GraphFourHeightStepSize
                if (GermanyGraphFourHeight < GraphFourHeightMin):
                    GermanyGraphFourHeight = GraphFourHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 6) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphSixHeight += GraphSixHeightStepSize
                if (GermanyGraphSixHeight > GraphSixHeightMax):
                    GermanyGraphSixHeight = GraphSixHeightMax
            if event.button == 5:
                GermanyGraphSixHeight -= GraphSixHeightStepSize
                if (GermanyGraphSixHeight < GraphSixHeightMin):
                    GermanyGraphSixHeight = GraphSixHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 7) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphSevenHeight += GraphSevenHeightStepSize
                if (GermanyGraphSevenHeight > GraphSevenHeightMax):
                    GermanyGraphSevenHeight = GraphSevenHeightMax
            if event.button == 5:
                GermanyGraphSevenHeight -= GraphSevenHeightStepSize
                if (GermanyGraphSevenHeight < GraphSevenHeightMin):
                    GermanyGraphSevenHeight = GraphSevenHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 9) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphNineHeight += GraphNineHeightStepSize
                if (GermanyGraphNineHeight > GraphNineHeightMax):
                    GermanyGraphNineHeight = GraphNineHeightMax
            if event.button == 5:
                GermanyGraphNineHeight -= GraphNineHeightStepSize
                if (GermanyGraphNineHeight < GraphNineHeightMin):
                    GermanyGraphNineHeight = GraphNineHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 10) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphTenHeight += GraphTenHeightStepSize
                if (GermanyGraphTenHeight > GraphTenHeightMax):
                    GermanyGraphTenHeight = GraphTenHeightMax
            if event.button == 5:
                GermanyGraphTenHeight -= GraphTenHeightStepSize
                if (GermanyGraphTenHeight < GraphTenHeightMin):
                    GermanyGraphTenHeight = GraphTenHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 11) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphElevenHeight += GraphElevenHeightStepSize
                if (GermanyGraphElevenHeight > GraphElevenHeightMax):
                    GermanyGraphElevenHeight = GraphElevenHeightMax
            if event.button == 5:
                GermanyGraphElevenHeight -= GraphElevenHeightStepSize
                if (GermanyGraphElevenHeight < GraphElevenHeightMin):
                    GermanyGraphElevenHeight = GraphElevenHeightMin

        if (MenuSelection == "Germany") and (MouseOverGraph == 12) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                GermanyGraphTwelveHeight += GraphTwelveHeightStepSize
                if (GermanyGraphTwelveHeight > GraphTwelveHeightMax):
                    GermanyGraphTwelveHeight = GraphTwelveHeightMax
            if event.button == 5:
                GermanyGraphTwelveHeight -= GraphTwelveHeightStepSize
                if (GermanyGraphTwelveHeight < GraphTwelveHeightMin):
                    GermanyGraphTwelveHeight = GraphTwelveHeightMin

        #Scroll Vertical Graph Scale France
        if (MenuSelection == "France") and (MouseOverGraph == 1) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphOneHeight += GraphOneHeightStepSize
                if (FranceGraphOneHeight > GraphOneHeightMax):
                    FranceGraphOneHeight = GraphOneHeightMax
            if event.button == 5:
                FranceGraphOneHeight -= GraphOneHeightStepSize
                if (FranceGraphOneHeight < GraphOneHeightMin):
                    FranceGraphOneHeight = GraphOneHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 2) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphTwoHeight += GraphTwoHeightStepSize
                if (FranceGraphTwoHeight > GraphTwoHeightMax):
                    FranceGraphTwoHeight = GraphTwoHeightMax
            if event.button == 5:
                FranceGraphTwoHeight -= GraphTwoHeightStepSize
                if (FranceGraphTwoHeight < GraphTwoHeightMin):
                    FranceGraphTwoHeight = GraphTwoHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 3) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphThreeHeight += GraphThreeHeightStepSize
                if (FranceGraphThreeHeight > GraphThreeHeightMax):
                    FranceGraphThreeHeight = GraphThreeHeightMax
            if event.button == 5:
                FranceGraphThreeHeight -= GraphThreeHeightStepSize
                if (FranceGraphThreeHeight < GraphThreeHeightMin):
                    FranceGraphThreeHeight = GraphThreeHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 4) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphFourHeight += GraphFourHeightStepSize
                if (FranceGraphFourHeight > GraphFourHeightMax):
                    FranceGraphFourHeight = GraphFourHeightMax
            if event.button == 5:
                FranceGraphFourHeight -= GraphFourHeightStepSize
                if (FranceGraphFourHeight < GraphFourHeightMin):
                    FranceGraphFourHeight = GraphFourHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 6) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphSixHeight += GraphSixHeightStepSize
                if (FranceGraphSixHeight > GraphSixHeightMax):
                    FranceGraphSixHeight = GraphSixHeightMax
            if event.button == 5:
                FranceGraphSixHeight -= GraphSixHeightStepSize
                if (FranceGraphSixHeight < GraphSixHeightMin):
                    FranceGraphSixHeight = GraphSixHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 7) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphSevenHeight += GraphSevenHeightStepSize
                if (FranceGraphSevenHeight > GraphSevenHeightMax):
                    FranceGraphSevenHeight = GraphSevenHeightMax
            if event.button == 5:
                FranceGraphSevenHeight -= GraphSevenHeightStepSize
                if (FranceGraphSevenHeight < GraphSevenHeightMin):
                    FranceGraphSevenHeight = GraphSevenHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 9) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphNineHeight += GraphNineHeightStepSize
                if (FranceGraphNineHeight > GraphNineHeightMax):
                    FranceGraphNineHeight = GraphNineHeightMax
            if event.button == 5:
                FranceGraphNineHeight -= GraphNineHeightStepSize
                if (FranceGraphNineHeight < GraphNineHeightMin):
                    FranceGraphNineHeight = GraphNineHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 10) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphTenHeight += GraphTenHeightStepSize
                if (FranceGraphTenHeight > GraphTenHeightMax):
                    FranceGraphTenHeight = GraphTenHeightMax
            if event.button == 5:
                FranceGraphTenHeight -= GraphTenHeightStepSize
                if (FranceGraphTenHeight < GraphTenHeightMin):
                    FranceGraphTenHeight = GraphTenHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 11) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphElevenHeight += GraphElevenHeightStepSize
                if (FranceGraphElevenHeight > GraphElevenHeightMax):
                    FranceGraphElevenHeight = GraphElevenHeightMax
            if event.button == 5:
                FranceGraphElevenHeight -= GraphElevenHeightStepSize
                if (FranceGraphElevenHeight < GraphElevenHeightMin):
                    FranceGraphElevenHeight = GraphElevenHeightMin

        if (MenuSelection == "France") and (MouseOverGraph == 12) and (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 4:
                FranceGraphTwelveHeight += GraphTwelveHeightStepSize
                if (FranceGraphTwelveHeight > GraphTwelveHeightMax):
                    FranceGraphTwelveHeight = GraphTwelveHeightMax
            if event.button == 5:
                FranceGraphTwelveHeight -= GraphTwelveHeightStepSize
                if (FranceGraphTwelveHeight < GraphTwelveHeightMin):
                    FranceGraphTwelveHeight = GraphTwelveHeightMin

    if (PAUSE == False) or (STEP == True):
        #labour Allocation
        GermanyLabourA = GermanySupplyLabour * (GermanyLabourPercentA/Percent)
        GermanyLabourB = GermanySupplyLabour * (GermanyLabourPercentB/Percent)
        GermanyLabourC = GermanySupplyLabour * (GermanyLabourPercentC/Percent)

        FranceLabourA = FranceSupplyLabour * (FranceLabourPercentA/Percent)
        FranceLabourB = FranceSupplyLabour * (FranceLabourPercentB/Percent)
        FranceLabourC = FranceSupplyLabour * (FranceLabourPercentC/Percent)

        #supply
        GermanySupplyA = GermanyProductionFunctionA(GermanyLabourA)
        GermanySupplyB = GermanyProductionFunctionB(GermanyLabourB)
        GermanySupplyC = GermanyProductionFunctionC(GermanyLabourC)

        FranceSupplyA = FranceProductionFunctionA(FranceLabourA)
        FranceSupplyB = FranceProductionFunctionB(FranceLabourB)
        FranceSupplyC = FranceProductionFunctionC(FranceLabourC)

        #Money Demand
        GermanyMoneyDemandA = GermanyIncome * (GermanyBudgetPercentA/Percent)
        GermanyMoneyDemandB = GermanyIncome * (GermanyBudgetPercentB/Percent)
        GermanyMoneyDemandC = GermanyIncome * (GermanyBudgetPercentC/Percent)

        FranceMoneyDemandA = FranceIncome * (FranceBudgetPercentA/Percent)
        FranceMoneyDemandB = FranceIncome * (FranceBudgetPercentB/Percent)
        FranceMoneyDemandC = FranceIncome * (FranceBudgetPercentC/Percent)

        #money demand foreign domestic
        GermanyMoneyDemandForeignA = GermanyMoneyDemandA * (GermanyImportPercentA/ImportPercent)
        GermanyMoneyDemandForeignB = GermanyMoneyDemandB * (GermanyImportPercentB/ImportPercent)
        GermanyMoneyDemandForeignC = GermanyMoneyDemandC * (GermanyImportPercentC/ImportPercent)
        GermanyMoneyDemandDomesticA = GermanyMoneyDemandA * (GermanyDomesticPercentA/ImportPercent)
        GermanyMoneyDemandDomesticB = GermanyMoneyDemandB * (GermanyDomesticPercentB/ImportPercent)
        GermanyMoneyDemandDomesticC = GermanyMoneyDemandC * (GermanyDomesticPercentC/ImportPercent)

        FranceMoneyDemandForeignA = FranceMoneyDemandA * (FranceImportPercentA/ImportPercent)
        FranceMoneyDemandForeignB = FranceMoneyDemandB * (FranceImportPercentB/ImportPercent)
        FranceMoneyDemandForeignC = FranceMoneyDemandC * (FranceImportPercentC/ImportPercent)
        FranceMoneyDemandDomesticA = FranceMoneyDemandA * (FranceDomesticPercentA/ImportPercent)
        FranceMoneyDemandDomesticB = FranceMoneyDemandB * (FranceDomesticPercentB/ImportPercent)
        FranceMoneyDemandDomesticC = FranceMoneyDemandC * (FranceDomesticPercentC/ImportPercent)

        #money demand foreign -> money spent foreign & tariff revenue
        GermanyTariffRevenueA = GermanyMoneyDemandForeignA * (GermanyTariffRateA/(1+GermanyTariffRateA))
        GermanyMoneySpentForeignA = GermanyMoneyDemandForeignA - GermanyTariffRevenueA
        GermanyTariffRevenueB = GermanyMoneyDemandForeignB * (GermanyTariffRateB/(1+GermanyTariffRateB))
        GermanyMoneySpentForeignB = GermanyMoneyDemandForeignB - GermanyTariffRevenueB
        GermanyTariffRevenueC = GermanyMoneyDemandForeignC * (GermanyTariffRateC/(1+GermanyTariffRateC))
        GermanyMoneySpentForeignC = GermanyMoneyDemandForeignC - GermanyTariffRevenueC

        FranceTariffRevenueA = FranceMoneyDemandForeignA * (FranceTariffRateA/(1+FranceTariffRateA))
        FranceMoneySpentForeignA = FranceMoneyDemandForeignA - FranceTariffRevenueA
        FranceTariffRevenueB = FranceMoneyDemandForeignB * (FranceTariffRateB/(1+FranceTariffRateB))
        FranceMoneySpentForeignB = FranceMoneyDemandForeignB - FranceTariffRevenueB
        FranceTariffRevenueC = FranceMoneyDemandForeignC * (FranceTariffRateC/(1+FranceTariffRateC))
        FranceMoneySpentForeignC = FranceMoneyDemandForeignC - FranceTariffRevenueC

        #wage
        GermanyWageRate = GermanyIncome / GermanySupplyLabour
        FranceWageRate = FranceIncome / FranceSupplyLabour

        #prices
        GermanyPriceA = (GermanyMoneyDemandDomesticA + FranceMoneySpentForeignA) / GermanySupplyA
        GermanyPriceB = (GermanyMoneyDemandDomesticB + FranceMoneySpentForeignB) / GermanySupplyB
        GermanyPriceC = (GermanyMoneyDemandDomesticC + FranceMoneySpentForeignC) / GermanySupplyC

        FrancePriceA = (FranceMoneyDemandDomesticA + GermanyMoneySpentForeignA) / FranceSupplyA
        FrancePriceB = (FranceMoneyDemandDomesticB + GermanyMoneySpentForeignB) / FranceSupplyB
        FrancePriceC = (FranceMoneyDemandDomesticC + GermanyMoneySpentForeignC) / FranceSupplyC

        #Tariff Adjusted Prices
        TARIFF_GermanyPriceA = GermanyPriceA * (1+FranceTariffRateA)
        TARIFF_GermanyPriceB = GermanyPriceB * (1+FranceTariffRateB)
        TARIFF_GermanyPriceC = GermanyPriceC * (1+FranceTariffRateC)

        TARIFF_FrancePriceA = FrancePriceA * (1+GermanyTariffRateA)
        TARIFF_FrancePriceB = FrancePriceB * (1+GermanyTariffRateB)
        TARIFF_FrancePriceC = FrancePriceC * (1+GermanyTariffRateC)

        #Anticipated Demand
        GermanyAnticipatedDemandA = (GermanyMoneyDemandDomesticA/GermanyPriceA) + (GermanyMoneyDemandForeignA/TARIFF_FrancePriceA)
        GermanyAnticipatedDemandB = (GermanyMoneyDemandDomesticB/GermanyPriceB) + (GermanyMoneyDemandForeignB/TARIFF_FrancePriceB)
        GermanyAnticipatedDemandC = (GermanyMoneyDemandDomesticC/GermanyPriceC) + (GermanyMoneyDemandForeignC/TARIFF_FrancePriceC)

        FranceAnticipatedDemandA = (FranceMoneyDemandDomesticA/FrancePriceA) + (FranceMoneyDemandForeignA/TARIFF_GermanyPriceA)
        FranceAnticipatedDemandB = (FranceMoneyDemandDomesticB/FrancePriceB) + (FranceMoneyDemandForeignB/TARIFF_GermanyPriceB)
        FranceAnticipatedDemandC = (FranceMoneyDemandDomesticC/FrancePriceC) + (FranceMoneyDemandForeignC/TARIFF_GermanyPriceC)

        #MUΔ$ABC (use lowest global prices)
        GermanyMarginalUtilityMoneySpentA = GermanyMarginalUtilityFunctionA(GermanyAnticipatedDemandA) / min(GermanyPriceA,TARIFF_FrancePriceA)
        GermanyMarginalUtilityMoneySpentB = GermanyMarginalUtilityFunctionB(GermanyAnticipatedDemandB) / min(GermanyPriceB,TARIFF_FrancePriceB)
        GermanyMarginalUtilityMoneySpentC = GermanyMarginalUtilityFunctionC(GermanyAnticipatedDemandC) / min(GermanyPriceC,TARIFF_FrancePriceC)

        FranceMarginalUtilityMoneySpentA = FranceMarginalUtilityFunctionA(FranceAnticipatedDemandA) / min(TARIFF_GermanyPriceA,FrancePriceA)
        FranceMarginalUtilityMoneySpentB = FranceMarginalUtilityFunctionB(FranceAnticipatedDemandB) / min(TARIFF_GermanyPriceB,FrancePriceB)
        FranceMarginalUtilityMoneySpentC = FranceMarginalUtilityFunctionC(FranceAnticipatedDemandC) / min(TARIFF_GermanyPriceC,FrancePriceC)

        #MDUΔ$
        GermanyMarginalDisUtilityMoneyEarned = GermanyMarginalDisUtilityLabourFunction(GermanySupplyLabour) / GermanyWageRate
        FranceMarginalDisUtilityMoneyEarned = FranceMarginalDisUtilityLabourFunction(FranceSupplyLabour) / FranceWageRate

        #ΔQABC * PABC
        GermanyMarginalValueProductionA = (GermanyProductionFunctionA(GermanyLabourA + MarginalLabour) - GermanyProductionFunctionA(GermanyLabourA)) * GermanyPriceA
        GermanyMarginalValueProductionB = (GermanyProductionFunctionB(GermanyLabourB + MarginalLabour) - GermanyProductionFunctionB(GermanyLabourB)) * GermanyPriceB
        GermanyMarginalValueProductionC = (GermanyProductionFunctionC(GermanyLabourC + MarginalLabour) - GermanyProductionFunctionC(GermanyLabourC)) * GermanyPriceC

        FranceMarginalValueProductionA = (FranceProductionFunctionA(FranceLabourA + MarginalLabour) - FranceProductionFunctionA(FranceLabourA)) * FrancePriceA
        FranceMarginalValueProductionB = (FranceProductionFunctionB(FranceLabourB + MarginalLabour) - FranceProductionFunctionB(FranceLabourB)) * FrancePriceB
        FranceMarginalValueProductionC = (FranceProductionFunctionC(FranceLabourC + MarginalLabour) - FranceProductionFunctionC(FranceLabourC)) * FrancePriceC

        #adjust budget
        if (max(GermanyMarginalUtilityMoneySpentA,GermanyMarginalUtilityMoneySpentB,GermanyMarginalUtilityMoneySpentC) == GermanyMarginalUtilityMoneySpentA):
            GermanyBudgetPercentA,GermanyBudgetPercentB,GermanyBudgetPercentC = IncrementPercentage(GermanyBudgetPercentA,GermanyBudgetPercentB,GermanyBudgetPercentC)

        if (max(GermanyMarginalUtilityMoneySpentA,GermanyMarginalUtilityMoneySpentB,GermanyMarginalUtilityMoneySpentC) == GermanyMarginalUtilityMoneySpentB):
            GermanyBudgetPercentB,GermanyBudgetPercentA,GermanyBudgetPercentC = IncrementPercentage(GermanyBudgetPercentB,GermanyBudgetPercentA,GermanyBudgetPercentC)

        if (max(GermanyMarginalUtilityMoneySpentA,GermanyMarginalUtilityMoneySpentB,GermanyMarginalUtilityMoneySpentC) == GermanyMarginalUtilityMoneySpentC):
            GermanyBudgetPercentC,GermanyBudgetPercentB,GermanyBudgetPercentA = IncrementPercentage(GermanyBudgetPercentC,GermanyBudgetPercentB,GermanyBudgetPercentA)

        if (max(FranceMarginalUtilityMoneySpentA,FranceMarginalUtilityMoneySpentB,FranceMarginalUtilityMoneySpentC) == FranceMarginalUtilityMoneySpentA):
            FranceBudgetPercentA,FranceBudgetPercentB,FranceBudgetPercentC = IncrementPercentage(FranceBudgetPercentA,FranceBudgetPercentB,FranceBudgetPercentC)

        if (max(FranceMarginalUtilityMoneySpentA,FranceMarginalUtilityMoneySpentB,FranceMarginalUtilityMoneySpentC) == FranceMarginalUtilityMoneySpentB):
            FranceBudgetPercentB,FranceBudgetPercentA,FranceBudgetPercentC = IncrementPercentage(FranceBudgetPercentB,FranceBudgetPercentA,FranceBudgetPercentC)

        if (max(FranceMarginalUtilityMoneySpentA,FranceMarginalUtilityMoneySpentB,FranceMarginalUtilityMoneySpentC) == FranceMarginalUtilityMoneySpentC):
            FranceBudgetPercentC,FranceBudgetPercentB,FranceBudgetPercentA = IncrementPercentage(FranceBudgetPercentC,FranceBudgetPercentB,FranceBudgetPercentA)

        #adjust import & domestic

                #GERMANY

            #if france is cheaper
        if (GermanyPriceA > TARIFF_FrancePriceA):
            GermanyImportPercentA,GermanyDomesticPercentA = IncrementTwo(GermanyImportPercentA,GermanyDomesticPercentA)
        if (GermanyPriceB > TARIFF_FrancePriceB):
            GermanyImportPercentB,GermanyDomesticPercentB = IncrementTwo(GermanyImportPercentB,GermanyDomesticPercentB)
        if (GermanyPriceC > TARIFF_FrancePriceC):
            GermanyImportPercentC,GermanyDomesticPercentC = IncrementTwo(GermanyImportPercentC,GermanyDomesticPercentC)

            #if germany is cheaper
        if (GermanyPriceA < TARIFF_FrancePriceA):
            GermanyDomesticPercentA,GermanyImportPercentA = IncrementTwo(GermanyDomesticPercentA,GermanyImportPercentA)
        if (GermanyPriceB < TARIFF_FrancePriceB):
            GermanyDomesticPercentB,GermanyImportPercentB = IncrementTwo(GermanyDomesticPercentB,GermanyImportPercentB)
        if (GermanyPriceC < TARIFF_FrancePriceC):
            GermanyDomesticPercentC,GermanyImportPercentC = IncrementTwo(GermanyDomesticPercentC,GermanyImportPercentC)

                #FRANCE

            #if france is cheaper
        if (TARIFF_GermanyPriceA > FrancePriceA):
            FranceDomesticPercentA,FranceImportPercentA = IncrementTwo(FranceDomesticPercentA,FranceImportPercentA)
        if (TARIFF_GermanyPriceB > FrancePriceB):
            FranceDomesticPercentB,FranceImportPercentB = IncrementTwo(FranceDomesticPercentB,FranceImportPercentB)
        if (TARIFF_GermanyPriceC > FrancePriceC):
            FranceDomesticPercentC,FranceImportPercentC = IncrementTwo(FranceDomesticPercentC,FranceImportPercentC)

            #if germany is cheaper
        if (TARIFF_GermanyPriceA < FrancePriceA):
            FranceImportPercentA,FranceDomesticPercentA = IncrementTwo(FranceImportPercentA,FranceDomesticPercentA)
        if (TARIFF_GermanyPriceB < FrancePriceB):
            FranceImportPercentB,FranceDomesticPercentB = IncrementTwo(FranceImportPercentB,FranceDomesticPercentB)
        if (TARIFF_GermanyPriceC < FrancePriceC):
            FranceImportPercentC,FranceDomesticPercentC = IncrementTwo(FranceImportPercentC,FranceDomesticPercentC)

        #adjust supply labour
        if (GermanyMarginalDisUtilityMoneyEarned > max(GermanyMarginalUtilityMoneySpentA,GermanyMarginalUtilityMoneySpentB,GermanyMarginalUtilityMoneySpentC)):
            GermanySupplyLabour = GermanySupplyLabour / RateChangeSupplyLabour
        if (GermanyMarginalDisUtilityMoneyEarned < max(GermanyMarginalUtilityMoneySpentA,GermanyMarginalUtilityMoneySpentB,GermanyMarginalUtilityMoneySpentC)):
            GermanySupplyLabour = GermanySupplyLabour * RateChangeSupplyLabour

        if (FranceMarginalDisUtilityMoneyEarned > max(FranceMarginalUtilityMoneySpentA,FranceMarginalUtilityMoneySpentB,FranceMarginalUtilityMoneySpentC)):
            FranceSupplyLabour = FranceSupplyLabour / RateChangeSupplyLabour
        if (FranceMarginalDisUtilityMoneyEarned < max(FranceMarginalUtilityMoneySpentA,FranceMarginalUtilityMoneySpentB,FranceMarginalUtilityMoneySpentC)):
            FranceSupplyLabour = FranceSupplyLabour * RateChangeSupplyLabour

        #adjust labour allocation
        if (max(GermanyMarginalValueProductionA,GermanyMarginalValueProductionB,GermanyMarginalValueProductionC) == GermanyMarginalValueProductionA):
            GermanyLabourPercentA,GermanyLabourPercentB,GermanyLabourPercentC = IncrementPercentage(GermanyLabourPercentA,GermanyLabourPercentB,GermanyLabourPercentC)

        if (max(GermanyMarginalValueProductionA,GermanyMarginalValueProductionB,GermanyMarginalValueProductionC) == GermanyMarginalValueProductionB):
            GermanyLabourPercentB,GermanyLabourPercentA,GermanyLabourPercentC = IncrementPercentage(GermanyLabourPercentB,GermanyLabourPercentA,GermanyLabourPercentC)

        if (max(GermanyMarginalValueProductionA,GermanyMarginalValueProductionB,GermanyMarginalValueProductionC) == GermanyMarginalValueProductionC):
            GermanyLabourPercentC,GermanyLabourPercentB,GermanyLabourPercentA = IncrementPercentage(GermanyLabourPercentC,GermanyLabourPercentB,GermanyLabourPercentA)


        if (max(FranceMarginalValueProductionA,FranceMarginalValueProductionB,FranceMarginalValueProductionC) == FranceMarginalValueProductionA):
            FranceLabourPercentA,FranceLabourPercentB,FranceLabourPercentC = IncrementPercentage(FranceLabourPercentA,FranceLabourPercentB,FranceLabourPercentC)

        if (max(FranceMarginalValueProductionA,FranceMarginalValueProductionB,FranceMarginalValueProductionC) == FranceMarginalValueProductionB):
            FranceLabourPercentB,FranceLabourPercentA,FranceLabourPercentC = IncrementPercentage(FranceLabourPercentB,FranceLabourPercentA,FranceLabourPercentC)

        if (max(FranceMarginalValueProductionA,FranceMarginalValueProductionB,FranceMarginalValueProductionC) == FranceMarginalValueProductionC):
            FranceLabourPercentC,FranceLabourPercentB,FranceLabourPercentA = IncrementPercentage(FranceLabourPercentC,FranceLabourPercentB,FranceLabourPercentA)

        #income of the various markets
        GermanyMarketIncomeA = GermanyMoneyDemandDomesticA + FranceMoneySpentForeignA
        GermanyMarketIncomeB = GermanyMoneyDemandDomesticB + FranceMoneySpentForeignB
        GermanyMarketIncomeC = GermanyMoneyDemandDomesticC + FranceMoneySpentForeignC

        FranceMarketIncomeA = FranceMoneyDemandDomesticA + GermanyMoneySpentForeignA
        FranceMarketIncomeB = FranceMoneyDemandDomesticB + GermanyMoneySpentForeignB
        FranceMarketIncomeC = FranceMoneyDemandDomesticC + GermanyMoneySpentForeignC

        #National Income
        GermanyIncome = GermanyMarketIncomeA + GermanyMarketIncomeB + GermanyMarketIncomeC + GermanyTariffRevenueA + GermanyTariffRevenueB + GermanyTariffRevenueC
        FranceIncome = FranceMarketIncomeA + FranceMarketIncomeB + FranceMarketIncomeC + FranceTariffRevenueA + FranceTariffRevenueB + FranceTariffRevenueC

    #Check Mouse over Debug Window
    MouseOverDebugWindow = False
    if (DebugWindowX < MouseX < DebugWindowX+DebugWindowWidth) and (DebugWindowY < MouseY < DebugWindowY+DebugWindowHeight) and (DebugWindow == True):
        MouseOverDebugWindow = True

    if (MouseDragDebugWindow == True):
        DebugWindowX += Mouse_RelX
        DebugWindowY += Mouse_RelY

    #check for mouse over buttons
    ButtonMouseOver = "None"
    if (PauseButtonX < MouseX < PauseButtonX+PauseButtonWidth) and (PauseButtonY < MouseY < PauseButtonY+PauseButtonHeight) and ((MenuSelection == "France") or (MenuSelection == "Germany")):
        ButtonMouseOver = "Pause"
    if (StepButtonX < MouseX < StepButtonX+StepButtonWidth) and (StepButtonY < MouseY < StepButtonY+StepButtonHeight) and ((MenuSelection == "France") or (MenuSelection == "Germany")):
        ButtonMouseOver = "Step"
    if (SliderHitboxButtonX < MouseX < SliderHitboxButtonX+SliderHitboxButtonWidth) and (SliderHitboxButtonY < MouseY < SliderHitboxButtonY+SliderHitboxButtonHeight) and ((MenuSelection == "France") or (MenuSelection == "Germany")):
        ButtonMouseOver = "SliderHitbox"
    if (DebugWindowButtonX < MouseX < DebugWindowButtonX+DebugWindowButtonWidth) and (DebugWindowButtonY < MouseY < DebugWindowButtonY+DebugWindowButtonHeight) and ((MenuSelection == "France") or (MenuSelection == "Germany")):
        ButtonMouseOver = "DebugWindow"

    #Move Slider Bar When Click and Drag
    if (MenuSelection == "Germany") and (SliderSelection == "One"):
        GermanySliderDotOneX = MouseX
        if (GermanySliderDotOneX < SliderX):
            GermanySliderDotOneX = SliderX
        if (GermanySliderDotOneX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotOneX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Two"):
        GermanySliderDotTwoX = MouseX
        if (GermanySliderDotTwoX < SliderX):
            GermanySliderDotTwoX = SliderX
        if (GermanySliderDotTwoX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotTwoX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Three"):
        GermanySliderDotThreeX = MouseX
        if (GermanySliderDotThreeX < SliderX):
            GermanySliderDotThreeX = SliderX
        if (GermanySliderDotThreeX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotThreeX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Four"):
        GermanySliderDotFourX = MouseX
        if (GermanySliderDotFourX < SliderX):
            GermanySliderDotFourX = SliderX
        if (GermanySliderDotFourX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotFourX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Five"):
        GermanySliderDotFiveX = MouseX
        if (GermanySliderDotFiveX < SliderX):
            GermanySliderDotFiveX = SliderX
        if (GermanySliderDotFiveX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotFiveX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Six"):
        GermanySliderDotSixX = MouseX
        if (GermanySliderDotSixX < SliderX):
            GermanySliderDotSixX = SliderX
        if (GermanySliderDotSixX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotSixX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Seven"):
        GermanySliderDotSevenX = MouseX
        if (GermanySliderDotSevenX < SliderX):
            GermanySliderDotSevenX = SliderX
        if (GermanySliderDotSevenX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotSevenX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Eight"):
        GermanySliderDotEightX = MouseX
        if (GermanySliderDotEightX < SliderX):
            GermanySliderDotEightX = SliderX
        if (GermanySliderDotEightX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotEightX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Nine"):
        GermanySliderDotNineX = MouseX
        if (GermanySliderDotNineX < SliderX):
            GermanySliderDotNineX = SliderX
        if (GermanySliderDotNineX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotNineX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Ten"):
        GermanySliderDotTenX = MouseX
        if (GermanySliderDotTenX < SliderX):
            GermanySliderDotTenX = SliderX
        if (GermanySliderDotTenX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotTenX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Eleven"):
        GermanySliderDotElevenX = MouseX
        if (GermanySliderDotElevenX < SliderX):
            GermanySliderDotElevenX = SliderX
        if (GermanySliderDotElevenX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotElevenX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Twelve"):
        GermanySliderDotTwelveX = MouseX
        if (GermanySliderDotTwelveX < SliderX):
            GermanySliderDotTwelveX = SliderX
        if (GermanySliderDotTwelveX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotTwelveX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "Germany") and (SliderSelection == "Thirteen"):
        GermanySliderDotThirteenX = MouseX
        if (GermanySliderDotThirteenX < SliderX):
            GermanySliderDotThirteenX = SliderX
        if (GermanySliderDotThirteenX > SliderX+SliderWidth-SliderThickness):
            GermanySliderDotThirteenX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "One"):
        FranceSliderDotOneX = MouseX
        if (FranceSliderDotOneX < SliderX):
            FranceSliderDotOneX = SliderX
        if (FranceSliderDotOneX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotOneX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Two"):
        FranceSliderDotTwoX = MouseX
        if (FranceSliderDotTwoX < SliderX):
            FranceSliderDotTwoX = SliderX
        if (FranceSliderDotTwoX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotTwoX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Three"):
        FranceSliderDotThreeX = MouseX
        if (FranceSliderDotThreeX < SliderX):
            FranceSliderDotThreeX = SliderX
        if (FranceSliderDotThreeX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotThreeX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Four"):
        FranceSliderDotFourX = MouseX
        if (FranceSliderDotFourX < SliderX):
            FranceSliderDotFourX = SliderX
        if (FranceSliderDotFourX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotFourX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Five"):
        FranceSliderDotFiveX = MouseX
        if (FranceSliderDotFiveX < SliderX):
            FranceSliderDotFiveX = SliderX
        if (FranceSliderDotFiveX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotFiveX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Six"):
        FranceSliderDotSixX = MouseX
        if (FranceSliderDotSixX < SliderX):
            FranceSliderDotSixX = SliderX
        if (FranceSliderDotSixX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotSixX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Seven"):
        FranceSliderDotSevenX = MouseX
        if (FranceSliderDotSevenX < SliderX):
            FranceSliderDotSevenX = SliderX
        if (FranceSliderDotSevenX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotSevenX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Eight"):
        FranceSliderDotEightX = MouseX
        if (FranceSliderDotEightX < SliderX):
            FranceSliderDotEightX = SliderX
        if (FranceSliderDotEightX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotEightX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Nine"):
        FranceSliderDotNineX = MouseX
        if (FranceSliderDotNineX < SliderX):
            FranceSliderDotNineX = SliderX
        if (FranceSliderDotNineX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotNineX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Ten"):
        FranceSliderDotTenX = MouseX
        if (FranceSliderDotTenX < SliderX):
            FranceSliderDotTenX = SliderX
        if (FranceSliderDotTenX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotTenX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Eleven"):
        FranceSliderDotElevenX = MouseX
        if (FranceSliderDotElevenX < SliderX):
            FranceSliderDotElevenX = SliderX
        if (FranceSliderDotElevenX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotElevenX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Twelve"):
        FranceSliderDotTwelveX = MouseX
        if (FranceSliderDotTwelveX < SliderX):
            FranceSliderDotTwelveX = SliderX
        if (FranceSliderDotTwelveX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotTwelveX = SliderX+SliderWidth-SliderThickness

    if (MenuSelection == "France") and (SliderSelection == "Thirteen"):
        FranceSliderDotThirteenX = MouseX
        if (FranceSliderDotThirteenX < SliderX):
            FranceSliderDotThirteenX = SliderX
        if (FranceSliderDotThirteenX > SliderX+SliderWidth-SliderThickness):
            FranceSliderDotThirteenX = SliderX+SliderWidth-SliderThickness

    #Mouse Over
    MouseOver = "None"
    if (GermanyMenuButtonX < MouseX < GermanyMenuButtonX+GermanyMenuWidth) and (GermanyMenuButtonY < MouseY < GermanyMenuButtonY+GermanyMenuHeight):
        MouseOver = "GermanyMenuButton"
    if (FranceMenuButtonX < MouseX < FranceMenuButtonX+FranceMenuButtonWidth) and (FranceMenuButtonY < MouseY < FranceMenuButtonY+FranceMenuButtonHeight):
        MouseOver = "FranceMenuButton"

    #Fluid Variable Text
    if (MenuSelection == "Germany"):
        VariableSupplyA_TEXT = font1.render(str(round(GermanySupplyA,2)), 1, Blue)
        VariableSupplyB_TEXT = font1.render(str(round(GermanySupplyB,2)), 1, Red)
        VariableSupplyC_TEXT = font1.render(str(round(GermanySupplyC,2)), 1, Green)
        VariablePriceA_TEXT = font1.render("$"+str(round(GermanyPriceA)), 1, Blue)
        VariablePriceB_TEXT = font1.render("$"+str(round(GermanyPriceB)), 1, Red)
        VariablePriceC_TEXT = font1.render("$"+str(round(GermanyPriceC)), 1, Green)
        VariableSupplyLabour_TEXT = font1.render(str(round(GermanySupplyLabour,2)), 1, White)
        VariableIncome_TEXT = font1.render("Income $"+str(round(GermanyIncome)), 1, White)
        VariableTotalExports_TEXT = font1.render("$"+str(round(FranceMoneySpentForeignA+FranceMoneySpentForeignB+FranceMoneySpentForeignC)), 1, White)
        VariableExportsA = font1.render("$"+str(round(FranceMoneySpentForeignA)), 1, Blue)
        VariableExportsB = font1.render("$"+str(round(FranceMoneySpentForeignB)), 1, Red)
        VariableExportsC = font1.render("$"+str(round(FranceMoneySpentForeignC)), 1, Green)
        VariableTotalImports_TEXT = font1.render("$"+str(round(GermanyMoneySpentForeignA+GermanyMoneySpentForeignB+GermanyMoneySpentForeignC)), 1, White)
        VariableImportsA = font1.render("$"+str(round(GermanyMoneySpentForeignA)), 1, Blue)
        VariableImportsB = font1.render("$"+str(round(GermanyMoneySpentForeignB)), 1, Red)
        VariableImportsC = font1.render("$"+str(round(GermanyMoneySpentForeignC)), 1, Green)
        VariableWageRate = font1.render("$"+str(round(GermanyWageRate)), 1, White)
        VariableMUSpendMoneyA = font1.render(str(round(GermanyMarginalUtilityMoneySpentA,5)), 1, Blue)
        VariableMUSpendMoneyB = font1.render(str(round(GermanyMarginalUtilityMoneySpentB,5)), 1, Red)
        VariableMUSpendMoneyC = font1.render(str(round(GermanyMarginalUtilityMoneySpentC,5)), 1, Green)
        VariableMDUEarnMoney = font1.render(str(round(GermanyMarginalDisUtilityMoneyEarned,5)), 1, Gold)
        VariableMVPA_TEXT = font1.render("$"+str(round(GermanyMarginalValueProductionA,2)), 1, Blue)
        VariableMVPB_TEXT = font1.render("$"+str(round(GermanyMarginalValueProductionA,2)), 1, Red)
        VariableMVPC_TEXT = font1.render("$"+str(round(GermanyMarginalValueProductionA,2)), 1, Green)
        LabourPercentA_Text = font1.render("%"+str(round(GermanyLabourPercentA,2)), 1, Blue)
        LabourPercentB_Text = font1.render("%"+str(round(GermanyLabourPercentB,2)), 1, Red)
        LabourPercentC_Text = font1.render("%"+str(round(GermanyLabourPercentC,2)), 1, Green)
        BudgetPercentA_Text = font1.render("%"+str(round(GermanyBudgetPercentA,2)), 1, Blue)
        BudgetPercentB_Text = font1.render("%"+str(round(GermanyBudgetPercentB,2)), 1, Red)
        BudgetPercentC_Text = font1.render("%"+str(round(GermanyBudgetPercentC,2)), 1, Green)

    if (MenuSelection == "France"):
        VariableSupplyA_TEXT = font1.render(str(round(FranceSupplyA,2)), 1, Blue)
        VariableSupplyB_TEXT = font1.render(str(round(FranceSupplyB,2)), 1, Red)
        VariableSupplyC_TEXT = font1.render(str(round(FranceSupplyC,2)), 1, Green)
        VariablePriceA_TEXT = font1.render("$"+str(round(FrancePriceA)), 1, Blue)
        VariablePriceB_TEXT = font1.render("$"+str(round(FrancePriceB)), 1, Red)
        VariablePriceC_TEXT = font1.render("$"+str(round(FrancePriceC)), 1, Green)
        VariableSupplyLabour_TEXT = font1.render(str(round(FranceSupplyLabour,2)), 1, White)
        VariableIncome_TEXT = font1.render("Income $"+str(round(FranceIncome)), 1, White)
        VariableTotalExports_TEXT = font1.render("$"+str(round(GermanyMoneySpentForeignA+GermanyMoneySpentForeignB+GermanyMoneySpentForeignC)), 1, White)
        VariableExportsA = font1.render("$"+str(round(GermanyMoneySpentForeignA)), 1, Blue)
        VariableExportsB = font1.render("$"+str(round(GermanyMoneySpentForeignB)), 1, Red)
        VariableExportsC = font1.render("$"+str(round(GermanyMoneySpentForeignC)), 1, Green)
        VariableTotalImports_TEXT = font1.render("$"+str(round(FranceMoneySpentForeignA+FranceMoneySpentForeignB+FranceMoneySpentForeignC)), 1, White)
        VariableImportsA = font1.render("$"+str(round(FranceMoneySpentForeignA)), 1, Blue)
        VariableImportsB = font1.render("$"+str(round(FranceMoneySpentForeignB)), 1, Red)
        VariableImportsC = font1.render("$"+str(round(FranceMoneySpentForeignC)), 1, Green)
        VariableWageRate = font1.render("$"+str(round(FranceWageRate)), 1, White)
        VariableMUSpendMoneyA = font1.render(str(round(FranceMarginalUtilityMoneySpentA,5)), 1, Blue)
        VariableMUSpendMoneyB = font1.render(str(round(FranceMarginalUtilityMoneySpentB,5)), 1, Red)
        VariableMUSpendMoneyC = font1.render(str(round(FranceMarginalUtilityMoneySpentC,5)), 1, Green)
        VariableMDUEarnMoney = font1.render(str(round(FranceMarginalDisUtilityMoneyEarned,5)), 1, Gold)
        VariableMVPA_TEXT = font1.render("$"+str(round(FranceMarginalValueProductionA,2)), 1, Blue)
        VariableMVPB_TEXT = font1.render("$"+str(round(FranceMarginalValueProductionA,2)), 1, Red)
        VariableMVPC_TEXT = font1.render("$"+str(round(FranceMarginalValueProductionA,2)), 1, Green)
        LabourPercentA_Text = font1.render("%"+str(round(FranceLabourPercentA,2)), 1, Blue)
        LabourPercentB_Text = font1.render("%"+str(round(FranceLabourPercentB,2)), 1, Red)
        LabourPercentC_Text = font1.render("%"+str(round(FranceLabourPercentC,2)), 1, Green)
        BudgetPercentA_Text = font1.render("%"+str(round(FranceBudgetPercentA,2)), 1, Blue)
        BudgetPercentB_Text = font1.render("%"+str(round(FranceBudgetPercentB,2)), 1, Red)
        BudgetPercentC_Text = font1.render("%"+str(round(FranceBudgetPercentC,2)), 1, Green)

    #Fluid Label Text
    if (MenuSelection == "Germany"):
        #Vertical
        GraphOneHeightLabel0_TEXT = font2.render(str(round(GermanyGraphOneHeight)), 1, Dark_Gray1)
        GraphOneHeightLabel1_TEXT = font2.render(str(round(GermanyGraphOneHeight*(1/4))), 1, Dark_Gray1)
        GraphOneHeightLabel2_TEXT = font2.render(str(round(GermanyGraphOneHeight*(2/4))), 1, Dark_Gray1)
        GraphOneHeightLabel3_TEXT = font2.render(str(round(GermanyGraphOneHeight*(3/4))), 1, Dark_Gray1)
        GraphTwoHeightLabel0_TEXT = font2.render(str(round(GermanyGraphTwoHeight)), 1, Dark_Gray1)
        GraphTwoHeightLabel1_TEXT = font2.render(str(round(GermanyGraphTwoHeight*(1/4))), 1, Dark_Gray1)
        GraphTwoHeightLabel2_TEXT = font2.render(str(round(GermanyGraphTwoHeight*(2/4))), 1, Dark_Gray1)
        GraphTwoHeightLabel3_TEXT = font2.render(str(round(GermanyGraphTwoHeight*(3/4))), 1, Dark_Gray1)
        GraphThreeHeightLabel0_TEXT = font2.render(str(round(GermanyGraphThreeHeight)), 1, Dark_Gray1)
        GraphThreeHeightLabel1_TEXT = font2.render(str(round(GermanyGraphThreeHeight*(1/4))), 1, Dark_Gray1)
        GraphThreeHeightLabel2_TEXT = font2.render(str(round(GermanyGraphThreeHeight*(2/4))), 1, Dark_Gray1)
        GraphThreeHeightLabel3_TEXT = font2.render(str(round(GermanyGraphThreeHeight*(3/4))), 1, Dark_Gray1)
        GraphFourHeightLabel0_TEXT = font2.render(str(round(GermanyGraphFourHeight)), 1, Dark_Gray1)
        GraphFourHeightLabel1_TEXT = font2.render(str(round(GermanyGraphFourHeight*(1/4))), 1, Dark_Gray1)
        GraphFourHeightLabel2_TEXT = font2.render(str(round(GermanyGraphFourHeight*(2/4))), 1, Dark_Gray1)
        GraphFourHeightLabel3_TEXT = font2.render(str(round(GermanyGraphFourHeight*(3/4))), 1, Dark_Gray1)
        GraphSixHeightLabel0_TEXT = font2.render(str(round(GermanyGraphSixHeight)), 1, Dark_Gray1)
        GraphSixHeightLabel1_TEXT = font2.render(str(round(GermanyGraphSixHeight*(1/4))), 1, Dark_Gray1)
        GraphSixHeightLabel2_TEXT = font2.render(str(round(GermanyGraphSixHeight*(2/4))), 1, Dark_Gray1)
        GraphSixHeightLabel3_TEXT = font2.render(str(round(GermanyGraphSixHeight*(3/4))), 1, Dark_Gray1)
        GraphSevenHeightLabel0_TEXT = font2.render(str(round(GermanyGraphSevenHeight)), 1, Dark_Gray1)
        GraphSevenHeightLabel1_TEXT = font2.render(str(round(GermanyGraphSevenHeight*(1/4))), 1, Dark_Gray1)
        GraphSevenHeightLabel2_TEXT = font2.render(str(round(GermanyGraphSevenHeight*(2/4))), 1, Dark_Gray1)
        GraphSevenHeightLabel3_TEXT = font2.render(str(round(GermanyGraphSevenHeight*(3/4))), 1, Dark_Gray1)
        GraphNineHeightLabel0_TEXT = font2.render(str(round(GermanyGraphNineHeight)), 1, Dark_Gray1)
        GraphNineHeightLabel1_TEXT = font2.render(str(round(GermanyGraphNineHeight*(1/4))), 1, Dark_Gray1)
        GraphNineHeightLabel2_TEXT = font2.render(str(round(GermanyGraphNineHeight*(2/4))), 1, Dark_Gray1)
        GraphNineHeightLabel3_TEXT = font2.render(str(round(GermanyGraphNineHeight*(3/4))), 1, Dark_Gray1)
        GraphTenHeightLabel0_TEXT = font2.render(str(round(GermanyGraphTenHeight)), 1, Dark_Gray1)
        GraphTenHeightLabel1_TEXT = font2.render(str(round(GermanyGraphTenHeight*(1/4))), 1, Dark_Gray1)
        GraphTenHeightLabel2_TEXT = font2.render(str(round(GermanyGraphTenHeight*(2/4))), 1, Dark_Gray1)
        GraphTenHeightLabel3_TEXT = font2.render(str(round(GermanyGraphTenHeight*(3/4))), 1, Dark_Gray1)
        GraphElevenHeightLabel0_TEXT = font2.render(str(round(GermanyGraphElevenHeight,3)), 1, Dark_Gray1)
        GraphElevenHeightLabel1_TEXT = font2.render(str(round(GermanyGraphElevenHeight*(1/4),3)), 1, Dark_Gray1)
        GraphElevenHeightLabel2_TEXT = font2.render(str(round(GermanyGraphElevenHeight*(2/4),3)), 1, Dark_Gray1)
        GraphElevenHeightLabel3_TEXT = font2.render(str(round(GermanyGraphElevenHeight*(3/4),3)), 1, Dark_Gray1)
        GraphTwelveHeightLabel0_TEXT = font2.render(str(round(GermanyGraphTwelveHeight)), 1, Dark_Gray1)
        GraphTwelveHeightLabel1_TEXT = font2.render(str(round(GermanyGraphTwelveHeight*(1/4))), 1, Dark_Gray1)
        GraphTwelveHeightLabel2_TEXT = font2.render(str(round(GermanyGraphTwelveHeight*(2/4))), 1, Dark_Gray1)
        GraphTwelveHeightLabel3_TEXT = font2.render(str(round(GermanyGraphTwelveHeight*(3/4))), 1, Dark_Gray1)
        #Horizontal
        GraphOneWidthLabel0_TEXT = font2.render(str(round(GermanyGraphOneWidth)), 1, Dark_Gray1)
        GraphOneWidthLabel1_TEXT = font2.render(str(round(GermanyGraphOneWidth*(1/4))), 1, Dark_Gray1)
        GraphOneWidthLabel2_TEXT = font2.render(str(round(GermanyGraphOneWidth*(2/4))), 1, Dark_Gray1)
        GraphOneWidthLabel3_TEXT = font2.render(str(round(GermanyGraphOneWidth*(3/4))), 1, Dark_Gray1)
        GraphTwoWidthLabel0_TEXT = font2.render(str(round(GermanyGraphTwoWidth)), 1, Dark_Gray1)
        GraphTwoWidthLabel1_TEXT = font2.render(str(round(GermanyGraphTwoWidth*(1/4))), 1, Dark_Gray1)
        GraphTwoWidthLabel2_TEXT = font2.render(str(round(GermanyGraphTwoWidth*(2/4))), 1, Dark_Gray1)
        GraphTwoWidthLabel3_TEXT = font2.render(str(round(GermanyGraphTwoWidth*(3/4))), 1, Dark_Gray1)
        GraphThreeWidthLabel0_TEXT = font2.render(str(round(GermanyGraphThreeWidth)), 1, Dark_Gray1)
        GraphThreeWidthLabel1_TEXT = font2.render(str(round(GermanyGraphThreeWidth*(1/4))), 1, Dark_Gray1)
        GraphThreeWidthLabel2_TEXT = font2.render(str(round(GermanyGraphThreeWidth*(2/4))), 1, Dark_Gray1)
        GraphThreeWidthLabel3_TEXT = font2.render(str(round(GermanyGraphThreeWidth*(3/4))), 1, Dark_Gray1)
    if (MenuSelection == "France"):
        #Vertical
        GraphOneHeightLabel0_TEXT = font2.render(str(round(FranceGraphOneHeight)), 1, Dark_Gray1)
        GraphOneHeightLabel1_TEXT = font2.render(str(round(FranceGraphOneHeight*(1/4))), 1, Dark_Gray1)
        GraphOneHeightLabel2_TEXT = font2.render(str(round(FranceGraphOneHeight*(2/4))), 1, Dark_Gray1)
        GraphOneHeightLabel3_TEXT = font2.render(str(round(FranceGraphOneHeight*(3/4))), 1, Dark_Gray1)
        GraphTwoHeightLabel0_TEXT = font2.render(str(round(FranceGraphTwoHeight)), 1, Dark_Gray1)
        GraphTwoHeightLabel1_TEXT = font2.render(str(round(FranceGraphTwoHeight*(1/4))), 1, Dark_Gray1)
        GraphTwoHeightLabel2_TEXT = font2.render(str(round(FranceGraphTwoHeight*(2/4))), 1, Dark_Gray1)
        GraphTwoHeightLabel3_TEXT = font2.render(str(round(FranceGraphTwoHeight*(3/4))), 1, Dark_Gray1)
        GraphThreeHeightLabel0_TEXT = font2.render(str(round(FranceGraphThreeHeight)), 1, Dark_Gray1)
        GraphThreeHeightLabel1_TEXT = font2.render(str(round(FranceGraphThreeHeight*(1/4))), 1, Dark_Gray1)
        GraphThreeHeightLabel2_TEXT = font2.render(str(round(FranceGraphThreeHeight*(2/4))), 1, Dark_Gray1)
        GraphThreeHeightLabel3_TEXT = font2.render(str(round(FranceGraphThreeHeight*(3/4))), 1, Dark_Gray1)
        GraphFourHeightLabel0_TEXT = font2.render(str(round(FranceGraphFourHeight)), 1, Dark_Gray1)
        GraphFourHeightLabel1_TEXT = font2.render(str(round(FranceGraphFourHeight*(1/4))), 1, Dark_Gray1)
        GraphFourHeightLabel2_TEXT = font2.render(str(round(FranceGraphFourHeight*(2/4))), 1, Dark_Gray1)
        GraphFourHeightLabel3_TEXT = font2.render(str(round(FranceGraphFourHeight*(3/4))), 1, Dark_Gray1)
        GraphSixHeightLabel0_TEXT = font2.render(str(round(FranceGraphSixHeight)), 1, Dark_Gray1)
        GraphSixHeightLabel1_TEXT = font2.render(str(round(FranceGraphSixHeight*(1/4))), 1, Dark_Gray1)
        GraphSixHeightLabel2_TEXT = font2.render(str(round(FranceGraphSixHeight*(2/4))), 1, Dark_Gray1)
        GraphSixHeightLabel3_TEXT = font2.render(str(round(FranceGraphSixHeight*(3/4))), 1, Dark_Gray1)
        GraphSevenHeightLabel0_TEXT = font2.render(str(round(FranceGraphSevenHeight)), 1, Dark_Gray1)
        GraphSevenHeightLabel1_TEXT = font2.render(str(round(FranceGraphSevenHeight*(1/4))), 1, Dark_Gray1)
        GraphSevenHeightLabel2_TEXT = font2.render(str(round(FranceGraphSevenHeight*(2/4))), 1, Dark_Gray1)
        GraphSevenHeightLabel3_TEXT = font2.render(str(round(FranceGraphSevenHeight*(3/4))), 1, Dark_Gray1)
        GraphNineHeightLabel0_TEXT = font2.render(str(round(FranceGraphNineHeight)), 1, Dark_Gray1)
        GraphNineHeightLabel1_TEXT = font2.render(str(round(FranceGraphNineHeight*(1/4))), 1, Dark_Gray1)
        GraphNineHeightLabel2_TEXT = font2.render(str(round(FranceGraphNineHeight*(2/4))), 1, Dark_Gray1)
        GraphNineHeightLabel3_TEXT = font2.render(str(round(FranceGraphNineHeight*(3/4))), 1, Dark_Gray1)
        GraphTenHeightLabel0_TEXT = font2.render(str(round(FranceGraphTenHeight)), 1, Dark_Gray1)
        GraphTenHeightLabel1_TEXT = font2.render(str(round(FranceGraphTenHeight*(1/4))), 1, Dark_Gray1)
        GraphTenHeightLabel2_TEXT = font2.render(str(round(FranceGraphTenHeight*(2/4))), 1, Dark_Gray1)
        GraphTenHeightLabel3_TEXT = font2.render(str(round(FranceGraphTenHeight*(3/4))), 1, Dark_Gray1)
        GraphElevenHeightLabel0_TEXT = font2.render(str(round(FranceGraphElevenHeight,3)), 1, Dark_Gray1)
        GraphElevenHeightLabel1_TEXT = font2.render(str(round(FranceGraphElevenHeight*(1/4),3)), 1, Dark_Gray1)
        GraphElevenHeightLabel2_TEXT = font2.render(str(round(FranceGraphElevenHeight*(2/4),3)), 1, Dark_Gray1)
        GraphElevenHeightLabel3_TEXT = font2.render(str(round(FranceGraphElevenHeight*(3/4),3)), 1, Dark_Gray1)
        GraphTwelveHeightLabel0_TEXT = font2.render(str(round(FranceGraphTwelveHeight)), 1, Dark_Gray1)
        GraphTwelveHeightLabel1_TEXT = font2.render(str(round(FranceGraphTwelveHeight*(1/4))), 1, Dark_Gray1)
        GraphTwelveHeightLabel2_TEXT = font2.render(str(round(FranceGraphTwelveHeight*(2/4))), 1, Dark_Gray1)
        GraphTwelveHeightLabel3_TEXT = font2.render(str(round(FranceGraphTwelveHeight*(3/4))), 1, Dark_Gray1)
        #Horizontal
        GraphOneWidthLabel0_TEXT = font2.render(str(round(FranceGraphOneWidth)), 1, Dark_Gray1)
        GraphOneWidthLabel1_TEXT = font2.render(str(round(FranceGraphOneWidth*(1/4))), 1, Dark_Gray1)
        GraphOneWidthLabel2_TEXT = font2.render(str(round(FranceGraphOneWidth*(2/4))), 1, Dark_Gray1)
        GraphOneWidthLabel3_TEXT = font2.render(str(round(FranceGraphOneWidth*(3/4))), 1, Dark_Gray1)
        GraphTwoWidthLabel0_TEXT = font2.render(str(round(FranceGraphTwoWidth)), 1, Dark_Gray1)
        GraphTwoWidthLabel1_TEXT = font2.render(str(round(FranceGraphTwoWidth*(1/4))), 1, Dark_Gray1)
        GraphTwoWidthLabel2_TEXT = font2.render(str(round(FranceGraphTwoWidth*(2/4))), 1, Dark_Gray1)
        GraphTwoWidthLabel3_TEXT = font2.render(str(round(FranceGraphTwoWidth*(3/4))), 1, Dark_Gray1)
        GraphThreeWidthLabel0_TEXT = font2.render(str(round(FranceGraphThreeWidth)), 1, Dark_Gray1)
        GraphThreeWidthLabel1_TEXT = font2.render(str(round(FranceGraphThreeWidth*(1/4))), 1, Dark_Gray1)
        GraphThreeWidthLabel2_TEXT = font2.render(str(round(FranceGraphThreeWidth*(2/4))), 1, Dark_Gray1)
        GraphThreeWidthLabel3_TEXT = font2.render(str(round(FranceGraphThreeWidth*(3/4))), 1, Dark_Gray1)

    #Loop Over Function List Germany
    GermanyProductionFunctionAList = [(x,(GraphOneY+GraphHeight)-PixelGermanyProductionFunctionA(x)) for (x,y) in GermanyProductionFunctionAList]
    GermanyProductionFunctionBList = [(x,(GraphOneY+GraphHeight)-PixelGermanyProductionFunctionB(x)) for (x,y) in GermanyProductionFunctionBList]
    GermanyProductionFunctionCList = [(x,(GraphOneY+GraphHeight)-PixelGermanyProductionFunctionC(x)) for (x,y) in GermanyProductionFunctionCList]
    GermanyMarginalDisUtilityLabourList = [(x,(GraphTwoY+GraphHeight)-PixelGermanyMarginalDisUtilityLabourFunction(x)) for (x,y) in GermanyMarginalDisUtilityLabourList]
    GermanyMarginalUtilityAList = [(x,(GraphThreeY+GraphHeight)-PixelGermanyMarginalUtilityFunctionA(x)) for (x,y) in GermanyMarginalUtilityAList]
    GermanyMarginalUtilityBList = [(x,(GraphThreeY+GraphHeight)-PixelGermanyMarginalUtilityFunctionB(x)) for (x,y) in GermanyMarginalUtilityBList]
    GermanyMarginalUtilityCList = [(x,(GraphThreeY+GraphHeight)-PixelGermanyMarginalUtilityFunctionC(x)) for (x,y) in GermanyMarginalUtilityCList]

    #Loop Over Function List France
    FranceProductionFunctionAList = [(x,(GraphOneY+GraphHeight)-PixelFranceProductionFunctionA(x)) for (x,y) in FranceProductionFunctionAList]
    FranceProductionFunctionBList = [(x,(GraphOneY+GraphHeight)-PixelFranceProductionFunctionB(x)) for (x,y) in FranceProductionFunctionBList]
    FranceProductionFunctionCList = [(x,(GraphOneY+GraphHeight)-PixelFranceProductionFunctionC(x)) for (x,y) in FranceProductionFunctionCList]
    FranceMarginalDisUtilityLabourList = [(x,(GraphTwoY+GraphHeight)-PixelFranceMarginalDisUtilityLabourFunction(x)) for (x,y) in FranceMarginalDisUtilityLabourList]
    FranceMarginalUtilityAList = [(x,(GraphThreeY+GraphHeight)-PixelFranceMarginalUtilityFunctionA(x)) for (x,y) in FranceMarginalUtilityAList]
    FranceMarginalUtilityBList = [(x,(GraphThreeY+GraphHeight)-PixelFranceMarginalUtilityFunctionB(x)) for (x,y) in FranceMarginalUtilityBList]
    FranceMarginalUtilityCList = [(x,(GraphThreeY+GraphHeight)-PixelFranceMarginalUtilityFunctionC(x)) for (x,y) in FranceMarginalUtilityCList]

    if (PAUSE == False) or (STEP == True):
        #Raw List Germany
        GermanyRawPriceAList.append((GraphFourX+len(GermanyRawPriceAList),GermanyPriceA))
        if (len(GermanyRawPriceAList) > (GraphWidth)):
            GermanyRawPriceAList.pop(0)
            GermanyRawPriceAList = [(x-1,y) for (x,y) in GermanyRawPriceAList]
        GermanyRawPriceBList.append((GraphFourX+len(GermanyRawPriceBList),GermanyPriceB))
        if (len(GermanyRawPriceBList) > (GraphWidth)):
            GermanyRawPriceBList.pop(0)
            GermanyRawPriceBList = [(x-1,y) for (x,y) in GermanyRawPriceBList]
        GermanyRawPriceCList.append((GraphFourX+len(GermanyRawPriceCList),GermanyPriceC))
        if (len(GermanyRawPriceCList) > (GraphWidth)):
            GermanyRawPriceCList.pop(0)
            GermanyRawPriceCList = [(x-1,y) for (x,y) in GermanyRawPriceCList]
        GermanyRawExportABCList.append((GraphSixX+len(GermanyRawExportABCList),FranceMoneySpentForeignA+FranceMoneySpentForeignB+FranceMoneySpentForeignC))
        if (len(GermanyRawExportABCList) > (GraphWidth)):
            GermanyRawExportABCList.pop(0)
            GermanyRawExportABCList = [(x-1,y) for (x,y) in GermanyRawExportABCList]
        GermanyRawExportBCList.append((GraphSixX+len(GermanyRawExportBCList),FranceMoneySpentForeignB+FranceMoneySpentForeignC))
        if (len(GermanyRawExportBCList) > (GraphWidth)):
            GermanyRawExportBCList.pop(0)
            GermanyRawExportBCList = [(x-1,y) for (x,y) in GermanyRawExportBCList]
        GermanyRawExportCList.append((GraphSixX+len(GermanyRawExportCList),FranceMoneySpentForeignC))
        if (len(GermanyRawExportCList) > (GraphWidth)):
            GermanyRawExportCList.pop(0)
            GermanyRawExportCList = [(x-1,y) for (x,y) in GermanyRawExportCList]
        GermanyRawSupplyLabourList.append((GraphSevenX+len(GermanyRawSupplyLabourList),GermanySupplyLabour))
        if (len(GermanyRawSupplyLabourList) > (GraphWidth)):
            GermanyRawSupplyLabourList.pop(0)
            GermanyRawSupplyLabourList = [(x-1,y) for (x,y) in GermanyRawSupplyLabourList]
        GermanyRawImportABCList.append((GraphNineX+len(GermanyRawImportABCList),GermanyMoneySpentForeignA+GermanyMoneySpentForeignB+GermanyMoneySpentForeignC))
        if (len(GermanyRawImportABCList) > (GraphWidth)):
            GermanyRawImportABCList.pop(0)
            GermanyRawImportABCList = [(x-1,y) for (x,y) in GermanyRawImportABCList]
        GermanyRawImportBCList.append((GraphNineX+len(GermanyRawImportBCList),GermanyMoneySpentForeignB+GermanyMoneySpentForeignC))
        if (len(GermanyRawImportBCList) > (GraphWidth)):
            GermanyRawImportBCList.pop(0)
            GermanyRawImportBCList = [(x-1,y) for (x,y) in GermanyRawImportBCList]
        GermanyRawImportCList.append((GraphNineX+len(GermanyRawImportCList),GermanyMoneySpentForeignC))
        if (len(GermanyRawImportCList) > (GraphWidth)):
            GermanyRawImportCList.pop(0)
            GermanyRawImportCList = [(x-1,y) for (x,y) in GermanyRawImportCList]
        GermanyRawWageRateList.append((GraphTenX+len(GermanyRawWageRateList),GermanyWageRate))
        if (len(GermanyRawWageRateList) > (GraphWidth)):
            GermanyRawWageRateList.pop(0)
            GermanyRawWageRateList = [(x-1,y) for (x,y) in GermanyRawWageRateList]
        GermanyRawMUMoneyAList.append((GraphElevenX+len(GermanyRawMUMoneyAList),GermanyMarginalUtilityMoneySpentA))
        if (len(GermanyRawMUMoneyAList) > (GraphWidth)):
            GermanyRawMUMoneyAList.pop(0)
            GermanyRawMUMoneyAList = [(x-1,y) for (x,y) in GermanyRawMUMoneyAList]
        GermanyRawMUMoneyBList.append((GraphElevenX+len(GermanyRawMUMoneyBList),GermanyMarginalUtilityMoneySpentB))
        if (len(GermanyRawMUMoneyBList) > (GraphWidth)):
            GermanyRawMUMoneyBList.pop(0)
            GermanyRawMUMoneyBList = [(x-1,y) for (x,y) in GermanyRawMUMoneyBList]
        GermanyRawMUMoneyCList.append((GraphElevenX+len(GermanyRawMUMoneyCList),GermanyMarginalUtilityMoneySpentC))
        if (len(GermanyRawMUMoneyCList) > (GraphWidth)):
            GermanyRawMUMoneyCList.pop(0)
            GermanyRawMUMoneyCList = [(x-1,y) for (x,y) in GermanyRawMUMoneyCList]
        GermanyRawMDUMoneyList.append((GraphElevenX+len(GermanyRawMDUMoneyList),GermanyMarginalDisUtilityMoneyEarned))
        if (len(GermanyRawMDUMoneyList) > (GraphWidth)):
            GermanyRawMDUMoneyList.pop(0)
            GermanyRawMDUMoneyList = [(x-1,y) for (x,y) in GermanyRawMDUMoneyList]
        GermanyRawMPVAList.append((GraphTwelveX+len(GermanyRawMPVAList),GermanyMarginalValueProductionA))
        if (len(GermanyRawMPVAList) > (GraphWidth)):
            GermanyRawMPVAList.pop(0)
            GermanyRawMPVAList = [(x-1,y) for (x,y) in GermanyRawMPVAList]
        GermanyRawMPVBList.append((GraphTwelveX+len(GermanyRawMPVBList),GermanyMarginalValueProductionB))
        if (len(GermanyRawMPVBList) > (GraphWidth)):
            GermanyRawMPVBList.pop(0)
            GermanyRawMPVBList = [(x-1,y) for (x,y) in GermanyRawMPVBList]
        GermanyRawMPVCList.append((GraphTwelveX+len(GermanyRawMPVCList),GermanyMarginalValueProductionC))
        if (len(GermanyRawMPVCList) > (GraphWidth)):
            GermanyRawMPVCList.pop(0)
            GermanyRawMPVCList = [(x-1,y) for (x,y) in GermanyRawMPVCList]

        #Raw List France
        FranceRawPriceAList.append((GraphFourX+len(FranceRawPriceAList),FrancePriceA))
        if (len(FranceRawPriceAList) > (GraphWidth)):
            FranceRawPriceAList.pop(0)
            FranceRawPriceAList = [(x-1,y) for (x,y) in FranceRawPriceAList]
        FranceRawPriceBList.append((GraphFourX+len(FranceRawPriceBList),FrancePriceB))
        if (len(FranceRawPriceBList) > (GraphWidth)):
            FranceRawPriceBList.pop(0)
            FranceRawPriceBList = [(x-1,y) for (x,y) in FranceRawPriceBList]
        FranceRawPriceCList.append((GraphFourX+len(FranceRawPriceCList),FrancePriceC))
        if (len(FranceRawPriceCList) > (GraphWidth)):
            FranceRawPriceCList.pop(0)
            FranceRawPriceCList = [(x-1,y) for (x,y) in FranceRawPriceCList]
        FranceRawExportABCList.append((GraphSixX+len(FranceRawExportABCList),GermanyMoneySpentForeignA+GermanyMoneySpentForeignB+GermanyMoneySpentForeignC))
        if (len(FranceRawExportABCList) > (GraphWidth)):
            FranceRawExportABCList.pop(0)
            FranceRawExportABCList = [(x-1,y) for (x,y) in FranceRawExportABCList]
        FranceRawExportBCList.append((GraphSixX+len(FranceRawExportBCList),GermanyMoneySpentForeignB+GermanyMoneySpentForeignC))
        if (len(FranceRawExportBCList) > (GraphWidth)):
            FranceRawExportBCList.pop(0)
            FranceRawExportBCList = [(x-1,y) for (x,y) in FranceRawExportBCList]
        FranceRawExportCList.append((GraphSixX+len(FranceRawExportCList),GermanyMoneySpentForeignC))
        if (len(FranceRawExportCList) > (GraphWidth)):
            FranceRawExportCList.pop(0)
            FranceRawExportCList = [(x-1,y) for (x,y) in FranceRawExportCList]
        FranceRawSupplyLabourList.append((GraphSevenX+len(FranceRawSupplyLabourList),FranceSupplyLabour))
        if (len(FranceRawSupplyLabourList) > (GraphWidth)):
            FranceRawSupplyLabourList.pop(0)
            FranceRawSupplyLabourList = [(x-1,y) for (x,y) in FranceRawSupplyLabourList]
        FranceRawImportABCList.append((GraphNineX+len(FranceRawImportABCList),FranceMoneySpentForeignA+FranceMoneySpentForeignB+FranceMoneySpentForeignC))
        if (len(FranceRawImportABCList) > (GraphWidth)):
            FranceRawImportABCList.pop(0)
            FranceRawImportABCList = [(x-1,y) for (x,y) in FranceRawImportABCList]
        FranceRawImportBCList.append((GraphNineX+len(FranceRawImportBCList),FranceMoneySpentForeignB+FranceMoneySpentForeignC))
        if (len(FranceRawImportBCList) > (GraphWidth)):
            FranceRawImportBCList.pop(0)
            FranceRawImportBCList = [(x-1,y) for (x,y) in FranceRawImportBCList]
        FranceRawImportCList.append((GraphNineX+len(FranceRawImportCList),FranceMoneySpentForeignC))
        if (len(FranceRawImportCList) > (GraphWidth)):
            FranceRawImportCList.pop(0)
            FranceRawImportCList = [(x-1,y) for (x,y) in FranceRawImportCList]
        FranceRawWageRateList.append((GraphTenX+len(FranceRawWageRateList),FranceWageRate))
        if (len(FranceRawWageRateList) > (GraphWidth)):
            FranceRawWageRateList.pop(0)
            FranceRawWageRateList = [(x-1,y) for (x,y) in FranceRawWageRateList]
        FranceRawMUMoneyAList.append((GraphElevenX+len(FranceRawMUMoneyAList),FranceMarginalUtilityMoneySpentA))
        if (len(FranceRawMUMoneyAList) > (GraphWidth)):
            FranceRawMUMoneyAList.pop(0)
            FranceRawMUMoneyAList = [(x-1,y) for (x,y) in FranceRawMUMoneyAList]
        FranceRawMUMoneyBList.append((GraphElevenX+len(FranceRawMUMoneyBList),FranceMarginalUtilityMoneySpentB))
        if (len(FranceRawMUMoneyBList) > (GraphWidth)):
            FranceRawMUMoneyBList.pop(0)
            FranceRawMUMoneyBList = [(x-1,y) for (x,y) in FranceRawMUMoneyBList]
        FranceRawMUMoneyCList.append((GraphElevenX+len(FranceRawMUMoneyCList),FranceMarginalUtilityMoneySpentC))
        if (len(FranceRawMUMoneyCList) > (GraphWidth)):
            FranceRawMUMoneyCList.pop(0)
            FranceRawMUMoneyCList = [(x-1,y) for (x,y) in FranceRawMUMoneyCList]
        FranceRawMDUMoneyList.append((GraphElevenX+len(FranceRawMDUMoneyList),FranceMarginalDisUtilityMoneyEarned))
        if (len(FranceRawMDUMoneyList) > (GraphWidth)):
            FranceRawMDUMoneyList.pop(0)
            FranceRawMDUMoneyList = [(x-1,y) for (x,y) in FranceRawMDUMoneyList]
        FranceRawMPVAList.append((GraphTwelveX+len(FranceRawMPVAList),FranceMarginalValueProductionA))
        if (len(FranceRawMPVAList) > (GraphWidth)):
            FranceRawMPVAList.pop(0)
            FranceRawMPVAList = [(x-1,y) for (x,y) in FranceRawMPVAList]
        FranceRawMPVBList.append((GraphTwelveX+len(FranceRawMPVBList),FranceMarginalValueProductionB))
        if (len(FranceRawMPVBList) > (GraphWidth)):
            FranceRawMPVBList.pop(0)
            FranceRawMPVBList = [(x-1,y) for (x,y) in FranceRawMPVBList]
        FranceRawMPVCList.append((GraphTwelveX+len(FranceRawMPVCList),FranceMarginalValueProductionC))
        if (len(FranceRawMPVCList) > (GraphWidth)):
            FranceRawMPVCList.pop(0)
            FranceRawMPVCList = [(x-1,y) for (x,y) in FranceRawMPVCList]

        #Bake List Germany
        GermanyBakePriceAList = [(x,(GraphFourY+GraphHeight)-round((y/GermanyGraphFourHeight)*GraphHeight)) for (x,y) in GermanyRawPriceAList]
        GermanyBakePriceBList = [(x,(GraphFourY+GraphHeight)-round((y/GermanyGraphFourHeight)*GraphHeight)) for (x,y) in GermanyRawPriceBList]
        GermanyBakePriceCList = [(x,(GraphFourY+GraphHeight)-round((y/GermanyGraphFourHeight)*GraphHeight)) for (x,y) in GermanyRawPriceCList]
        GermanyBakeExportABCList = [(x,(GraphSixY+GraphHeight)-round((y/GermanyGraphSixHeight)*GraphHeight)-1) for (x,y) in GermanyRawExportABCList]
        GermanyBakeExportBCList = [(x,(GraphSixY+GraphHeight)-round((y/GermanyGraphSixHeight)*GraphHeight)-1) for (x,y) in GermanyRawExportBCList]
        GermanyBakeExportCList = [(x,(GraphSixY+GraphHeight)-round((y/GermanyGraphSixHeight)*GraphHeight)-1) for (x,y) in GermanyRawExportCList]
        GermanyBakeExportABCList.extend([(GraphSixX+GraphWidth-1,GraphSixY+GraphHeight-1),(GraphSixX,GraphSixY+GraphHeight-1)])
        GermanyBakeExportBCList.extend([(GraphSixX+GraphWidth-1,GraphSixY+GraphHeight-1),(GraphSixX,GraphSixY+GraphHeight-1)])
        GermanyBakeExportCList.extend([(GraphSixX+GraphWidth-1,GraphSixY+GraphHeight-1),(GraphSixX,GraphSixY+GraphHeight-1)])
        GermanyBakeSupplyLabourList = [(x,(GraphSevenY+GraphHeight)-round((y/GermanyGraphSevenHeight)*GraphHeight)) for (x,y) in GermanyRawSupplyLabourList]
        GermanyBakeImportABCList = [(x,(GraphNineY+GraphHeight)-round((y/GermanyGraphNineHeight)*GraphHeight)-1) for (x,y) in GermanyRawImportABCList]
        GermanyBakeImportBCList = [(x,(GraphNineY+GraphHeight)-round((y/GermanyGraphNineHeight)*GraphHeight)-1) for (x,y) in GermanyRawImportBCList]
        GermanyBakeImportCList = [(x,(GraphNineY+GraphHeight)-round((y/GermanyGraphNineHeight)*GraphHeight)-1) for (x,y) in GermanyRawImportCList]
        GermanyBakeImportABCList.extend([(GraphNineX+GraphWidth-1,GraphNineY+GraphHeight-1),(GraphNineX,GraphNineY+GraphHeight-1)])
        GermanyBakeImportBCList.extend([(GraphNineX+GraphWidth-1,GraphNineY+GraphHeight-1),(GraphNineX,GraphNineY+GraphHeight-1)])
        GermanyBakeImportCList.extend([(GraphNineX+GraphWidth-1,GraphNineY+GraphHeight-1),(GraphNineX,GraphNineY+GraphHeight-1)])
        GermanyBakeWageRateList = [(x,(GraphTenY+GraphHeight)-round((y/GermanyGraphTenHeight)*GraphHeight)) for (x,y) in GermanyRawWageRateList]
        GermanyBakeMUMoneyAList = [(x,(GraphElevenY+GraphHeight)-round((y/GermanyGraphElevenHeight)*GraphHeight)) for (x,y) in GermanyRawMUMoneyAList]
        GermanyBakeMUMoneyBList = [(x,(GraphElevenY+GraphHeight)-round((y/GermanyGraphElevenHeight)*GraphHeight)) for (x,y) in GermanyRawMUMoneyBList]
        GermanyBakeMUMoneyCList = [(x,(GraphElevenY+GraphHeight)-round((y/GermanyGraphElevenHeight)*GraphHeight)) for (x,y) in GermanyRawMUMoneyCList]
        GermanyBakeMDUMoneyList = [(x,(GraphElevenY+GraphHeight)-round((y/GermanyGraphElevenHeight)*GraphHeight)) for (x,y) in GermanyRawMDUMoneyList]
        GermanyBakeMPVAList = [(x,(GraphTwelveY+GraphHeight)-round((y/GermanyGraphTwelveHeight)*GraphHeight)) for (x,y) in GermanyRawMPVAList]
        GermanyBakeMPVBList = [(x,(GraphTwelveY+GraphHeight)-round((y/GermanyGraphTwelveHeight)*GraphHeight)) for (x,y) in GermanyRawMPVBList]
        GermanyBakeMPVCList = [(x,(GraphTwelveY+GraphHeight)-round((y/GermanyGraphTwelveHeight)*GraphHeight)) for (x,y) in GermanyRawMPVCList]

        #Bake List France
        FranceBakePriceAList = [(x,(GraphFourY+GraphHeight)-round((y/FranceGraphFourHeight)*GraphHeight)) for (x,y) in FranceRawPriceAList]
        FranceBakePriceBList = [(x,(GraphFourY+GraphHeight)-round((y/FranceGraphFourHeight)*GraphHeight)) for (x,y) in FranceRawPriceBList]
        FranceBakePriceCList = [(x,(GraphFourY+GraphHeight)-round((y/FranceGraphFourHeight)*GraphHeight)) for (x,y) in FranceRawPriceCList]
        FranceBakeExportABCList = [(x,(GraphSixY+GraphHeight)-round((y/FranceGraphSixHeight)*GraphHeight)-1) for (x,y) in FranceRawExportABCList]
        FranceBakeExportBCList = [(x,(GraphSixY+GraphHeight)-round((y/FranceGraphSixHeight)*GraphHeight)-1) for (x,y) in FranceRawExportBCList]
        FranceBakeExportCList = [(x,(GraphSixY+GraphHeight)-round((y/FranceGraphSixHeight)*GraphHeight)-1) for (x,y) in FranceRawExportCList]
        FranceBakeExportABCList.extend([(GraphSixX+GraphWidth-1,GraphSixY+GraphHeight-1),(GraphSixX,GraphSixY+GraphHeight-1)])
        FranceBakeExportBCList.extend([(GraphSixX+GraphWidth-1,GraphSixY+GraphHeight-1),(GraphSixX,GraphSixY+GraphHeight-1)])
        FranceBakeExportCList.extend([(GraphSixX+GraphWidth-1,GraphSixY+GraphHeight-1),(GraphSixX,GraphSixY+GraphHeight-1)])
        FranceBakeSupplyLabourList = [(x,(GraphSevenY+GraphHeight)-round((y/FranceGraphSevenHeight)*GraphHeight)) for (x,y) in FranceRawSupplyLabourList]
        FranceBakeImportABCList = [(x,(GraphNineY+GraphHeight)-round((y/FranceGraphNineHeight)*GraphHeight)-1) for (x,y) in FranceRawImportABCList]
        FranceBakeImportBCList = [(x,(GraphNineY+GraphHeight)-round((y/FranceGraphNineHeight)*GraphHeight)-1) for (x,y) in FranceRawImportBCList]
        FranceBakeImportCList = [(x,(GraphNineY+GraphHeight)-round((y/FranceGraphNineHeight)*GraphHeight)-1) for (x,y) in FranceRawImportCList]
        FranceBakeImportABCList.extend([(GraphNineX+GraphWidth-1,GraphNineY+GraphHeight-1),(GraphNineX,GraphNineY+GraphHeight-1)])
        FranceBakeImportBCList.extend([(GraphNineX+GraphWidth-1,GraphNineY+GraphHeight-1),(GraphNineX,GraphNineY+GraphHeight-1)])
        FranceBakeImportCList.extend([(GraphNineX+GraphWidth-1,GraphNineY+GraphHeight-1),(GraphNineX,GraphNineY+GraphHeight-1)])
        FranceBakeWageRateList = [(x,(GraphTenY+GraphHeight)-round((y/FranceGraphTenHeight)*GraphHeight)) for (x,y) in FranceRawWageRateList]
        FranceBakeMUMoneyAList = [(x,(GraphElevenY+GraphHeight)-round((y/FranceGraphElevenHeight)*GraphHeight)) for (x,y) in FranceRawMUMoneyAList]
        FranceBakeMUMoneyBList = [(x,(GraphElevenY+GraphHeight)-round((y/FranceGraphElevenHeight)*GraphHeight)) for (x,y) in FranceRawMUMoneyBList]
        FranceBakeMUMoneyCList = [(x,(GraphElevenY+GraphHeight)-round((y/FranceGraphElevenHeight)*GraphHeight)) for (x,y) in FranceRawMUMoneyCList]
        FranceBakeMDUMoneyList = [(x,(GraphElevenY+GraphHeight)-round((y/FranceGraphElevenHeight)*GraphHeight)) for (x,y) in FranceRawMDUMoneyList]
        FranceBakeMPVAList = [(x,(GraphTwelveY+GraphHeight)-round((y/FranceGraphTwelveHeight)*GraphHeight)) for (x,y) in FranceRawMPVAList]
        FranceBakeMPVBList = [(x,(GraphTwelveY+GraphHeight)-round((y/FranceGraphTwelveHeight)*GraphHeight)) for (x,y) in FranceRawMPVBList]
        FranceBakeMPVCList = [(x,(GraphTwelveY+GraphHeight)-round((y/FranceGraphTwelveHeight)*GraphHeight)) for (x,y) in FranceRawMPVCList]

    #Slider Normlized Value Germany
    GermanySliderNormalizedValueOne = (GermanySliderDotOneX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueTwo = (GermanySliderDotTwoX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueThree = (GermanySliderDotThreeX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueFour = (GermanySliderDotFourX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueFive = (GermanySliderDotFiveX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueSix = (GermanySliderDotSixX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueSeven = (GermanySliderDotSevenX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueEight = (GermanySliderDotEightX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueNine = (GermanySliderDotNineX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueTen = (GermanySliderDotTenX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueEleven = (GermanySliderDotElevenX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueTwelve = (GermanySliderDotTwelveX-SliderX)/(SliderWidth-SliderThickness)
    GermanySliderNormalizedValueThirteen = (GermanySliderDotThirteenX-SliderX)/(SliderWidth-SliderThickness)

    #Slider Normlized Value France
    FranceSliderNormalizedValueOne = (FranceSliderDotOneX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueTwo = (FranceSliderDotTwoX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueThree = (FranceSliderDotThreeX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueFour = (FranceSliderDotFourX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueFive = (FranceSliderDotFiveX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueSix = (FranceSliderDotSixX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueSeven = (FranceSliderDotSevenX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueEight = (FranceSliderDotEightX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueNine = (FranceSliderDotNineX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueTen = (FranceSliderDotTenX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueEleven = (FranceSliderDotElevenX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueTwelve = (FranceSliderDotTwelveX-SliderX)/(SliderWidth-SliderThickness)
    FranceSliderNormalizedValueThirteen = (FranceSliderDotThirteenX-SliderX)/(SliderWidth-SliderThickness)

    #Slider Percent Values Text Germany
    GermanySliderPercentValueTextOne = font1.render("+%"+str(round(SliderMaxPercentValueOne*GermanySliderNormalizedValueOne)), 1, Green)
    GermanySliderPercentValueTextTwo = font1.render("+%"+str(round(SliderMaxPercentValueTwo*GermanySliderNormalizedValueTwo)), 1, Green)
    GermanySliderPercentValueTextThree = font1.render("+%"+str(round(SliderMaxPercentValueThree*GermanySliderNormalizedValueThree)), 1, Green)
    GermanySliderPercentValueTextFour = font1.render("+%"+str(round(SliderMaxPercentValueFour*GermanySliderNormalizedValueFour)), 1, Red)
    GermanySliderPercentValueTextFive = font1.render("+%"+str(round(SliderMaxPercentValueFive*GermanySliderNormalizedValueFive)), 1, Green)
    GermanySliderPercentValueTextSix = font1.render("+%"+str(round(SliderMaxPercentValueSix*GermanySliderNormalizedValueSix)), 1, Green)
    GermanySliderPercentValueTextSeven = font1.render("+%"+str(round(SliderMaxPercentValueSeven*GermanySliderNormalizedValueSeven)), 1, Green)
    GermanySliderPercentValueTextEight = font1.render("+%"+str(round(SliderMaxPercentValueEight*GermanySliderNormalizedValueEight)), 1, Red)
    GermanySliderPercentValueTextNine = font1.render("+%"+str(round(SliderMaxPercentValueNine*GermanySliderNormalizedValueNine)), 1, Red)
    GermanySliderPercentValueTextTen = font1.render("+%"+str(round(SliderMaxPercentValueTen*GermanySliderNormalizedValueTen)), 1, Red)

    #Slider Percent Values Text France
    FranceSliderPercentValueTextOne = font1.render("+%"+str(round(SliderMaxPercentValueOne*FranceSliderNormalizedValueOne)), 1, Green)
    FranceSliderPercentValueTextTwo = font1.render("+%"+str(round(SliderMaxPercentValueTwo*FranceSliderNormalizedValueTwo)), 1, Green)
    FranceSliderPercentValueTextThree = font1.render("+%"+str(round(SliderMaxPercentValueThree*FranceSliderNormalizedValueThree)), 1, Green)
    FranceSliderPercentValueTextFour = font1.render("+%"+str(round(SliderMaxPercentValueFour*FranceSliderNormalizedValueFour)), 1, Red)
    FranceSliderPercentValueTextFive = font1.render("+%"+str(round(SliderMaxPercentValueFive*FranceSliderNormalizedValueFive)), 1, Green)
    FranceSliderPercentValueTextSix = font1.render("+%"+str(round(SliderMaxPercentValueSix*FranceSliderNormalizedValueSix)), 1, Green)
    FranceSliderPercentValueTextSeven = font1.render("+%"+str(round(SliderMaxPercentValueSeven*FranceSliderNormalizedValueSeven)), 1, Green)
    FranceSliderPercentValueTextEight = font1.render("+%"+str(round(SliderMaxPercentValueEight*FranceSliderNormalizedValueEight)), 1, Red)
    FranceSliderPercentValueTextNine = font1.render("+%"+str(round(SliderMaxPercentValueNine*FranceSliderNormalizedValueNine)), 1, Red)
    FranceSliderPercentValueTextTen = font1.render("+%"+str(round(SliderMaxPercentValueTen*FranceSliderNormalizedValueTen)), 1, Red)

    #Tariff Rate
    GermanyTariffRateA = GermanySliderNormalizedValueEight
    GermanyTariffRateB = GermanySliderNormalizedValueNine
    GermanyTariffRateC = GermanySliderNormalizedValueTen
    FranceTariffRateA = FranceSliderNormalizedValueEight
    FranceTariffRateB = FranceSliderNormalizedValueNine
    FranceTariffRateC = FranceSliderNormalizedValueTen

    STEP = False

    Game()
    if (MenuSelection == "Germany"):
        DrawCountryGraphs()
        DrawGermanyGraphLines()
        DrawBoxesLast()
        DrawGermanySliders()
        PieChart3(GermanyLabourPercentA,GermanyLabourPercentB,GermanyLabourPercentC,GraphFiveX+GraphWidth-round(GraphHeight/2),GraphFiveY+round(GraphHeight/2),round(GraphHeight/2))
        PieChart3(GermanyBudgetPercentA,GermanyBudgetPercentB,GermanyBudgetPercentC,GraphEightX+GraphWidth-round(GraphHeight/2),GraphEightY+round(GraphHeight/2),round(GraphHeight/2))
        DrawButtons()
        MouseToolTips()
    if (MenuSelection == "France"):
        DrawCountryGraphs()
        DrawFranceGraphLines()
        DrawBoxesLast()
        DrawFranceSliders()
        PieChart3(FranceLabourPercentA,FranceLabourPercentB,FranceLabourPercentC,GraphFiveX+GraphWidth-round(GraphHeight/2),GraphFiveY+round(GraphHeight/2),round(GraphHeight/2))
        PieChart3(FranceBudgetPercentA,FranceBudgetPercentB,FranceBudgetPercentC,GraphEightX+GraphWidth-round(GraphHeight/2),GraphEightY+round(GraphHeight/2),round(GraphHeight/2))
        DrawButtons()
        MouseToolTips()
    if (DebugWindow == True):
        DebugWindowFunction()

    pygame.display.update()

    counter+=1
    if (time.time() - start_time) > xxx :
        FPS = counter / (time.time() - start_time)
        counter = 0
        start_time = time.time()

pygame.quit()
