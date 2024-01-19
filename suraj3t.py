import random
import math
node = []
for i in range(0,10):
     x = random.randint(0,10)
     y = random.randint(0,50)
     node.append([x,y])
print(node)
d_mat = []
for i in range(0,10):
     d_mat.append([0]*10)
     
for i in range(0,10):
     for j in range(0,10):
          dis = math.sqrt(math.pow((node[i][0]-node[j][0]),2))+(math.pow((node[i][-1]-node[j][-1]),2))
          d_mat[i][j]=dis
print(d_mat)

area_nearby = int(input("Enter the neighbour area"))
router = []
print(router)
for i in range(0,10):
     for j in range(0,10):
          app = []
          if area_nearby<= d_mat[i][j]:
               app.append(j)
     router.append(app)
print(router)


          
     
          
     
     
     