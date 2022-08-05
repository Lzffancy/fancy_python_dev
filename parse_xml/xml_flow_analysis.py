"""
desc 解析SmartFlow调用依赖关系
"""

import xml.etree.ElementTree as ET

tree = ET.parse('FlowZhuoFanEcho.xml')
root = tree.getroot()

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


for step in tree.find("PROCESS"):
    print(step.attrib["name"])
    # print(list(step))
    for e in step:
        if e.tag == "SOINFO":
            print(e.attrib["so"])
            so_name = e.attrib["so"]
            if so_name.statrwith("Flow"):



