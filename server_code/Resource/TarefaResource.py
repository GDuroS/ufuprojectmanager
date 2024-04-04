import anvil.server

from OruData.Service import AbstractService

TABLE = 'Tarefa'

@anvil.server.callable
def getTarefaById(sequence:int):
  return AbstractService.get(TABLE, {'Sequence': sequence})

@anvil.server.callable
def getTarefasFind(*args, **kwargs):
  return AbstractService.find(TABLE, *args, **kwargs)

@anvil.server.callable(require_user=True)
def postTarefa(tarefa):
  from anvil import users
  tarefa['Criador'] = users.get_user()
  return AbstractService.save(TABLE, tarefa, True)

@anvil.server.callable(require_user=True)
def putTarefa(row, tarefa):
  return AbstractService.update(row, tarefa)

@anvil.server.callable(require_user=True)
def deleteTarefa(tarefa):
  return AbstractService.delete(tarefa)