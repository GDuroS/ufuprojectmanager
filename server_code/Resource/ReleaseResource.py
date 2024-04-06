import anvil.server

from OruData.Service import AbstractService

TABLE = 'Release'

@anvil.server.callable
def getReleaseById(sequence:int):
  return AbstractService.get(TABLE, {'Sequence': sequence})

@anvil.server.callable
def getReleasesFind(*args, **kwargs):
  return AbstractService.find(TABLE, *args, **kwargs)

@anvil.server.callable(require_user=True)
def postRelease(release):
  return AbstractService.save(TABLE, release, True)

@anvil.server.callable(require_user=True)
def putRelease(row, release):
  return AbstractService.update(row, release)

@anvil.server.callable(require_user=True)
def deleteRelease(release):
  return AbstractService.delete(release)