import os
import logging
from datetime import datetime
from config import Folders


def produce_datetime(types:int=1) -> str:
    """
    Function which is dedicated to produce datetime for logs
    Input:  types = int parameters to return selected values
    Output: we developed the datetime values for several purposes
    """
    if types == 1:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if types == 2:
        return f'{datetime.now().strftime("%Y-%m-%d")}.log'

def produce_basic_logs(value_message:list, value_bool:bool=True):
    """
    Function which is dedicated to make the log value basic
    Input:  value_message = list of selected values to send
            value_bool = bool values 
    Output: 
    """
    if not value_message:
        return
    value_message.insert(0, produce_datetime(1))
    k = ' | '.join(value_message)
    produce_basic_logs_writing(k)
    if value_bool:
        print(k)

def produce_basic_logs_writing(value_message:str) -> None:
    """
    Function which is dedicated to develop the blog
    Input:  value_message = message which is used
    Output: we wrote the log to it
    """
    logging.basicConfig(
        filename=os.path.join(Folders.folder_here, Folders.folder_logs, produce_datetime(2)), 
        format='%(message)s', 
        level=logging.INFO
    )
    logging.info(value_message)