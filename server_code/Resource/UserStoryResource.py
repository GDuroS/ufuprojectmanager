import anvil.server

from OruData.Service import AbstractService

TABLE = 'UserStory'

@anvil.server.callable
def getUserStoryById(sequence:int):
  return AbstractService.get(TABLE, {'Sequence': sequence})

@anvil.server.callable
def getUserStoriesFind(*args, **kwargs):
  return AbstractService.find(TABLE, *args, **kwargs)

@anvil.server.callable(require_user=True)
def postUserStory(user_story):
  from anvil import users
  user_story['Criador'] = users.get_user()
  return AbstractService.save(TABLE, user_story, True)

@anvil.server.callable(require_user=True)
def putUserStory(row, user_story):
  return AbstractService.update(row, user_story)

@anvil.server.callable(require_user=True)
def deleteUserStory(user_story):
  return AbstractService.delete(user_story)