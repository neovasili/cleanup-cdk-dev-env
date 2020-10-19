from src.model.cloudformation import CloudFormationStack
from src.service.cloudformation import CloudFormationService

class CleanUpStacksController():

  def __init__(self):
    super().__init__()
    self.cloudformation_service = CloudFormationService()

class CleanUpStacksControllerRetriever(CleanUpStacksController):

  def __init__(self, name_patterns: str, self_stack_name: str):
    super().__init__()
    self.__name_patterns = name_patterns
    self.__self_stack_name = self_stack_name

  def __check_stack_name_filter(self, stack_name: str):
    for stack_name_pattern in self.__name_patterns:
      if stack_name.startswith(stack_name_pattern):
        return True

    return False

  def __check_self_stack_name_filter(self, stack_name: str):
    return stack_name != self.__self_stack_name

  @classmethod
  def __check_cdk_metadata_resource(cls, stack_resource: dict):
    resource_type = stack_resource['ResourceType']

    return resource_type == 'AWS::CDK::Metadata'

  def __check_stack_resource_from_cdk(self, stack_resource: dict):
    stack_name = stack_resource['StackName']
    resource_logical_id = stack_resource['LogicalResourceId']

    resource_detail = self.cloudformation_service.get_stack_resource_detail(
      stack_name,
      resource_logical_id
    )

    if 'Metadata' in resource_detail:
      resource_detail_metadata = resource_detail['Metadata']

      if 'aws:cdk:path' in resource_detail_metadata:
        return True

    return False

  def __check_is_cdk_stack(self, stack_name: str):
    stack_resources = self.cloudformation_service.get_stack_resources(stack_name)

    for resource in stack_resources or []:
      if self.__check_cdk_metadata_resource(resource) or \
        self.__check_stack_resource_from_cdk(resource):
        return True

    return False

  @classmethod
  def __check_retention_policy(cls, stack: CloudFormationStack):
    return stack.get_retention_policy() != 'RETAIN'

  def get_developer_stacks_to_delete(self):
    stacks = self.cloudformation_service.get_developer_stacks()

    stack_names = list()
    for stack in stacks or []:
      stack_name = stack.get_name()
      if self.__check_self_stack_name_filter(stack_name) and \
          self.__check_stack_name_filter(stack_name) and \
          self.__check_is_cdk_stack(stack_name) and \
          self.__check_retention_policy(stack):
        stack_names.append(stack_name)

    return stack_names

class CleanUpStacksControllerDeleter(CleanUpStacksController):

  def delete_developer_stack(self, stack_name: str):
    self.cloudformation_service.delete_stack(stack_name)

class CleanUpStacksControllerChecker(CleanUpStacksController):

  def get_status(self, stack_name: str):
    return self.cloudformation_service.get_stack_status(stack_name)
