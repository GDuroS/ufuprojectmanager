from ._anvil_designer import UserStoryCadastroTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

@RoutingUtils.route('story/new')
@RoutingUtils.route('story/{id}/view')
@RoutingUtils.route('story/{id}/edit')
class UserStoryCadastro(CrudInterface, UserStoryCadastroTemplate):
  def __init__(self, item_row=None, **properties):
    # Set Form properties and Data Bindings.
    CrudInterface.__init__(self, 'UserStory', item_row)
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
