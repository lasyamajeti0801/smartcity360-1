"""
SmartCity360 - Municipal Department Routing Model Training Pipeline
Trains an NLP model to classify incoming civic complaints into responsible departments
(ROADS, SANITATION, ELECTRICAL, WATER, etc.) using TF-IDF + LogisticRegression.
Strict Zero-Fabrication: Actual metrics calculated on held-out test split.
"""

import json
import sys
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, f1_score
import joblib

# Add project root to sys.path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from ml.dataset import generate_civic_dataset

def train_and_evaluate():
    print("=" * 70)
    print("SMARTCITY360 - AI/ML DEPARTMENT ROUTER TRAINING")
    print("=" * 70)

    # 1. Dataset generation
    df = generate_civic_dataset(2000)
    X = df["text"]
    y = df["department"]

    # 2. Train / Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Training samples: {len(X_train)} | Test samples: {len(X_test)}")

    # 3. Model Pipeline
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=3000, lowercase=True)),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced"))
    ])

    print("[INFO] Fitting TF-IDF Vectorizer and Logistic Regression...")
    pipeline.fit(X_train, y_train)

    # 4. Evaluation
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average="macro")
    report = classification_report(y_test, y_pred, output_dict=True)

    print(f"\nModel Performance Metrics:")
    print(f"  - Accuracy: {accuracy * 100:.2f}%")
    print(f"  - Macro F1-Score: {f1_macro:.4f}")
    print("\nDetailed Per-Class Metrics:")
    for dept_name in sorted(y.unique()):
        if dept_name in report:
            m = report[dept_name]
            print(f"  [{dept_name:<12}] Precision: {m['precision']:.3f} | Recall: {m['recall']:.3f} | F1: {m['f1-score']:.3f} (Support: {m['support']})")

    # 5. Persist artifact & metadata
    artifacts_dir = root_dir / "ml" / "artifacts"
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    model_path = artifacts_dir / "department_classifier_v1.joblib"
    metrics_path = artifacts_dir / "department_metrics.json"

    joblib.dump(pipeline, model_path)

    metadata = {
        "model_key": "DEPARTMENT_ROUTING_CLASSIFIER",
        "version": "1.0.0",
        "task": "NLP_MULTICLASS_CLASSIFICATION",
        "framework": "scikit-learn",
        "vectorizer": "TF-IDF (1,2 n-grams)",
        "classifier": "LogisticRegression (L2, balanced)",
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "metrics": {
            "accuracy": round(float(accuracy), 4),
            "macro_f1": round(float(f1_macro), 4),
            "per_class": report
        },
        "artifact_file": str(model_path.name)
    }

    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n[SUCCESS] Model artifact persisted to {model_path}")
    print(f"[SUCCESS] Metrics manifest persisted to {metrics_path}")
    print("=" * 70)

if __name__ == "__main__":
    train_and_evaluate()
