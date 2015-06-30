#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bp'
__version__ = (0, 0, 1)


import carstate

class Car(object):
    """
    Класс автомобиля.
    Заправляется
    Задовиться
    Ездит
    Останавливается
    """
    def __init__(self):
        self.fuel = 0
        self.fuel_max = 3
        self.engine_stopped = carstate.EngineStopped(self)
        self.engine_started = carstate.EngineStarted(self)
        self.driving = carstate.Driving(self)
        self.no_fuel = carstate.EmptyFuelTank(self)
        self.fuel_tank_filled = carstate.EngineStopped(self)
        self.state = self.engine_stopped


    def start_engine(self):
        try:
            self.state.start_engine()
        except Exception as E:
            print E.message


    def stop_engine(self):
        try:
            self.state.stop_engine()
        except Exception as E:
            print E.message


    def fill_tank(self):
        try:
            self.state.fill_tank()
        except Exception as E:
            print E.message


    def drive(self):
        try:
            self.state.drive()
        except Exception as E:
            print E.message

    def stop(self):
        try:
            self.state.stop()
        except Exception as E:
            print E.message


if __name__ == '__main__':
    car = Car()
    car.drive()
    car.start_engine()
    car.fill_tank()
    car.start_engine()
    car.stop()
    car.drive()
    car.drive()
    car.stop()
    car.stop()
    car.drive()
    car.drive()
    car.drive()
    car.start_engine()