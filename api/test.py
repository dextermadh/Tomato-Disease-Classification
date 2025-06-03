import os

def get_class_names(path):
    class_directories = os.listdir(path)
    str = ''
    class_names = []

    for i in range(len(class_directories)):
        for j in range(len(class_directories[i].split('_'))):
            str = str + ' ' + class_directories[i].split('_')[j]
        class_names.append(str)
        str = ''

    print(class_names)
    print(len(class_names))

classes_path = '../training/PlantVillage'

get_class_names(classes_path)