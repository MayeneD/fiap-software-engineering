# Engenharia de Software — FIAP 2026

**Aluno:** Mayene D | [github.com/MayeneD](https://github.com/MayeneD/fiap-software-engineering)

---

## Como executar

Pré-requisito: Python 3.10+

```bash
git clone https://github.com/MayeneD/fiap-software-engineering.git
cd fiap-software-engineering
python aula-03-rf-nf/gymtrack.py
```

---

## Exercícios implementados

### Aula 02 — Levantamento de Requisitos *(bônus)*

Código: `aula-02-elicitacao/conversor_temperatura.py`
Output: `aula-02-elicitacao/aula02-output.png`

Conversor de temperatura entre Celsius, Fahrenheit e Kelvin com validação de entrada via `try/except` e menu interativo em loop. Os requisitos RF e RNF foram documentados diretamente no código antes da implementação.

---

### Aula 03 — Requisitos Funcionais e Não-Funcionais

Código: `aula-03-rf-nf/gymtrack.py`
Output: `aula-03-rf-nf/aula03-output.png`

Validador de treino GymTrack que verifica nome, peso (1–300 kg) e repetições (1–50). O RNF de performance é medido em tempo real com `time`, exibindo o tempo de execução em ms.

---

### Aula 04 — Documento SRS

Código: `aula-04-srs/srs_marketplace.py`
Output: `aula-04-srs/aula04-output.png`

SRS do FIAP Marketplace com 4 requisitos funcionais e 3 não-funcionais usando `@dataclass`. A função `validar_requisito()` checa se cada requisito tem descrição adequada, pré-condição definida e critério mensurável.

---

### Aula 05 — UML e Casos de Uso

Diagrama: `aula-05-uml/diagrama-casos-de-uso.png`
Código: `aula-05-uml/biblioteca_digital.py`
Output: `aula-05-uml/aula05-output.png`

Diagrama de casos de uso e implementação da Biblioteca Digital FIAP cobrindo UC-01 Listar, UC-02 Buscar, UC-03 Emprestar com `<<include>>` verificar disponibilidade e UC-04 Devolver com `<<extend>>` aplicar multa por atraso.

---

### Aula 06 — Diagramas de Atividades

Diagrama: `aula-06-diagramas/diagrama-atividades.png`
Código: `aula-06-diagramas/cadastro_usuario.py`
Output: `aula-06-diagramas/aula06-output.png`

Diagrama com swimlanes e função `cadastro_usuario()` que espelha cada losango de decisão: validação de e-mail via regex, verificação de duplicidade e confirmação de conta. Inclui 4 cenários de teste.

---

### Aula 07 — Diagramas de Sequência

Diagrama: `aula-07-sequencia/diagrama-sequencia.png`
Código: `aula-07-sequencia/sistema_transferencia.py`
Output: `aula-07-sequencia/aula07-output.png`

Diagrama de sequência e simulação de transferência Nubank com três lifelines (`AppNubank → ServidorNubank → BancoDeDados`) e fragmento `[alt]` para aprovação ou recusa por saldo insuficiente.

---

### Aula 08 — Diagramas de Classes

Diagrama: `aula-08-classes/diagrama-classes.png`
Código: `aula-08-classes/streaming.py`
Output: `aula-08-classes/aula08-output.png`

Diagrama de classes e sistema de streaming (Netflix) com cinco classes demonstrando composição (`Plataforma → Catalogo`, `Usuario → Avaliacao`), agregação (`Catalogo → Filme`) e associação (`Avaliacao → Filme`).

---

### Aula 09 — Arquitetura MVC

Diagrama: `aula-09-arquietura/mvc.png`
Output Figma: `aula-09-arquietura/figma.png`

Diagrama de arquitetura em 3 camadas (Apresentação, Negócio, Dados) com padrão MVC aplicado ao To-Do List. Protótipo com duas telas no Figma: `View_ListaTarefas` e `View_AdicionarTarefa`, conectadas por prototype links.

---

## Links

GitHub: [MayeneD/fiap-software-engineering](https://github.com/MayeneD/fiap-software-engineering)
Diagramas Miro: [Workspace das Aulas](https://whimsical.com)