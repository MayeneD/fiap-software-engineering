# ============================================================
#      SISTEMA DE BIBLIOTECA DIGITAL — Biblioteca FIAP 🏛
# Cada seção = um Caso de Uso do diagrama
# ============================================================

# ----------------------------
#      DADOS DO SISTEMA 📦
# ----------------------------
catalogo = [
    {"titulo": "Clean Code",               "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "The Pragmatic Programmer", "autor": "Hunt & Thomas",    "disponivel": True},
    {"titulo": "Design Patterns",          "autor": "Gang of Four",     "disponivel": True},
]
emprestimos = []  # lista de {"leitor": ..., "livro": ...}

# ============================================================
# UC-01: LISTAR CATÁLOGO
# Ator: Leitor
# ============================================================
print("📚 Catálogo disponível:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']} — {livro['autor']}")

# ============================================================
# UC-02: BUSCAR LIVRO
# Ator: Leitor
# Pré-condição: catálogo não vazio
# ============================================================
print("\n🔍 Buscando livro...")
busca = "clean"  # o leitor digitou isso

encontrados = []
for livro in catalogo:
    if busca.lower() in livro["titulo"].lower():
        encontrados.append(livro)

if encontrados:
    for livro in encontrados:
        status = "✅" if livro["disponivel"] else "❌"
        print(f"  {status} {livro['titulo']} — {livro['autor']}")
else:
    print("  Nenhum livro encontrado para a busca.")

# ============================================================
# UC-03: EMPRESTAR LIVRO
# Ator: Leitor
# <<include>> UC-04 Verificar Disponibilidade
# ============================================================
print("\n📌 Empréstimo:")
leitor = "Ana Silva"
titulo = "Clean Code"

livro_encontrado = None
for livro in catalogo:
    if livro["titulo"] == titulo:
        livro_encontrado = livro
        break

if livro_encontrado is None:
    print("  ❌ Livro não encontrado no catálogo.")
elif livro_encontrado["disponivel"] == False:
    print(f"  ⚠️  '{titulo}' já está emprestado!")
else:
    livro_encontrado["disponivel"] = False
    emprestimos.append({"leitor": leitor, "livro": titulo})
    print(f"  ✅ '{titulo}' emprestado para {leitor}!")

# ============================================================
# UC-04: DEVOLVER LIVRO
# Ator: Leitor
# <<extend>> UC-05 Aplicar Multa (só se atrasado)
# ============================================================
print("\n🔄 Devolução:")
leitor_devolvendo  = "Ana Silva"
titulo_devolvendo  = "Clean Code"

registro_encontrado = None
for registro in emprestimos:
    if registro["leitor"] == leitor_devolvendo and registro["livro"] == titulo_devolvendo:
        registro_encontrado = registro
        break

if registro_encontrado is None:
    print("  ❌ Empréstimo não encontrado para esse leitor/livro.")
else:
    # Marca livro como disponível no catálogo
    for livro in catalogo:
        if livro["titulo"] == titulo_devolvendo:
            livro["disponivel"] = True
            break

    emprestimos.remove(registro_encontrado)
    print(f"  ✅ '{titulo_devolvendo}' devolvido por {leitor_devolvendo}!")

    # <<extend>> — Aplicar Multa (só se houve atraso)
    houve_atraso = True  # simula atraso; troque para False para testar sem multa
    if houve_atraso:
        print("  💸 Multa aplicada por atraso na devolução!")

# ============================================================
#      ESTADO FINAL 🔎
# ============================================================
print("\n📖 Catálogo após operações:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']}")

print(f"\n📋 Empréstimos ativos: {emprestimos}")