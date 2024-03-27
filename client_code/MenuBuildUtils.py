from OruData.Utils import MenuUtils
from OruData.Model.Menu import Menu

MENUS = []

CADASTRAR_USER_STORY = Menu(key="CADASTRAR_USER_STORY", name="User Stories", secure=True, icon="fa:file-signature", action="route", route={'url_hash': 'story'})
CADASTRAR_TASK = Menu(key="CADASTRAR_TASK", name="Tarefas", secure=True, icon="fa:list-check", action="route", route={'url_hash': 'task'})
CADASTRAR_ITERACAO = Menu(key="CADASTRAR_ITERACAO", name="Sprints", secure=True, icon="fa:person-chalkboard", action="route", route={'url_hash': 'sprint'})
CADASTRAR_RELEASE = Menu(key="CADASTRAR_RELEASE", name="Releases", secure=True, icon="fa:code-merge", action="route", route={'url_hash': 'releases'})
SCRUM_BOARD = Menu(key="SCRUM_BOARD", name="Scrum Board", secure=False, icon="fa:file-signature", action="route", route={'url_hash': 'story'})

def get_menu():
  return [
    CADASTRAR_USER_STORY,
    CADASTRAR_ITERACAO,
    CADASTRAR_RELEASE
  ]

def get_menu_array():
  global MENUS
  
  if len(MENUS) == 0:
    MENUS = MenuUtils.cria_components(get_menu())
  return MENUS