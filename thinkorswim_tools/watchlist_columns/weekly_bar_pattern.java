#------------------------------------
# SCENARIOS
#------------------------------------
def H = high;
def L = low;
def C = close;
def O = open;

def insidebar =  (H < H[1] and L > L[1]) or (H == H[1] and L > L[1]) or (H < H[1] and L == L[1]) or (H == H[1] and L == L[1]);
def outsidebar =  H  > H[1] and L <  L[1];
def twoup  = H > H[1] and L >= L[1];
def twodown  = H <= H[1] and L < L[1];

def current_week = if insidebar then 1 else if outsidebar then 3 else if twoup then 2 else if twodown then 4 else 0;
def last_week = if insidebar[1] then 1 else if outsidebar[1] then 3 else if (twoup[1] or twodown[1]) then 2 else 0;
def first_week = if insidebar[2] then 1 else if outsidebar[2] then 3 else if (twoup[2] or twodown[2]) then 2 else 0;


AddLabel(yes, 
Concat(if first_week == 3 then "3 " else if first_week == 1 then "1 " else if first_week == 2 then "2u" else "2d", 
Concat(" - ", 
Concat(if last_week == 3 then " 3 " else if last_week == 1 then " 1 " else if last_week == 2 then "2u" else "2d", 
Concat(" - ", 
Concat(if current_week == 3 then " 3" else if current_week == 1 then " 1" else if current_week == 2 then "2u" else "2d", 
"  "))))), if close < open and !insidebar then color.WHITE else Color.BLACK);

AssignBackgroundColor(if insidebar then Color.WHITE else if
C > O then Color.LIGHT_GREEN else if C < O then Color.LIGHT_RED else Color.BLACK); 
