# report_generator.py

def export_feedback_to_txt(filename="feedback.txt", output_filename="feedback_report.txt"):
    """Exports feedback data from 'feedback.txt' to a new .txt file."""

    try:
        with open(filename, "r") as input_file, open(output_filename, "w") as output_file:
            output_file.write("Student Name,Course Name,Rating,Comments\n") # Header

            for line in input_file:
                output_file.write(line)

        return f"Feedback exported to {output_filename}"

    except FileNotFoundError:
        return "Error: feedback.txt not found."

if __name__ == "__main__":
    result = export_feedback_to_txt()
    print(result)