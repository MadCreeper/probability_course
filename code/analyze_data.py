import csv
import numpy as np
import pandas as pd


day_cycle = 108
total_days = 10
tot_canteens = 10

avg_day = np.zeros((day_cycle, tot_canteens))

if __name__ == "__main__":
    df = pd.read_csv('data_raw.csv', sep=',',header=None)
    #print(df.values)
    data = df.values
    for st_time in range(0, (total_days - 1) * day_cycle, day_cycle):
        avg_day += data[st_time : st_time + day_cycle]
    
    avg_day /= total_days
    print(avg_day)
    np.savetxt("average_day.csv", avg_day, delimiter=",")
    """
    if (idx - 1) % day_cycle == 0 or (idx - 108) % day_cycle == 0:
        print(idx, line[2:4])
    """
            
            