#!/usr/bin/env python


import os


def simple_test():
    here = os.path.dirname(os.path.realpath(__file__))
    www = os.path.join(here, "www")
    assert os.path.exists(www)


if __name__ == "__main__":
    simple_test()
    print("Test passed. www directory exists.")

