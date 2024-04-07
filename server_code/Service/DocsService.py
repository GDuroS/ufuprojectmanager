import anvil.server

def generate_report():
  from anvil.pdf import PDFRenderer
  return PDFRenderer(filename="ProjectManager Documentação e Requisitos.pdf", page_size="A4").render_form(
    'Views.Docs.DocsSummary', for_printing=True
  )
