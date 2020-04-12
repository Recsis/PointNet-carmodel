import h5py
import numpy as np
from utils import get_classfiy as gc
database = ".\\car-model\\2048_velocity_pointcloud"

def save_h5(h5_filename, data, label, data_dtype=np.float32, label_dtype='uint8'):
    h5_fout = h5py.File(h5_filename)
    h5_fout.create_dataset(
            'data', data=data,
            compression='gzip', compression_opts=1,
            dtype=data_dtype)
    h5_fout.create_dataset(
            'label', data=label,
            compression='gzip', compression_opts=1,
            dtype=label_dtype)
    h5_fout.close()

file = database + '\\' + 'train271_2048_velocity.txt'
x1 = np.loadtxt(file,dtype=np.float32).reshape(1,2048,4)
for i in range(272,301,1):
    files = database + "\\" + 'train' + str(i) + '_2048_velocity.txt'
    x_temp = np.loadtxt(files,dtype=np.float32).reshape(1,2048,4)
    x1 = np.append(x1,x_temp,axis=0)
y_label = gc.get_class()
print(x1.shape,y_label.shape)
save_h5('./test1.h5',data=x1,label=y_label)
#save_h5('./test01.h5',data=x1,label=y_label)