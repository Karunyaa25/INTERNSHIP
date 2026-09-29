import pandas as pd
from sklearn.tree import DecisionTreeClassifier
students = pd.read_csv("data/students.csv")
content = pd.read_csv("data/learning_content.csv")
progress = pd.read_csv("data/student_progress.csv")
style_map = {
    "Video": "Visual",
    "Article": "Reading",
    "Practice": "Practice"
}
progress["learning_style"] = progress["module_id"].map(
    content.set_index("module_id")["content_type"]
).map(style_map)
style_score = progress.groupby(
    ["student_id", "learning_style"]
)["score"].mean()
detected_style = style_score.groupby(
    level=0
).idxmax()
students["detected_learning_style"] = students[
    "student_id"
].map(
    detected_style.apply(lambda x: x[1])
)
students["detected_learning_style"] = students[
    "detected_learning_style"
].fillna(
    students["learning_style"]
)

X = students[
    ["score", "engagement", "practice_score", "time_spent"]
]
y = students["learning_style"]
model = DecisionTreeClassifier(
    random_state=42
)
model.fit(X, y)
students["ml_predicted_style"] = model.predict(X)
results = []
for student_id in students["student_id"]:

    student = students[
        students["student_id"] == student_id
    ].iloc[0]


    # Modules completed by student
    completed = progress[
        (progress["student_id"] == student_id) &
        (progress["completion"] == 100)
    ]["module_id"].tolist()


    # Find learning path
    remaining = content[
        ~content["module_id"].isin(completed)
    ].sort_values("difficulty")


    learning_path = []

    for _, module in remaining.iterrows():

        prerequisite = module["prerequisite"]

        if (
            pd.isna(prerequisite)
            or prerequisite in completed
            or prerequisite in learning_path
        ):
            learning_path.append(
                module["module_id"]
            )
    # Student progress
    student_progress = progress[
        progress["student_id"] == student_id
    ]


    if len(student_progress) > 0:

        completion = student_progress[
            "completion"
        ].mean()

        average_score = student_progress[
            "score"
        ].mean()

        total_time = student_progress[
            "time_spent"
        ].sum()

    else:

        completion = 0
        average_score = 0
        total_time = 0


    # ML-based recommendation
    recommended = content[
        content["learning_style"] ==
        student["ml_predicted_style"]
    ]

    recommended = recommended[
        ~recommended["module_id"].isin(completed)
    ]


    recommended_modules = recommended[
        "module_id"
    ].tolist()


    # Store result
    results.append({

        "student_id": student_id,

        "learning_level":
            student["learning_level"],

        "learning_style":
            student["ml_predicted_style"],

        "completed_modules":
            len(completed),

        "completion_percentage":
            completion,

        "average_score":
            average_score,

        "total_time_hours":
            total_time,

        "learning_path":
            ", ".join(learning_path),

        "recommended_modules":
            ", ".join(recommended_modules)
    })


# 5. FINAL RESULTS

results = pd.DataFrame(results)
print("\n PERSONALIZED LEARNING RESULTS")
print(results)
print(results.to_string(index=False))
results.to_csv(
    "personalized_learning_results.csv",
    index=False
)
print(
    "\nResults saved to personalized_learning_results.csv"
)

# NEW STUDENT PREDICTION

print("\nTest")
score = float(input("Enter Score: "))
engagement = float(input("Enter Engagement: "))
practice_score = float(input("Enter Practice Score: "))
time_spent = float(input("Enter Time Spent: "))
new_student = [[
    score,
    engagement,
    practice_score,
    time_spent
]]

predicted_style = model.predict(new_student)[0]
learning_path = content.sort_values("difficulty")["module_id"].tolist()
recommended = content[
    content["learning_style"] == predicted_style
]["module_id"].tolist()

print("\nLearning Path:", learning_path)
print("Recommended Modules:", recommended)
print("\nPredicted Learning Style:", predicted_style)

