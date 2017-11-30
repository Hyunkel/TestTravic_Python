import demo
import unittest


class UnittestSuper(unittest.TestCase, demo.DemoTestPython):

    def setUp(self):
        print("Thiep Lap Cac Truong Hop Cua Unittest")

    def tearDown(self):
        print("Don Dep Cac TH cua Unittest")


class TestNow(UnittestSuper):

    def runTest(self):
        self.return_number_x5(5)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestNow())
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
