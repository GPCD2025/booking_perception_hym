<<<<<<< HEAD
import pandas as pd
import os

=======
>>>>>>> b587a56225bd4cd577c06ccab2ca0aa010709c66
class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        """Realiza análisis descriptivo y de sentimiento."""
<<<<<<< HEAD
        # Verifica que las columnas necesarias existan
        if "Calificación" not in self.data.columns or "País" not in self.data.columns:
            raise ValueError("El DataFrame debe contener las columnas 'Calificación' y 'País'.")

        # Ejemplo: Calcular el promedio de calificaciones
        avg_rating = self.data["Calificación"].mean()
        print(f"Calificación promedio: {avg_rating}")

        # Calcular el promedio de calificaciones por país
        avg_ratings_by_country = self.data.groupby("País")["Calificación"].mean().reset_index()

        # Guardar los resultados en 'data/results/'
        os.makedirs("data/results", exist_ok=True)  # Crear la carpeta si no existe

        output_path = "data/results/avg_ratings_by_country.csv"
        print(f"Guardando resultados en: {os.path.abspath(output_path)}")

        try:
            avg_ratings_by_country.to_csv(output_path, index=False)
            print("Resultados guardados en 'data/results/avg_ratings_by_country.csv'.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

=======
        # Ejemplo: Calcular el promedio de calificaciones
        avg_rating = self.data["Calificación"].mean()
        print(f"Calificación promedio: {avg_rating}")
>>>>>>> b587a56225bd4cd577c06ccab2ca0aa010709c66
        return avg_rating