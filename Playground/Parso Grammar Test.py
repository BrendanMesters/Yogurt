import parso

with open("grammar38.txt") as f:
    bnf_text = f.read()

grammar = parso.grammar.PythonGrammar(parso.grammar.parse_version_string("3.8"), bnf_text)

with open("Hello_world.py") as f:
    program_text = f.read()

parseTree = grammar.parse(program_text)