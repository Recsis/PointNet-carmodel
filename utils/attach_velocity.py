def attach_velocity(dir,index,index2,born_dir):
    velocity = [' 10.0',' 15.0',' 20.0',' 25.0',' 30.0',' 35.0',' 40.0',' 45.0',' 50.0',' 55.0']
    file_dir = dir + "\\" + "model" + str(index) + "_2048_normalize.txt"
    inter_list = list()
    born_file_dir = born_dir + "\\" + "train" + str(10*(index-1) + index2 + 1) + "_2048_velocity.txt"
    with open(file_dir,'r') as source_file, open(born_file_dir,'w') as destination_file:
        for line in source_file.readlines():
            line = line.strip('\n')
            line += velocity[index2]
            inter_list.append(line)
        for element in inter_list:
            destination_file.writelines(element + '\n')

dir_name = "E:\\meng\\dataset\\2048_pointcloud_normalize"
dir_born = "E:\\meng\\dataset\\2048_velocity_pointcloud"

for k in range(1,31):
    for p in range(0,10):
        attach_velocity(dir_name,k,p,dir_born)
        print('Please wait ----{}%'.format(k*(p+1)/30*10))


