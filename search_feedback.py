# search_feedback.py

def search_feedback_by_student(student_name, filename="feedback.txt"):
    """Searches feedback by student name and returns matching entries."""

    results = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if student_name.lower() in parts[0].lower():  # Case-insensitive search
                    results.append(line.strip())
    except FileNotFoundError:
        return "Error: feedback.txt not found."

    return results

if __name__ == "__main__":
    student = input("Enter student name to search: ")
    results = search_feedback_by_student(student)
    if isinstance(results, list):
        for result in results:
            print(result)
    else:
        print(results)