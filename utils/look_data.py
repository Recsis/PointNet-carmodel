from utils import data_prep_util as da

filename = '.\\data\\meng_2048_velocity\\train0.h5'
f ='.\\data\\modelnet40_ply_hdf5_2048\\ply_data_train0.h5'
data, label = da.load_h5(filename)
datas, labels = da.load_h5(f)
#print(data,label)
print(data)
print(label)

# print(datas)
# print(labels.dtype)