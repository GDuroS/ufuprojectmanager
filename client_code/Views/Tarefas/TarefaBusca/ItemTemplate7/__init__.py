from ._anvil_designer import ItemTemplate7Template
from anvil import *

class ItemTemplate7(ItemTemplate7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
