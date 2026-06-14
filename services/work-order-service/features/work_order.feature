Feature: Abertura de ordem de servico
  Scenario: Cliente relata problema urgente no freio
    Given um cliente com veiculo cadastrado
    When o atendente abre uma ordem com urgencia alta
    Then a ordem deve ser criada com prioridade alta
    And um evento de ordem criada deve ser publicado

  Scenario: Cliente solicita atendimento preventivo de baixa urgencia
    Given um cliente com veiculo cadastrado
    When o atendente abre uma ordem com urgencia baixa e reclamacao "Troca de oleo"
    Then a ordem deve ser criada com prioridade baixa

  Scenario: Cliente relata vazamento mesmo com urgencia baixa
    Given um cliente com veiculo cadastrado
    When o atendente abre uma ordem com urgencia baixa e reclamacao "Vazamento de oleo"
    Then a ordem deve ser criada com prioridade alta
