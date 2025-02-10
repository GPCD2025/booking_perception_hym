class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        """Realiza análisis descriptivo y de sentimiento."""
        # Ejemplo: Calcular el promedio de calificaciones
        avg_rating = self.data["Calificación"].mean()
        print(f"Calificación promedio: {avg_rating}")
        return avg_rating