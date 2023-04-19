#------------------------------------
# INPUTS
#------------------------------------'
input Alert_Reversals = no;
input aggregationPeriod = AggregationPeriod.DAY;
#------------------------------------
# SCENARIOS
#------------------------------------
def daygreen = close(period = "DAY") > open(period = "DAY");
def dayred = close(period = "DAY") < open(period = "DAY");
def H = high(period = DAY);
def L = low(period = DAY);
def C = close(period = DAY);
def O = open(period = aggregationPeriod);

def insidebar =  (H < H[1] and L > L[1]) or (H == H[1] and L > L[1]) or (H < H[1] and L == L[1]) or (H == H[1] and L == L[1]);
def outsidebar =  H  > H[1] and L <  L[1];

def insidebarup  = insidebar and O < C;
def twoup  = H > H[1] and L >= L[1];
def outsidebarup  = outsidebar and O > C;
def insidebardown  = insidebar and O > C;
def twodown  = H <= H[1] and L < L[1];
def outsidebardown  = outsidebar and O < C;

#------------------------------------
# REVERSALS
#------------------------------------

# Bullish
def TwoOneTwoBull = daygreen and twoup and insidebar[1] and C > O;
def ThreeOneTwoBull = daygreen and twoup and insidebar[1] and outsidebar[2] and C > O;
def ThreeTwoTwoBull = daygreen and twoup and twodown[1] and outsidebar[2] and C > O;
def RevStratBull = daygreen and twoup and twodown[1] and insidebar[2] and C > O;
def TwoTwoRevBull = daygreen and twodown[1] and twoup and C > O;
def two_down_three = twodown and close(period ="DAY") > hl2(period ="DAY")[1];

# Bearish
def TwoOneTwoBear = dayred and twodown and insidebar[1] and C < O;
def ThreeOneTwoBear = dayred and twodown and insidebar[1] and outsidebar[2] and C < O;
def ThreeTwoTwoBear = dayred and twodown and twoup[1] and outsidebar[2] and C < O;
def RevStratBear = dayred and twodown and twoup[1] and insidebar[2] and C < O;
def TwoTwoRevBear = dayred and twoup[1] and twodown and C < O;
def two_up_three = twoup and close(period ="DAY") < hl2(period ="DAY")[1];

# -------------------------
# Labels
# -------------------------
# Bullish
AddLabel(!ThreeTwoTwoBull and !RevStratBull and TwoTwoRevBull, "Day: 2-2 Rev", Color.LIGHT_GREEN);
AddLabel(!ThreeOneTwoBull and TwoOneTwoBull, "Day: 2-1-2", Color.LIGHT_GREEN);
AddLabel(ThreeOneTwoBull, "Day: 3-1-2", Color.LIGHT_GREEN);
AddLabel(ThreeTwoTwoBull, "Day: 3-2-2", Color.LIGHT_GREEN);
AddLabel(RevStratBull, "Day: 1-2-2", Color.LIGHT_GREEN);
AddLabel(two_down_three, "Day: 50% 2go3", Color.LIGHT_GREEN);

# Bearish
AddLabel(!ThreeTwoTwoBear and !RevStratBear and TwoTwoRevBear, "Day: 2-2 Rev", Color.LIGHT_RED);
AddLabel(!ThreeOneTwoBear and TwoOneTwoBear, "Day: 2-1-2", Color.LIGHT_RED);
AddLabel(ThreeOneTwoBear, "Day: 3-1-2", Color.LIGHT_RED);
AddLabel(ThreeTwoTwoBear, "Day: 3-2-2", Color.LIGHT_RED);
AddLabel(RevStratBear, "Day: 1-2-2", Color.LIGHT_RED);
AddLabel(two_up_three, "Day: 50% 2go3", Color.LIGHT_RED);

# -------------------------
# ALERTS
# -------------------------
# Bullish
Alert(Alert_Reversals and !ThreeTwoTwoBull and !RevStratBull and TwoTwoRevBull, "Day: 2-2 Rev", Alert.ONCE, Sound.Bell); 
Alert(Alert_Reversals and !ThreeOneTwoBull and TwoOneTwoBull, "Day: 2-1-2", Alert.ONCE, Sound.Bell);  
Alert(Alert_Reversals and ThreeOneTwoBull, "Day: 3-1-2", Alert.ONCE, Sound.Bell);  
Alert(Alert_Reversals and ThreeTwoTwoBull, "Day: 3-2-2", Alert.ONCE, Sound.Bell);  
Alert(Alert_Reversals and RevStratBull, "Day: 1-2-2", Alert.ONCE, Sound.Bell);  
Alert(Alert_Reversals and two_down_three, "Day: 50%", Alert.ONCE, Sound.Bell);

# Bearish
Alert(Alert_Reversals and !ThreeTwoTwoBear and !RevStratBear and TwoTwoRevBear, "Day: 2-2 Rev", Alert.ONCE, Sound.Bell);
Alert(Alert_Reversals and !ThreeOneTwoBear and TwoOneTwoBear,  "Day: 2-1-2", Alert.ONCE, Sound.Bell);
Alert(Alert_Reversals and ThreeOneTwoBear,  "Day: 3-1-2", Alert.ONCE, Sound.Bell);
Alert(Alert_Reversals and ThreeTwoTwoBear, "Day: 3-2-2", Alert.ONCE, Sound.Bell);
Alert(Alert_Reversals and RevStratBear,  "Day: 1-2-2", Alert.ONCE, Sound.Bell);
Alert(Alert_Reversals and two_up_three, "Day: 50%", Alert.ONCE, Sound.Bell);
