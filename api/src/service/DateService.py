import datetime
from python_helper import DateTimeHelper, ObjectHelper
from python_framework import Service, ServiceMethod

from dto import DateDto
from model import Date


@Service()
class DateService:

    @ServiceMethod(requestClass=[DateDto.CalendarDateParamsDto])
    def createCalendarByYear(self, paramsDto):
        firstDateOfTheYear = DateTimeHelper.of(date=f'{paramsDto.year}-01-01')
        lastDateOfTheYear = DateTimeHelper.of(date=f'{paramsDto.year}-12-31')
        return self.mapper.date.fromModelListToResponseDtoList(
            self.saveAllModel([
                self.mapper.date.buildNewModelByDate(DateTimeHelper.dateOf(dateTime=DateTimeHelper.plusDays(firstDateOfTheYear, days=days)))
                for days in range((lastDateOfTheYear - firstDateOfTheYear).days)
            ])
        )


    @ServiceMethod(requestClass=[DateDto.DateRequestDto])
    def update(self, dto):
        model = self.findByKey(dto.key)
        if ObjectHelper.isNone(model):
            model = self.findById(dto.id)
        self.mapper.date.overrideModel(dto, model)
        return self.mapper.date.fromModelToResponseDto(self.saveModel(model))


    @ServiceMethod(requestClass=[DateDto.CalendarDateParamsDto])
    def findAllByCalendarParams(self, paramsDto):
        firstDateOfTheYear = DateTimeHelper.of(date=f'{paramsDto.year}-01-01')
        lastDateOfTheYear = DateTimeHelper.of(date=f'{paramsDto.year}-12-31')
        return self.mapper.date.fromModelListToResponseDtoList(
            self.repository.date.findAllBetwenDates(firstDateOfTheYear, lastDateOfTheYear)
        )


    @ServiceMethod()
    def findAll(self):
        return self.mapper.date.fromModelListToResponseDtoList(self.repository.date.findAll())


    @ServiceMethod(requestClass=[DateDto.ValidateDateParamsDto])
    def validateTypeByDate(self, paramsDto):
        self.validator.date.validateTypeByDate(paramsDto.date, paramsDto.type)


    @ServiceMethod(requestClass=[datetime.date])
    def findByKey(self, key):
        return self.repository.date.findByKey(key)


    @ServiceMethod(requestClass=[int])
    def findById(self, id):
        return self.repository.date.findById(id)


    @ServiceMethod(requestClass=[Date.Date])
    def saveModel(self, model):
        return self.repository.date.save(model)


    @ServiceMethod(requestClass=[[Date.Date]])
    def saveAllModel(self, modelList):
        return self.repository.date.saveAll(modelList)
