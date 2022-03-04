from utilities.produce_text import text_user_return
from utilities.produce_log import produce_basic_logs, produce_datetime


class ModelsBasic:
    """
    class which is dedicated to use basic transforms to models
    """
    def __init__(self) -> None:
        pass

    def check_presence_user(self, user_id:int) -> bool:
        """
        Method which is dedicated to check the presence of selected user
        Input:  user_id = id of selected user
        Output: boolean values which signifies it
        """
        return False

    def add_users(self, value_list:list) -> None:
        """
        Method which is dedicated to add the users to db
        Input:  value_list = list of the 
        Output: we added the user to it
        """
        user_id, user_name_first, user_name_last, user_name = value_list
        produce_datetime(1)
        #TODO add here the insert
        return

    def return_user_emo(self, user_id:int) -> list:
        """
        Method which is dedicated to return all the values
        Input:  user_id = id of the selected user
        Output: list with selected values which could be used
        """
        #TODO add here emo functions for db
        return [
            (1, '☀️'),
            (2, '🌤'),
            (3, '⛅️'),
            (4, '☁️')
        ]

    def return_users_friends(self, user_id:int) -> list:
        """
        Method which is dedicated to return all the friends
        Input:  user_id = id of the selected user
        Output: list with selected values which could be used
        """
        #TODO add here function for friends
        return [
            text_user_return(f) 
            for f in [
                (1, 'friend_name', 'friend_surname', 'friend_username'),
                (1, 'friend_name_2', '', 'friend_username_2'),
                (2, 'friend_name', 'friend_surname_3', 'friend_username_3')
            ]
        ]

