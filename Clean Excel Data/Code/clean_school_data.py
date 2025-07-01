import pandas as pd


path = r"C:\Users\sujai\Desktop\pranavi"

# Load 
df = pd.read_excel(f"{path}\\school_data_complex.xlsx")

#remove
df = df.drop_duplicates()

#Drop missing values
df = df.dropna(thresh=20)  


categorical_cols = ['Gender', 'Section', 'Sports', 'Extra_Curricular', 'Fee_Status', 'Remarks']
df[categorical_cols] = df[categorical_cols].fillna("Unknown")

#Invalid Email
df["Parent_Email"] = df["Parent_Email"].apply(lambda x: x if pd.notnull(x) and "@" in str(x) else None)

#Fill missing contact
df[["Parent_Email", "Parent_Contact"]] = df[["Parent_Email", "Parent_Contact"]].fillna("Not Provided")

#date to datetime
df["Date_of_Birth"] = pd.to_datetime(df["Date_of_Birth"], errors="coerce")
df["Registration_Date"] = pd.to_datetime(df["Registration_Date"], errors="coerce")

#Attendance > 100%
df["Attendance (%)"] = df["Attendance (%)"].apply(lambda x: min(x, 100) if pd.notnull(x) else x)

#Fill Missing numeric scores with -1
score_cols = ["Math_Score", "English_Score", "Science_Score", "Social_Science_Score"]
df[score_cols] = df[score_cols].fillna(-1)

# Save cleaned file only
df.to_excel(f"{path}\\cleaned_school_data.xlsx", index=False)

print(" Cleaned file saved at:", f"{path}\\cleaned_school_data.xlsx")
