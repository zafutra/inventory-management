import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def predict_demand(data):
    X = data[['month', 'product_id']].values
    y = data['sales'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("Model Score:", model.score(X_test, y_test))
    return model
