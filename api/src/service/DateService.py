import datetime
from python_helper import DateTimeHelper, ObjectHelper
from python_framework import Service, ServiceMethod

from dto import DateDto
from model import DateModel


@Service()
class DateService:

    @ServiceMethod(requestClass=[DateDto.CalendarDateParamsDto])
    def createCalendarByYear(self, paramsDto):
        firstDateOfTheYear = DateTimeHelper.of(date=f'{paramsDto.year}-01-01')
        lastDateOfTheYear = DateTimeHelper.of(date=f'{paramsDto.year}-12-31')
        return self.mapper.date.fromModelListToResponseDtoList(
            self.saveAllModel([
                self.mapper.date.buildNewModelByDate(DateTimeHelper.dateOf(dateTime=DateTimeHelper.plusDays(firstDateOfTheYear, days=days)))
                for days in range((lastDateOfTheYear - firstDateOfTheYear).days + 1)
                if not self.existsByKey(DateTimeHelper.dateOf(dateTime=DateTimeHelper.plusDays(firstDateOfTheYear, days=days)))
            ])
        )


    @ServiceMethod(requestClass=[DateDto.DateRequestDto])
    def update(self, dto):
        model = self.findModelByKey(dto.key)
        if ObjectHelper.isNone(model):
            model = self.findById(dto.id)
        self.mapper.date.overrideModel(dto, model)
        return self.mapper.date.fromModelToResponseDto(self.saveModel(model))


    @ServiceMethod(requestClass=[[DateDto.DateRequestDto]])
    def updateAll(self, dtoList):
        return [
            self.update(dto)
            for dto in dtoList
        ]


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


    @ServiceMethod(requestClass=[str])
    def findByKey(self, keyAsString):
        key = DateTimeHelper.dateOf(dateTime=DateTimeHelper.of(date=keyAsString))
        return self.mapper.date.fromModelToResponseDto(self.findModelByKey(key))


    @ServiceMethod(requestClass=[datetime.date])
    def findModelByKey(self, key):
        return self.repository.date.findByKey(key)


    @ServiceMethod(requestClass=[int])
    def findById(self, id):
        return self.repository.date.findById(id)


    @ServiceMethod(requestClass=[DateModel.DateModel])
    def saveModel(self, model):
        return self.repository.date.save(model)


    @ServiceMethod(requestClass=[[DateModel.DateModel]])
    def saveAllModel(self, modelList):
        return self.repository.date.saveAll(modelList)


    @ServiceMethod(requestClass=[datetime.date])
    def existsByKey(self, key):
        return self.repository.date.existsByKey(key)
