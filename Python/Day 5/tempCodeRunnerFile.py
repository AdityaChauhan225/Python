data = np.random.rand(1000)

plt.hist(data, bins=30,color='teal',edgecolor='black')
plt.title("Histogram if Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")