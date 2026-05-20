# ============================================================
#   TRANSFERENCIA NUBANK — Diagrama de Sequencia
#   Aula 07 - Diagramas de Sequencia
# ============================================================

# CELULA 1 — BancoDeDados (Participante 4)
class BancoDeDados:
    def __init__(self):
        self.saldos = {"user_123": 500.0}

    def verificar_saldo(self, user_id: str) -> float:
        return self.saldos.get(user_id, 0.0)

    def debitar(self, user_id: str, valor: float) -> bool:
        if self.saldos.get(user_id, 0.0) >= valor:
            self.saldos[user_id] -= valor
            return True
        return False

# CELULA 2 — ServidorNubank
class ServidorNubank:
    def __init__(self):
        self.banco = BancoDeDados()

    def processar_transferencia(self, user_id: str, valor: float) -> dict:
    saldo = self.banco.verificar_saldo(user_id)

    if saldo >= valor:
        self.banco.debitar(user_id, valor)
        saldo_restante = self.banco.verificar_saldo(user_id)
        return {"status": "aprovado", "saldo_restante": saldo_restante}
    else:
        return {"status": "recusado", "motivo": "saldo insuficiente"}

