class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, input, message):
        self.input = input
        self.message = message 
    
    def __str__(self):
        return f'{self.input} -> {self.message}'

    def input(name,message):
        if name=="":
           return f'{self.input} -> {self.message}'
        else:
            return 1
