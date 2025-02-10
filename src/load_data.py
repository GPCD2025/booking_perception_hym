import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Carga los datos desde un archivo CSV."""
        try:
            data = pd.read_csv(self.file_path)
            print("Datos cargados exitosamente.")
            return data
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return None