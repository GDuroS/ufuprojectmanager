from ._anvil_designer import TarefaCadastroTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

from ....Model.Enums import Prioridade, TipoTarefa
from ....Model.Entities import Tarefa, UserStory
user_story_class = UserStory

from datetime import date

@RoutingUtils.route('task/new')
@RoutingUtils.route('task/{id}/view')
@RoutingUtils.route('task/{id}/edit')
class TarefaCadastro(CrudInterface, TarefaCadastroTemplate):
  def __init__(self, item_row=None, **properties):
    # Set Form properties and Data Bindings.
    CrudInterface.__init__(self, Tarefa, item_row, on_navigate=self.on_navigate)
    self.tipo_drop_down.items = TipoTarefa.attr_key_tuple('nome')
    self.prioridade_drop_down.items = Prioridade.attr_key_tuple('nome')
    

    if self.has_entity:
      self.descricao_quill.set_html(self.item['Descricao'])
      self.story_autocomplete.set_selected_value(self.item.user_story)

    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validationUtils.define_componentes_obrigatorios([
      (self.titulo_text_box, self.tipo_input_label),
      (self.tipo_drop_down, self.tipo_input_label),
      (self.prioridade_drop_down, self.prioridade_input_label),
      (self.prazo_date_picker, self.prazo_input_label),
      (self.tempo_text_box, self.tempo_input_label),
      (self.descricao_quill, self.descricao_input_label),
      (self.story_autocomplete, self.story_input_label)
    ])

  @property
  def hoje(self):
    return date.today()

  @property
  def entity_class(self):
    return user_story_class

  @property
  def has_dev(self):
    try:
      return self.item['Desenvolvedor'] is not None
    except:
      return False

  @property
  def desenvolvedor_nome(self):
    if self.has_dev:
      return self.item['Desenvolvedor']['display_name']
    return None

  @property
  def sprint_nome(self):
    if self.has_dev:
      return self.item['Sprint']['Nome']
    return None

  @property
  def story_nome(self):
    try:
      return self.item.user_story
    except:
      return None

  def tempo_text_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    value = self.tempo_text_box.text
    if value and value < 0:
      self.tempo_text_box.text = 0

  def before_save(self):
    self.item['Descricao'] = self.descricao_quill.get_html()

  def go_back(self, **event_args):
    self.routingUtils.set_url_hash('task')

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.story_autocomplete.visible = self.create_mode or self.edit_mode
    RoutingUtils.set_navbar_links(
      back_visible=True, back_callback=self.go_back,
      save_visible=self.create_mode or self.edit_mode, save_callback=self.action_link_click,
      edit_visible=self.view_mode, edit_callback=self.action_link_click
    )

  def on_navigate(self, from_mode:str, to_mode:str):
    if to_mode.upper() in ['VIEW', 'EDIT']:
      self.descricao_quill.set_html(self.item['Descricao'])
    self.story_autocomplete.visible = to_mode.upper() in ['EDIT', 'NEW']
    RoutingUtils.set_navbar_links(
      back_visible=True, back_callback=self.go_back,
      save_visible=to_mode.upper() in ['NEW', 'EDIT'], save_callback=self.action_link_click,
      edit_visible=to_mode.upper() == 'VIEW', edit_callback=self.action_link_click
    )

  def story_autocomplete_selected_value_change(self, selected_value, **event_args):
    self.item['UserStory'] = selected_value
