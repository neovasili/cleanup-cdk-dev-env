from src.service.cloudformation import CloudFormationService

class CleanUpStacksController():

  def __init__(self):
    super().__init__()
    self.__cloudformation_service = CloudFormationService()

  def get_developer_stacks(self, name_pattern: str, self_stack_name: str):
    stacks = self.__cloudformation_service.get_developer_stacks(name_pattern, self_stack_name)

    stack_names = list()
    for stack in stacks or []:
      stack_name = stack.get_name()
      if self.check_cdk_stack(stack_name):
        stack_names.append(stack_name)

    return stack_names

  @classmethod
  def __check_cdk_metadata_resource(cls, stack_resource: dict):
    resource_type = stack_resource['ResourceType']

    return resource_type == 'AWS::CDK::Metadata'

  def __check_stack_resource_from_cdk(self, stack_resource: dict):
    stack_name = stack_resource['StackName']
    resource_logical_id = stack_resource['LogicalResourceId']

    resource_detail = self.__cloudformation_service.get_stack_resource_detail(
      stack_name,
      resource_logical_id
    )

    if 'Metadata' in resource_detail:
      resource_detail_metadata = resource_detail['Metadata']

      if 'aws:cdk:path' in resource_detail_metadata:
        return True

    return False

  def check_cdk_stack(self, stack_name: str):
    stack_resources = self.__cloudformation_service.get_stack_resources(stack_name)

    for resource in stack_resources or []:
      if self.__check_cdk_metadata_resource(resource) or \
        self.__check_stack_resource_from_cdk(resource):
        return True

    return False

  def delete_developer_stack(self, stack_name: str):
    self.__cloudformation_service.delete_stack(stack_name)

  def get_status(self, stack_name: str):
    return self.__cloudformation_service.get_stack_status(stack_name)
