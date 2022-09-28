from python_framework import Enum, EnumItem


@Enum()
class DateTypeEnumeration :
    HOLLIDAY = EnumItem()
    VACATION = EnumItem()
    REGULAR = EnumItem()
    NONE = EnumItem()


DateType = DateTypeEnumeration()
