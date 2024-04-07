from ._anvil_designer import DocsReleaseTemplate
from anvil import *

from OruData.Utils import RoutingUtils

@RoutingUtils.route('docs/release')
class DocsRelease(DocsReleaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
