# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from src.package_data_to_format.DataConverter.DataManager import ReturningData
from src.package_data_to_format.utils.Factory import Factory
from src.package_data_to_format.utils.RabbitRabbit import RabbitRabbit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rrd:ReturningData = ReturningData(os.getenv("path_to_datafile".upper(),"testFile.csv"))
    factory:Factory = Factory()
    rabbitReader:RabbitRabbit = RabbitRabbit(factory)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
