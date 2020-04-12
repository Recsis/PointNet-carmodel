import numpy as np

labelfile = ".\\car-model\\test1.txt"
def get_class():
    y_label = np.loadtxt(labelfile,dtype=np.float32).reshape(30,1)
    #print(y_label)
    #print(y_label.shape)
    for i in range(y_label.shape[0]):
        if 0.16 < y_label[i] <= 0.20:
            y_label[i] = 0
        elif 0.20 < y_label[i] <= 0.24:
            y_label[i] = 1
        elif 0.24 < y_label[i] <= 0.28:
            y_label[i] =2
        elif 0.28 < y_label[i] <= 0.34:
            y_label[i] =3
        elif 0.34 < y_label[i] <= 0.46:
            y_label[i] =4
    y_label = np.int8(y_label)
    return y_label
y = get_class()
