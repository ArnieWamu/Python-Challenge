# Import modules
import os
import csv

# Set path for file
PyBankcsv = os.path.join("Resources", "budget_data.csv")
PyBankcsv = r'C:\Users\arnol\OneDrive\Desktop\Python-Challenge\Instructions\PyBank\Resources\budget_data.csv'
file_to_output = os.path.join("Output", "results.txt")
file_to_output = r'C:\Users\arnol\OneDrive\Desktop\Python-Challenge\Instructions\PyBank\Resources\Output\results.txt'

# Set variables
total_months = 0
total_profit = 0
profit_changes = 0
initial_profit = 0
final_profit = 0
months = []
profit_loss = []

# Open csv file
with open(PyBankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:

        # Total number of months in dataset
        total_months = total_months + 1

        # Total amount of Profit/Losses over the entire period
        final_profit = int(row[1])
        total_profit = total_profit + final_profit

        if (total_months == 1):
            # Make the value of previous month to be equal to current month
            initial_profit = final_profit
            continue

        else:

            # Compute change in profit loss 
            profit_changes = final_profit - initial_profit

            # Append each month to the months list
            months.append(row[0])

            # Append each profit change to the profit_loss list
            profit_loss.append(profit_changes)
            initial_profit = final_profit

    # Sum and average of the changes in profit/loss over the entire period
    sum_profit = sum (profit_loss)
    average_profit = round (sum_profit/(total_months - 1), 2)

    # The greatest increase and decrease in profits (date and amount) over the entire period
    increase_profit = max(profit_loss)
    decrease_profit = min(profit_loss)

    # Locate the index value of greatest increase and decrease in profit/loss over the entire period
    increase_month = profit_loss.index(increase_profit)
    decrease_month = profit_loss.index(decrease_profit)

    # Assign greatest increase and decrease month
    highest = months[increase_month]
    lowest = months[decrease_month]



# open the output file in write mode
with open(file_to_output,'w') as analysis:
# Print results in terminal
    print("Financial Analysis")
    print("\n--------------------------------------------")
    print(f"\nTotal Months: {len(months)}")
    print("Total Profits: " + "$ " + str(total_profit))
    print(f"\nAverage Change: ${round(average_profit,2)}")  
    print(f"\nGreatest Increase: {highest} (${increase_profit})")
    print(f"\nGreatest Decrease: {lowest} (${decrease_profit})")

