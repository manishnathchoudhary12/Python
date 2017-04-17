import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
weather=pd.read_csv('C:/programming/Analyses/Weather Data/Datasets/yearly_rdu_weather.csv')
del weather['Unnamed: 0']

weather['PRCP_inch']=weather['PRCP'].map(lambda x: round(x*.0393701,2))
weather['TAVG_faren']=weather['TAVG'].map(lambda x: round(x*(9/5) + 32,2))
print(weather.head())

def print_graph_prcp(x,y):  

    fig, ax = plt.subplots(1, 1, figsize=(15, 9))
    ax.plot(x,y,lw=3, label='PRCP', color='green')
    ax.set_xlabel("Year",size=14)
    ax.set_ylabel("PRCP",size=14)
    ax.set_xlim(xmin=x[0], xmax=weather['Year'][len(x)-1])
    ax.legend(loc='best')
    plt.title("Total Yearly RDU Rainfall in Inches", size=16)
    plt.grid(True)
    plt.show()

#print_graph_prcp(weather['Year'], weather['PRCP_inch'])


def print_graph_temp(x,y): 
   
    fig, ax = plt.subplots(1, 1, figsize=(15, 9))
    ax.plot(x,y,lw=3, label='PRCP', color='green')
    ax.set_xlabel("Year",size=14)
    ax.set_ylabel("Avg Temp in F",size=14)
    ax.set_xlim(xmin=x[0], xmax=weather['Year'][len(x)-1])
    ax.legend(loc='best')
    plt.title("Avg RDU Yearly Temp in degrees F", size=16)
    plt.grid(True)
    plt.show()

#print_graph_temp(weather['Year'], weather['TAVG_faren'])


def print_graph_combined(x,y,y2):

    fig, ax = plt.subplots(1, 1, figsize=(18, 9))
    ax.plot(x,y,lw=3, label='PRCP', color='green')
    ax.set_xlabel("Year",size=14)
    ax.set_ylabel("PRCP ",size=14)
    ax.set_xlim(xmin=x[0], xmax=weather['Year'][len(x)-1])
    ax.legend(loc='best')

    ax2=ax.twinx()
    ax2.plot(x,y2, lw=3, label='AVG Temp', color='red')
    ax2.set_xlim(xmin=x[0], xmax=weather['Year'][len(x)-1])
    ax2.legend(loc='upper left')

    plt.title("Total Yearly RDU Rainfall in Inches and AVG temp in Degrees F", size=16)
    plt.grid(True)
    plt.show()

#print_graph_combined(weather['Year'], weather['PRCP_inch'], weather['TAVG_faren'])


