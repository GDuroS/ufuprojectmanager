from ._anvil_designer import DocsBoardTemplate
from anvil import *

from OruData.Utils import RoutingUtils

@RoutingUtils.route('docs/board')
class DocsBoard(DocsBoardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
