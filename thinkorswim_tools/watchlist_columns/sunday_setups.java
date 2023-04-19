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
def TwoOneTwoBull =  insidebar and C > O;
def ThreeOneTwoBull =  insidebar and outsidebar[1] and C > O;
def ThreeTwoTwoBull =  twodown and outsidebar[1] and C > O;
def RevStratBull =  twodown and insidebar[1] and C > O;
def TwoTwoRevBull =  twodown and C > O;

# Bearish
def TwoOneTwoBear = insidebar and C < O;
def ThreeOneTwoBear = insidebar and outsidebar[1] and C < O;
def ThreeTwoTwoBear = twoup and outsidebar[1] and C < O;
def RevStratBear = twoup and insidebar[1] and C < O;
def TwoTwoRevBear = twoup and C < O;

# -------------------------
# Labels
# -------------------------

AddLabel(yes, if 
TwoTwoRevBull and !ThreeTwoTwoBull and !RevStratBull then " 2-2 Rev" else if 
TwoOneTwoBull and !ThreeOneTwoBull then " 2-1-2" else if 
ThreeOneTwoBull then "  3-1-2" else if 
ThreeTwoTwoBull then "  3-2-2" else if 
RevStratBull then " 1-2-2" else if
TwoTwoRevBear and !ThreeTwoTwoBear and !RevStratBear then " 2-2 Rev" else if 
TwoOneTwoBear and !ThreeOneTwoBear then " 2-1-2" else if 
ThreeOneTwoBear then "  3-1-2" else if 
ThreeTwoTwoBear then "  3-2-2" else if 
RevStratBear then " 1-2-2" else "-", 
if TwoOneTwoBear or 
ThreeOneTwoBear or 
ThreeTwoTwoBear or 
RevStratBear or 
TwoTwoRevBear then Color.WHITE else Color.BLACK); 

AssignBackgroundColor(if 
TwoOneTwoBull or 
ThreeOneTwoBull or 
ThreeTwoTwoBull or 
RevStratBull or 
TwoTwoRevBull then Color.LIGHT_GREEN else if
TwoOneTwoBear or 
ThreeOneTwoBear or 
ThreeTwoTwoBear or 
RevStratBear or 
TwoTwoRevBear then Color.LIGHT_RED else if 
insidebar then Color.WHITE else if
outsidebar then Color.BLUE
else Color.BLACK); 

