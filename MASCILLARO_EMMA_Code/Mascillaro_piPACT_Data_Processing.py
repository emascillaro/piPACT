import pandas as pd
import os
import glob
import re

# Stores list of folders in the "Experiment_2" directory
objects = ["Nothing", "Blue Wallet", "Blue Wallet (RFID)", "Jeans", "Brown Bag", "BWSI Backpack"]

for obj in objects:

    # Stores list of all .csv files
    csvs = glob.glob(f"{obj}/*.csv")
    
    # Iterate over all csv files
    for csv in csvs:
        # Extract distance from csv file name
        distance = int(re.findall(r"_(\d+)ft_", csv)[0])
        print("distance", distance)

        # Create dataframes for each file
        temp_dataframe = pd.read_csv(csv, usecols=["RSSI"])
        temp_dataframe["Distance"] = distance
        temp_dataframe["Object"] = obj
        print(temp_dataframe.head())

        # Compiles all data into one file
        try:
            dataset = dataset.append(temp_dataframe, ignore_index=True)
        except:
            dataset = temp_dataframe

# Save as csv
dataset.to_csv("raw_data.csv")