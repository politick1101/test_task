import os
from time import time
from psutil import virtual_memory
from random import randint
from abc import abstractmethod


class TestSystem:
    tc_id = 0

    def execute(self):
        try:
            self.prep()
        except AssertionError as reason:
            print(f"Test interruption. Reason: '{reason}'.")
            return
        self.run()
        self.clean_up()

    @staticmethod
    @abstractmethod
    def prep():
        pass

    @staticmethod
    @abstractmethod
    def run():
        pass

    @staticmethod
    @abstractmethod
    def clean_up():
        pass


class TestCase1(TestSystem):
    def __init__(self):
        TestSystem.tc_id += 1
        self.name = "Time Test"
        self.tc_id = TestSystem.tc_id

    @staticmethod
    def prep():
        assert int(time()) % 2 == 0, "UNIX time is not multiple of 2"

    @staticmethod
    def run():
        home = os.path.expanduser("~")
        print(*os.listdir(home), sep="\n")

    @staticmethod
    def clean_up():
        pass


class TestCase2(TestSystem):
    def __init__(self):
        TestSystem.tc_id += 1
        self.name = "Memory Test"
        self.tc_id = TestSystem.tc_id

    @staticmethod
    def prep():
        assert virtual_memory().total >= 1073741824, "Not enough memory"

    @staticmethod
    def run():
        with open("test", "w+") as new_file:
            line = map(str, [randint(0, 1) for _ in range(1024 ** 2)])
            new_file.write("".join(line))

    @staticmethod
    def clean_up():
        os.remove("test")

# # Пример использования

# test_1 = TestCase1()
# test_1.execute()
# print(f"Тест: {test_1.name}")
# print(f"ID: {test_1.tc_id}")

# test_2 = TestCase2()
# test_2.execute()
# print(f"Тест: {test_2.name}")
# print(f"ID: {test_2.tc_id}")