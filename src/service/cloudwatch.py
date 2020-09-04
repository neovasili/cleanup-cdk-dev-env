from src.model.cloudwatch import CWLogGroup
from src.helper.boto import BotoHelper

class CWlogsService(BotoHelper):

  def __init__(self, region: str = "eu-west-1"):
    super().__init__('logs', region)

  def get_log_groups(self, log_groups_prefix: str):
    response = self.client.describe_log_groups(
      logGroupNamePrefix=log_groups_prefix
    )

    log_groups = list()
    for log_group in response['logGroups'] or []:
      log_group_element = CWLogGroup(
        log_group_name=log_group['logGroupName'],
        log_group_creation=log_group['creationTime']
      )
      log_groups.append(log_group_element)

    return log_groups

  def delete_log_group(self, log_group_name: str):
    self.client.delete_log_group(
      logGroupName=log_group_name
    )
