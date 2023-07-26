#  ********** first way ********

import csv
 
files = open("test.csv","w")
writer = csv.writer(files)
writer.writerow(["Title", "Name"]) 
writer.writerow

a = 11
for i in range(a):
    writer.writerow([i])




#  ********** second way  *********** 

# import csv
# with open('first.csv','w') as f1:
#     wri=csv.writer(f1)

#     lis = []
 
#     for i in range(1, 11):
#         if i == 0:
#             lis.append(['Title'])
#         else:
#             lis.append([i])
#     wri.writerows(lis)




#  ******** third way ***********

# with open("numbers.csv", 'w') as fileW:
#     for i in  range(11):
#         fileW.write('%s\n'%i)

