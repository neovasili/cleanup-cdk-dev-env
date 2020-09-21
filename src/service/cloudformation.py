from src.model.cloudformation import CloudFormationStack
from src.helper.boto import BotoHelper

from botocore.exceptions import ClientError

class CloudFormationService(BotoHelper):

  def __init__(self, region: str = "eu-west-1"):
    super().__init__('cloudformation', region)

  def get_developer_stacks(self, name_pattern: str, self_stack_name: str):
    response = self.client.describe_stacks()

    stacks = list()
    for stack in response['Stacks'] or []:
      stack_name = stack['StackName']
      if stack_name.startswith(name_pattern) and stack_name != self_stack_name:
        stack_element = CloudFormationStack(
          stack_id=stack['StackId'],
          name=stack_name,
          creation_time=stack['CreationTime'].strftime("%Y-%m-%d %H:%M:%S")
        )
        stacks.append(stack_element)

    return stacks

  def get_stack_resources(self, stack_name: str):
    response = self.client.describe_stack_resources(StackName=stack_name)

    stack_resources = list()
    if 'StackResources' in response:
      stack_resources = response['StackResources']

    return stack_resources

  def get_stack_resource_detail(self, stack_name: str, resource_logical_id: str):
    response = self.client.describe_stack_resource(
      StackName=stack_name,
      LogicalResourceId=resource_logical_id
    )

    resource_detail = None
    if 'StackResourceDetail' in response:
      resource_detail = response['StackResourceDetail']

    return resource_detail

  def get_stack_status(self, stack_name: str):
    stack_status = "DELETE_COMPLETE"

    try:
      response = self.client.describe_stacks(
        StackName=stack_name
      )

      if 'Stacks' in response:
        first_stack = response['Stacks'][0]
        stack_status = first_stack['StackStatus']
    except ClientError:
      print("Stack already deleted")

    return stack_status

  def delete_stack(self, stack_name: str):
    self.client.delete_stack(
      StackName=stack_name
    )
