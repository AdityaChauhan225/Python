### MATPLOTLIB

'''
is a powerfull plotting library commonly used for static animated or interactive visualization
'''

import matplotlib.pyplot as plt
import numpy as np
##### Line plot

# x=[1,2,3,4,5]
# y=[10,15,13,18,16]

# # plt.plot(x,y)
# plt.title("Basic line plot")
# plt.xlabel("x-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)

# # plt.plot(x,y,color="blue",marker='s',linestyle='--',linewidth=2) # marker can be ^ (triangle) or s (square)

# y1=[1,4,9,16,25]
# y2=[25,16,9,4,1]
# plt.plot(x,y1,label='Ascending')
# plt.plot(x,y2,label='Descending')
# plt.legend()


##### Bar Graph

# categories=['A','B','C','D']
# Values=[10,24,36,18]
# # plt.bar(categories,Values,color="green") # for vertical
# plt.barh(categories,Values,color="green") # for Horizontal

#### Scatter Plot

# x=[5,7,8,7,2,17,2,9]
# y=[99,86,87,88,100,86,103,87]
# plt.scatter(x,y,color="purple",marker='s')
# plt.title("Scatter plot example")
# plt.xlabel("X values")
# plt.ylabel("Y values")

# # Histogram
# data = np.random.randn(1000)

# plt.hist(data, bins=30,color='teal',edgecolor='black')
# plt.title("Histogram if Random Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")


# #### Pie chart 
# series = [30,40,15,15]
# lables= ['Python','java','c++','JavaScript']
# plt.pie(series,labels=lables,autopct='%1.1f%%',startangle=90)
# plt.title("programming language usage")
# plt.axis('equal')

# #### Subplot
# x=[1,2,3,4,5]
# y=[5,7,4,6,8]

# plt.subplot(1,2,1) # 1 row 2 columns, 1st plot
# plt.plot(x,y)
# plt.subplot(1,2,2) # 1 row 2 columns, 2nd plot
# plt.bar(x,y)
# plt.tight_layout()

plt.savefig("Plot.png")

plt.show()

