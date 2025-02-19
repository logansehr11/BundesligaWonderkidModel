import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

data = pd.read_csv("bundesliga_player.csv")

# Fill any NaN values with mean for int/float and mode for string
for column in data.columns:
        if np.issubdtype(data[column].dtype, np.number):
                data.fillna({column: data[column].mean()}, inplace=True)
        else:
                data.fillna({column: data[column].mode()[0]}, inplace=True)
# print(data)

# Set up the data and the correlation we want to extract
data['age_to_mv_ratio'] = data['age'] / data['max_price']
features = data[['age', 'max_price', 'age_to_mv_ratio']]
market_val = data[['price']]

features = features.fillna(features.mean())
market_val = market_val.fillna(market_val.mean())

# Start the Wonderkid Scouting by training and building the model
X_train, X_test, y_train, y_test = train_test_split(features, market_val, test_size=0.2, random_state=42)
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

model = RandomForestRegressor()
model.fit(X_train, y_train)

# Create a subgroup of prediction solely for players under 21 in the dataset
X_test_wk = X_test[X_test['age'] < 21]
y_test_wk = y_test[X_test['age'] < 21]

y_pred = model.predict(X_test)
wonderkid_pred = model.predict(X_test_wk)
# mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error: ", mse)

# Filter for wonderkids
wonderkids = data[data['age'] < 21]

# Predict values for wonderkids
wonderkids_features = wonderkids[['age', 'max_price', 'age_to_mv_ratio']]
wonderkids = wonderkids.copy()
wonderkids.loc[:,'wonderkid_score'] = model.predict(wonderkids_features)

# Display actual and predicted values for wonderkids
top_n = 10
print(wonderkids[['name', 'age', 'max_price', 'wonderkid_score']])
print("---------------------------------------------------------------------")
best_wonderkids = wonderkids.sort_values(by='wonderkid_score', ascending=False)
print(best_wonderkids[['name', 'age', 'max_price', 'wonderkid_score']].head(top_n))

# Evaluate the performance of the model
wonderkids_mse = mean_squared_error(wonderkids['max_price'], wonderkids['wonderkid_score'])
print("Mean Squared Error for Wonderkids: ", wonderkids_mse)
accuracy = model.score(X_test, y_test)
print("---------------------------------------------------------------------")
print("Final Report on the Data")
print("Total Players in Data Set: ", data.shape[0])
print("Total Players Under 21: ", wonderkids.shape[0])
print("Overall Data Set Accuracy: ", accuracy)
wonderkid_accuracy = model.score(X_test_wk, y_test_wk)
print("Wonderkid Subset Accuracy: ", wonderkid_accuracy)
