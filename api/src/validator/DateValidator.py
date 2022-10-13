import datetime
from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus, EnumItem

from model import DateModel


@Validator()
class DateValidator:

    @ValidatorMethod(requestClass=[datetime.date, EnumItem])
    def validateTypeByDate(self, date, type):
        model = self.service.date.findByKey(date)
        self.validateIsNotNone(model)
        if not type == model.type:
            raise GlobalException(message=f'The {date} date is not a {type}. It is a {model.type} date', status=HttpStatus.BAD_REQUEST)


    @ValidatorMethod(requestClass=[DateModel.DateModel])
    def validateIsNotNone(self, model):
        if ObjectHelper.isNone(model):
            raise GlobalException(message=f'Date not found', status=HttpStatus.NOT_FOUND)
