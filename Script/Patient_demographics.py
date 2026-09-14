import pandas as pd

class Patient_demographics:
    def __init__(self, path: str):
        self.df = pd.read_csv(path)
        
        self.MaleCount = (self.df["SEX"] == "Male").sum()
        self.FemaleCount = (self.df["SEX"] == "Female").sum()
        
        self.MaleCountSaudi = ((self.df["NATIONALITY"] == "Saudi") & (self.df["SEX"] == "Male")).sum()
        self.FemaleCountSaudi = ((self.df["NATIONALITY"] == "Saudi") & (self.df["SEX"] == "Female")).sum()
        
        self.MaleCountNonSaudi = ((self.df["NATIONALITY"] == "Non Saudi") & (self.df["SEX"] == "Male")).sum()
        self.FemaleCountNonSaudi = ((self.df["NATIONALITY"] == "Non Saudi") & (self.df["SEX"] == "Female")).sum()
        
        self.RegionDistribution = self.df["REGION"].value_counts().to_dict()
        self.FacilityDistribution = self.df["LOC_FACILITY_CD_DESC"].value_counts().to_dict()
        self.DepartmentDistribution = self.df["DEPARTMENT_NAME"].value_counts().to_dict()