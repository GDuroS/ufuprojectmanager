from ._anvil_designer import TarefaBuscaTemplate
from anvil import *

from OruData.Utils import RoutingUtils
from OruData.Views.CrudInterface import CrudInterface

@RoutingUtils.route('task')
class TarefaBusca(TarefaBuscaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from anvil import server
    self.sprint_drop_down.items = server.call('getSprintsFind')
    self.dev_drop_down.items = [(d['display_name'], d) for d in server.call('getDesenvolvedores')]
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def search(self, **event_args):
    from anvil.tables import query as q
    from anvil import server
    from ....Model.Entities import Tarefa
    from OruData.Utils import ObjectUtils
    filter = {
      'Titulo': self.titulo_text_box.text if len(self.titulo_text_box.text) > 0 else None,
      'Descricao': q.ilike(f"%{self.descricao_text_box.text}%") if len(self.descricao_text_box.text) > 0 else None,
      'Prioridade': self.prioridade_drop_down.selected_value,
      'Tipo': self.tipo_drop_down.selected_value,
      'Sprint': self.sprint_drop_down.selected_value,
      'Desenvolvedor': self.dev_drop_down.selected_value,
      'Tempo': None if self.tempo_number_range_component.item is None else self.tempo_number_range_component.item.get_comparator(),
      'Prazo': None if self.prazo_date_range_component.item is None else self.prazo_date_range_component.item.get_comparator()
    }
    self.result_data_panel.items = ObjectUtils.search_iterator_to_entity_class_list(
      server.call('getTarefasFind', **{k:v for k, v in filter.items() if v is not None}),
      UserStory
    )
    self.result_data_grid.visible = True
    self.result_data_panel.visible = len(self.result_data_panel.items) > 0
    self.no_result_label.visible = not self.result_data_panel.visible


  def create(self, **event_args):
    RoutingUtils.set_url_hash('task/new')

  def clear(self, **event_args):
    self.titulo_text_box.text = None
    self.descricao_text_box.text = None
    self.prioridade_drop_down.selected_value = None
    self.tipo_drop_down.selected_value = None
    self.tempo_number_range_component.clear_button_click()
    self.prazo_date_range_component.clear_button_click()
    self.sprint_drop_down.selected_value = None
    self.dev_drop_down.selected_value = None

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    RoutingUtils.set_navbar_links(
      create_visible=True, create_callback=self.create,
      search_visible=True, search_callback=self.search,
      clear_visible=True, clear_callback=self.clear
    )
    self.clear()
