import demo
import unittest
import sys
sys.stdout.flush()


class UnittestSuper(unittest.TestCase, demo.DemoTestPython):

    def setUp(self):
        print("Thiep Lap Cac Truong Hop Cua Unittest")
        sys.stdout.flush()

    def tearDown(self):
        print("Don Dep Cac TH cua Unittest")
        sys.stdout.flush()


class TestNow(UnittestSuper):

    def runTest(self):
        self.return_number_x5(5)
        self.check_type_data("4")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestNow())
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
