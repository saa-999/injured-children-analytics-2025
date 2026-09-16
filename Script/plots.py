import matplotlib.pyplot as plt
from  Script.Patient_demographics  import Patient_demographics 
import pandas as pd 


class Plots:
    def __init__(self):
        pass

    @staticmethod
    def plot_patient_monthly_counts(patient_data: Patient_demographics) -> None:
        month = list(patient_data.MonthDistribution.keys())
        patient = list(patient_data.MonthDistribution.values())

        plt.plot(month, patient, marker='o')

        plt.title("Monthly Distribution")
        plt.xlabel("Month")
        plt.ylabel("Counts")

        plt.xticks(month)
        plt.show()

    @staticmethod
    def bar_saudi_and_non_saudi_patient(patient_data: Patient_demographics) -> None:
        categories = ['Male - Saudi', 'Male - Non Saudi', 'Female - Saudi', 'Female - Non Saudi']
        counts = [
        patient_data.MaleCountSaudi, 
        patient_data.MaleCountNonSaudi, 
        patient_data.FemaleCountSaudi, 
        patient_data.FemaleCountNonSaudi
        ]

        colors = ['#1f77b4',"#f30e0e","#00ff51" , "#eeff00"]

        plt.bar(categories , counts , color=colors)
        plt.title("Patient Distribution by Gender and Nationality", fontweight='bold')
        plt.xlabel("Category")
        plt.ylabel("Number of Patients")
        plt.xticks(rotation=15) 
        plt.tight_layout()

        plt.show()

    @staticmethod
    def pie_saudi_and_non_saudi_patient(patient_data: Patient_demographics) -> None:
        labels = ['Male - Saudi ' , 'Male - Non Saudi' , 'Female - Saudi' , 'Female - Non Saudi']
        size = [
        patient_data.MaleCountSaudi, 
        patient_data.MaleCountNonSaudi, 
        patient_data.FemaleCountSaudi, 
        patient_data.FemaleCountNonSaudi
        ]

        colors = ["#3f7de7","#f30e0e","#00ff51" , "#eeff00"]

        plt.pie(size , labels=labels , colors=colors , autopct='%1.1f%%' , startangle=90)
        plt.title("Percentage of Patients by Gender and Nationality", fontweight='bold')
        plt.axis('equal')
        plt.show()

    @staticmethod
    def plot_wounded_distribution(patient_data: Patient_demographics) -> None:

        v_dict = patient_data.NumberOfWoundedMonthFacilityDistribution

        data_series = pd.Series(v_dict)

        df_plot = data_series.unstack(1).fillna(0)

        df_plot.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='Set1')
    

        plt.title("Wounded Distribution by Month, Facility, and Nationality", fontsize=14, fontweight='bold')
        plt.xlabel("(Month, Facility)", fontsize=12)
        plt.ylabel("Number of Patients", fontsize=12)
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.show()

