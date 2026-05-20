# Portfólio – Engenharia de Software | FIAP 2026

## Sobre este repositório

**Aluno:** Mayene Doria RM558858
— [MayeneD](https://github.com/MayeneD)

Repositório com os exercícios práticos das aulas de Engenharia de Software da FIAP. Cada pasta contém o código-fonte comentado, diagramas UML e capturas de execução quando disponíveis.

---

## Como executar

```bash
git clone https://github.com/MayeneD/fiap-software-engineering.git
cd fiap-software-engineering
```

Execute o script da aula desejada:

```bash
python aula-02-elicitacao/conversor_temperatura.py
python aula-03-rf-nf/gymtrack.py
python aula-04-srs/srs_marketplace.py
python aula-05-uml/biblioteca_digital.py
python aula-06-diagramas/cadastro_usuario.py
python aula-07-sequencia/sistema_transferencia.py
python aula-08-classes/streaming.py
```

**Pré-requisito:** Python 3.10 ou superior.

---

## Exercícios por Aula

---

### Aula 02 – Levantamento de Requisitos e Técnicas de Elicitação

| Item | Arquivo |
|------|---------|
| Código | `aula-02-elicitacao/conversor_temperatura.py` |

Conversor de temperatura entre Celsius, Fahrenheit e Kelvin. O exercício documenta os requisitos diretamente no código antes da implementação, aplicando a técnica de elicitação orientada a requisitos.

**Requisitos Funcionais implementados:**

| ID | Requisito | Implementação |
|----|-----------|---------------|
| RF01 | Converter Celsius → Fahrenheit | `celsius_para_fahrenheit()` — fórmula `(C × 9/5) + 32` |
| RF02 | Converter Fahrenheit → Celsius | `fahrenheit_para_celsius()` — fórmula `(F - 32) × 5/9` |
| RF03 | Múltiplas conversões sem reiniciar | loop `while True` com menu |
| RF04 | Exibir resultado com unidade | `f"{temp}°C = {resultado:.1f}°F"` |

**Requisitos Não-Funcionais implementados:**

| ID | Requisito | Implementação |
|----|-----------|---------------|
| RNF01 | Resultado imediato (< 1s) | operação matemática direta, sem I/O extra |
| RNF02 | Interface simples com menu numerado | `exibir_menu()` com opções 0–3 |
| RNF03 | Aceitar apenas entradas numéricas | `ler_temperatura()` com `try/except ValueError` em loop |

**Bônus:** conversão Celsius → Kelvin via `celsius_para_kelvin()` (`K = C + 273.15`).

---

### Aula 03 – Requisitos Funcionais vs. Não-Funcionais

| Item | Arquivo |
|------|---------|
| Código | `aula-03-rf-nf/gymtrack.py` |

Validador de dados de treino para o sistema **GymTrack**. Demonstra na prática a diferença entre RFs (o que o sistema valida) e RNFs (como ele se comporta), com medição real de performance via `time`.

**Requisitos Funcionais:**

| ID | Validação | Regra de negócio |
|----|-----------|-----------------|
| RF01 | Nome do exercício | campo não pode ser vazio |
| RF02 | Peso em kg | entre 1 e 300 kg |
| RF03 | Repetições | entre 1 e 50 |

**Requisito Não-Funcional:**

| ID | Requisito | Medição |
|----|-----------|---------|
| RNF01 | Registro em menos de 200ms | `time.time()` antes/depois — resultado exibido em ms |

**Reflexão documentada no código:** RFs viraram `if` de validação; o RNF virou medição de tempo. RNF não implementado identificado: autenticação do aluno antes de registrar dados.

---

### Aula 04 – Documento SRS

| Item | Arquivo |
|------|---------|
| Código | `aula-04-srs/srs_marketplace.py` |

Implementação de um Software Requirements Specification (SRS) para o **FIAP Marketplace** usando `@dataclass` e `List` do módulo `typing`.

**Requisitos Funcionais (RF):**

| ID | Descrição | Pré-condição | Critério de Aceitação |
|----|-----------|-------------|----------------------|
| RF-001 | Cadastro de produtos | Aluno autenticado | Produto salvo e visível em < 3s |
| RF-002 | Busca por categoria | Mínimo 1 produto cadastrado | Lista filtrada exibida corretamente |
| RF-003 | Checkout com cálculo de total | Carrinho com ao menos 1 item | Pedido registrado + e-mail em < 5s |
| RF-004 | Avaliação do vendedor (1–5 estrelas) | Compra finalizada e entregue | Média atualizada em tempo real |

**Requisitos Não-Funcionais (RNF):**

| ID | Categoria | Descrição |
|----|-----------|-----------|
| RNF-001 | Disponibilidade | 99,9% ao mês (< 9h de downtime/ano) |
| RNF-002 | Performance | Busca < 2s para até 1.000 usuários simultâneos |
| RNF-003 | Segurança | Conformidade com LGPD (Lei 13.709/2018) |

**Função `validar_requisito(rf)`:** verifica 3 critérios de qualidade — descrição com mais de 20 caracteres, pré-condição definida e critério de aceitação mensurável (contém número).

---

### Aula 05 – UML e Casos de Uso

| Item | Arquivo |
|------|---------|
| Código | `aula-05-uml/biblioteca_digital.py` |

Sistema de **Biblioteca Digital FIAP** implementando diretamente os casos de uso do diagrama UML. Cada seção do código corresponde a um UC.

| Caso de Uso | Implementação | Detalhe |
|-------------|---------------|---------|
| UC-01 Listar Catálogo | loop `for` no `catalogo` | exibe status ✅/❌ e autor |
| UC-02 Buscar Livro | list comprehension case-insensitive | `busca.lower() in livro["titulo"].lower()` |
| UC-03 Emprestar Livro | altera `disponivel = False` + registra em `emprestimos` | `<<include>>` verificação de disponibilidade |
| UC-04 Devolver Livro | restaura `disponivel = True` + remove de `emprestimos` | `<<extend>>` aplica multa se `houve_atraso` |

**Dados de teste fixos:** catálogo com *Clean Code*, *The Pragmatic Programmer* e *Design Patterns*. Leitor padrão: `"Ana Silva"`.

---

### Aula 06 – Diagramas de Atividades

| Item | Arquivo |
|------|---------|
| Código | `aula-06-diagramas/cadastro_usuario.py` |

Função `cadastro_usuario(email, senha, email_ja_existe, confirmou_email)` implementada seguindo o fluxo do diagrama de atividades (estilo iFood). Cada `if` espelha um losango de decisão do diagrama.

| Nó do Diagrama | Código | Retorno |
|----------------|--------|---------|
| E-mail válido? | `re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email)` | `"❌ E-mail inválido..."` |
| Já cadastrado? | `if email_ja_existe` | `"⚠️ E-mail já cadastrado..."` |
| Criar conta | `print(f"✅ Conta criada para: {email}")` | — |
| Confirmou e-mail? | `if not confirmou_email` | `"⏳ Cadastro pendente..."` |
| Liberar acesso | fluxo principal | `"🎉 Acesso liberado!"` |

**4 testes incluídos:** fluxo completo com sucesso, e-mail inválido, e-mail já cadastrado e confirmação pendente.

---

### Aula 07 – Diagramas de Sequência

| Item | Arquivo |
|------|---------|
| Código | `aula-07-sequencia/sistema_transferencia.py` |

Simulação de transferência bancária Nubank com três classes representando as lifelines do diagrama de sequência:

```
AppNubank → ServidorNubank → BancoDeDados
```

| Classe | Lifeline | Responsabilidade |
|--------|----------|-----------------|
| `AppNubank` | Interface do usuário | chama `transferir()`, exibe resultado |
| `ServidorNubank` | Lógica de negócio | chama `verificar_saldo()` e decide aprovar/reprovar |
| `BancoDeDados` | Persistência | armazena saldos, executa `debitar()` |

**Fragmento `[alt]` implementado:** dentro de `processar_transferencia()`, se `saldo >= valor` → aprova e debita; senão → retorna `"saldo insuficiente"`.

**3 testes incluídos:** transferência dentro do saldo (R$ 200), acima do saldo (R$ 500) e múltiplas transferências sequenciais.

---

### Aula 08 – Diagramas de Classes

| Item | Arquivo |
|------|---------|
| Código | `aula-08-classes/streaming.py` |
| Diagrama | `aula-08-classes/diagrama-classes.png` |

Sistema de streaming (Netflix) modelado a partir do diagrama UML de classes, com os três tipos de relacionamento entre objetos:

| Relacionamento | Símbolo | Par de Classes | Justificativa |
|----------------|---------|----------------|---------------|
| Composição | ◆ | `Plataforma → Catalogo` | O catálogo não existe sem a plataforma |
| Agregação | ◇ | `Catalogo → Filme` | O filme sobrevive sem o catálogo (`del catalogo` confirma) |
| Composição | ◆ | `Usuario → Avaliacao` | Avaliação pertence ao usuário; deletar usuário remove avaliações |
| Associação | → | `Avaliacao → Filme` | `avaliacao.filme = filme` — referência simples, sem posse |

**Classes e métodos:**

```python
Plataforma(nome, pais)            → adicionar_catalogo(catalogo)
Catalogo(titulo, qtd_filmes)      → add_filme(filme), listar_filmes()
Filme(titulo, duracao, genero)
Usuario(nome, email, plano)       → avaliar(filme, avaliacao), ver_avaliacoes()
Avaliacao(nota, comentario)       → nota validada entre 0 e 10
```

**Demonstração do exercício:**

```python
netflix = Plataforma("Netflix", "EUA")
catalogo = Catalogo("Filmes em Destaque", 0)
filme1 = Filme("Oppenheimer", 180, "Drama")
filme2 = Filme("Barbie", 114, "Comédia")
catalogo.add_filme(filme1)
catalogo.add_filme(filme2)
usuario = Usuario("Ana", "ana@email.com", "Premium")
avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")
usuario.avaliar(filme1, avaliacao)
catalogo.listar_filmes()
usuario.ver_avaliacoes()
```

**Validação da agregação:** após `del catalogo`, `filme1` continua existindo em memória — confirmando que a agregação está correta.

---

### Aula 09 – Arquitetura de Software: Camadas e MVC

| Item | Arquivo |
|------|---------|
| Diagrama de camadas | `aula-09-arquietura/mvc.png` |
| Telas Figma | `aula-09-arquietura/figma.png` |

Modelagem de um app **To-Do List** usando Arquitetura em Camadas + padrão MVC.

**Arquitetura em 3 camadas:**

| Camada | Responsabilidade | Exemplos no app |
|--------|-----------------|-----------------|
| Apresentação | Interface com o usuário — padrão MVC | `View_ListaTarefas`, `View_AdicionarTarefa` |
| Negócio | Regras e validações | filtro por status, validação de campo vazio |
| Dados | Persistência | `localStorage`, arquivo JSON |

**Model — estrutura de dados:**

```javascript
{ id: 1, title: "Estudar MVC", tag: "ES", done: false }
```

**View — duas telas nomeadas seguindo o padrão MVC:**
- `View_ListaTarefas`: lista de tarefas, filtros (Todas / Pendentes / Feitas), contadores
- `View_AdicionarTarefa`: campo de título, seletor de categoria, botão Salvar

**Controller — três ações:**

| Ação | Função | O que faz |
|------|--------|-----------|
| `adicionar()` | `saveTask()` | cria objeto Tarefa e insere no Model |
| `marcarFeita()` | `toggleTask(id)` | inverte o campo `done` pelo `id` |
| `excluir()` | `deleteTask(id)` | remove do array com `splice` |

**Fluxo de uma ação:**
```
View captura evento → Controller processa → Model atualiza → View re-renderiza
```

---

## Links

| Recurso | Link |
|---------|------|
| 🐙 GitHub | [MayeneD/fiap-software-engineering](https://github.com/MayeneD/fiap-software-engineering) |
| 📌 Diagramas Miro | [Workspace das Aulas](https://whimsical.com) |