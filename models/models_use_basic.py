from sqlalchemy import select, insert
from models.db import (
    engine,
    User,
    Emoji,
    EmojiSend,
    UserEmoji,
    UserNotification
)
from utilities.produce_text import text_user_return
from utilities.produce_log import produce_basic_logs, produce_datetime
from config import InlineButtonSend


class ModelsBasic:
    """
    class which is dedicated to use basic transforms to models
    """
    def __init__(self) -> None:
        self.connection = None
        self.produce_connection()

    def produce_connection(self) -> None:
        """
        Method which is dedicated to produce the
        Input:  None
        Output: we developed the 
        """
        try:
            self.connection = engine.connect()
            # self.connection.execution_options(isolation_level="AUTOCOMMIT")
            print(self.connection)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        except Exception as e:
            print(e)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    def close(self) -> None:
        """
        Method which is dedicated to develop closing of used connection
        Input:  None
        Output: we closed the required connection 
        """
        self.connection.close()

    def check_presence_user(self, user_id:int) -> bool:
        """
        Method which is dedicated to check the presence of selected user
        Input:  user_id = id of selected user
        Output: boolean values which signifies it
        """
        value_check = self.connection.execute(select(User).filter_by(id=user_id)).first()
        print(value_check)
        print('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
        # session.execute(select(User).filter_by(name="sandy")).scalar_one()
        return False

    def add_users(self, value_list:list) -> None:
        """
        Method which is dedicated to add the users to db
        Input:  value_list = list of the 
        Output: we added the user to it
        """
        user_id, user_name_first, user_name_last, user_name = value_list
        if self.check_presence_user(user_id):
            return
        #TODO add here the insert
        #TODO add here the log values
        produce_datetime(1)
        return

    def add_users_friend(self, value_list:list) -> None:
        """
        Method which is dedicated to add the selected friend to the collection
        Input:  value_list = list of the 
        Output: we developed the values of the friends
        """
        pass

    def check_users_notification(self, user_id:int, user_id_friend:int) -> bool:
        """
        Method which is dedicated to check the capability of the notifications to it
        Input:  user_id = id of the selected user to check
                user_id_friend = if of the selected friend to check
        Output: we developed the 
        """
        #TODO add here the insert
        pass

    def add_users_notification(self, user_id:int, user_id_friend:int) -> None:
        """
        Method which is dedicated to add the notification values
        Input:  user_id = id of the user
                user_friend = id of the friend which is about send the notification
        Output: we developed the norification to all of it
        """
        if self.check_users_notification(user_id, user_id_friend):
            return
        #TODO add here the insert
        #TODO add here the log values
        produce_datetime(1)
        return

    def delete_users_notification(self, users_id:int, user_id_friend:int) -> None:
        """
        Method which is dedicated to remove the notidication from one side
        Input:  user_id = user which wanted to remove
                user_id_friend = user of friend which wanted it to remove
        Output: we removed the user notification to all of it
        """
        #TODO add here the removal
        #TODO add here the log values
        produce_datetime(1)
        return

    def add_users_connection(self, user_id:int, user_id_friend:int) -> None:
        """
        Method which is dedicated to add the connection to the user
        Input:  user_id = id of the selected user
                user_id_friend = id of the selected friend
        Output: we developed the connection between the friends to it
        """
        if not self.check_presence_user(user_id) or not self.check_presence_user(user_id_friend):
            return
        #TODO add here the insert
        #TODO add here the log values
        produce_datetime(1)
        
    def remove_users_connection(self, user_id:int, user_id_friend:int) -> None:
        """
        Method which is dedicated to add the connection to the user
        Input:  user_id = id of the selected user
                user_id_friend = id of the friend to remove
        Output: we removed the connection to the
        """
        #TODO add here the remove
        #TODO add here the log values
        produce_datetime(1)
        pass

    def add_user_mark(self, user_id:int, user_id_friend:int, mark_id:int) -> None:
        """
        Method which is dedicated to work with adding the mark one user to another
        Input:  user_id = id of the selected user
                user_id_friend = id to send value to his friend
                mark_id = id of the mark which user would send
        Output: we developed the mark which we want
        """
        #TODO add here the insert
        #TODO add here the log values
        pass

    def return_user_emo(self, user_id:int) -> list:
        """
        Method which is dedicated to return all the values
        Input:  user_id = id of the selected user
        Output: list with selected values which could be used
        """
        #TODO add here emo functions for db
        return [
            InlineButtonSend.button_sun,
            InlineButtonSend.button_cloud,
            InlineButtonSend.button_cloud_sun,
            InlineButtonSend.button_sun_cloud
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

