from ._anvil_designer import ScrumBoardTemplate
from anvil import *

from ...Model.Enums import StatusTarefa
from ...Model.Entities import Sprint, Tarefa
from ...Components.StatusColumnComponent import StatusColumnComponent

sprint_class = Sprint

from OruData.Utils import RoutingUtils

@RoutingUtils.route('board', full_width_row=True)
class ScrumBoard(ScrumBoardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self._columns = {}
    for k, status in StatusTarefa.items():
      column = StatusColumnComponent(item=status)
      self._columns[k] = column
      self.board_panel.add_component(column)
    self.board_panel.add_event_handler('x-refresh', self.sprint_autocomplete_component_selected_value_change)

  @property
  def entity_class(self):
    return sprint_class

  def sprint_autocomplete_component_selected_value_change(self, selected_value, **event_args):
    """This method is called Event triggered when the selected value was changed."""
    for column in self._columns.values():
      column.sprint_selected = selected_value if selected_value is not None else None
      column.clear_tasks()
    if selected_value is not None:
      # Busca as tasks sem sprint e no sprint escolhido
      from anvil.tables import query as q
      from anvil import server
      from OruData.Utils import ObjectUtils
      results = ObjectUtils.search_iterator_to_entity_class_list(
        server.call('getTarefasFind', **{'Sprint': q.any_of(None, selected_value.original_row)}), 
        Tarefa
      )
      for ta in results:
        self._columns.get(ta['Status']).add_task(ta)
