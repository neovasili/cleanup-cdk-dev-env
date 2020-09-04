import os

from src.controller.cleanup_log_groups import CleanUpCWLogsController

LOG_GROUPS_NAME_PATTERN = os.environ['log_groups_name_pattern']

def handler(event, context):
  str(event)
  str(context)

  cleanup_controller = CleanUpCWLogsController()
  deleted_log_groups = cleanup_controller.cleanup_log_groups(name_pattern=LOG_GROUPS_NAME_PATTERN)

  response = {
    "log_groups_deleted": deleted_log_groups
  }

  return response
