import anvil.server

from OruData.Service import AbstractService

TABLE = 'Users'

@anvil.server.callable
def getUsersFind(*args, **kwargs):
  return AbstractService.find(TABLE, *args, **kwargs)

@anvil.server.callable
def getDesenvolvedores():
  return getUsersFind(dev=True)