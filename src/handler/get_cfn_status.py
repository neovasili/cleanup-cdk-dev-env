from src.controller.cleanup_stacks import CleanUpStacksController

def handler(event, context):
  str(context)

  to_delete_stacks = event['to_delete_stacks']
  stack_name = event['deleted_stack']

  cleanup_controller = CleanUpStacksController()
  status = cleanup_controller.get_status(stack_name=stack_name)

  response = {
    "deleted_stack": stack_name,
    "status": status,
    "to_delete_stacks": to_delete_stacks,
    "stacks_count": len(to_delete_stacks)
  }

  return response
