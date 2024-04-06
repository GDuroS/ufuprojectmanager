from ._anvil_designer import ReleaseCadastroTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

from ....Model.Entities import Release

from datetime import date

@RoutingUtils.route('release/new')
@RoutingUtils.route('release/{id}/view')
@RoutingUtils.route('release/{id}/edit')
class ReleaseCadastro(CrudInterface, ReleaseCadastroTemplate):
  def __init__(self, item_row=None, **properties):
    # Set Form properties and Data Bindings.
    CrudInterface.__init__(self, Release, item_row, on_navigate=self.on_navigate)

    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.validationUtils.define_componentes_obrigatorios([
      (self.inicio_date_picker, self.inicio_input_label),
      (self.termino_date_picker, self.termino_input_label)
    ])

  @property
  def hoje(self):
    return date.today()

  @property
  def min_termino(self):
    return self.inicio_date_picker.date if self.inicio_date_picker.date is not None else self.hoje

  def go_back(self, **event_args):
    self.routingUtils.set_url_hash('release')

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
