from ._anvil_designer import SprintCadastroTemplate
from anvil import *

from OruData.Utils import RoutingUtils, ObjectUtils
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
    self.release_drop_down.items = [(str(r), r) for r in ObjectUtils.search_iterator_to_entity_class_list(server.call('getReleasesFind'), Release)]
    CrudInterface.__init__(self, Sprint, item_row, on_navigate=self.on_navigate)

    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validationUtils.define_componentes_obrigatorios([
      (self.titulo_text_box, self.titulo_input_label),
      (self.inicio_date_picker, self.inicio_input_label),
      (self.termino_date_picker, self.termino_input_label),
      (self.release_drop_down, self.release_input_label)
    ])

  @property
  def hoje(self):
    return date.today()

  @property
  def min_termino(self):
    return self.inicio_date_picker.date if self.inicio_date_picker.date is not None else self.hoje

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
    RoutingUtils.set_navbar_links(
      back_visible=True, back_callback=self.go_back,
      save_visible=self.create_mode or self.edit_mode, save_callback=self.action_link_click,
      edit_visible=self.view_mode, edit_callback=self.action_link_click
    )

  def on_navigate(self, from_mode:str, to_mode:str):
    RoutingUtils.set_navbar_links(
      back_visible=True, back_callback=self.go_back,
      save_visible=to_mode.upper() in ['NEW', 'EDIT'], save_callback=self.action_link_click,
      edit_visible=to_mode.upper() == 'VIEW', edit_callback=self.action_link_click
    )

  def release_autocomplete_selected_value_change(self, selected_value, **event_args):
    self.item['Release'] = selected_value
