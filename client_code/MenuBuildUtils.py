from OruData.Utils import MenuUtils
from OruData.Model.Menu import Menu

MENUS = []

HOME = Menu(key='HOME', name="Home", secure=False, icon="fa:home", action="route", route={'url_hash': ''})

CADASTRAR_USER_STORY = Menu(key="CADASTRAR_USER_STORY", name="User Stories", secure=True, icon="fa:file-signature", action="route", route={'url_hash': 'story'})
CADASTRAR_TASK = Menu(key="CADASTRAR_TASK", name="Tarefas", secure=True, icon="fa:list-check", action="route", route={'url_hash': 'task'})
CADASTRAR_ITERACAO = Menu(key="CADASTRAR_ITERACAO", name="Sprints", secure=True, icon="fa:person-chalkboard", action="route", route={'url_hash': 'sprint'})
CADASTRAR_RELEASE = Menu(key="CADASTRAR_RELEASE", name="Releases", secure=True, icon="fa:code-merge", action="route", route={'url_hash': 'release'})

SCRUM_BOARD = Menu(key="SCRUM_BOARD", name="Scrum Board", secure=True, icon="fa:bars-progress", action="route", route={'url_hash': 'board'})

DOCUMENTATION = Menu(key="DOCUMENTATION", name="Documentação", secure=False, icon="fa:book", action="route", route={'url_hash': 'docs'})
CREDITS = Menu(key="CREDITS", name="Sobre", secure=False, icon="fas:circle-question", action="route", route={'url_hash': 'about'})

def get_menu():
  return [
    HOME,
    CADASTRAR_USER_STORY,
    CADASTRAR_TASK,
    CADASTRAR_RELEASE,
    CADASTRAR_ITERACAO,
    SCRUM_BOARD,
    DOCUMENTATION,
    CREDITS
  ]

def get_menu_array():
  global MENUS
  
  if len(MENUS) == 0:
    MENUS = MenuUtils.cria_components(get_menu())
  return MENUS