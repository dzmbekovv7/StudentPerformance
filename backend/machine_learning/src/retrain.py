import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from students.models import Student
from students.models import Prediction

def build_dataset():
    data = []

    for p in Prediction.objects.all():
        data.append({
            "attendance": p.student.attendance_percentage,
            "study_hours": p.student.study_hours_per_week,
            "previous_gpa": p.student.previous_gpa,
            "final": p.predicted_final_percentage
        })

    return pd.DataFrame(data)

df = build_dataset()

X = df.drop(columns=["final"])
y = df["final"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, 'models/final_score_prediction.pkl')