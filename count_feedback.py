# count_feedback.py

def count_feedback_entries(filename="feedback.txt"):
    """Counts the total number of feedback entries in the file."""

    count = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                count += 1
    except FileNotFoundError:
        return "Error: feedback.txt not found."

    return count

if __name__ == "__main__":
    count = count_feedback_entries()
    print(f"Total feedback entries: {count}")