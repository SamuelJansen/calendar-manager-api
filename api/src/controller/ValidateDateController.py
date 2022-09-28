from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import DateDto

@Controller(url='/callendar/date/validate', tag='Validate Date', description='Validate Date controller')
class ValidateDateController:

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestParamClass=[DateDto.ValidateDateParamsDto]
        , logRequest = True
        , logResponse = True
    )
    def get(self, params=None):
        return self.service.date.validateTypeByDate(params), HttpStatus.OK
