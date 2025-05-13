# Import bibliotek
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych
df = pd.read_csv("heart.csv")

# Podgląd danych
df.head()
# Przegląd rozkładu niektórych kolumn
fig, axes = plt.subplots(1, 4, figsize=(12, 3))
columns = ["Age", "Cholesterol", "RestingBP"]
for ax, col in zip(axes, columns):
    df[col].plot(kind="hist", title=f"Rozkład {col}", ax=ax)

df["Sex"].value_counts().plot(kind="bar", title="Rozkład płci", ax=axes[-1])
plt.tight_layout()
plt.show()
