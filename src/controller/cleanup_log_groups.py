from src.service.cloudwatch import CWlogsService

class CleanUpCWLogsController():

  def __init__(self):
    super().__init__()
    self.__cwlogs_service = CWlogsService()

  def cleanup_log_groups(self, name_pattern: str):
    pattern_log_groups = self.__cwlogs_service.get_log_groups(name_pattern)
    deleted_log_groups = list()

    for log_group in pattern_log_groups or []:
      self.__cwlogs_service.delete_log_group(log_group.get_log_group_name())
      deleted_log_groups.append(log_group.get_log_group_name())

    return deleted_log_groups
