# Engenharia de Software — FIAP 2026

**Aluno:** Mayene Doria RM558858 
[github.com/MayeneD](https://github.com/MayeneD/fiap-software-engineering)

---

## Estrutura do repositório

```
fiap-software-engineering/
├── aula-02-elicitacao/
│   └── conversor_temperatura.py
├── aula-03-rf-nf/
│   └── gymtrack.py
├── aula-04-srs/
│   └── srs_marketplace.py
├── aula-05-uml/
│   ├── diagrama-casos-de-uso.png
│   └── biblioteca_digital.py
├── aula-06-diagramas/
│   ├── diagrama-atividades.png
│   └── cadastro_usuario.py
├── aula-07-sequencia/
│   ├── diagrama-sequencia.png
│   └── sistema_transferencia.py
├── aula-08-classes/
│   ├── diagrama-classes.png
│   └── streaming.py
└── aula-09-arquietura/
    ├── mvc.png
    └── figma.png
```

---

## Como executar

**Pré-requisito:** Python 3.10+

```bash
git clone https://github.com/MayeneD/fiap-software-engineering.git
cd fiap-software-engineering
python aula-03-rf-nf/gymtrack.py
```

---

## Exercícios implementados

### Aula 02 — Levantamento de Requisitos *(bônus)*

| | |
|--|--|
| Código | `aula-02-elicitacao/conversor_temperatura.py` |
| Output | `aula-02-elicitacao/aula02-output.png` |

Conversor de temperatura entre Celsius, Fahrenheit e Kelvin com validação de entrada via `try/except` e menu interativo em loop, documentando RFs e RNFs diretamente no código.

---

### Aula 03 — Requisitos Funcionais e Não-Funcionais

| | |
|--|--|
| Código | `aula-03-rf-nf/gymtrack.py` |
| Output | `aula-03-rf-nf/aula03-output.png` |

GymTrack — validador de treino com verificação de nome, peso (1–300 kg) e repetições (1–50), com medição de performance em ms para o RNF de tempo de resposta.

---

### Aula 04 — Documento SRS

| | |
|--|--|
| Código | `aula-04-srs/srs_marketplace.py` |
| Output | `aula-04-srs/aula04-output.png` |

SRS do FIAP Marketplace com 4 requisitos funcionais e 3 não-funcionais usando `@dataclass`. Inclui função `validar_requisito()` que verifica descrição, pré-condição e critério mensurável.

---

### Aula 05 — UML e Casos de Uso

| | |
|--|--|
| Diagrama | `aula-05-uml/diagrama-casos-de-uso.png` |
| Código | `aula-05-uml/biblioteca_digital.py` |
| Output | `aula-05-uml/aula05-output.png` |

Diagrama de casos de uso + implementação da Biblioteca Digital FIAP com UC-01 Listar, UC-02 Buscar, UC-03 Emprestar (`<<include>>`) e UC-04 Devolver (`<<extend>>` multa por atraso).

---

### Aula 06 — Diagramas de Atividades

| | |
|--|--|
| Diagrama | `aula-06-diagramas/diagrama-atividades.png` |
| Código | `aula-06-diagramas/cadastro_usuario.py` |
| Output | `aula-06-diagramas/aula06-output.png` |

Diagrama com swimlanes + função `cadastro_usuario()` que espelha cada losango de decisão do diagrama: validação de e-mail via regex, verificação de duplicidade e confirmação de conta.

---

### Aula 07 — Diagramas de Sequência

| | |
|--|--|
| Diagrama | `aula-07-sequencia/diagrama-sequencia.png` |
| Código | `aula-07-sequencia/sistema_transferencia.py` |
| Output | `aula-07-sequencia/aula07-output.png` |

Diagrama de sequência + simulação de transferência Nubank com três lifelines (`AppNubank → ServidorNubank → BancoDeDados`) e fragmento `[alt]` para saldo suficiente ou insuficiente.

---

### Aula 08 — Diagramas de Classes

| | |
|--|--|
| Diagrama | `aula-08-classes/diagrama-classes.png` |
| Código | `aula-08-classes/streaming.py` |
| Output | `aula-08-classes/aula08-output.png` |

Diagrama de classes + sistema de streaming (Netflix) com cinco classes (`Plataforma`, `Catalogo`, `Filme`, `Usuario`, `Avaliacao`) demonstrando composição ◆, agregação ◇ e associação →.

---

### Aula 09 — Arquitetura MVC

| | |
|--|--|
| Diagrama | `aula-09-arquietura/mvc.png` |
| Output Figma | `aula-09-arquietura/figma.png` |

Diagrama de arquitetura em 3 camadas (Apresentação, Negócio, Dados) com padrão MVC aplicado ao To-Do List. Protótipo com duas telas no Figma: `View_ListaTarefas` e `View_AdicionarTarefa`.

---

## Links

| Recurso | Link |
|---------|------|
| GitHub | [MayeneD/fiap-software-engineering](https://github.com/MayeneD/fiap-software-engineering) |
| Diagramas Miro | [Workspace das Aulas](https://whimsical.com) |