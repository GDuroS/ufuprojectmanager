from ._anvil_designer import UserStoryCadastroTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

from ....Model.Enums import Prioridade, TipoTarefa

@RoutingUtils.route('story/new')
@RoutingUtils.route('story/{id}/view')
@RoutingUtils.route('story/{id}/edit')
class UserStoryCadastro(CrudInterface, UserStoryCadastroTemplate):
  def __init__(self, item_row=None, **properties):
    # Set Form properties and Data Bindings.
    CrudInterface.__init__(self, 'UserStory', item_row)
    self.tipo_drop_down.items = TipoTarefa.attr_key_tuple('nome')
    self.prioridade_drop_down.items = Prioridade.attr_key_tuple('nome')

    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validationUtils.define_componentes_obrigatorios([
      (self.titulo_text_box, self.tipo_input_label),
      (self.tipo_drop_down, self.tipo_input_label),
      (self.prioridade_drop_down, self.prioridade_input_label),
      (None, self.pontos_input_label),
      (None, self.limite_input_label),
      (self.descricao_quill, self.descricao_input_label)
    ])
