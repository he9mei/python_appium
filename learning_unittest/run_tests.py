import unittest

top_level_dir="/Users/hehuaimei/PycharmProjects/python_appium/learning_unittest"
start_dir="./test_case"
pattern="test*.py"

suit=unittest.defaultTestLoader.discover(start_dir,pattern,top_level_dir)

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(suit)