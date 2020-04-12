import numpy as np
def select_point(dir,index,born_dir,selec_point=2048):
    file_dir = dir + "\\" + "model" + str(index) + ".txt"
    born_file_dir = born_dir + "\\" + "model" + str(index) + "_" + str(selec_point) + '.txt'
    inter_list = list()
    with open(file_dir,'r') as source_file, open(born_file_dir,'w') as destination_file:
        for line in source_file.readlines():
            inter_list.append(line.replace(',',' '))
        for j in range(2048):
            n = np.random.randint(0,len(inter_list))
            destination_file.writelines(inter_list[n])


dir_name = "E:\\meng\\dataset\\new_pointcloud"
dir_born = "E:\\meng\\dataset\\2048_pointcloud"

for k in range(1,31):
    select_point(dir_name,k,dir_born)
    print('Please wait ----{}%'.format(k/31))