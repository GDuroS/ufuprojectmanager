from ._anvil_designer import AssignDevAlertTemplate
from anvil import *

class AssignDevAlert(AssignDevAlertTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    from anvil import server
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down.items = [(d['display_name'], d) for d in server.call('getDesenvolvedores')]

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event('x-close-alert', value=None)

  def confirm_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.drop_down.selected_value is None:
      Notification("Escolha um desenvolvedor para continuar.", style="warning").show()
      return
    self.raise_event('x-close-alert', value=self.drop_down.selected_value)
