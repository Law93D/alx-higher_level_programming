#!/usr/bin/python3
def raise_exception_msg(message=""):
    class CustomNameError(NameError):
        def __init__(self, message):
            self.message = message

    try:
        raise CustomNameError(message)
    except CustomNameError as ne:
        print(ne.message)
