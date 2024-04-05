from ._anvil_designer import DefaultResultsRowTemplateTemplate
from anvil import *

class DefaultResultsRowTemplate(DefaultResultsRowTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.role = 'autocomplete-result'


  @property
  def grid_data(self):
    try:
      return self.parent
    except:
      return None

  def item_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.grid_data.raise_event('x-item-selected', value=self.item)

