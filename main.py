from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show,output_file
from bokeh.embed import components
from bokeh.resources import CDN

print()
print("--------------------------------------------------------------------------------------------------------------------------")
print("                                       Welcome to The Stock Vizualizer")
print("--------------------------------------------------------------------------------------------------------------------------")
print()
print("--READ THIS--")
print()
print("1) THE RECTANGLES IN BLUE REPRESENTS DATA OF THE DAYS WHERE CLOSING PRICE WAS GREATER THAN OPENING PRICE")
print("2) THE RECTANGLES IN RED REPRESENTS DATA OF THE DAYS WHERE OPENING PRICE WAS GREATER THAN CLOSING PRICE")
print("3) THE UPPER END OF VERTICALS LINE REPRESENTS THE HIGH VALUE OF THE STOCKS ON RESPECTIVE DATE")
print("4) THE LOWER END OF VERTICALS LINE REPRESENTS THE LOW VALUE OF THE STOCKS ON RESPECTIVE DATE")
print()
print("***************************************************************************************************************************")
startDate=list(map(int,input("Enter the Start Date: e.g (29/6/2019) : ").split("/")))
print()
endDate=list(map(int,input("Enter the End Date: e.g (29/7/2019): ").split("/")))
print()
company=input("Enter the stock symbol of a Listed Company of your choice: ").upper()
print()
# startMonth=int(input())
# startYear=int(input())
# -------------------------------------------------------

start=datetime.datetime(startDate[2],startDate[1],startDate[0])
end=datetime.datetime(endDate[2],endDate[1],endDate[0])
df=data.DataReader(company,'yahoo',start,end)

# --------------------------------------------------------

# date_increased=df.index[df.Close>df.Open]
# date_decreased=df.index[df.Close < df.Open]
# print(abs(df.Close-df.Open))
def inc_dec(c,o):
    if c > o:
        value="Increased"
    elif c == o:
        value = "Equal"
    else:
        value = "Decreased"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

# -----------------------------------------------------------

p=figure(x_axis_type='datetime',width=1000, height=400,sizing_mode='scale_width')
p.title.text="Candelstick Chart for " + company +" stocks"

hours_12=12*60*60*1000

# p.rect(2,4,4,6)
p.segment(df.index,df.High,df.index,df.Low,color="Black")

p.rect(df.index[df.Status=="Increased"],df.Middle[df.Status=="Increased"],
       hours_12, df.Height[df.Status=="Increased"],fill_color="#60b8ff",line_color="black")

p.rect(df.index[df.Status=="Decreased"],df.Middle[df.Status=="Decreased"],
       hours_12, df.Height[df.Status=="Decreased"],fill_color="#ff2c49",line_color="black")

script1,div1=components(p)
cdn_js=CDN.js_files
cdn_css=CDN.css_files

output_file("CS.html")
show(p)