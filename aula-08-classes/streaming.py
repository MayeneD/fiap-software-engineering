# Sistema de Streaming — implementação baseada no diagrama de classes UML

class Filme:
    """Entidade independente. Sobrevive sem catálogo (agregação)."""

    def __init__(self, titulo: str, duracao: int, genero: str):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero

    def __repr__(self):
        return f"Filme('{self.titulo}', {self.duracao}min, {self.genero})"