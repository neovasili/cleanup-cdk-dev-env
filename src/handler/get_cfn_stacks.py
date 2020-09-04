import os

from src.controller.cleanup_stacks import CleanUpStacksController

STACKS_NAME_PATTERN = os.environ['stacks_name_start_pattern']
SELF_STACK_NAME = os.environ['self_stack_name']

def handler(event, context):
  str(event)
  str(context)

  cleanup_controller = CleanUpStacksController()
  to_delete_stacks = cleanup_controller.get_developer_stacks(
    name_pattern=STACKS_NAME_PATTERN,
    self_stack_name=SELF_STACK_NAME
  )

  response = {
    "to_delete_stacks": to_delete_stacks,
    "stacks_count": len(to_delete_stacks)
  }

  return response
