import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

energy=pd.read_csv('C:/programming/Analyses/Weather Data/Datasets/LSU_Energy_Usage.csv')
energy=energy.iloc[::-1]
energy['Month']=energy['Month'].map(lambda x: x[-3:]+ " " + "2016")


weather=pd.read_csv('C:/programming/Analyses/Weather Data/Datasets/LSU_Weather.csv')
weather['Month']=weather['year'].map(lambda x: x[:7])
weather['PRCP_inch']=weather['PRCP'].map(lambda x: round(x*.0393701,2))
weather['TAVG_faren']=weather['TAVG'].map(lambda x: round(x*(9/5) + 32,2))

del weather['year']
del weather['Unnamed: 0']

def print_graph(x,y,y2,y3):  
    x_scale=list(range(1,len(x)+1))

    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    plt.xticks(x_scale,x)

    l1=ax.plot(x_scale,y,lw=3, label='Monthly Rain Amount', color='green')
    l2=ax.plot(x_scale,y2,lw=3, label='AVG Daily Energy Usage', color='red')

    ax2=ax.twinx()
    l3=ax2.plot(x_scale, y3, label='AVG temp in faren', color='blue')

    l4=l1+l2+l3
    labels=[l.get_label() for l in l4]

    ax.legend(l4, labels, loc=0)
    ax.set_xlabel("Month",size=14)
    ax.set_ylabel("Monthly PRCP & Daily Energy Usage",size=14)
    ax2.set_ylabel("AVG temp in faren", size=14)

    plt.title("Monthly LSU Rainfall", size=16)
    plt.grid(True)
    plt.show()

#print_graph(energy['Month'], weather['PRCP_inch'], energy['Avg. Daily Usage'], weather['TAVG_faren'])

