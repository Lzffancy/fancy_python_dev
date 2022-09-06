import json


def generate_tree(source, parent):
    tree_data = []
    for item in source:
        if item["parent"] == parent:
            if item["name"].startswith("Cmd"):
                tree_data.append(item)
            else:
                item["child"] = generate_tree(source, item["id"])
                tree_data.append(item)
    return tree_data


if __name__ == '__main__':
    permission_source =[{'id': 1, 'name': 'FlowZhuoFanEcho', 'parent': 0}, {'id': 2, 'name': 'CmdZhuoFanEcho111', 'parent': 1}, {'id': 2, 'name': 'CmdZhuoFanEcho222', 'parent': 1}, {'id': 2, 'name': 'FlowBeCallZhuoFanEcho', 'parent': 1}, {'id': 3, 'name': 'CmdZhuoFanEchoinbecall', 'parent': 2}]

    permission_tree = generate_tree(permission_source, 0)

    print(json.dumps(permission_tree, ensure_ascii=False))
