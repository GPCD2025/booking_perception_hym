from load_data import DataLoader
from clean_data import DataCleaner
from analyze_data import DataAnalyzer

def main():
    # Cargar datos
    loader = DataLoader("data/raw/reviews_booking.csv")
    data = loader.load_data()

    if data is not None:
        # Limpiar datos
        cleaner = DataCleaner(data)
        cleaned_data = cleaner.clean_data()

        # Guardar datos limpios en un archivo CSV
        cleaned_data.to_csv("data/results/cleaned_data.csv", index=False)
        print("Datos limpios guardados en 'data/results/cleaned_data.csv'.")

        # Analizar datos
        analyzer = DataAnalyzer(cleaned_data)
        analyzer.analyze()

if __name__ == "__main__":
    main()