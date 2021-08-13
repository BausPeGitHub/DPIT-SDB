class ProgramError(Exception):
    pass

class ValidationError(ProgramError):
    pass

class DuplicateException(ProgramError):
    def __init__(self, entity) :
        message = '{0} already exists!'.format(entity)
        super().__init__(message)

class NotFoundException(ProgramError):
    def __init__(self, entity) :
        message = '{0} does not exist!'.format(entity)
        super().__init__(message) 
