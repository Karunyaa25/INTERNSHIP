# AI Personalized Learning Assistant

## Project Overview

The AI Personalized Learning Assistant is a project that creates personalized learning paths for students.

The system analyzes student information, previous performance, learning progress, and learning preferences. Based on this information, it predicts a suitable learning preference, creates a learning path, recommends suitable learning content, and provides learning progress analytics.

---

## Objectives

- Understand student learning patterns
- Identify suitable learning preferences
- Predict learning preferences using Machine Learning
- Create personalized learning paths
- Recommend suitable learning content
- Track student progress
- Generate learning analytics

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Decision Tree Classifier
- CSV files

---

## Project Structure

```text
AI ASSISTED PROJECT
│
├── data
│   ├── students.csv
│   ├── learning_content.csv
│   └── student_progress.csv
│
├── main.py
│
├── personalized_learning_results.csv
│
└── README.md
---

## Dataset

The project uses three datasets.

### 1. students.csv

Contains information about students such as:

- Student ID
- Age
- Score
- Engagement
- Practice Score
- Time Spent
- Learning Style
- Learning Pace
- Learning Level

### 2. learning_content.csv

Contains information about available learning modules such as:

- Module ID
- Title
- Category
- Difficulty
- Prerequisite
- Duration
- Content Type
- Learning Style

### 3. student_progress.csv

Contains information about student learning activity such as:

- Student ID
- Module ID
- Completion
- Score
- Time Spent

---

## Working Process

1. Collect student information.
2. Collect available learning content.
3. Collect student progress information.
4. Analyze the student's previous performance.
5. Identify the student's learning preference.
6. Prepare student performance information.
7. Train the Machine Learning model.
8. Predict the suitable learning preference.
9. Check the modules already completed by the student.
10. Find the modules still available to learn.
11. Check the prerequisites of the modules.
12. Create a personalized learning path.
13. Analyze the student's learning progress.
14. Recommend suitable learning content.
15. Generate the final personalized result.
16. Save the results for each student.

---

## Machine Learning

A Decision Tree Classifier is used in the project.

The model uses student-related information such as:

- Score
- Engagement
- Practice Score
- Time Spent

The model predicts the student's learning preference.

The predicted preference is then used to recommend suitable learning content.

---

## Learning Path Generation

The learning path is created by considering:

- Modules already completed
- Module difficulty
- Module prerequisites
- Available learning modules

This helps the system provide a suitable order for learning.

---

## Learning Analytics

The system calculates:

- Number of completed modules
- Completion percentage
- Average score
- Total learning time
- Personalized learning path
- Recommended modules

---

## Output

The final personalized results are saved in:

```text
personalized_learning_results.csv