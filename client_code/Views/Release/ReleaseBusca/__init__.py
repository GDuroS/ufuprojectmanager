from ._anvil_designer import ReleaseBuscaTemplate
from anvil import *

from OruData.Utils import RoutingUtils, ObjectUtils
from ....Model.Entities import Release

@RoutingUtils.route('release')
class ReleaseBusca(ReleaseBuscaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from anvil import server
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def search(self, **event_args):
    from anvil.tables import query as q
    from anvil import server
    filter = {
      'Titulo': self.titulo_text_box.text if len(self.titulo_text_box.text) > 0 else None,
      'Inicio': None if self.inicio_date_range_component.item is None else self.inicio_date_range_component.item.get_comparator(),
      'Termino': None if self.termino_date_range_component.item is None else self.termino_date_range_component.item.get_comparator()
    }
    self.result_data_panel.items = ObjectUtils.search_iterator_to_entity_class_list(
      server.call('getReleasesFind', **{k:v for k, v in filter.items() if v is not None}),
      Release
    )
    self.result_data_grid.visible = True
    self.result_data_panel.visible = len(self.result_data_panel.items) > 0
    self.no_result_label.visible = not self.result_data_panel.visible


  def create(self, **event_args):
    RoutingUtils.set_url_hash('release/new', load_from_cache=False)

  def clear(self, **event_args):
    self.titulo_text_box.text = None
    self.inicio_date_range_component.clear_button_click()
    self.termino_date_range_component.clear_button_click()

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    RoutingUtils.set_navbar_links(
      create_visible=True, create_callback=self.create,
      search_visible=True, search_callback=self.search,
      clear_visible=True, clear_callback=self.clear
    )
    self.clear()
