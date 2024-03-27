from OruData.Model.Enum import BaseEnum

class Prioridade(BaseEnum):
  __options__ = {
    'BAIXA': {'nivel': 1, 'nome': 'Baixa', 
              'descricao': 'Não há prazo para conclusão nem prejuízo em realizá-la apenas quando não houver outras prioridades.', 
              'prazo': None}, # Ilimitado
    'NORMAL': {'nivel': 2, 'nome': 'Normal', 
               'descricao': 'Precisa ser feita eventualmente, dentro de uma fila, porém não há urgência no atendimento. Caso ela seja adiada por muito tempo, poderá se tornar crítica.', 
               'prazo': 600}, # 1 mês
    'ALTA': {'nivel': 3, 'nome': 'Alta', 
             'descricao': 'Importante e deverá ser planejada de acordo. Precisa ser atendida em breve, antes das situações normais. Ainda não é uma emergência, mas poderá facilmente se tornar uma caso seja adiada.', 
             'prazo': 120}, # 1 Semana
    'URGENTE': {'nivel': 4, 'nome': 'Urgente', 
                'descricao': 'É imperativo que a seja atendido imediatamente.', 
                'prazo': 48}
  }

  _nivel = None
  _nome = None
  _descricao = None
  _prazo = None

  @property
  def nivel(self):
    return self._nivel

  @property
  def nome(self):
    return self._nome

  @property
  def descricao(self):
    return self._descricao

  @property
  def prazo(self):
    return self._prazo


class TipoTarefa(BaseEnum):
  __options__ = {
    'PROCEDIMENTO': {
      'ordem': 1, 'grau': 3, 'nome': 'Solicitação de Procedimento', 
      'descricao': 'Realização de procedimento pontual, como inserção, correção, exportação ou remoção de dado do usuário.'
    },
    'MELHORIA': {
      'ordem': 2, 'grau': 2, 'nome': 'Solicitação de Funcionalidade', 
      'descricao': 'Criação de nova funcionalidade para o sistema ou melhoria, expansão ou ajuste de funcionalidade já existente no sistema.'
    },
    'BUG': {
      'ordem': 3, 'grau': 4, 'nome': 'Reportar um Erro', 
      'descricao': 'Um problema foi encontrado em determinada operação ou funcionadade.'
    },
    'OUTROS': {
      'ordem': 4, 'grau': 1, 'nome': 'Outros Assuntos', 
      'descricao': 'Solicitações diversas que não se enquadram em nenhuma opção anterior, como pedido de suporte técnico para dúvidas, solicitação de orçamentos, sugestões de alterações, reclamações, elogios, etc.'
    }
  }
  _ordem = None
  _grau = None
  _nome = None
  _descricao = None

  @property
  def grau(self):
    return self._grau

  @property
  def ordem(self):
    return self._ordem

  @property
  def nome(self):
    return self._nome

  @property
  def descricao(self):
    return self._descricao