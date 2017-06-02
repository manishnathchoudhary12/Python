import numpy as np
from itertools import accumulate
import matplotlib.pyplot as plt

#location of the prize (door 0,1,2) for nsim simulations
def simulate_prizedoor(nsim):
    result=np.random.randint(0,3,nsim)
    return result
prizedoors=simulate_prizedoor(100000)

#simulate contestant's guesses for nsim simulations
#Guess all zero here
def simulate_guess(nsim):
    result=np.random.randint(0,3,nsim)
    return(result)
guesses=simulate_guess(100000)

#Simulate the opening of a "goat door" that the contestant doesn't open
def goat_door(prizedoors, guesses):
    result=np.random.randint(0,3, prizedoors.size)
    while True:
        bad = (result==prizedoors) | (result==guesses)
        if not bad.any():
            return result
        result[bad]=np.random.randint(0,3,bad.sum())
goat=goat_door(prizedoors, guesses)

#Always switch doors
def switch_guess(guesses, goatdoors):
    result=np.random.randint(0,3,guesses.size)
    while True:
        bad = (result==guesses) | (result==goatdoors)
        if not bad.any():
            return result
        result[bad]=np.random.randint(0,3,bad.sum())
switch_guess=switch_guess(guesses, goat)

#High level win percentage
def win_percentage(guess_vector, prizedoors):
    return(100*(guess_vector == prizedoors).mean())

print("win percent don't change", win_percentage(guesses, prizedoors))
print("win percent changing", win_percentage(switch_guess, prizedoors))

#Cumulative chance of winning over total simulations
def cumulative_win(guess_vector, prizedoors):
    cumulative_perc=[]
    cumulative_total=list(accumulate((guess_vector==prizedoors).astype(float)))
    
    for i in range(len(cumulative_total)):
        cumulative_perc.append(cumulative_total[i]/(i+1))
   
    return cumulative_perc

pctswitch = cumulative_win(switch_guess, prizedoors)
pctnever = cumulative_win(guesses, prizedoors)

def print_graph(nsim,y,y2,):  #x=numsim
    x=list(range(nsim))

    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    ax.plot(x,y,lw=3, label='Always', color='green')
    ax.plot(x,y2,lw=3, label='Never',color='blue',alpha=0.5)
    ax.fill_between(x,y2,y, facecolor='green',alpha=0.6)
    ax.fill_between(x,0,y2, facecolor='blue',alpha=0.5)
    ax.set_xlabel("Iterations",size=14)
    ax.set_ylabel("Win Pct",size=14)
    ax.legend(loc='best')
    plt.title("Cumulative chances of winning on Let's Make a Deal", size=16)
    plt.grid(True)
    plt.show()

print_graph(100000,pctswitch, pctnever)