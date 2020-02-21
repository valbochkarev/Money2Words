import re

class Amount2TextUKR(object):
    '''
    Сlass containing dictionaries and text formatting rules about the amount of money for the Ukrainian language
    '''
    
    def __init__(self, hryvnyas, pennies):
        '''
        Dictionaries declaration.
        '''
        self.hryvnyas = int(hryvnyas)
        self.pennies  = int(pennies)
        self.units = { 0:'',
            1:{1:'один', 2:'одна'},  2:{1:'два', 2:'дві'}, 3:'три',   
            4:'чотири',  5:'п\'ять', 6:'шість',            7:'сім', 
            8:'вісім', 9:'дев\'ять', 10:'десять',
            11:'одинадцять',   12:'дванадцять',   13:'тринадцять',
            14:'чотирнадцять', 15:'п\'ятнадцять', 16:'шістнадцять',
            17:'сімнадцять',   18:'вісімнадцять', 19:'дев\'ятнадцать'}
        self.dozens = {
            2:'двадцять',   3:'тридцять', 4:'сорок',      5:'п\'ятдесят',
            6:'шістдесят',  7:'сімдесят', 8:'вісімдесят', 9:'дев\'яносто'}
        self.hundreds = {
            1:'сто',          2:'двісті',      3:'триста',
            4:'чотириста',    5:'п\'ятсот',    6:'шістсот',
            7:'сімсот',       8:'вісімсот',    9:'дев\'ятсот'}
        #plural            =  {'zero'(0), 'one'(1), 'few'(2-4), 'many'(5+), 'grammatical gender'(1 if masculine, 2 if feminine)}
        self.hryvnyas_dict = [{'zero':'',       'one':'гривня',  'few':'гривні',   'many':'гривень',    'grammatical_gender':2},
                              {'zero':'',       'one':'тисяча',  'few':'тисячі',   'many':'тисяч',      'grammatical_gender':2},
                              {'zero':'',       'one':'мільйон', 'few':'мільйони', 'many':'мільйонів',  'grammatical_gender':1},
                              {'zero':'',       'one':'мільярд', 'few':'мільярди', 'many':'мільярдів',  'grammatical_gender':1}]
        self.pennies_dict  =  {'zero':'',       'one':'копійка', 'few':'копійки',  'many':'копійок' ,   'grammatical_gender':2}
        

    def parse_threeorder(self, number,strPart):
        """
        Three-digit number processing method.
        """
        tempStr = ""
        quantity = 'many'
        if number > 99:
            temp = number // 100
            tempStr += f'{self.hundreds[temp]} '
            number %= 100
        if number > 19:
            temp = number // 10
            tempStr += f'{self.dozens[temp]} '
            number %= 10
        if number > 0:
            if (number == 1) or (number == 2):
                tempStr += '{} '.format(self.units[number][strPart['grammatical_gender']])
            else:
                tempStr += f'{self.units[number]} '
            if number == 1:
                quantity = 'one'
            elif (number > 1) and (number < 5):
                quantity = 'few'    
            elif number >= 5:
                quantity = 'many'
        if tempStr != '':
            return f'{tempStr}{strPart[quantity]}'
        return ''

   
    def text_compilation(self):
        '''
        Function collecting a text string from a number broken into three-digit numbers.
        '''
        pennies=self.pennies
        hryvnyas=self.hryvnyas
                
        pennie_str=self.parse_threeorder(pennies,self.pennies_dict)
        hryvnya_str=''
        for dict_ in self.hryvnyas_dict:
            units = hryvnyas%1000
            hryvnyas //= 1000
            hryvnya_str = f'{self.parse_threeorder(units,dict_)} {hryvnya_str}'
        
        if (self.hryvnyas != 0) and (self.hryvnyas % 1000 == 0):
            hryvnya_str += self.hryvnyas_dict[0]['many']

        return re.sub(r'\s+', ' ', f'{hryvnya_str} {pennie_str}').strip( )