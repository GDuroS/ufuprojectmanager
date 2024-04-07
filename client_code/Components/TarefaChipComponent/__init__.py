from ._anvil_designer import TarefaChipComponentTemplate
from anvil import *

from ...Model.Enums import StatusTarefa

class TarefaChipComponent(TarefaChipComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.role = 'tarefa-chip-component'
    self._sprint_selected = None

  @property
  def sprint_selected(self):
    return self._sprint_selected

  @sprint_selected.setter
  def sprint_selected(self, value):
    self._sprint_selected = value

  @property
  def next_icon(self):
    next_status = self.item.status_enum.next
    if next_status is None:
      return None
    return StatusTarefa.by_key(next_status).icon

  @property
  def previous_icon(self):
    prev_status = self.item.status_enum.previous
    if prev_status is None:
      return None
    return StatusTarefa.by_key(prev_status).icon

  def tarefa_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    from OruData.Utils import RoutingUtils
    RoutingUtils.set_url_hash(f'task/{self.item["Sequence"]}/view')

  def move_left_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from anvil import server
    if self.item.status_enum.previous == 'BACKLOG':
      self.item['Desenvolvedor'] = None
      self.item['Sprint'] = None
    self.item['Status'] = self.item.status_enum.previous
    server.call('putTarefa', self.item.original_row, self.item.row_changes)
    self.raise_event('moved', new_status=self.item.status_enum.previous)

  def move_right_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    from anvil import server
    if self.item.status_enum.next == 'ATRIBUIDA':
      from .AssignDevAlert import AssignDevAlert
      cb = alert(AssignDevAlert(), buttons=[], dismissible=False)
      if cb is None:
        return
      self.item['Desenvolvedor'] = cb
      self.item['Sprint'] = self.sprint_selected.original_row
    self.item['Status'] = self.item.status_enum.next
    server.call('putTarefa', self.item.original_row, self.item.row_changes)
    self.raise_event('moved', new_status=self.item.status_enum.next)
