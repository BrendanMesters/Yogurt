import parso


def printParseTree(tree, indent = 0):
    for node in tree.children:
        if True or not str(node).__contains__("PythonNode"):
            print(indent * "  " + str(node))
        if hasattr(node, "children"):
            printParseTree(node, indent + 1)


with open("YogurtGrammar.txt") as f:
    bnf_text = f.read()

grammar = parso.grammar.PythonGrammar(parso.grammar.parse_version_string("3.8"), bnf_text)

with open("Yogurt.py") as f:
    program_text = f.read()

parseTree = grammar.parse(program_text)
#foo = parseTree.children


printParseTree(parseTree)

print(f"the ParseTree = {type(parseTree)}")