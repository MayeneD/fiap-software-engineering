# Engenharia de Software — FIAP 2026

**Aluno:** Mayene Doria RM558858 | [github.com/MayeneD](https://github.com/MayeneD/fiap-software-engineering)

---

## Como executar

Pré-requisito: Python 3.10+

```bash
git clone https://github.com/MayeneD/fiap-software-engineering.git
cd fiap-software-engineering
python nome-da-pasta/nome-do-arquivo
exemplo do que executar
python aula-03-rf-nf/gymtrack.py 
```

---

## Exercícios implementados

### Aula 02 — Levantamento de Requisitos *(bônus)*

Código: `aula-02-elicitacao/conversor_temperatura.py`
Output: [conversor_output.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-02-elicitacao/conversor_output.png)

Conversor de temperatura entre Celsius, Fahrenheit e Kelvin com validação de entrada via `try/except` e menu interativo em loop. Os requisitos RF e RNF foram documentados diretamente no código antes da implementação.

---

### Aula 03 — Requisitos Funcionais e Não-Funcionais

Código: `aula-03-rf-nf/gymtrack.py`
Output: [gymtrack_output.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-03-rf-nf/gymtrack_output.png)

Validador de treino GymTrack que verifica nome, peso (1–300 kg) e repetições (1–50). O RNF de performance é medido em tempo real com `time`, exibindo o tempo de execução em ms.

---

### Aula 04 — Documento SRS

Código: `aula-04-srs/srs_marketplace.py`
Output: [marketplace_output.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-04-srs/marketplace_output.png)

SRS do FIAP Marketplace com 4 requisitos funcionais e 3 não-funcionais usando `@dataclass`. A função `validar_requisito()` checa se cada requisito tem descrição adequada, pré-condição definida e critério mensurável.

---

### Aula 05 — UML e Casos de Uso

Diagrama: [diagramadecasos.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-05-uml/diagramadecasos.png)
Código: `aula-05-uml/biblioteca_digital.py`
Output: [biblioteca_output.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-05-uml/biblioteca_output.png)

Diagrama de casos de uso e implementação da Biblioteca Digital FIAP cobrindo UC-01 Listar, UC-02 Buscar, UC-03 Emprestar com `<<include>>` verificar disponibilidade e UC-04 Devolver com `<<extend>>` aplicar multa por atraso.

---

### Aula 06 — Diagramas de Atividades

Diagrama: [diagrama.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-06-diagramas/diagrama.png)
Código: `aula-06-diagramas/cadastro_usuario.py`
Output: [aula06-output.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-06-diagramas/aula06-output.png)

Diagrama com swimlanes e função `cadastro_usuario()` que espelha cada losango de decisão: validação de e-mail via regex, verificação de duplicidade e confirmação de conta. Inclui 4 cenários de teste.

---

### Aula 07 — Diagramas de Sequência

Diagrama: [Diagrama_sequencia.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-07-sequencia/Diagrama_sequencia.png)
Código: `aula-07-sequencia/sistema_transferencia.py`
Output: [output_nubank.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-07-sequencia/output_nubank.png)

Diagrama de sequência e simulação de transferência Nubank com três lifelines (`AppNubank → ServidorNubank → BancoDeDados`) e fragmento `[alt]` para aprovação ou recusa por saldo insuficiente.

---

### Aula 08 — Diagramas de Classes

Diagrama: [diagrama de classes.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-08-classes/diagrama%20de%20classes.png)
Código: `aula-08-classes/streaming.py`
Output: [output_streaming.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-08-classes/output_streaming.png)

Diagrama de classes e sistema de streaming (Netflix) com cinco classes demonstrando composição (`Plataforma → Catalogo`, `Usuario → Avaliacao`), agregação (`Catalogo → Filme`) e associação (`Avaliacao → Filme`).

---

### Aula 09 — Arquitetura MVC

Diagrama: [mvc.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-09-arquietura/mvc.png)
Output Figma: [figma.png](https://github.com/MayeneD/fiap-software-engineering/blob/main/aula-09-arquietura/figma.png)

Diagrama de arquitetura em 3 camadas (Apresentação, Negócio, Dados) com padrão MVC aplicado ao To-Do List. Protótipo com duas telas no Figma: `View_ListaTarefas` e `View_AdicionarTarefa`, conectadas por prototype links.

---

## Links

GitHub: [MayeneD/fiap-software-engineering](https://github.com/MayeneD/fiap-software-engineering)

Diagramas Miro:
- [Aula 02 — Levantamento de Requisitos](https://whimsical.com/aula-es-02-levantamento-de-requisitos-tecnicas-de-elicitacao-8bk2penxoukq4Tq3Bx6yi2)
- [Aula 03 — Requisitos Funcionais vs. Não-Funcionais](https://whimsical.com/aula-es-03-requisitos-funcionais-vs-nao-funcionais-VeRe2FAFiQkj7bRSeUU7km)
- [Aula 04 — Documento SRS](https://whimsical.com/aula-es-04-documento-de-especificacao-de-requisitos-de-software--YChfpWcG8f9w7qx2uC2wLH)
- [Aula 05 — UML e Casos de Uso](https://whimsical.com/aula-es-05-introducao-a-uml-e-diagramas-de-casos-de-uso-2xASW5FbDUd4n7R1hPMdbZ)
- [Aula 06 — Diagramas de Atividades](https://whimsical.com/aula-es-06-diagramas-de-atividades-para-processos-de-negocio-TGccPNXDmV16wG3EFemG1M)
- [Aula 07 — Diagramas de Sequência](https://whimsical.com/aula-es-07-diagramas-de-sequencia-interacao-entre-objetos-Q6mdtrvJoAevsCs3LQnYER)
- [Aula 08 — Diagramas de Classes](https://whimsical.com/aula-es-08-diagramas-de-classes-estrutura-relacionamentos-atribu-Fq8bUxi9VTtzjAiBQxxypK)
- [Aula 09 — Arquitetura MVC](https://whimsical.com/aula-es-09-arquitetura-de-software-introducao-a-camadas-e-mvc-KgpgBBV8RN7ZJiaDgqo48N)
- [Aula 10 — Wireframes](https://whimsical.com/aula-es-10-de-requisitos-a-wireframes-baixa-fidelidade-Wgh814XebntrEdtFjSxMii)
- [Aula 11 — Design System](https://whimsical.com/aula-es-11-design-system-industrial-e-ui-components-7D1P5w19nv5TgQ51C7ozKt)