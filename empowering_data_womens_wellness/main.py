# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

#If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell175.csv")

print("Vietnam and Egypt are both lower-middle-income countries, but they have taken different paths in education and economic development.\n")
print("This data represents women living in these two countries and compares female literacy with average household wealth.\n")
input("Press return to continue.\n")

print("While exploring the data, I noticed that women in Vietnam consistently have high literacy rates, even though Vietnam has a lower average wealth index than Egypt.\n")
print("In Egypt, the average wealth index is generally higher, but female literacy varies much more across the data.\n")

print("Based on these findings, my proposed research question is:\n")
print("Why does Vietnam maintain consistently high female literacy despite having a lower average International Wealth Index than Egypt?\n")

vietnamBooleanList = lwd["country_name"]=="Vietnam"
vietnamData = lwd.loc[vietnamBooleanList]

egyptBooleanList = lwd["country_name"]=="Egypt"
egyptData = lwd.loc[egyptBooleanList]

plt.scatter(x="WL_wealth_mean", y="ED_litt_p", data=vietnamData, label="Vietnam")
plt.scatter(x="WL_wealth_mean", y="ED_litt_p", data=egyptData, label="Egypt")

plt.xlabel('Average of the International Wealth Index')
plt.ylabel('Women who are literate (%)')
plt.legend()
plt.show()
