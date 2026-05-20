from dataclasses import dataclass
from typing import List

# ====================================
# SRS — FIAP Marketplace
# Aula 04 - Documento SRS
# ====================================

@dataclass
class RequisitoFuncional:
    id: str
    descricao: str
    pre_condicao: str
    criterio_aceitacao: str

@dataclass
class RequisitoNaoFuncional:
    id: str
    descricao: str
    categoria: str

# ====================================
# PARTE 1 — REQUISITOS DO FIAP MARKETPLACE
# ====================================

requisitos_funcionais: List[RequisitoFuncional] = [
    RequisitoFuncional(
        id="RF-001",
        descricao="O sistema deve permitir o cadastro de produtos com nome, descrição, preço e categoria",
        pre_condicao="Aluno autenticado no sistema",
        criterio_aceitacao="Produto salvo e visível no marketplace em menos de 3 segundos"
    ),
    RequisitoFuncional(
        id="RF-002",
        descricao="O sistema deve permitir busca de produtos por categoria com retorno em até 2 segundos",
        pre_condicao="Pelo menos 1 produto cadastrado no sistema",
        criterio_aceitacao="Lista de produtos filtrada pela categoria selecionada exibida corretamente"
    ),
    RequisitoFuncional(
        id="RF-003",
        descricao="O sistema deve processar o checkout com cálculo de total e confirmação de pedido",
        pre_condicao="Aluno com pelo menos 1 item no carrinho",
        criterio_aceitacao="Pedido registrado e e-mail de confirmação enviado em até 5 segundos"
    ),
    RequisitoFuncional(
        id="RF-004",
        descricao="O sistema deve permitir avaliação do vendedor com nota de 1 a 5 estrelas",
        pre_condicao="Compra finalizada e entregue",
        criterio_aceitacao="Avaliação registrada e média do vendedor atualizada em tempo real"
    ),
]

requisitos_nao_funcionais: List[RequisitoNaoFuncional] = [
    RequisitoNaoFuncional(
        id="RNF-001",
        descricao="O sistema deve ter disponibilidade de 99,9% ao mês (menos de 9h de downtime/ano)",
        categoria="Disponibilidade"
    ),
    RequisitoNaoFuncional(
        id="RNF-002",
        descricao="O tempo de resposta da busca deve ser inferior a 2 segundos para até 1000 usuários simultâneos",
        categoria="Performance"
    ),
    RequisitoNaoFuncional(
        id="RNF-003",
        descricao="O sistema deve armazenar dados pessoais em conformidade com a LGPD (Lei 13.709/2018)",
        categoria="Segurança"
    ),
]

# ====================================
# PARTE 2 — VALIDADOR DE REQUISITOS
# ====================================

def validar_requisito(rf: RequisitoFuncional) -> dict:
    """
    Valida se um requisito funcional segue as boas práticas.
    Retorna um dict com os resultados da validação.
    """
    resultados = {}

    # Dica 1: descrição deve ter mais de 20 caracteres
    resultados["descricao_suficiente"] = len(rf.descricao) > 20

    # Dica 2: pré-condição não pode ser vazia
    resultados["pre_condicao_definida"] = rf.pre_condicao != ""

    # Dica 3: critério deve conter números (mensurável)
    resultados["criterio_mensuravel"] = any(char.isdigit() for char in rf.criterio_aceitacao)

    return resultados


# ====================================
# EXIBIÇÃO DO SRS
# ====================================

print("=" * 50)
print("   SRS — FIAP Marketplace 🛒")
print("=" * 50)

print("\n📋 REQUISITOS FUNCIONAIS\n")
for rf in requisitos_funcionais:
    print(f"  [{rf.id}] {rf.descricao}")
    print(f"  Pré-condição: {rf.pre_condicao}")
    print(f"  Critério: {rf.criterio_aceitacao}")

    resultado = validar_requisito(rf)
    status_desc  = "✅" if resultado["descricao_suficiente"]  else "❌"
    status_pre   = "✅" if resultado["pre_condicao_definida"] else "❌"
    status_crit  = "✅" if resultado["criterio_mensuravel"]   else "❌"

    print(f"  Validação → Descrição OK: {status_desc} | Pré-condição OK: {status_pre} | Mensurável: {status_crit}")
    print()

print("📋 REQUISITOS NÃO-FUNCIONAIS\n")
for rnf in requisitos_nao_funcionais:
    print(f"  [{rnf.id}] ({rnf.categoria}) {rnf.descricao}")

print("\n" + "=" * 50)