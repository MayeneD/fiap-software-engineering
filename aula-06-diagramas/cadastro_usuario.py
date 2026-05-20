# ============================================================
#   CADASTRO E APROVAÇÃO DE USUÁRIO
#   Aula 06 - Diagramas de Atividades
# ============================================================

import re

def cadastro_usuario(email: str, senha: str, email_ja_existe: bool, confirmou_email: bool) -> str:
    """
    Implementação baseada no Diagrama de Atividades (Miro).

    Fluxo:
    1. Validar formato do e-mail
    2. Verificar se e-mail já está cadastrado
    3. Criar conta
    4. Enviar e-mail de confirmação
    5. Aguardar confirmação do usuário
    6. Liberar acesso ou expirar cadastro
    """

    # ----------------------------------------------------
    # DECISÃO 1 — E-mail válido?
    # Verifica formato usando regex
    # ----------------------------------------------------
    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    if not re.match(padrao_email, email):
        return "❌ E-mail inválido. Verifique o formato e tente novamente."

    # ----------------------------------------------------
    # DECISÃO 2 — Já cadastrado?
    # ----------------------------------------------------
    if email_ja_existe:
        return "⚠️  E-mail já cadastrado. Faça login ou recupere sua senha."

    # ----------------------------------------------------
    # Criar conta no sistema
    # ----------------------------------------------------
    print(f"  ✅ Conta criada para: {email}")

    # ----------------------------------------------------
    # Enviar e-mail de confirmação (E-mail Service)
    # ----------------------------------------------------
    print(f"  📧 E-mail de confirmação enviado para: {email}")

    # ----------------------------------------------------
    # Aguardar clique de confirmação (usuário)
    # ----------------------------------------------------
    if not confirmou_email:
        return "⏳ Cadastro pendente. Confirme seu e-mail para liberar o acesso."

    # ----------------------------------------------------
    # Liberar acesso
    # ----------------------------------------------------
    return "🎉 Acesso liberado! Bem-vindo ao sistema."


# ============================================================
# TESTES
# ============================================================
print("=" * 50)
print("TESTE 1 — fluxo completo com sucesso")
print(cadastro_usuario("joao@email.com", "senha123", False, True))

print("\n" + "=" * 50)
print("TESTE 2 — e-mail inválido")
print(cadastro_usuario("email-invalido", "senha123", False, True))

print("\n" + "=" * 50)
print("TESTE 3 — e-mail já cadastrado")
print(cadastro_usuario("joao@email.com", "senha123", True, True))

print("\n" + "=" * 50)
print("TESTE 4 — não confirmou o e-mail")
print(cadastro_usuario("maria@email.com", "senha456", False, False))