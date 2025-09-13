# Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib

# ---------------------------
# Import Libraries
# ---------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ---------------------------
# Task 1: Load and Explore the Dataset
# ---------------------------

try:
    # Load Iris dataset
    iris = load_iris()
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nDataset info:")
    print(df.info())

    print("\nCheck for missing values:")
    print(df.isnull().sum())

except Exception as e:
    print(f"Error loading dataset: {e}")

# ---------------------------
# Task 2: Basic Data Analysis
# ---------------------------

# Basic statistics
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Group by species and compute mean for numerical columns
species_group = df.groupby('species').mean()
print("\nMean of numerical columns by species:")
print(species_group)

# Observations
print("\nObservations:")
print("Setosa has smaller petal length and width compared to Versicolor and Virginica.")
print("Virginica tends to have the largest sepal and petal dimensions.")

# ---------------------------
# Task 3: Data Visualization
# ---------------------------

# Set seaborn style for nicer visuals
sns.set(style="whitegrid")

# 1. Line Chart - trend of sepal length per species
plt.figure(figsize=(8,5))
for species_name in df['species'].unique():
    subset = df[df['species'] == species_name]
    plt.plot(subset.index, subset['sepal length (cm)'], label=species_name)
plt.title("Sepal Length Trend by Species")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - sepal length vs petal length
plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()

# ---------------------------
# End of Assignment
# ---------------------------
