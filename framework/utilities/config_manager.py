import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))


def convert_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


config_data = convert_json(dir_path + "\\..\\resources\\config.json")
test_data = convert_json(dir_path + "\\..\\..\\project\\resources\\test_data.json")
