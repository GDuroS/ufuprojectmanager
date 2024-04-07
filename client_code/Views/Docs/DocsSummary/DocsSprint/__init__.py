from ._anvil_designer import DocsSprintTemplate
from anvil import *

from OruData.Utils import RoutingUtils

@RoutingUtils.route('docs/sprint')
class DocsSprint(DocsSprintTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
