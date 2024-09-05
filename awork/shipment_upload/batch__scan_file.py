import json
import os
import requests


def find_xml_files(directory):
    xml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml') and '_KF' in file:
                xml_files.append(os.path.join(root, file))
    return xml_files


def has_duplicates(lst):
    return len(lst) != len(set(lst))


def main(directory):
    xml_files = find_xml_files(directory)
    for xml_file in xml_files:
        print(f"{xml_file}")


    # file_names = [os.path.basename(file) for file in xml_files]
    # s = set()
    # for xml in xml_files:
    #     short_name = os.path.basename(xml)
    #     if short_name in s:
    #         print(f"Duplicate file name found: {xml}")
    #     s.add(short_name)



if __name__ == "__main__":
    directory_to_search = r'E:\开发文档\202409\01 eagle kaifa 200k'  # 替换为你的文件夹路径
    main(directory_to_search)
