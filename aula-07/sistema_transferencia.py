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
        return {"status": "negado", "motivo": "saldo insuficiente"}

# CELULA 3 — AppNubank
class AppNubank:
    def __init__(self):
        self.servidor = ServidorNubank()

    def transferir(self, user_id: str, valor: float):
    print(f"[APP] Iniciando transferência de R$ {valor:.2f}...")
    resultado = self.servidor.processar_transferencia(user_id, valor)

    if resultado["status"] == "aprovado":
        print(f"[APP] ✅ Transferência aprovada! Saldo: R$ {resultado['saldo_restante']:.2f}")
    else:
        print(f"[APP] ❌ Transferência recusada: {resultado['motivo']}")

# CELULA 4 — Testes
app = AppNubank()

print("=== Teste 1: Transferência dentro do saldo ===")
app.transferir("user_123", 200.0)
