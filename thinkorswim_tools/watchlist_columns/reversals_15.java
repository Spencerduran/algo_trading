#------------------------------------
# SCENARIOS
#------------------------------------
def H = high;
def L = low;
def C = close;
def O = open;

def insidebar =  (H < H[1] and L > L[1]) or (H == H[1] and L > L[1]) or (H < H[1] and L == L[1]) or (H == H[1] and L == L[1]);
def outsidebar =  H  > H[1] and L <  L[1];

def insidebarup  = insidebar and O < C;
def twoup  = H > H[1] and L >= L[1];
def outsidebarup  = outsidebar and O < C;
def insidebardown  = insidebar and O > C;
def twodown  = H <= H[1] and L < L[1];
def outsidebardown  = outsidebar and O > C;

#------------------------------------
# REVERSALS
#------------------------------------

# Bullish
def TwoOneTwoBull =  twoup and insidebar[1] and C > O;
def ThreeOneTwoBull =  twoup and insidebar[1] and outsidebar[2] and C > O;
def ThreeTwoTwoBull =  twoup and twodown[1] and outsidebar[2] and C > O;
def RevStratBull =  twoup and twodown[1] and insidebar[2] and C > O;
def TwoTwoRevBull =  twodown[1] and twoup and C > O;
def two_down_three = twodown and close > hl2[1];

# Bearish
def TwoOneTwoBear = twodown and insidebar[1] and C < O;
def ThreeOneTwoBear = twodown and insidebar[1] and outsidebar[2] and C < O;
def ThreeTwoTwoBear = twodown and twoup[1] and outsidebar[2] and C < O;
def RevStratBear = twodown and twoup[1] and insidebar[2] and C < O;
def TwoTwoRevBear = twoup[1] and twodown and C < O;
def two_up_three = twoup and close < hl2[1];
# -------------------------
# Labels
# -------------------------

AddLabel(yes, if 
TwoTwoRevBull and !ThreeTwoTwoBull and !RevStratBull then " 2-2 Rev" else if 
TwoOneTwoBull and !ThreeOneTwoBull then " 2-1-2" else if 
ThreeOneTwoBull then "  3-1-2" else if 
ThreeTwoTwoBull then "  3-2-2" else if 
RevStratBull then " 1-2-2" else if
two_up_three then " 50% " else if
TwoTwoRevBear and !ThreeTwoTwoBear and !RevStratBear then " 2-2 Rev" else if 
TwoOneTwoBear and !ThreeOneTwoBear then " 2-1-2" else if 
ThreeOneTwoBear then "  3-1-2" else if 
ThreeTwoTwoBear then "  3-2-2" else if 
two_down_three then " 50% " else if
RevStratBear then " 1-2-2" else "-", 
if TwoOneTwoBear or 
ThreeOneTwoBear or 
ThreeTwoTwoBear or 
two_up_three or
RevStratBear or 
TwoTwoRevBear then Color.WHITE else if ThreeTwoTwoBear or ThreeTwoTwoBull then Color.BLUE else Color.BLACK); 

AssignBackgroundColor(if 
TwoOneTwoBull or 
ThreeOneTwoBull or 
ThreeTwoTwoBull or 
RevStratBull or 
two_down_three or
TwoTwoRevBull then Color.LIGHT_GREEN else if
two_up_three or
TwoOneTwoBear or 
ThreeOneTwoBear or 
ThreeTwoTwoBear or 
RevStratBear or 
TwoTwoRevBear then Color.LIGHT_RED else Color.BLACK); 
