from ._anvil_designer import UserStoryCadastroTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

from ....Model.Enums import Prioridade, TipoTarefa
from ....Model.Entities import UserStory

from datetime import date

@RoutingUtils.route('story/new')
@RoutingUtils.route('story/{id}/view')
@RoutingUtils.route('story/{id}/edit')
class UserStoryCadastro(CrudInterface, UserStoryCadastroTemplate):
  def __init__(self, item_row=None, **properties):
    # Set Form properties and Data Bindings.
    CrudInterface.__init__(self, UserStory, item_row)
    self.tipo_drop_down.items = TipoTarefa.attr_key_tuple('nome')
    self.prioridade_drop_down.items = Prioridade.attr_key_tuple('nome')

    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validationUtils.define_componentes_obrigatorios([
      (self.titulo_text_box, self.tipo_input_label),
      (self.tipo_drop_down, self.tipo_input_label),
      (self.prioridade_drop_down, self.prioridade_input_label),
      (self.pontos_text_box, self.pontos_input_label),
      (self.limite_date_picker, self.limite_input_label),
      (self.descricao_quill, self.descricao_input_label)
    ])

  @property
  def hoje(self):
    return date.today()

  def pontos_text_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    value = self.pontos_text_box.text
    if value and value < 0:
      self.pontos_text_box.text = 0

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    RoutingUtils.set_navbar_links(
      back_visible=True, back_callback=lambda:self.routingUtils.go_back(),
      save_visible=True, save_callback=None
    )

  def save_click(self, **event_args):
    pass
