from load_data import DataLoader
from clean_data import DataCleaner
from analyze_data import DataAnalyzer
<<<<<<< HEAD
import os

def main():
    # Crear las carpetas 'processed' y 'results' si no existen
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/results", exist_ok=True)

=======

def main():
>>>>>>> b587a56225bd4cd577c06ccab2ca0aa010709c66
    # Cargar datos
    loader = DataLoader("data/raw/reviews_booking.csv")
    data = loader.load_data()

    if data is not None:
        # Limpiar datos
        cleaner = DataCleaner(data)
        cleaned_data = cleaner.clean_data()

<<<<<<< HEAD
        # Guardar datos limpios en la carpeta 'processed'
        cleaned_data.to_csv("data/processed/cleaned_data.csv", index=False)
        print("Datos limpios guardados en 'data/processed/cleaned_data.csv'.")
=======
        # Guardar datos limpios en un archivo CSV
        cleaned_data.to_csv("data/results/cleaned_data.csv", index=False)
        print("Datos limpios guardados en 'data/results/cleaned_data.csv'.")
>>>>>>> b587a56225bd4cd577c06ccab2ca0aa010709c66

        # Analizar datos
        analyzer = DataAnalyzer(cleaned_data)
        analyzer.analyze()

if __name__ == "__main__":
    main()