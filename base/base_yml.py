import yaml


def yml_data_with_file(file_name):    # 给我这个一个方法 调一个名字就可以
    with open("./data/"+ file_name +".yml", "r") as f:
        yaml.load(f)