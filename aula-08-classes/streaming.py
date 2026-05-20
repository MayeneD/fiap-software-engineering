# Sistema de Streaming — implementação baseada no diagrama de classes UML

class Filme:
    """Entidade independente. Sobrevive sem catálogo (agregação)."""

    def __init__(self, titulo: str, duracao: int, genero: str):
        self.titulo = titulo
        self.duracao = duracao
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
        self.filme: Filme | None = None

    def __repr__(self):
        titulo = self.filme.titulo if self.filme else "sem filme"
        return f"Avaliacao(nota={self.nota}, filme='{titulo}')"
    
    class Catalogo:

    def __init__(self, titulo: str, qtd_filmes: int = 0):
        self.titulo = titulo
        self.qtd_filmes = qtd_filmes
        self._filmes: list[Filme] = []

def add_filme(self, filme: Filme) -> None:
    self._filmes.append(filme)
    self.qtd_filmes = len(self._filmes)
    print(f"  ✔ '{filme.titulo}' adicionado ao catálogo '{self.titulo}'.")

def listar_filmes(self) -> None:
    print(f"\n📽  Catálogo: {self.titulo} ({self.qtd_filmes} filme(s))")
    print("  " + "─" * 40)

    for filme in self._filmes:
        print(f"  • {filme.titulo:<20} {filme.duracao}min  [{filme.genero}]")

class Usuario:
    def __init__(self, nome: str, email: str, plano: str):
        self.nome = nome
        self.email = email
        self.plano = plano
        self._avaliacoes: list[Avaliacao] = []

def avaliar(self, filme: Filme, avaliacao: Avaliacao) -> None:
    avaliacao.filme = filme
    self._avaliacoes.append(avaliacao)

    print(f"  ⭐ {self.nome} avaliou '{filme.titulo}' com nota {avaliacao.nota}.")

def ver_avaliacoes(self) -> None:
    print(f"\n👤 Avaliações de {self.nome} ({self.plano})")
    print("  " + "─" * 40)

    for av in self._avaliacoes:
        print(f"  • {av.filme.titulo:<20} nota: {av.nota}")
        print(f"    \"{av.comentario}\"")

class Plataforma:
    def __init__(self, nome: str, pais: str):
        self.nome = nome
        self.pais = pais
        self._catalogos: list[Catalogo] = []

    def adicionar_catalogo(self, catalogo: Catalogo) -> None:
        self._catalogos.append(catalogo)
        