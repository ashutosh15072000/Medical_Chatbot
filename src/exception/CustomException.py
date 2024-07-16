import os
import sys

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message with file name, line number, and error message.

    Args:
        error (Exception): The error object
        error_detail (sys): The sys object containing error information

    Returns:
        str: A detailed error message

    Example:
        try:
            # some code that raises an error
            x = 1 / 0
        except Exception as e:
            error_message = error_message_detail(e, sys)
            print(error_message)
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured Python Script Name[{0}] line number[{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    """
    A custom exception class that provides a detailed error message.

    Args:
        error_message (str): The error message
        error_detail (sys): The sys object containing error information

    Attributes:
        error_message (str): The detailed error message

    Example:
        try:
            # some code that raises an error
            x = 1 / 0
        except Exception as e:
            custom_exception = CustomException("Error occurred", sys)
            print(custom_exception)
    """
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message