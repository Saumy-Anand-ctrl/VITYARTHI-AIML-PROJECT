# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    'Cost_of_Living': [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    'Locality_Rating': [3, 4, 5, 6, 7, 8, 9, 10],   # Scale (1–10)
    'Population': [100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000],
    'Price': [20, 30, 40, 50, 65, 80, 95, 120]  # House price (in lakhs)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features (X) and target (y)
X = df[['Cost_of_Living', 'Locality_Rating', 'Population']]
y = df['Price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Show predictions
print("Predicted Prices:", y_pred)

# Example: Predict new house price
incof=int(input("input cost of living"))
locs=int(input("entter locality scale i e disiance from down towm(0-10)"))
pop=int(input("enter aprox population of city"))
new_data = np.array([[incof, locs, pop]])
predicted_price = model.predict(new_data)

print("Predicted house price (in lakhs):", predicted_price[0])
