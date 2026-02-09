import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# SYNTHETIC DATASET (Simulating 1000 students)
# Features: [Visual_Interest, Logic_Interest, Math_Interest]
# 0 = Low, 1 = High
# Targets: 1=Frontend, 2=Backend, 3=Data Science, 4=DevOps

data = {
    'visual': [],
    'logic':  [],
    'math':   [],
    'target': []
}

# Define Rules to generate realistic data
# Frontend: Loves Visuals (1), Low Math (0)
# Backend: Loves Logic (1), Visuals indifferent
# Data Science: Loves Math (1), Loves Logic (1)
# DevOps: Loves Logic (1), Low Visuals (0)

# Generate 20 samples for each category to teach the model
for _ in range(20):
    # Frontend Profile
    data['visual'].append(1); data['logic'].append(0); data['math'].append(0); data['target'].append(1)
    # Backend Profile
    data['visual'].append(0); data['logic'].append(1); data['math'].append(0); data['target'].append(2)
    # Data Science Profile
    data['visual'].append(0); data['logic'].append(1); data['math'].append(1); data['target'].append(3)
    # DevOps Profile
    data['visual'].append(0); data['logic'].append(1); data['math'].append(0); data['target'].append(4)

df = pd.DataFrame(data)

# Train the model
X = df[['visual', 'logic', 'math']]
y = df['target']

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, 'smart_quiz_model.pkl')
print("✅ Smart AI Model Trained & Saved!")