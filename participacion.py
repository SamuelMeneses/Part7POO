@dataclass
class Elemento:
    nombre: str

    def __eq__(self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return NotImplemented


class Conjunto:
    _contador: int = 0

    def __init__(self, nombre: str):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        type(self)._contador += 1
        self.__id = type(self)._contador

    def id(self) -> int:
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        for e in self.elementos:
            if e.nombre == elemento.nombre:
                return True
        return False

    def agregar_elemento(self, elemento: Elemento) -> None:
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto: "Conjunto") -> "Conjunto":
        nuevo_conjunto = Conjunto(f"{self.nombre}, {otro_conjunto.nombre}")
        for e in self.elementos:
            nuevo_conjunto.agregar_elemento(e)
        for e in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(e)
        return nuevo_conjunto

    def __add__(self, otro_conjunto: "Conjunto") -> "Conjunto":
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1: "Conjunto", conjunto2: "Conjunto") -> "Conjunto":
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre}, {conjunto2.nombre}")
        for e in conjunto1.elementos:
            if conjunto2.contiene(e):
                nuevo_conjunto.agregar_elemento(e)
        return nuevo_conjunto

    def __str__(self) -> str:
        elementos_str = ", ".join([e.nombre for e in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"
