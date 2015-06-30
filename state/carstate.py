#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bp'
__version__ = (0, 0, 1)


################################################################################
class BaseState(object):
    """
    Базовый класс состояния автомобиля.
    Описание исключений.
    Может все. В наследуемых классах методы управления состоянием будут перекрыты
    """
    class BaseException(Exception):
        def __init__(self, message):
            self.message = message

    class EngineCannotBeStarted(BaseException):
        def __init__(self):
            super(BaseState.EngineCannotBeStarted, self).__init__(u'Двигатель не может быть повторно запущен')

    class EngineCannotBeStop(BaseException):
        def __init__(self):
            super(BaseState.EngineCannotBeStop, self).__init__(u'Двигатель не может быть повторно остановлен')

    class CannotDrive(BaseException):
        def __init__(self):
            super(BaseState.CannotDrive, self).__init__(u'Нет возможности ехать: двигатель заглушен')

    class FuelTankIsFull(BaseException):
        def __init__(self):
            super(BaseState.FuelTankIsFull, self).__init__(u'Нельзя залить топливо: он полон')

    class FuelTankIsEmpty(BaseException):
        def __init__(self):
            super(BaseState.FuelTankIsEmpty, self).__init__(u'Не заводиться: бак пуст')

    class FuelCannotBeFilled(BaseException):
        def __init__(self):
            super(BaseState.FuelCannotBeFilled, self).__init__(u'Нельзя залить топливо: работает двигатель')

    class AlreadyStopped(BaseException):
        def __init__(self):
            super(BaseState.AlreadyStopped, self).__init__(u'Нельзя остановить: уже стоим')

    def __init__(self, car):
        self.__car = car

    def drive(self):
        if self.__car.fuel > 0:
            self.__car.fuel -= 1
            self.__car.state = self.__car.driving
            print u'...Проехал 1км...'
        else:
            self.__car.state = self.__car.engine_stopped
            print u'...Двигатель заглушен...'

    def fill_tank(self):
        if self.__car.fuel < self.__car.fuel_max:
            self.__car.fuel = self.__car.fuel_max
            self.__car.state = self.__car.fuel_tank_filled
            print u'...Заправились...'
        else:
            raise self.FuelTankIsFull

    def start_engine(self):
        if self.__car.fuel > 0:
            self.__car.state = self.__car.engine_started
        else:
            self.__car.state = self.__car.no_fuel
            raise self.FuelTankIsEmpty

    def stop_engine(self):
        self.__car.state = self.__car.engine_stopped

    def stop(self):
        if self.__car.state == self.__car.engine_started:
            raise self.AlreadyStopped
        self.__car.state = self.__car.engine_started
        print u'...Остановились...'

################################################################################


################################################################################
class EngineStopped(BaseState):
    def drive(self):
        raise self.CannotDrive

    def stop_engine(self):
        raise self.EngineCannotBeStop

################################################################################


################################################################################
class EngineStarted(BaseState):
    def start_engine(self):
        raise self.EngineCannotBeStarted

    def fill_tank(self):
        raise self.FuelCannotBeFilled

################################################################################


################################################################################
class EmptyFuelTank(BaseState):
    def drive(self):
        raise self.CannotDrive

    def start_engine(self):
        raise self.FuelTankIsEmpty

    def stop_engine(self):
        raise self.EngineCannotBeStop

################################################################################


################################################################################
class Driving(BaseState):
    def start_engine(self):
        raise self.EngineCannotBeStarted

    def stop_engine(self):
        raise self.EngineCannotBeStop

    def fill_tank(self):
        raise self.FuelCannotBeFilled

################################################################################