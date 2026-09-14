import Script.Patient_demographics as pd

if __name__ == "__main__":
    analyzer =pd.Patient_demographics("data.csv")
    print(analyzer.MaleCountNonSaudi)