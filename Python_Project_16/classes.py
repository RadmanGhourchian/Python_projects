from Python_Project_16.database import *
import mysql.connector

class Product(Database):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

class Electrical(Product):
    def __init__(self, name, price, weight, voltage):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage

class Mobile(Electrical):
    def __init__(self, name, price, weight, voltage, screen_size):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage
        self.screen_size = screen_size

class Samsung(Mobile):
    def __init__(self, name, price, weight, voltage, screen_size, serial):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage
        self.screen_size = screen_size
        self.serial = serial
class Apple(Mobile):
    def __init__(self, name, price, weight, voltage, screen_size, standard):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage
        self.screen_size = screen_size
        self.standard = standard











class Laptop(Electrical):
    def __init__(self, name, price, weight, voltage, cpu, ram):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage
        self.cpu = cpu
        self.ram = ram


class Asus(Laptop):
    def __init__(self, name, price, weight, voltage, cpu, ram, maker_country):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage
        self.cpu = cpu
        self.ram = ram
        self.maker_country = maker_country





class Monitor(Electrical):
    def __init__(self, name, price, weight, voltage, contrast):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage
        self.contrast = contrast


class LG(Monitor):
    def __init__(self, name, price, weight, voltage, contrast, monitor_type):
        self.name = name
        self.price = price
        self.weight = weight
        self.voltage = voltage
        self.contrast = contrast
        self.monitor_type = monitor_type









class Unelectrical(Product):
    def __init__(self, name, price, weight, usage):
        self.name = name
        self.price = price
        self.weight = weight
        self.usage = usage

class Sofa(Unelectrical):
    def __init__(self, name, price, weight, usage):
        self.name = name
        self.price = price
        self.weight = weight
        self.usage = usage

class Table(Unelectrical):
    def __init__(self, name, price, weight, usage):
        self.name = name
        self.price = price
        self.weight = weight
        self.usage = usage