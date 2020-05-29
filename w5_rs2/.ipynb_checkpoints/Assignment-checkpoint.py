# import csv

# with open("StudentsPerformance2.csv") as f:
#     row_1 = csv.reader(f)
#     listRow = []
#     for content in row_1:
#         listRow += content

# size = len(listRow) 
# idx_list = [idx + 1 for idx, val in
#             enumerate(listRow) if val == ''] 
  
  
# res = [listRow[i: j] for i, j in
#         zip([0] + idx_list, idx_list + 
#         ([size] if idx_list[-1] != size else []))] 
  
# # print result 
# # print("The list after splitting by a value : " + str(res)) 

# size = len(listRow) 
# idx_list = [idx + 1 for idx, val in
#             enumerate(listRow) if val == ''] 
  
  
# res1 = [listRow[i: j] for i, j in
#         zip([0] + idx_list, idx_list + 
#         ([size] if idx_list[-1] != size else []))] 

# # print("The list after splitting by a value : " + str(res1)) 

# idx_list = [idx + 1 for idx, val in
#             enumerate(listRow) if val == ''] 
  
  
# res2 = [listRow[i: j] for i, j in
#         zip([0] + idx_list, idx_list + 
#         ([size] if idx_list[-1] != size else []))] 

# # print("The list after splitting by a value : " + str(res2)) 

# idx_list = [idx + 1 for idx, val in
#             enumerate(listRow) if val == ''] 
  
  
# res3 = [listRow[i: j] for i, j in
#         zip([0] + idx_list, idx_list + 
#         ([size] if idx_list[-1] != size else []))] 

# # print("The list after splitting by a value : " + str(res3)) 

# idx_list = [idx + 1 for idx, val in
#             enumerate(listRow) if val == ''] 
  
  
# res4 = [listRow[i: j] for i, j in
#         zip([0] + idx_list, idx_list + 
#         ([size] if idx_list[-1] != size else []))] 

# # print("The list after splitting by a value : " + str(res4))

# idx_list = [idx + 1 for idx, val in
#             enumerate(listRow) if val == ''] 
  
  
# res5 = [listRow[i: j] for i, j in
#         zip([0] + idx_list, idx_list + 
#         ([size] if idx_list[-1] != size else []))] 

# # print("The list after splitting by a value : " + str(res5)) 

# StudentPerformance = [res1,res2,res3,res4,res5]
# # studentPerformanceLabels = []
# # studentPerformanceLabels.append(res5[1])
# # print(studentPerformanceLabels)

# print(res5[2])
sstr = "gender,female,female,female,male,male,female,female,male,male,female,male,male,female,male,female,female,male,female,male,female,male,female,male,female,male,male,male,female,male,female,female,female,female,male,male,male,female,female,female,male,male,female,female,male,female,male,female,female,female,male,male,male,male,male,female,female,female,male,male,female,male,male,male,female,female,male,male,female,male,female,female,male,female,male,male,male,male,male,female,female,female,male,male,male,male,female,female,female,female,female,female,male,male,male,female,male,male,female,female,female,male,male,female,male,male,female,female,male,female,female,female,male,male,female,female,male,female,female,female,female,female,male,female,male,male,female,male,male,male,female,male,male,male,female,male,male,male,male,female,male,female,female,female,male,male,female,male,male,female,male,male,male,female,male,male,female,female,male,female,male,male,female,male,male,female,female,male,female,female,female,male,male,female,female,female,female,female,female,female,female,male,female,female,female,male,male,male,male,male,female,female,male,female,male,female,male,male,male,female,female,female,female,male,female,male,male,male,male,female,female,male,male,female,male,male,male,female,female,male,male,female,male,female,male,female,female,female,male,male,female,male,male,female,male,male,male,male,female,male,male,male,female,female,male,male,male,male,female,female,male,male,female,female,male,male,female,female,male,female,female,female,male,female,female,male,male,female,female,female,female,male,male,female,female,male,male,female,female,female,male,male,male,female,female,female,male,male,female,male,male,male,male,male,female,male,male,male,male,male,male,male,male,female,male,female,male,male,male,female,female,female,male,male,female,female,male,female,male,male,female,female,female,female,female,female,female,male,male,male,female,male,male,male,male,female,female,male,male,female,female,male,female,female,male,male,female,male,female,male,male,female,male,female,female,female,female,male,female,male,female,female,male,female,female,male,male,male,male,female,female,male,female,male,female,female,male,female,female,female,male,female,male,male,female,female,female,female,female,female,male,male,female,male,male,female,male,female,female,male,male,female,male,female,female,female,female,male,female,female,male,female,male,male,male,female,male,male,male,male,male,female,female,female,female,male,female,male,male,male,male,male,female,male,female,male,male,male,male,male,male,female,female,female,female,male,female,male,male,male,male,female,female,female,male,female,male,female,male,female,male,male,male,female,female,male,female,female,male,female,male,female,female,female,female,female,female,male,male,female,male,male,female,male,male,female,male,male,female,male,male,female,female,female,female,female,male,female,female,female,male,female,female,male,female,female,female,male,male,male,female,male,male,male,female,female,female,female,female,female,female,male,female,male,male,male,male,male,female,female,female,female,female,male,female,male,female,male,female,male,male,male,male,female,female,female,male,female,male,female,male,male,male,female,male,male,female,female,male,female,male,female,female,male,female,male,male,female,female,male,male,male,male,female,female,female,male,male,female,female,female,female,female,female,female,female,female,female,female,female,female,male,male,male,female,female,female,male,male,female,female,female,female,female,male,male,male,female,female,female,female,male,female,male,female,female,female,female,male,male,male,female,male,male,male,female,male,male,male,male,female,male,male,female,female,male,male,female,female,male,female,male,female,female,female,male,female,female,female,female,female,male,female,female,female,female,female,male,male,female,male,male,male,female,female,male,female,female,female,male,male,female,male,female,female,female,female,female,female,male,male,female,male,male,female,male,female,male,male,male,male,female,female,female,female,female,female,female,female,female,male,female,female,male,female,female,male,male,male,male,female,male,female,female,male,female,female,male,female,female,male,female,male,female,male,male,male,female,male,female,male,female,male,female,male,female,male,male,female,male,male,male,female,female,female,male,male,male,male,female,male,male,male,male,female,male,female,male,male,female,male,female,female,male,female,male,female,female,male,female,male,male,male,female,female,male,female,female,female,female,male,female,female,female,female,male,female,female,female,male,female,female,female,male,male,female,female,male,female,male,female,male,male,female,female,female,male,female,female,male,male,male,male,female,male,female,male,female,male,female,female,female,female,male,female,female,male,female,female,female,male,female,female,male,female,male,female,male,female,male,female,female,male,female,male,female,male,male,male,female,male,male,female,female,male,male,female,male,female,male,male,female,female,male,female,male,male,male,male,male,male,male,female,male,male,female,male,male,male,female,female,male,female,female,male,female,female,female,male,female,male,female,female,female,male,female,female,male,female,male,female,male,female,female,female,female,male,male,female,female,male,male,female,female,female,female,female,male,female,female,male,male,female,male,female,male,male,male,female,male,female,male,male,male,male,male,male,male,female,male,male,male,female,male,male,female,female,male,female,male,female,male,female,female,male,female,male,male,female,female,male,female,female,female,female,male,female,male,male,female,female,female,male,female,female,female,female,male,male,male,female,female,male,male,female,female,male,female,male,female,female,male,female,female,female,male,female,male,female,female,female"

listin1=[sstr.split(',')]
print(listin1)