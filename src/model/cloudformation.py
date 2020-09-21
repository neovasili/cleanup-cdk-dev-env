class CloudFormationStack():

  def __init__(self, stack_id: str, name: str, creation_time: str, tags: list):
    super().__init__()
    self.__id = stack_id
    self.__name = name
    self.__creation_time = creation_time
    self.__tags = tags

  def get_id(self):
    return self.__id

  def get_name(self):
    return self.__name

  def get_creation_time(self):
    return self.__creation_time

  def get_tags(self):
    return self.__tags

  def get_retention_policy(self):
    retention_policy = 'DELETE'

    if self.__tags:
      for tag in self.__tags or []:
        if tag['Key'] =='RetentionPolicy':
          return tag['Value']

    return retention_policy
