# arquivo: test_estacionamento.py
import pytest
from pytest_bdd import scenarios, given, when, then
from datetime import datetime, timedelta
from estacionamento import Estacionamentos
from ticket import Ticket

# Carregar o cenário do arquivo estacionamento.feature
scenarios('estacionamento.feature')

@pytest.fixture
def estacionamento():
    return Estacionamentos()

@pytest.fixture
def ticket():
    return Ticket(placa='ABC1234', modelo='Fusca')

@given('um veículo entra no estacionamento')
def veiculo_entra(estacionamento, ticket):
    estacionamento.emitir_tickets(ticket)

@when('o frentista emite um ticket para o vaículo')
def emitir_ticket(estacionamento, ticket):
    estacionamento.emitir_tickets(ticket)

@then('o ticket contém informações corretas sobre a entrada do veículo')
def validar_ticket(ticket):
    assert ticket.placa == 'ABC1234'
    assert ticket.modelo == 'Fusca'
    assert isinstance(ticket.entrada, datetime)

@given('um veículo está estacionado há 2 anos')
def veiculo_estacionado_2_anos(ticket):
    ticket.entrada = datetime.now() - timedelta(days=2*365)

@when('o cliente apresenta o ticket de entrada para a saída')
def cliente_apresenta_ticket(estacionamento, ticket):
    estacionamento.registrar_saida(ticket)

@then('o frentista calcula o valor devido corretamente')
def calcular_valor_devido(estacionamento, ticket):
    valor = estacionamento.calcular_valor_devido(ticket)
    expected_valor = 15 + (2*365*24 - 1) * 5  # Calcula o valor esperado para 2 anos
    assert valor == pytest.approx(expected_valor, rel=1e-3)
