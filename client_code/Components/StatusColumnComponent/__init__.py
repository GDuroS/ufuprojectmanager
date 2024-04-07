from ._anvil_designer import StatusColumnComponentTemplate
from anvil import *

class StatusColumnComponent(StatusColumnComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.role = 'board-column'
    self.title_label.role = 'board-column'
    self.column_panel.role = 'board-column'
    self._sprint_selected = None

  @property
  def sprint_selected(self):
    return self._sprint_selected

  @sprint_selected.setter
  def sprint_selected(self, value):
    self._sprint_selected = value

  def add_task(self, task):
    from ..TarefaChipComponent import TarefaChipComponent
    chip = TarefaChipComponent(item=task)
    chip.sprint_selected = self.sprint_selected
    chip.add_event_handler('moved', self.refresh)
    self.column_panel.add_component(chip)

  def clear_tasks(self):
    self.column_panel.clear()

  def refresh(self, **event_args):
    self.parent.raise_event('x-refresh', selected_value=self.sprint_selected)
    