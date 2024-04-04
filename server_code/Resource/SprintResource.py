import anvil.server

from OruData.Service import AbstractService

TABLE = 'Sprint'

@anvil.server.callable
def getSprintById(sequence:int):
  return AbstractService.get(TABLE, {'Sequence': sequence})

@anvil.server.callable
def getSprintsFind(*args, **kwargs):
  return AbstractService.find(TABLE, *args, **kwargs)

@anvil.server.callable(require_user=True)
def postSprint(sprint):
  from anvil import users
  sprint['Criador'] = users.get_user()
  return AbstractService.save(TABLE, sprint, True)

@anvil.server.callable(require_user=True)
def putSprint(row, sprint):
  return AbstractService.update(row, sprint)

@anvil.server.callable(require_user=True)
def deleteSprint(sprint):
  return AbstractService.delete(sprint)