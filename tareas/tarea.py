class Tarea:
    def __init__(self, titulo, descripcion, prioridad, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = "pendiente"

    def marcar_completa(self):
        self.estado = "completa"

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nPrioridad: {self.prioridad}\nFecha de vencimiento: {self.fecha_vencimiento}\nEstado: {self.estado}"
