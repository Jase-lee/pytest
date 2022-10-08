import yaml


class YamlUtil:

    def __init__(self, yaml_file):
        """ 通过 init 方法把yaml文件传入到类 """
        self.yaml_file = yaml_file

    # 读取 yaml 文件
    def read_yaml(self):
        """
        读取yaml,对 yaml 文件进行返序列化萌骑士就是把 yaml 格式转化成 dict 格式
        :return:
        """
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            print(value)



if __name__ == '__main__':
    YamlUtil('testapi.yaml').read_yaml()    # {'jack': {'age': 18, 'country': 'USA'}}