# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


#Import Dependencies
import os
import csv

#Begin my function
def PyBank(data):
    #Create csv variable to store my data more permanently (in case I want to loop through it more than once)
    # csv = []
    # for row in data:
    #     csv.append(row)
    
    #Total number of months in the dataset
    months = 0
    #Net total amount of "Profit/Losses"
    net_total = 0
    #List of weekly profit/losses over entire period
    weekly_amount = []
    #List of each week
    weeks = []

    # for row in csv:
    for row in data:
        months += 1
        net_total = net_total + int(row[1])
        weekly_amount.append(row[1])
        weeks.append(row[0])

    #Generate list of week to week changes which we can caluclate the average, min, and max from
    weekly_change = []
    #for amount in weekly_amount:
    for i in range(len(weekly_amount)-1): # "-1" so we keep the index in bounds
        weekly_change.append(int(weekly_amount[i+1])-int(weekly_amount[i]))
    
    #Now let's loop through weekly_change list to determine min and max
    for j in range(len(weekly_change)-1): # once again, "-1" so we keep the index in bounds
        if j == 0:
            #Initialize my max and min values
            max_change = weekly_change[0]
            min_change = weekly_change[0]
        else: # j == 1 through length of (weekly_change - 1)
            if weekly_change[j] > max_change:
                max_change = weekly_change[j]
                #so the max/min week will correspond to index j+1 in the list "weeks" since there is one less item in the weekly_change list
                max_week = weeks[j+1]
            elif weekly_change[j] < min_change:
                min_change = weekly_change[j]
                min_week = weeks[j+1]
            else: #if they're equal
                max_change = max_change
                min_change = min_change
    ## Can I just just do something like: min(weekly_change) or max(weekly_change)??? I guess that wouldn't give me the corresponding week of the max/min though

    avg_change  = round(sum(weekly_change)/len(weekly_change),2)

    return [months,net_total,avg_change,max_change,min_change,max_week,min_week]


#Set the path for my csv file
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #Skip the header line
    header = next(csvreader)
    analysis = PyBank(csvreader)

print(f"Total months: {analysis[0]}\nNet Total Profit/Loss: ${analysis[1]}\nAverage Weekly Change: ${analysis[2]}\nMax Weekly Change: {analysis[5]} (${analysis[3]})\nMin Weekly Change: {analysis[6]} (${analysis[4]})")

with open("PyBank.txt","w") as text_file:
    text_file.write(f"Total months: {analysis[0]}\nNet Total Profit/Loss: ${analysis[1]}\nAverage Weekly Change: ${analysis[2]}\nMax Weekly Change: {analysis[5]} (${analysis[3]})\nMin Weekly Change: {analysis[6]} (${analysis[4]})")
             


        
