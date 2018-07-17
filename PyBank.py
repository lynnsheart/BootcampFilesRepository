#Dependencies
import os
import csv

csvPath = os.path.join('budget_data.csv')
print(csvPath)

#File to load
RevCalc = 0
with open("budget_data.csv") as dataFile:
    type(dataFile)
    reader = csv.DictReader(dataFile)
    print(type(reader))
    print('----------')
  
    for dataItem in reader:
        thisRev = int (dataItem["Revenue"])
        RevCalc = RevCalc + thisRev
print(RevCalc)

RevCalc = 0
#Read CSV and convert into a list of dictionaries
with open("budget_data.csv") as dataFile:
    type(dataFile)
    reader = csv.DictReader(dataFile)
    print(type(reader))
    print('----------')
    
    for dataItem in reader:
        print(dataItem)

#Total Revenue parameters
ttlMnths = 0
ttlRev = 0
mnthofChg = []
revChgList = []
greatestInc = ["", 0]
greatestDec = ["", 999999999999999999999999999]

#Read csv and convert to a list of dictionaries
with open("budget_data.csv") as revData:
    reader = csv.DictReader(revData)
    
    for row in reader:
        
        #Track the Total Months
        ttlMnths = ttlMnths + 1
        ttlRev = ttlRev + int(row["Revenue"])
        
        #Track the Total Revenue Change
        prevRev = int(row["Revenue"])
        revChg = int(row["Revenue"]) - prevRev
        revChgList.append(revChg)
        mnthofChg.append(row["Date"])
        
        #Calculate Greatest Increase
        if (revChg > greatestInc[1]):
            greatestInc[0] = row["Date"]
            greatestInc[1] = revChg
            
        #Calculate Greatest Decrease
        if (revChg < greatestDec[1]):
            greatestDec[0] = row["Date"]
            greatestDec[1] = revChg
            
#Calculate Average Revenue Change
revenueAvg = sum (revChgList)/len (revChgList)

#Generate output summary
output = (
            f"\nFinancial Analysis\n"
            f"--------------------\n"
            f"Total Months: {ttlMnths}\n"
            f"Total Revenue: ${ttlRev}\n"
            f"Average Revenue Change: ${revenueAvg}\n"
            f"Greatest Increase in Revenue: {greatestInc[0]} (${greatestInc[1]})\n"
            f"Greatest Decrease in Revenue: {greatestDec[0]} (${greatestDec[1]})\n")

#Print output to Terminal
print(output)

print(ttlMnths)
print(ttlRev)