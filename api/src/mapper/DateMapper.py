import datetime
from python_helper import DateTimeHelper
from python_framework import Mapper, MapperMethod, WeekDayConstant, StaticConverter

from enumeration.DateType import DateType
from model import DateModel
from dto import DateDto

@Mapper()
class DateMapper:

    @MapperMethod(requestClass=[[DateDto.DateRequestDto]], responseClass=[[DateModel.DateModel]])
    def fromRequestDtoListToModelList(self, dtoList, modelList) :
        return modelList

    @MapperMethod(requestClass=[[DateModel.DateModel]], responseClass=[[DateDto.DateResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList):
        return dtoList

    @MapperMethod(requestClass=[DateDto.DateRequestDto], responseClass=[DateModel.DateModel])
    def fromRequestDtoToModel(self, dto, model) :
        return model

    @MapperMethod(requestClass=[DateModel.DateModel], responseClass=[DateDto.DateResponseDto])
    def fromModelToResponseDto(self, model, dto) :
        return dto

    @MapperMethod(requestClass=[datetime.date])
    def buildNewModelByDate(self, date):
        return DateModel.DateModel(
            key = date,
            type = DateType.REGULAR if DateTimeHelper.getWeekDayOf(date=date) in WeekDayConstant.WEEK_DAY_LIST else DateType.HOLLIDAY
        )

    @MapperMethod(requestClass=[DateDto.DateRequestDto, DateModel.DateModel])
    def overrideModel(self, dto, model):
        model.type = StaticConverter.getValueOrDefault(dto.type, model.type)
        return model.reload()
