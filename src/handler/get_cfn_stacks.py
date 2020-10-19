import os

from src.controller.cleanup_stacks import CleanUpStacksControllerRetriever

STACKS_NAME_PATTERNS = os.environ['stacks_name_start_patterns']
SELF_STACK_NAME = os.environ['self_stack_name']

def handler(event, context):
  str(event)
  str(context)

  stack_name_patterns = STACKS_NAME_PATTERNS.split(',')

  cleanup_controller = CleanUpStacksControllerRetriever(
    name_patterns=stack_name_patterns,
    self_stack_name=SELF_STACK_NAME
  )
  to_delete_stacks = cleanup_controller.get_developer_stacks_to_delete()

  response = {
    "to_delete_stacks": to_delete_stacks,
    "stacks_count": len(to_delete_stacks)
  }

  return response
