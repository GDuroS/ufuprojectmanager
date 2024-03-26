from OruData.Utils import MenuUtils
from OruData.Model.Menu import Menu

MENUS = []

CADASTRAR_USER_STORY = Menu(key="CADASTRAR_USER_STORY", name="User Stories", secure=True, icon="", action="route", route={'url_hash': 'story'})
CADASTRAR_ITERACAO = Menu(key="CADASTRAR_ITERACAO", name="Sprints", secure=True, icon="", action="route", route={'url_hash': 'sprint'})
CADASTRAR_RELEASE = Menu(key="CADASTRAR_RELEASE", name="Releases", secure=True, icon="", action="route", route={'url_hash': 'releases'})

