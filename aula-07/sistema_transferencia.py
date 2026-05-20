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


