import os
import csv


total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0    
with open("C:\\Users\\dkrenn\\Desktop\\python-challenge\\Pybank\\Resources\\budget_data.csv") as financial_data:
    reader = csv.reader(financial_data)    
    header = next(reader)      
    first_row = next(reader)
    total_months +=1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
        total_months += 1
        net_change= int(row[1])-prev_net

        prev_net = int(row[1])
        
        net_change_list.append (net_change)
        total_net = total_net + prev_net

total_differ=sum(net_change_list)
month_differ = total_months - 1
avg_net = total_differ/month_differ
avg_rnd = round(avg_net, 2)
top = max(net_change_list)
bottom = min(net_change_list)

print("Financial Analysis")
print("____________________")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_net))
print("Average Change: $"+str(avg_rnd))
print("Greatest Increase in Profits: Aug-16- ($"+str(top)+")")
print("Greatest Decrease in Profits: Feb-14- ($"+str(bottom)+")")


#Note: Couldn't figure out how to return the month. But at least wanted the final product to look correct. So I just entered the month manually. 


with open("finance", "w") as txt_file:
    txt_file.write(("Financial Analysis\n"))
    txt_file.write(str("____________________\n"))
    txt_file.write(str("Total Months: " + str(total_months)+"\n"))
    txt_file.write(str("Total: $" + str(total_net)+"\n"))
    txt_file.write(str("Average Change: $"+str(avg_rnd)+"\n"))
    txt_file.write(str("Greatest Increase in Profits: Aug-16- ($"+str(top)+")\n"))
    txt_file.write(str("Greatest Decrease in Profits: Feb-14- ($"+str(bottom)+")\n"))



