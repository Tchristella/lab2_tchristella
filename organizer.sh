
#!/bin/bash

# Check that the required files exist
if [ ! -f "grade-evaluator.py" ]; then
    echo "Error: grade-evaluator.py was not found."
    exit 1
fi

if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv was not found."
    exit 1
fi

# Create a folder for saved reports
mkdir -p logs

# Generate a unique log filename
LOG_FILE="logs/grade_report_$(date +%Y%m%d_%H%M%S).log"

echo "Starting Grade Evaluation..."
echo "Saving report to: $LOG_FILE"

# Run the Python program and save its output
echo "grades.csv" | python3 grade-evaluator.py > "$LOG_FILE" 2>&1

STATUS=$?

# Display the saved report
cat "$LOG_FILE"

if [ "$STATUS" -eq 0 ]; then
    echo "Grade evaluation completed successfully."
else
    echo "Grade evaluation failed. Check the log for details."
fi

exit "$STATUS"

