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

@anvil.server.portable_class
class Tarefa(Entity):
  _prioridade_enum = None
  _tipo_enum = None

  @property
  def prioridade_enum(self):
    if self._prioridade_enum is None:
      if self['Prioridade'] is not None:
        from .Enums import Prioridade
        self._prioridade_enum = Prioridade.by_key(self['Prioridade'])
    return self._prioridade_enum

  @property
  def tipo_enum(self):
    if self._tipo_enum is None:
      if self['Tipo'] is not None:
        from .Enums import TipoTarefa
        self._tipo_enum = TipoTarefa.by_key(self['Tipo'])
    return self._tipo_enum