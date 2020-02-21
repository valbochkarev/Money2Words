from Localized_uk_ua import Amount2TextUKR
from Localized_en_us import Amount2TextENG
from MyError import My_error

class Menu:
    '''
    UI class
    '''

    def __init__(self):
        '''
        Initialization of fields and default values.
        '''
        self.selected_language = "unknown"
        self.entered_money = 0
        self.entered_pennies = 0
        self.supported_languages = {'ukr', 'eng'}
        self.supported_languages_str = "ukr, eng"
    
    def start(self):
        '''
        Call UI.
        '''
        self.select_language()
        if self.selected_language == 'ukr':
            A = Amount2TextUKR
        elif self.selected_language == 'eng':
            A = Amount2TextENG
        print("Enter a number from 0 to 2147483647 inclusive. For exit enter -1")
        while True:
            self.input_number()
            print(A(self.entered_money, self.entered_pennies).text_compilation())

    def select_language(self):
        '''
        User choice of supported language. Now its ukr for for Ukrainian language and currency and eng for English (USA) and currency.
        '''
        print("Hello! Choose language: ", self.supported_languages_str)
        while True:
            temp = input()
            if temp in self.supported_languages:
                print("Well done! You choosed:", temp)
                self.selected_language = temp
                return True
            print("Selection error. Choose: ", self.supported_languages_str)

    def delimiter(self):
        '''
        This method returns the delimiter for the selected language.
        '''
        if self.selected_language == "ukr":
            return ','
        elif self.selected_language == "eng":
            return '.'
        else:
            return '.'

    def input_number(self):
        '''
        User enters number until he enters correctly.
        '''
        temp = input()
        if not(self.parse_number(temp)):
            print("try again")
            self.input_number()
        

    def parse_number(self, input_str):
        '''
        Validation of user input. input_str should be a string containing only a real number.
        '''
        try:
            if input_str.isdigit():
                self.entered_money = int(input_str)
                self.entered_pennies = 0
                return True
            else:
                if input_str == '-1':
                    exit()
                parts = input_str.split(self.delimiter())
                if parts[0][0] == '-':
                    raise My_error('Value cannot be less than zero')
                elif len(parts)!=2:
                    raise My_error(f"""Probably, something wrong with delimiter
in {self.selected_language} use '{self.delimiter()}' once""")
                if not parts[0].isdigit():
                    raise My_error('Incorrect integer part')
                elif not parts[1].isdigit():
                    raise My_error('Incorrect fractional part')
                else:
                    self.entered_money = int(parts[0])
                    if self.entered_money > 2147483647:
                        raise My_error('The number is too long')
                    temp = parts[1]
                    if len(temp) == 1:
                        temp += '0'
                    if len(temp) > 2:
                        print("Too small money, rounding to two digits down")
                    self.entered_pennies = int(temp[0:2])
                    return True
        except My_error as e:
            print(e)
            return False

if __name__ == "__main__":
    Menu().start()
