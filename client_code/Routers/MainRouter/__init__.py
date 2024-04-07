from ._anvil_designer import MainRouterTemplate
from anvil import *

from OruData.Utils import RoutingUtils

"""Possible Routes"""
from OruData.Views import NoRoute, LoginForm
# Home
from ...Views import Home, ScrumBoard, About
# Documentação
# from ...Views.Docs import DocsSummary
from ...Views.Docs.DocsSummary import DocsSummary, DocsBoard, DocsUserStory, DocsTarefa, DocsRelease, DocsSprint
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

    self.add_component(get_sidebar_instance(show_user_options=False, menu_array=MenuBuildUtils.get_menu_array()), slot="left-nav")
    get_sidebar_instance(False)

  def on_navigation(self, **nav_args):
    from OruData.Utils import UserUtils
    if UserUtils.get_logged_user() is None:
      if not RoutingUtils.get_url_hash().startswith(tuple(['about', 'docs', '/login', '/signup'])) and not RoutingUtils.get_url_hash() == '':
        Notification("Não é permitido acessar a tela solicitada sem estar logado no sistema.", title="Não permitido", style="warning").show()
        RoutingUtils.set_url_hash('/login')
    RoutingUtils.clear_navbar_setup()

  def refresh_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    RoutingUtils.reload_page()

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    from anvil import js
    js.call('addMarginToContent')
