
import csv
import sys
import os


def load_csv_data():
    """Load assignment records from a CSV file."""
    filename = input(
        "Enter CSV filename (example: grades.csv): "
    ).strip()

    if not filename:
        print("Error: No filename was provided.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("Error: File '{}' was not found.".format(filename))
        sys.exit(1)

    assignments = []
    required = {"assignment", "group", "score", "weight"}

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or not required.issubset(
                    set(reader.fieldnames)):
                print("Error: CSV must contain assignment, group, "
                      "score and weight columns.")
                sys.exit(1)

            for line, row in enumerate(reader, start=2):
                if not all(row.get(field) and row[field].strip()
                           for field in required):
                    print("Error: Missing data on row {}.".format(line))
                    sys.exit(1)

                try:
                    score = float(row["score"])
                    weight = float(row["weight"])
                except ValueError:
                    print("Error: Score and weight must be numbers "
                          "on row {}.".format(line))
                    sys.exit(1)

                assignments.append({
                    "assignment": row["assignment"].strip(),
                    "group": row["group"].strip().title(),
                    "score": score,
                    "weight": weight
                })

        if not assignments:
            print("Error: CSV file contains no assignment records.")
            sys.exit(1)

        return assignments

    except (IOError, OSError) as error:
        print("Error reading file: {}".format(error))
        sys.exit(1)


def evaluate_grades(data):
    """Validate records, calculate grades and determine pass or fail."""
    print("\n--- GRADE EVALUATION ---")

    for item in data:
        if not 0 <= item["score"] <= 100:
            print("Error: Score for {} must be between 0 and 100."
                  .format(item["assignment"]))
            return

        if item["weight"] < 0:
            print("Error: Weight for {} cannot be negative."
                  .format(item["assignment"]))
            return

        if item["group"] not in ("Formative", "Summative"):
            print("Error: Invalid group '{}'. Use Formative or Summative."
                  .format(item["group"]))
            return

    total_weight = sum(item["weight"] for item in data)

    formative = [item for item in data
                 if item["group"] == "Formative"]
    summative = [item for item in data
                 if item["group"] == "Summative"]

    formative_weight = sum(item["weight"] for item in formative)
    summative_weight = sum(item["weight"] for item in summative)

    if (abs(total_weight - 100) > 0.01 or
            abs(formative_weight - 60) > 0.01 or
            abs(summative_weight - 40) > 0.01):
        print("Error: Incorrect assignment weights.")
        print("Total weight: {}% (required: 100%)".format(total_weight))
        print("Formative weight: {}% (required: 60%)"
              .format(formative_weight))
        print("Summative weight: {}% (required: 40%)"
              .format(summative_weight))
        return

    formative_grade = sum(
        item["score"] * item["weight"] for item in formative
    ) / formative_weight

    summative_grade = sum(
        item["score"] * item["weight"] for item in summative
    ) / summative_weight

    final_grade = sum(
        item["score"] * item["weight"] for item in data
    ) / 100

    gpa = (final_grade / 100) * 4

    print("\nFormative Grade: {:.2f}%".format(formative_grade))
    print("Summative Grade: {:.2f}%".format(summative_grade))
    print("Final Grade: {:.2f}%".format(final_grade))
    print("GPA (4.0 scale): {:.2f}".format(gpa))

    passed = formative_grade >= 50 and summative_grade >= 50

    failed_formative = [
        item for item in formative if item["score"] < 50
    ]

    print("\n--- RESUBMISSION OPTIONS ---")

    if failed_formative:
        highest_weight = max(
            item["weight"] for item in failed_formative
        )

        options = [
            item for item in failed_formative
            if item["weight"] == highest_weight
        ]

        print("Failed formative assignments:")
        for item in failed_formative:
            print("- {}: {}%".format(
                item["assignment"], item["score"]))

        print("\nHighest-weight assignment(s) for resubmission:")
        for item in options:
            print("- {} ({}% weight)".format(
                item["assignment"], item["weight"]))
    else:
        print("No failed formative assignments.")

    print("\n--- FINAL DECISION ---")

    if passed:
        print("PASSED")
    else:
        print("FAILED")
        if formative_grade < 50:
            print("Reason: Formative grade is below 50%.")
        if summative_grade < 50:
            print("Reason: Summative grade is below 50%.")


if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)

