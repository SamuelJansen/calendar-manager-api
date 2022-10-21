from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import DateDto

@Controller(
    url = '/callendar/date',
    tag = 'Date',
    description = 'Date controller'
    , logRequest = True
    , logResponse = True
)
class DateController:

    @ControllerMethod(
        url = '/<string:date>',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        responseClass=[DateDto.DateResponseDto]
        # , logRequest = True
        # , logResponse = True
    )
    def get(self, date=None):
        return self.service.date.findByKey(date), HttpStatus.OK


    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestClass=[DateDto.DateRequestDto],
        responseClass=[DateDto.DateResponseDto]
        # , logRequest = True
        # , logResponse = True
    )
    def put(self, dto):
        return self.service.date.update(dto), HttpStatus.ACCEPTED


@Controller(
    url = '/callendar/date/all',
    tag = 'Date',
    description = 'Date controller'
    , logRequest = True
    , logResponse = True
)
class DateAllController:

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        responseClass=[[DateDto.DateResponseDto]]
        # , logRequest = True
        # , logResponse = True
    )
    def get(self):
        return self.service.date.findAll(), HttpStatus.OK


@Controller(
    url = '/callendar/date',
    tag = 'Date',
    description = 'Date controller'
    , logRequest = True
    , logResponse = True
)
class DateBulkController:

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestParamClass=[DateDto.CalendarDateParamsDto],
        responseClass=[[DateDto.DateResponseDto]]
        # , logRequest = True
        # , logResponse = True
    )
    def get(self, params=None):
        return self.service.date.findAllByCalendarParams(params), HttpStatus.OK

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestParamClass=[DateDto.CalendarDateParamsDto],
        responseClass=[[DateDto.DateResponseDto]]
        # , logRequest = True
        # , logResponse = True
    )
    def post(self, params=None):
        return self.service.date.createCalendarByYear(params), HttpStatus.CREATED
