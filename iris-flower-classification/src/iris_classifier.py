import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


def load_data(path):
    df = pd.read_csv(path)
    X = df.drop(columns=["Id", "Species"])
    y = df["Species"]
    return X, y


def build_model():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", SVC(kernel="rbf", gamma="scale"))
    ])


def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = build_model()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("Model Accuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))


if __name__ == "__main__":
    X, y = load_data("data/Iris.csv")
    train_and_evaluate(X, y)
