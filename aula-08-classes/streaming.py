# Sistema de Streaming — implementação baseada no diagrama de classes UML
# Relacionamentos:
#   Plataforma ◆─── Catalogo   (composição)
#   Catalogo   ◇─── Filme      (agregação)
#   Usuario    ◆─── Avaliacao  (composição)
#   Avaliacao  ───> Filme      (associação)


class Filme:
    """Entidade independente. Sobrevive sem catálogo (agregação)."""

    def __init__(self, titulo: str, duracao: int, genero: str):
        self.titulo = titulo
        self.duracao = duracao   # minutos
        self.genero = genero

    def __repr__(self):
        return f"Filme('{self.titulo}', {self.duracao}min, {self.genero})"


class Avaliacao:
    """Pertence ao Usuario (composição) e referencia um Filme (associação)."""

    def __init__(self, nota: float, comentario: str):
        if not (0 <= nota <= 10):
            raise ValueError("Nota deve estar entre 0 e 10.")
        self.nota = nota
        self.comentario = comentario
        self.filme: Filme | None = None   # associação preenchida em usuario.avaliar()

    def __repr__(self):
        titulo = self.filme.titulo if self.filme else "sem filme"
        return f"Avaliacao(nota={self.nota}, filme='{titulo}')"


class Catalogo:
    """
    Pertence à Plataforma (composição) e agrega Filmes.
    Os filmes continuam existindo mesmo se o catálogo for removido.
    """

    def __init__(self, titulo: str, qtd_filmes: int = 0):
        self.titulo = titulo
        self.qtd_filmes = qtd_filmes
        self._filmes: list[Filme] = []

    def add_filme(self, filme: Filme) -> None:
        """Adiciona um Filme ao catálogo (agregação)."""
        self._filmes.append(filme)
        self.qtd_filmes = len(self._filmes)
        print(f"  ✔ '{filme.titulo}' adicionado ao catálogo '{self.titulo}'.")

    def listar_filmes(self) -> None:
        """Exibe todos os filmes do catálogo."""
        print(f"\n📽  Catálogo: {self.titulo} ({self.qtd_filmes} filme(s))")
        print("  " + "─" * 40)
        for filme in self._filmes:
            print(f"  • {filme.titulo:<20} {filme.duracao}min  [{filme.genero}]")

    def __repr__(self):
        return f"Catalogo('{self.titulo}', {self.qtd_filmes} filmes)"


class Usuario:
    """
    Usuário da plataforma. Possui suas avaliações (composição):
    se o usuário for removido, as avaliações somem junto.
    """

    def __init__(self, nome: str, email: str, plano: str):
        self.nome = nome
        self.email = email
        self.plano = plano
        self._avaliacoes: list[Avaliacao] = []

    def avaliar(self, filme: Filme, avaliacao: Avaliacao) -> None:
        """Associa a avaliação ao filme e a registra para o usuário."""
        avaliacao.filme = filme          # preenche a associação Avaliacao → Filme
        self._avaliacoes.append(avaliacao)
        print(f"  ⭐ {self.nome} avaliou '{filme.titulo}' com nota {avaliacao.nota}.")

    def ver_avaliacoes(self) -> None:
        """Exibe todas as avaliações feitas pelo usuário."""
        print(f"\n👤 Avaliações de {self.nome} ({self.plano})")
        print("  " + "─" * 40)
        for av in self._avaliacoes:
            print(f"  • {av.filme.titulo:<20} nota: {av.nota}")
            print(f"    \"{av.comentario}\"")

    def __repr__(self):
        return f"Usuario('{self.nome}', {self.plano})"


class Plataforma:
    """
    Raiz do sistema. O Catálogo é criado e gerenciado pela Plataforma
    (composição): se a plataforma fechar, o catálogo some.
    Os Filmes, porém, existem independentemente (agregação no Catálogo).
    """

    def __init__(self, nome: str, pais: str):
        self.nome = nome
        self.pais = pais
        self._catalogos: list[Catalogo] = []

    def adicionar_catalogo(self, catalogo: Catalogo) -> None:
        self._catalogos.append(catalogo)

    def __repr__(self):
        return f"Plataforma('{self.nome}', {self.pais})"


# ──────────────────────────────────────────────
# Demo — exatamente como especificado no enunciado
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 48)
    print("  Sistema de Streaming — Demo")
    print("=" * 48)

    # Plataforma (composição → cria e detém o Catálogo)
    netflix = Plataforma("Netflix", "EUA")

    # Catálogo (composto pela plataforma)
    catalogo = Catalogo("Filmes em Destaque", 0)
    netflix.adicionar_catalogo(catalogo)

    # Filmes (entidades independentes — agregadas ao catálogo)
    filme1 = Filme("Oppenheimer", 180, "Drama")
    filme2 = Filme("Barbie", 114, "Comédia")

    print("\n[ Adicionando filmes ao catálogo ]")
    catalogo.add_filme(filme1)
    catalogo.add_filme(filme2)

    # Usuário
    usuario = Usuario("Ana", "ana@email.com", "Premium")

    # Avaliação (composta pelo usuário; associada ao filme)
    avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")

    print("\n[ Registrando avaliação ]")
    usuario.avaliar(filme1, avaliacao)

    # Listagens
    catalogo.listar_filmes()
    usuario.ver_avaliacoes()

    print("\n" + "=" * 48)
    print("  Verificando independência dos objetos")
    print("=" * 48)
    del catalogo   # catálogo removido...
    print(f"  filme1 ainda existe: {filme1}")   # ...mas o filme continua!
    print("  (Agregação confirmada: Filme sobrevive sem o Catálogo)")