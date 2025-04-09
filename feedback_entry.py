# feedback_entry.py

def collect_feedback():
    """Collects student feedback from the command line."""

    feedback = {}
    feedback['student_name'] = input("Enter student name: ")
    feedback['course_name'] = input("Enter course name: ")
    feedback['rating'] = int(input("Enter rating (1-5): "))
    feedback['comments'] = input("Enter comments: ")

    return feedback

def save_feedback(feedback, filename="feedback.txt"):
    """Saves feedback to a file."""

    with open(filename, "a") as f:  # Append to file
        f.write(f"{feedback['student_name']},{feedback['course_name']},{feedback['rating']},{feedback['comments']}\n")

if __name__ == "__main__":
    feedback = collect_feedback()
    save_feedback(feedback)
    print("Feedback saved successfully!")