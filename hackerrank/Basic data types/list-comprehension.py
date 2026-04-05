if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Traditional method
# output_list = []  
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i + j + k != n:
#                 output_list.append([i,j,k])
# print(output_list)

# List comprehension
output_list = [[i,j,k] 
               for i in range(x + 1)
               for j in range(y + 1)
               for k in range(z + 1)
               if i +  + z != n
              ]
print(output_list)