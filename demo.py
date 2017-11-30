import os
import unittest


class DemoTestPython():
    def return_number_x5(self, number):
        # return data
        try:
            data = number*5
            print(data)
            if data < 50:
                print("Thoa Man < 50")
            else:
                print("Khong Thoa Man < 50")
                return
            return data
        except AssertionError as err:
            raise AssertionError(err)