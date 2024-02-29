# -*- coding: utf-8 -*-
import random


data = [
    {'Age': 35, 'Income': 50000, 'Months_Subscribed': 24, 'Has_Discount': 1, 'Churn': 0},
    {'Age': 45, 'Income': 80000, 'Months_Subscribed': 36, 'Has_Discount': 0, 'Churn': 0},
    {'Age': 30, 'Income': 30000, 'Months_Subscribed': 12, 'Has_Discount': 1, 'Churn': 1},
    {'Age': 50, 'Income': 75000, 'Months_Subscribed': 48, 'Has_Discount': 1, 'Churn': 0},
]

random.shuffle(data)


X = []
y = []
for row in data:
    X.append([row['Age'], row['Income'], row['Months_Subscribed'], row['Has_Discount']])
    y.append(row['Churn'])

split_index = int(0.8 * len(X))
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]


def train_decision_tree(X_train, y_train):
    
    
    pass

def predict_churn(X_test):

    return [1] * len(X_test)

train_decision_tree(X_train, y_train)

predictions = predict_churn(X_test)


correct_predictions = sum(1 for pred, actual in zip(predictions, y_test) if pred == actual)
accuracy = correct_predictions / len(y_test)
print("Accuracy:", accuracy)
