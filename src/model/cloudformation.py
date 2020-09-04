class CloudFormationStack():

  def __init__(self, stack_id: str, name: str, creation_time: str):
    super().__init__()
    self.__id = stack_id
    self.__name = name
    self.__creation_time = creation_time

  def get_id(self):
    return self.__id

  def get_name(self):
    return self.__name

  def get_creation_time(self):
    return self.__creation_time
