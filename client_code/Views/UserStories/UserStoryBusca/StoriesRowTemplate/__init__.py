from ._anvil_designer import StoriesRowTemplateTemplate
from anvil import *

class StoriesRowTemplate(StoriesRowTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def edit_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    from OruData.Utils import RoutingUtils
    RoutingUtils.set_url_hash(f'story/{self.item["Sequence"]}/view')
