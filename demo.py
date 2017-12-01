import os
import unittest


class DemoTestPython():
    def return_number_x5(self, number):
        # return data
        try:
            data = number*5
            print(data)
            sys.stdout.flush()
            if data < 50:
                print("Thoa Man < 50")
            else:
                print("Khong Thoa Man < 50")
                sys.stdout.flush()
                return
            return data
        except AssertionError as err:
            raise AssertionError(err)
    
    def check_type_data(self, data):
        # check type data
        if isinstance(data, str):
            raise AssertionError("Data Khong Phai Kieu Int")
        elif isinstance(data, dict):
            raise AssertionError("Data Khong Phai Kieu Int2")
        elif isinstance(data, list):
            raise AssertionError("Data Khong Phai Kieu Int3")
        else:
            print("Day La Kieu Int")
            sys.stdout.flush()