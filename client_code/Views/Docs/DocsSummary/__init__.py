from ._anvil_designer import DocsSummaryTemplate
from anvil import *

from OruData.Utils import RoutingUtils

@RoutingUtils.route('docs')
class DocsSummary(DocsSummaryTemplate):
  def __init__(self, for_printing=False, **properties):
    # Set Form properties and Data Bindings.
    self._for_printing = for_printing
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if for_printing:
      from .DocsBoard import DocsBoard
      from .DocsRelease import DocsRelease
      from .DocsSprint import DocsSprint
      from .DocsTarefa import DocsTarefa
      from .DocsUserStory import DocsUserStory
      from anvil_extras.PageBreak import PageBreak

      self.background = 'white'
      self.foreground = 'black'

      to_add_list = [DocsUserStory, DocsTarefa, DocsRelease, DocsSprint, DocsBoard]
      for doc in to_add_list:
        self.content_panel.add_component(PageBreak())
        self.content_panel.add_component(doc())

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    if not self._for_printing:
      RoutingUtils.set_navbar_links(
        export_visible=True, export_callback=self.export_docs
      )

  def export_docs(self, **event_args):
    from anvil import server, media
    pdf = server.call('getDocsReport')
    media.download(pdf)
    
