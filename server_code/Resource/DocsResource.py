import anvil.server

from ..Service import DocsService

@anvil.server.callable
def getDocsReport():
  return DocsService.generate_report()
