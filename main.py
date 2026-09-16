from Script.plots import Plots

from Script.Patient_demographics import Patient_demographics
if __name__ == "__main__":
    analyzer =Patient_demographics("data.csv")
    Plots.plot_patient_monthly_counts(analyzer)
    Plots.bar_saudi_and_non_saudi_patient(analyzer)
    Plots.pie_saudi_and_non_saudi_patient(analyzer)
    