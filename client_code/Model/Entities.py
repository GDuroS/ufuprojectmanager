import anvil.server
from OruData.Model.Entity import Entity

@anvil.server.portable_class
class UserStory(Entity):
  _prioridade_enum = None
  _tipo_enum = None

  @property
  def prioridade_enum(self):
    if self._prioridade_enum is None:
      from .Enums import Prioridade
      self._prioridade_enum = Prioridade.by_key(self['Prioridade'])
    return self._prioridade_enum

  @property
  def tipo_enum(self):
    if self._tipo_enum is None:
      from .Enums import TipoTarefa
      self._tipo_enum = TipoTarefa.by_key(self['Tipo'])
    return self._tipo_enum

  @property
  def tipo_nome(self):
    return self.prioridade_enum.nome

  @property
  def prioridade_nome(self):
    return self.prioridade_enum.nome

  @classmethod
  def from_(cls, row):
    return super().from_(row, 'Titulo')

@anvil.server.portable_class
class Tarefa(Entity):
  _prioridade_enum = None
  _tipo_enum = None
  _user_story = None

  @property
  def prioridade_enum(self):
    if self._prioridade_enum is None:
      from .Enums import Prioridade
      self._prioridade_enum = Prioridade.by_key(self['Prioridade'])
    return self._prioridade_enum

  @property
  def tipo_enum(self):
    if self._tipo_enum is None:
      from .Enums import TipoTarefa
      self._tipo_enum = TipoTarefa.by_key(self['Tipo'])
    return self._tipo_enum

  @property
  def tipo_nome(self):
    return self.prioridade_enum.nome

  @property
  def prioridade_nome(self):
    return self.prioridade_enum.nome

  @property
  def user_story(self):
    return self._user_story

  @classmethod
  def from_(cls, row):
    inst = super().from_(row, 'Titulo')
    if not inst.is_new:
      inst._user_story = UserStory.from_(row['UserStory'])
    return inst