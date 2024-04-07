from ._anvil_designer import DocsTarefaTemplate
from anvil import *

from OruData.Utils import RoutingUtils

@RoutingUtils.route('docs/task')
class DocsTarefa(DocsTarefaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
