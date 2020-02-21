import re

class Amount2TextENG(object):
    '''
    Сlass containing dictionaries and text formatting rules about the amount of money for the English (USA) language.
    '''
    
    def __init__(self, dollars, cents):
        '''
        Dictionaries declaration.
        '''
        self.dollars = int(dollars)
        self.cents  = int(cents)
        self.units = { 0:'',
            1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 
            8:'eight', 9:'nine', 10:'ten',
            11:'eleven',   12:'twelwe',   13:'thirteen',
            14:'fourteen', 15:'fifteen', 16:'sixteen',
            17:'seventeen',   18:'eighteen', 19:'nineteen'}
        self.dozens = {
            2:'twenty', 3:'thirty', 4:'forty', 5:'fifty',
            6:'sixty',  7:'seventy', 8:'eighty', 9:'ninety'}
        self.hundred = 'hundred'
        self.threeorder = ['', 'thousand', 'million', 'billion']
        #Many             = {'zero'(0)  'one'(1),       'many'(>1)      }
        self.dollars_dict = {'zero':'', 'one':'dollar', 'many':'dollars'}
        self.cents_dict   = {'zero':'', 'one':'cent ',  'many':'cents' }
        
    def parse_threeorder(self, number,strPart):
        """
        Three-digit number processing method.
        """
        tempStr = ''
        if number > 99:
            temp = number//100
            tempStr += f'{self.units[temp]} {self.hundred}'
            number %= 100
        if number > 19:
            temp = number//10
            if tempStr != '':
                tempStr += ' '
            tempStr += f'{self.dozens[temp]}'
            number %= 10
            if number > 0:
                tempStr += f'-{self.units[number]}'
        elif number > 0:
            if tempStr != '':
                tempStr += ' '
            tempStr += f'{self.units[number]}'
        if tempStr != '':
            return f'{tempStr} {strPart}'
        return ''

   
    def text_compilation(self):
        '''
        Function collecting a text string from a number broken into three-digit numbers.
        '''
        cents = self.cents
        dollars = self.dollars
        
        cents_str = self.parse_threeorder(cents,'')
        dollars_str = ''
        for rank_ in self.threeorder:
            units = dollars%1000
            dollars //= 1000
            dollars_str = f'{self.parse_threeorder(units,rank_)} {dollars_str}'

        if self.dollars == 1:
            dollars_str += self.dollars_dict['one']
        elif self.dollars > 1:
            dollars_str += self.dollars_dict['many']
        if self.cents == 1:
            cents_str += self.cents_dict['one']
        elif self.cents > 1:
            cents_str += self.cents_dict['many']
        dollars_str = dollars_str.strip(' ')
        cents_str = cents_str.strip(' ')
        if dollars_str != '' and cents_str != '':
            return re.sub(r'\s+', ' ', f'{dollars_str} and {cents_str}').strip( )
        return re.sub(r'\s+', ' ', f'{dollars_str}{cents_str}').strip( )