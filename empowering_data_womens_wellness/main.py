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
