import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
data = pd.read_csv("DCFaultData.csv")
data.dropna(inplace=True)

# Slice dataframe
X = data.iloc[:, :-1]  
Y = data.iloc[:, -1]   

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Create and train the SVM model with Polynomial Kernel
model = SVC(kernel='poly', degree=3)  # You can adjust degree (e.g., degree=2, 4, 5)
model.fit(X_train, Y_train)

# Make predictions
Y_predicted = model.predict(X_test)

# Evaluate model
conf_matrix = confusion_matrix(Y_test, Y_predicted)
print("Confusion Matrix:\n", conf_matrix)

classification_accuracy = accuracy_score(Y_test, Y_predicted)
print("Classification Accuracy:", classification_accuracy)

report = classification_report(Y_test, Y_predicted)
print("Classification Report:\n", report)

# Save the trained model
joblib.dump(model, "svm_model.pkl")



