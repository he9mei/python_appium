# encoding=utf-8
import unittest


if __name__ == "__main__":
    suit = unittest.defaultTestLoader.discover("./test_case", pattern="test*.py")
    runner = unittest.TextTestRunner()
    runner.run(suit)
