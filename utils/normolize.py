
import numpy as np
database = "E:\\meng\\dataset\\2048_pointcloud"
bornbase = "E:\\meng\\dataset\\2048_pointcloud_normalize"

for i in range(1,31):
    file = database + '\\' + 'model' + str(i) + '_2048.txt'
    files = bornbase + '\\' + 'model' + str(i) + '_2048_normalize.txt'
    x_temp = np.loadtxt(file, dtype=np.float32)
    sum_total =x_temp.sum()
    sum_row = x_temp.sum(axis=1)
    sum_col = x_temp.sum(axis=0)
    mean = np.mean(x_temp, axis=0,dtype=np.float32)
    std = np.std(x_temp, axis=0,dtype=np.float32)
    var = std**2
    nom_x1 = (x_temp - mean) / std
    np.savetxt(files,nom_x1,fmt='%.8f')
