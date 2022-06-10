import yaml
import os


def get_object_path():
    return os.getcwd()


def read_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, "r", encoding="utf-8") as f:
        res = yaml.load(stream=f, Loader=yaml.FullLoader)
        return res


def write_yaml(yaml_path, data):
    with open(get_object_path() + "/" + yaml_path, 'a', encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def clear_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, 'w', encoding='utf-8') as f:
        f.truncate()


def read_yaml_key(yaml_path, key):
    with open(get_object_path() + "/" + yaml_path, "r", encoding="utf-8") as f:
        res = yaml.load(stream=f, Loader=yaml.FullLoader)
        return res[key]

if __name__ == '__main__':
    a = get_object_path()
    print(a)