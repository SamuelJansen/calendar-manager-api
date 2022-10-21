from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import DateDto

@Controller(
    url = '/callendar/date',
    tag = 'Validate Date',
    description = 'Validate Date controller'
    # , logRequest = True
    # , logResponse = True
)
class ValidateDateController:

    @ControllerMethod(
        url = '/validate',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestParamClass=[DateDto.ValidateDateParamsDto]
        # , logRequest = True
        # , logResponse = True
    )
    def get(self, params=None):
        return self.service.date.validateTypeByDate(params), HttpStatus.OK
