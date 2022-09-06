"""
desc 解析SmartFlow调用依赖关系
"""
import argparse
import json
import xml.etree.ElementTree as ET
import sys
from collections import namedtuple
import pprint

# tree = ET.parse('FlowZhuoFanEcho.xml')
# root = tree.getroot()

# print(root.tag)
# print(root.attrib)
# print(root)
#
# print(list(root.iter()))
#
# print(root.tag, root.attrib["name"])
#
# print(tree.find("PROCESS"))
# print(tree.find("PROCESS").find("STEP"))
# print(tree.find("PROCESS").find("STEP").find("SOINFO"))
# soinfo_iter = tree.find("PROCESS").find("STEP").find("SOINFO").iter()
#
# for so in soinfo_iter:
#     print(so.attrib.get("so"))


Xml = namedtuple("Xml", ["id", "xml_name", "parent", "child"])


class Xml_obj:
    def __init__(self, id, name, parent, child):
        self.id = id
        self.name = name
        self.parent = parent
        self.child = child


xml_list = []


def parse_flow(flow_file, level_id=1):
    tree_data = ET.parse(flow_file)
    root = tree_data.getroot()
    # print(root.tag, root.attrib["name"])
    if level_id == 1:
        # 根节点为 0 ,在以第一层时，parent = 0 ,本层id = 1
        xml_obj = {"id": level_id, "name": root.attrib["name"], "parent": 0}
        xml_list.append(xml_obj)
    else:
        xml_obj = {"id": level_id, "name": root.attrib["name"], "parent": level_id - 1}
        xml_list.append(xml_obj)

    for step in tree_data.find("PROCESS"):
        # print(step.attrib["name"])
        flow_step = root.attrib["name"] + "--> " + step.attrib["name"] + "-->" + str(level_id)
        print(flow_step)
        for so in step:
            if so.tag == "SOINFO":
                so_name = so.attrib["so"]
                print(so_name)
                if so_name.startswith("Flow"):
                    try:
                        parse_flow(so_name + ".xml", level_id + 1)
                    except FileNotFoundError:
                        print(f"{so_name}.xml : 未找到！")
                    finally:
                        pass
                elif so_name.startswith("Cmd"):
                    so_obj = {"id": level_id + 1, "name": so_name, "parent": level_id}
                    xml_list.append(so_obj)
    return xml_list


def generate_tree(nodes, parent):
    tree_data = []
    for item in nodes:
        if item["parent"] == parent:
            if item["name"].startswith("Cmd"):
                tree_data.append(item)
            else:
                item["child"] = generate_tree(nodes, item["id"])
                tree_data.append(item)
    return tree_data


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='输入xml 如FlowMiniConfPlateformAfterPredict.xml,自动分析其调用关系')
    # parser.add_argument('-xml', type=str, help='输入xml 如FlowMiniConfPlateformAfterPredict.xml')
    # args = parser.parse_args()
    # parse_flow(args.xml)
    data_lis = parse_flow("FlowZhuoFanEcho.xml")
    print(data_lis)
    print("源数据")
    tree_data = generate_tree(data_lis, 0)
    # pprint.pprint(tree_data)
    #
    # # pp = pprint.PrettyPrinter(indent=5,width=200)
    print(json.dumps(tree_data, ensure_ascii=False, sort_keys=True))


