import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# 1. Create a dummy dataset (The "Textbook" for the AI)
# 0 = Frontend Choice, 1 = Backend Choice
# We map the inputs (Answers to Q1) to the Target (Domain ID)
data = {
    'q1': [0, 0, 0, 1, 1, 1],       # 0 represents "Visual", 1 represents "Logic"
    'target': [1, 1, 1, 2, 2, 2]    # 1 = Frontend Domain ID, 2 = Backend Domain ID
}
# Note: You must ensure these IDs (1 and 2) match your actual Database IDs for Frontend/Backend!

df = pd.DataFrame(data)

# 2. Separate inputs (X) and answers (y)
X = df[['q1']]
y = df['target']

# 3. Initialize the Brain (Decision Tree)
model = DecisionTreeClassifier()

# 4. Train the Brain
print("Training model...")
model.fit(X, y)

# 5. Save the trained brain to a file
joblib.dump(model, 'quiz_model.pkl')
print("Success! Model saved as 'quiz_model.pkl'")