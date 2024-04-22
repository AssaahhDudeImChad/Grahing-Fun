import numpy as np
import matplotlib.pyplot as plt

def find_z(num, ynum):
    if ynum == 2019:
        #print(num, ", ",  5.7445*num**5 - 13.113*num**4 + 10.66*num**3 - 2.7343*num**2 + 0.4187*num - 0.0171)
        return 5.7445*num**5 - 13.113*num**4 + 10.66*num**3 - 2.7343*num**2 + 0.4187*num - 0.0171
    elif(ynum == 2020):
        return 5.7531*num**5 - 12.967*num**4 + 10.326*num**3 - 2.5344*num**2 + 0.396*num - 0.0163
    elif(ynum == 2021):
        return 6.2332*num**5 - 14.268*num**4 + 11.641*num**3 - 3.1172*num**2 + 0.4876*num - 0.021
    elif(ynum == 2022):
        return 6.9042*num**5 - 16.136*num**4 + 13.583*num**3 - 3.9804*num**2 + 0.6154*num - 0.0266

    elif(ynum == 2023):
        return 7.3222*num**5 - 17.259*num**4 + 14.709*num**3 - 4.4785*num**2 + 0.6962*num - 0.0307
    else:
        return 0
    


x = np.arange(0, 1, 0.01).tolist()
y = [2019, 2020, 2021, 2022, 2023]
X, Y = np.meshgrid(x, y)

z = []
for i in y:
    foo = []
    for k in x:
        foo.append(find_z(k, i))

    z.append(foo)

Z = np.array(z)

print(z)
# create plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(Y, X, Z, cmap='coolwarm')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
