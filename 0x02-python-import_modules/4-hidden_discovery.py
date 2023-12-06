#!/usr/bin/python3
import marshal
import types

def get_names_from_pyc():
    with open('hidden_4.pyc', 'rb') as file:
        code = marshal.load(file)
        if isinstance(code, types.CodeType):
            names = code.co_names
            sorted_names = sorted(set(names))
            for name in sorted_names:
                if not name.startswith('__'):
                    print(name)

if __name__ == "__main__":
    get_names_from_pyc()
