from ._anvil_designer import UserStoryBuscaTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

@RoutingUtils.route('story')
class UserStoryBusca(UserStoryBuscaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
