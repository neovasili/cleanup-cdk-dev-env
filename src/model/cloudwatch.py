
class CWLogGroup():

  def __init__(self, log_group_name: str, log_group_creation: str):
    self.__log_group_name = log_group_name
    self.__log_group_creation = log_group_creation

  def get_log_group_name(self):
    return self.__log_group_name

  def get_log_group_creation(self):
    return self.__log_group_creation
