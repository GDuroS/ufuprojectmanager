import anvil.server

from OruData.Service import AbstractService

TABLE = 'UserStory'

@anvil.server.callable
def getUserStoryById(sequence:int):
  return AbstractService.get(TABLE, {'Sequence': sequence})

@anvil.server.callable
def getUserStoriesFind(*args, **kwargs):
  return AbstractService.find(TABLE, *args, **kwargs)

@anvil.server.callable
def postUserStory(user_story):
  return AbstractService.save(TABLE, user_story, True)

@anvil.server.callable
def putUserStory(row, user_story):
  return AbstractService.update(row, user_story)

@anvil.server.callable
def deleteUserStory(user_story):
  return AbstractService.delete(user_story)