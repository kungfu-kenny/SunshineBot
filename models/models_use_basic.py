from utilities.produce_log import produce_basic_logs, produce_datetime


class ModelsBasic:
    """
    class which is dedicated to use basic transforms to models
    """

    def check_presence_user(self, user_id:int) -> bool:
        """
        Method which is dedicated to check the presence of selected user
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
        #TODO add here the 