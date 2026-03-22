from modelos.visitante import Visitante


class VisitaServicio:
    def __init__(self):
        self._visitantes = []

    def registrar(self, cedula, nombre, motivo):
        for v in self._visitantes:
            if v.cedula == cedula:
                return False  # Cédula duplicada
        nuevo = Visitante(cedula, nombre, motivo)
        self._visitantes.append(nuevo)
        return True

    def obtener_todos(self):
        return list(self._visitantes)

    def eliminar(self, cedula):
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True
        return False