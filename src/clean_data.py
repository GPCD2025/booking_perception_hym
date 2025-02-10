class DataCleaner:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        """Realiza la limpieza de los datos."""
        # Ejemplo: Eliminar filas con valores faltantes en la columna "Calificación"
        self.data = self.data.dropna(subset=["Calificación"])
        print("Datos limpiados exitosamente.")
        return self.data