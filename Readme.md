
# Lab 2: Grade Evaluator

## Project Description

This project is a Python-based grade evaluation system that reads student assignment records from a CSV file, validates scores and weights, calculates final grades and GPA, and determines whether a student passes or fails.

It also identifies failed formative assignments and recommends the highest-weight assignments for resubmission.

## Project Files

- `grades.csv` - Contains assignment names, categories, scores, and weights.
- `grade-evaluator.py` - Reads and processes the CSV data and calculates grades.
- `organizer.sh` - Runs the Python program and saves its output.
- `logs/` - Stores generated grade evaluation reports.

## Requirements

- Python 3
- Linux terminal
- Bash shell

No external Python libraries are required. The program uses Python standard libraries.

## How to Run

1. Clone or download this repository.
2. Open the project directory in your terminal.
3. Make the shell script executable:

   ```bash
   chmod +x organizer.sh
   ```

4. Run the program directly:

   ```bash
   python3 grade-evaluator.py
   ```

5. Enter `grades.csv` when prompted.

Alternatively, run the shell script:

```bash
./organizer.sh
```

## Evaluation Rules

- All assignment scores must be between 0 and 100.
- Total assignment weight must equal 100%.
- Formative assignments must have a combined weight of 60%.
- Summative assignments must have a combined weight of 40%.
- Students must achieve at least 50% in both categories to pass.
- Formative assignments below 50% are identified for possible resubmission.
- The highest-weight failed formative assignments are recommended for resubmission.

## GPA Calculation

The program uses a proportional 4.0 scale:

GPA = (Final Grade / 100) * 4

This is an assumed conversion because no official GPA conversion table was provided.

## Error Handling

The program checks for:
- Missing CSV files.
- Missing or empty CSV fields.
- Invalid numeric values.
- Scores outside the 0-100 range.
- Invalid assignment categories.
- Incorrect assignment weights.

## Author

Tchristella

