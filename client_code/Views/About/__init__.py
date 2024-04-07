from ._anvil_designer import AboutTemplate
from anvil import *

from OruData.Utils import RoutingUtils

@RoutingUtils.route('about')
class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
