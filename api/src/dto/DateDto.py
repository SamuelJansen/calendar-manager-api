from python_helper import DateTimeHelper
from python_framework import StaticConverter

from constant import DateConstant
from enumeration.DateType import DateType


class DateRequestDto:
    def __init__(self,
        id = None,
        key = None,
        type = None
    ):
        self.id = id
        self.key = DateTimeHelper.dateOf(dateTime=DateTimeHelper.of(date=key))
        self.type = StaticConverter.getValueOrDefault(DateType.map(type), DateConstant.DEFAULT_TYPE)


class DateResponseDto:
    def __init__(self,
        id = None,
        key = None,
        type = None
    ):
        self.id = id
        self.key = DateTimeHelper.dateOf(dateTime=DateTimeHelper.of(date=key))
        self.type = StaticConverter.getValueOrDefault(DateType.map(type), DateConstant.DEFAULT_TYPE)


class CalendarDateParamsDto:
    def __init__(self,
        year = None
    ):
        self.year = year


class ValidateDateParamsDto:
    def __init__(self,
        date = None,
        type = None
    ):
        self.date = DateTimeHelper.dateOf(dateTime=DateTimeHelper.of(date=date))
        self.type = StaticConverter.getValueOrDefault(DateType.map(type), DateConstant.DEFAULT_TYPE)
