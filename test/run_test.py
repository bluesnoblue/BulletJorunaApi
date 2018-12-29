import unittest
cases = unittest.defaultTestLoader.discover("./case/", pattern="test*.py")
runner = unittest.TextTestRunner()
runner.run(cases)
