#!/usr/bin/python3
def import_variable():
    with open('variable_load_5.py', 'r') as file:
        code = file.read()
        namespace = {}
        exec(code, namespace)
        print(namespace.get('a'))

if __name__ == "__main__":
    import_variable()
