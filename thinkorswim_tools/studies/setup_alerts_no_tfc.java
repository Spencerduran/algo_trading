#------------------------------------
# INPUTS
#------------------------------------
input Alert_Reversals = yes;
input aggregationPeriod = AggregationPeriod.FIFTEEN_MIN;
#------------------------------------
# SCENARIOS
#------------------------------------
def H = high(period = aggregationPeriod);
def L = low(period = aggregationPeriod);
def C = close(period = aggregationPeriod);
def O = open(period = aggregationPeriod);

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
def TwoOneTwoBull = twoup and insidebar[1] and twodown[1] and C > O;
def ThreeOneTwoBull = twoup and insidebar[1] and outsidebar[2] and C > O;
def ThreeTwoTwoBull = twoup and twodown[1] and outsidebar[2] and C > O;
def RevStratBull = twoup and twodown[1] and insidebar[2] and C > O;
def TwoTwoRevBull = twodown[1] and twoup and C > O;

# Bearish
def TwoOneTwoBear = twodown and insidebar[1] and twoup[2] and C < O;
def ThreeOneTwoBear = twodown and insidebar[1] and outsidebar[2] and C < O;
def ThreeTwoTwoBear = twodown and twoup[1] and outsidebar[2] and C < O;
def RevStratBear = twodown and twoup[1] and insidebar[2] and C < O;
def TwoTwoRevBear = twoup[1] and twodown and C < O;

# Bullish
AddLabel(!ThreeTwoTwoBull and !RevStratBull and TwoTwoRevBull, "15: 2-2 Rev", Color.LIGHT_GREEN);
AddLabel(!ThreeOneTwoBull and TwoOneTwoBull, "15: 2-1-2", Color.LIGHT_GREEN);
AddLabel(ThreeOneTwoBull, "15: 3-1-2", Color.LIGHT_GREEN);
AddLabel(ThreeTwoTwoBull, "15: 3-2-2", Color.LIGHT_GREEN);
AddLabel(RevStratBull, "15: 1-2-2", Color.LIGHT_GREEN);

# Bearish
AddLabel(!ThreeTwoTwoBear and !RevStratBear and TwoTwoRevBear, "15: 2-2 Rev", Color.LIGHT_RED);
AddLabel(!ThreeOneTwoBear and TwoOneTwoBear, "15: 2-1-2", Color.LIGHT_RED);
AddLabel(ThreeOneTwoBear, "15: 3-1-2", Color.LIGHT_RED);
AddLabel(ThreeTwoTwoBear, "15: 3-2-2", Color.LIGHT_RED);
AddLabel(RevStratBear, "15: 1-2-2", Color.LIGHT_RED);


# -------------------------
# Alerts
# -------------------------
# Bullish
Alert(Alert_Reversals and !ThreeTwoTwoBull and !RevStratBull and TwoTwoRevBull, "15: 2-2 Rev", Alert.BAR, Sound.Bell); 
Alert(Alert_Reversals and !ThreeOneTwoBull and TwoOneTwoBull, "15: 2-1-2", Alert.BAR, Sound.Bell);  
Alert(Alert_Reversals and ThreeOneTwoBull, "15: 3-1-2", Alert.BAR, Sound.Bell);  
Alert(Alert_Reversals and ThreeTwoTwoBull, "15: 3-2-2", Alert.BAR, Sound.Bell);  
Alert(Alert_Reversals and RevStratBull, "15: 1-2-2", Alert.BAR, Sound.Bell);  

# Bearish
Alert(Alert_Reversals and !ThreeTwoTwoBear and !RevStratBear and TwoTwoRevBear, "15: 2-2 Rev", Alert.BAR, Sound.Bell);
Alert(Alert_Reversals and !ThreeOneTwoBear and TwoOneTwoBear,  "15: 2-1-2", Alert.BAR, Sound.Bell);
Alert(Alert_Reversals and ThreeOneTwoBear,  "15: 3-1-2", Alert.BAR, Sound.Bell);
Alert(Alert_Reversals and ThreeTwoTwoBear, "15: 3-2-2", Alert.BAR, Sound.Bell);
Alert(Alert_Reversals and RevStratBear,  "15: 1-2-2", Alert.BAR, Sound.Bell);
