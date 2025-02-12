from load_data import DataLoader
from clean_data import DataCleaner
from analyze_data import DataAnalyzer
import os

def main():
    # Crear las carpetas 'processed' y 'results' si no existen
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/results", exist_ok=True)

    # Cargar datos
    loader = DataLoader("data/raw/reviews_booking.csv")
    data = loader.load_data()

    if data is not None:
        # Limpiar datos
        cleaner = DataCleaner(data)
        cleaned_data = cleaner.clean_data()

        # Guardar datos limpios en la carpeta 'processed'
        cleaned_data.to_csv("data/processed/cleaned_data.csv", index=False)
        print("Datos limpios guardados en 'data/processed/cleaned_data.csv'.")

        # Analizar datos
        analyzer = DataAnalyzer(cleaned_data)
        analyzer.analyze()

if __name__ == "__main__":
    main()