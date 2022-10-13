from python_helper import DateTimeHelper
from python_framework import ConverterStatic
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import DATE, MODEL
from constant import DateConstant
from enumeration.DateType import DateType


class DateModel(MODEL):
    __tablename__ = DATE

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.Date, nullable=False, unique=True)
    type = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=DateConstant.DEFAULT_TYPE)


    def __init__(self,
        id = None,
        key = None,
        type = None
    ):
        self.id = id
        self.key = key
        self.type = type
        self.setDefaultValues()


    def setDefaultValues(self, *args, **kwargs):
        self.key = DateTimeHelper.dateOf(dateTime=DateTimeHelper.of(date=self.key))
        self.type = ConverterStatic.getValueOrDefault(DateType.map(self.type), DateConstant.DEFAULT_TYPE)
        return self


    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, key={self.key}, type={self.type})'
