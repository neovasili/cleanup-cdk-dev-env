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

  def check_cdk_stack(self, stack_name: str):
    stack_resources = self.__cloudformation_service.get_stack_resources(stack_name)

    for resource in stack_resources or []:
      resource_type = resource['ResourceType']
      if resource_type == 'AWS::CDK::Metadata':
        return True

    return False

  def delete_developer_stack(self, stack_name: str):
    self.__cloudformation_service.delete_stack(stack_name)

  def get_status(self, stack_name: str):
    return self.__cloudformation_service.get_stack_status(stack_name)
