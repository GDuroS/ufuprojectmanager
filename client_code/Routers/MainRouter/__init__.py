from ._anvil_designer import MainRouterTemplate
from anvil import *

from OruData.Utils import RoutingUtils

"""Possible Routes"""
from OruData.Views import NoRoute, LoginForm
# Home
from ...Views import Home, ScrumBoard
# Telas
from ...Views.UserStories import UserStoryBusca, UserStoryCadastro
from ...Views.Tarefas import TarefaBusca, TarefaCadastro
from ...Views.Sprint import SprintBusca, SprintCadastro
from ...Views.Release import ReleaseBusca, ReleaseCadastro

@RoutingUtils.default_template
class MainRouter(MainRouterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    from OruData.SidebarComponent import get_instance as get_sidebar_instance
    from ... import MenuBuildUtils

    self.add_component(get_sidebar_instance(menu_array=MenuBuildUtils.get_menu_array()), slot="left-nav")

  def on_navigation(self, **nav_args):
    RoutingUtils.clear_navbar_setup()

  def refresh_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    RoutingUtils.reload_page()
