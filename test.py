#perceptron_traning_rule


import csv
file = open("data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
# print(header)
w1 = 0.6 # weight for first criteria
w2 = 0.6 # weight for second criteria
t = 1 # threshold
LR = 0.5 # learning rate
Oa = 0 # actual output
rows = []
flag = True
for row in csvreader:
    rows.append(row)
print(rows)


while flag:
    for i in range(len(rows)):
        for j in rows[i]:
            wx = w1 * float(rows[i][0]) + w2 * float(rows[i][1])
            if wx < t:
                Oa = 0
                if rows[i][2] == Oa:
                    flag = True
                else:
                    flag = False
                    w1 = w1 + ((LR * (t - Oa)) * ((int(rows[i][0]) + int((rows[i][1])))))
                    w2 = w2 + ((LR * (t - Oa)) * ((int(rows[i][0]) + int((rows[i][1])))))
                    break
print("final weights are :- ",w1, w2)
                
            
    
    
        
file.close()
