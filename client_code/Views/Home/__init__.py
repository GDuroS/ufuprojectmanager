from ._anvil_designer import HomeTemplate
from anvil import *

from OruData.Utils import RoutingUtils

@RoutingUtils.route('')
class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.user_data_panel.items = [
      {'user': 'Admin', 'email': 'admin', 'pass': 'admin123'},
      {'user': 'Desenvolvedor', 'email': 'dev1', 'pass': 'dev123'},
      {'user': 'Usuário 1', 'email': 'user1', 'pass': 'user123'},
      {'user': 'Usuário 2', 'email': 'user2', 'pass': 'user233'}
    ]

    def teste_component():
      from anvil import server
      from ...Components.TarefaChipComponent import TarefaChipComponent
      from ...Model.Entities import Tarefa
      task = server.call('getTarefaById', 1)
      chip = TarefaChipComponent(item=Tarefa.from_(task))
      self.add_component(chip)

    teste_component()
      
