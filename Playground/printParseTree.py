import parso


def printParseTree(tree, indent = 0):
    for node in tree.children:
        if not str(node).__contains__("PythonNode"):
            print(indent * "  " + str(node))
        if hasattr(node, "children"):
            printParseTree(node, indent + 1)
