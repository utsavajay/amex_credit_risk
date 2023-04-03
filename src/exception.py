import sys
from src.logger import logging


def error_message(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    emessage = 'Error in script {0}, line {1}: {2}'.format(file_name, exc_tb.tb_lineno, str(error))
    return emessage    
    

class CustomException(Exception):
    def __init__(self, emessage, error_detail:sys):
        super().__init__(emessage)
        self.emessage = error_message(emessage, error_detail = error_detail)
        
    def __str__(self):
        return self.emessage 
        