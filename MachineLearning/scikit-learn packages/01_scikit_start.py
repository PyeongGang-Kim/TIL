# from sklearn import datasets
# import pandas as pd
# import matplotlib.pyplot as plt

# iris = datasets.load_iris()
# df = pd.DataFrame(iris.data)
# print(df.head())
# # print(iris.data)

# print(iris.target_names)

# print('Type:', type(iris)) 


# plt.title("Plot")
# plt.plot([1, 4, 9, 16])
# plt.show()

# import matplotlib.pyplot as plt
# from numpy.random import rand


# fig, ax = plt.subplots()
# for color in ['red', 'green', 'blue']:
#     n = 750
#     x, y = rand(2, n)
#     scale = 200.0 * rand(n)
#     ax.scatter(x, y, c=color, s=scale, label=color,
#                alpha=0.3, edgecolors='none')

# ax.legend()
# ax.grid(True)

# plt.show()

# from numpy.random import seed
# from numpy.random import randn
# from numpy import mean
# from numpy import var
# from numpy import std
# # seed the random number generator
# seed(1)
# # generate univariate observations
# data = 5 * randn(10000) + 50
# # calculate statistics
# print('Mean: %.3f' % mean(data))
# print('Variance: %.3f' % var(data))
# print('Standard Deviation: %.3f' % std(data))
# print(len(data))

# calculate correlation coefficient
from numpy.random import seed
from numpy.random import randn
from scipy.stats import pearsonr
# seed random number generator
seed(1)
# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 10000)
# calculate Pearson's correlation
corr, p = pearsonr(data1, data2)
# display the correlation
print('Pearsons correlation: %.3f' % corr)
print(p)