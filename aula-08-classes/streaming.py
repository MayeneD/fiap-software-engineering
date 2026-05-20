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