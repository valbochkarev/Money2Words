class My_error(ValueError):
    '''
    class for handling user input number exception
    '''
    def __init__(self, text):
        self.txt = text

