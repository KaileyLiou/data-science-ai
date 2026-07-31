# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWC_utilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell175.csv")

#Change x here:
# plt.hist(x='HD_women_size_mean', data=lwd, edgecolor='white', bins=10)
# plt.hist(x='ED_litt_p', data=lwd, edgecolor='white', bins=10)
# plt.hist(x='WL_wealth_mean', data=lwd, edgecolor='white', bins=10)
# plt.hist(x='DP_decide_money_p', data=lwd, edgecolor='white', bins=10)
# plt.hist(x='DV_phys_partner_p', data=lwd, edgecolor='white', bins=10)
plt.hist(x='RH_children_born_mean', data=lwd, edgecolor='white', bins=10)

#Change x-label here:
# plt.xlabel("Average number of household members")
# plt.xlabel("Women who are literate (%)")
# plt.xlabel("Average of the International Wealth Index")
# plt.xlabel("Women currently married or in union who were paid cash for their work, who decide alone how their money earned is spent (%)")
# plt.xlabel("Women who ever experienced physical violence by partner (%)")
plt.xlabel("Average number of children ever born")

plt.ylabel("Number of Data Points")
plt.show()
