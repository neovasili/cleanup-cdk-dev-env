from src.service.cloudformation import CloudFormationService

class CleanUpStacksController():

  def __init__(self):
    super().__init__()
    self.__cloudformation_service = CloudFormationService()

  def get_developer_stacks(self, name_pattern: str, self_stack_name: str):
    stacks = self.__cloudformation_service.get_developer_stacks(name_pattern, self_stack_name)

    stack_names = list()
    for stack in stacks or []:
      stack_names.append(stack.get_name())

    return stack_names

  def delete_developer_stack(self, stack_name: str):
    self.__cloudformation_service.delete_stack(stack_name)

  def get_status(self, stack_name: str):
    return self.__cloudformation_service.get_stack_status(stack_name)
