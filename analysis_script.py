# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# Step 2: Load the Data
file_path = 'customer_spending_data.xlsx'  # Adjust path as needed
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Step 3: Data Preprocessing
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['Age Group'] = pd.cut(df['Age'], bins=[17, 25, 35, 45, 55, 65],
                         labels=['18-25', '26-35', '36-45', '46-55', '56-65'])

# Step 4: General Overview
print("📊 Dataset Overview:")
print(df.info())
print(df.describe())

# Step 5: Categorical Distributions
categoricals = ['Gender', 'Location', 'Transaction Type', 'Transaction Category', 'Feature Usage']
for col in categoricals:
    print(f"\n🔸 {col} Distribution:")
    print(df[col].value_counts())

# Step 6: Plot - Login Frequency Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Login Frequency (per month)'], bins=30, kde=True)
plt.title("Login Frequency Distribution")
plt.xlabel("Logins per Month")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.show()

# 📉 Step 7: Plot - Session Duration by Age Group
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Age Group', y='Session Duration (minutes)')
plt.title("Session Duration by Age Group")
plt.ylabel("Session Duration (minutes)")
plt.xlabel("Age Group")
plt.tight_layout()
plt.show()

# 📉 Step 8: Plot - Feature Usage Distribution
plt.figure(figsize=(10, 5))
sns.countplot(data=df, y='Feature Usage', order=df['Feature Usage'].value_counts().index)
plt.title("Feature Usage Distribution")
plt.xlabel("Count")
plt.ylabel("Feature Used")
plt.tight_layout()
plt.show()

# 🔍 Step 9: Optional — Segment by Gender or Location
# Example: Average session duration by gender
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Gender', y='Session Duration (minutes)', ci='sd')
plt.title("Average Session Duration by Gender")
plt.tight_layout()
plt.show()

# 💡 Step 10: Correlation (Optional)
correlation = df[['Age', 'Transaction Amount', 'Login Frequency (per month)', 'Session Duration (minutes)']].corr()
print("\n🔗 Correlation Matrix:\n", correlation)

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
