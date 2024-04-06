from ._anvil_designer import SprintCadastroTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

from ....Model.Entities import Sprint, Release
user_story_class = Release

from datetime import date

@RoutingUtils.route('sprint/new')
@RoutingUtils.route('sprint/{id}/view')
@RoutingUtils.route('sprint/{id}/edit')
class SprintCadastro(CrudInterface, SprintCadastroTemplate):
  def __init__(self, item_row=None, **properties):
    # Set Form properties and Data Bindings.
    CrudInterface.__init__(self, Sprint, item_row, on_navigate=self.on_navigate)    

    if self.has_entity:
      self.release_autocomplete.set_selected_value(self.item['Release'])

    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validationUtils.define_componentes_obrigatorios([
      (self.titulo_text_box, self.tipo_input_label),
      (self.inicio_date_picker, self.inicio_input_label),
      (self.termino_date_picker, self.termino_input_label),
      (self.release_autocomplete, self.release_input_label)
    ])

  @property
  def hoje(self):
    return date.today()

  @property
  def entity_class(self):
    return user_story_class

  @property
  def release_nome(self):
    try:
      return f"{str(self.item['Release']['Sequence']).zfill(4)}: {'{:%d/%m/%Y}'.format(self.item['Release']['Inicio'])}"
    except:
      return None

  def go_back(self, **event_args):
    self.routingUtils.set_url_hash('sprint')

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.release_autocomplete.visible = self.create_mode or self.edit_mode
    RoutingUtils.set_navbar_links(
      back_visible=True, back_callback=self.go_back,
      save_visible=self.create_mode or self.edit_mode, save_callback=self.action_link_click,
      edit_visible=self.view_mode, edit_callback=self.action_link_click
    )

  def on_navigate(self, from_mode:str, to_mode:str):
    self.release_autocomplete.visible = to_mode.upper() in ['EDIT', 'NEW']
    RoutingUtils.set_navbar_links(
      back_visible=True, back_callback=self.go_back,
      save_visible=to_mode.upper() in ['NEW', 'EDIT'], save_callback=self.action_link_click,
      edit_visible=to_mode.upper() == 'VIEW', edit_callback=self.action_link_click
    )

  def release_autocomplete_selected_value_change(self, selected_value, **event_args):
    self.item['Release'] = selected_value
