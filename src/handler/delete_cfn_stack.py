from src.controller.cleanup_stacks import CleanUpStacksControllerDeleter

def handler(event, context):
  str(context)

  to_delete_stacks = event['to_delete_stacks']
  stack_name = to_delete_stacks.pop(0)

  cleanup_controller = CleanUpStacksControllerDeleter()
  cleanup_controller.delete_developer_stack(stack_name=stack_name)

  response = {
    "deleted_stack": stack_name,
    "to_delete_stacks": to_delete_stacks,
    "stacks_count": len(to_delete_stacks)
  }

  return response
