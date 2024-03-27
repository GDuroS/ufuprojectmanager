from ._anvil_designer import MainRouterTemplate
from anvil import *

from OruData.Utils import RoutingUtils

"""Possible Routes"""
from OruData.Views import NoRoute
# UserStories
from ...Views.UserStories.UserStoryBusca import UserStoryBusca
from ...Views.UserStories.UserStoryCadastro import UserStoryCadastro

@RoutingUtils.default_template
class MainRouter(MainRouterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    from OruData.SidebarComponent import get_instance as get_sidebar_instance
    from ... import MenuBuildUtils

    self.add_component(get_sidebar_instance(show_user=False, menu_array=MenuBuildUtils.get_menu_array()), slot="left-nav")
