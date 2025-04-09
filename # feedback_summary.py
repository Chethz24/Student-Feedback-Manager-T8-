# feedback_summary.py

def summarize_feedback(filename="feedback.txt"):
    """Summarizes feedback from the feedback file."""

    ratings = []
    grades = {} # Assuming you want to count grades (e.g., A, B, C)
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                rating = int(parts[2])
                ratings.append(rating)
                # Assuming grade is the 4th element (adjust if needed)
                if len(parts) > 3:
                    grade = parts[3].upper() # Convert to uppercase for consistency
                    grades[grade] = grades.get(grade, 0) + 1
    except FileNotFoundError:
        return "No feedback file found."

    if not ratings:
        return "No feedback data."

    top_scores = sorted(ratings, reverse=True)[:5]  # Get top 5 scores
    summary = {
        "average_rating": sum(ratings) / len(ratings),
        "top_scores": top_scores,
        "grade_counts": grades
    }
    return summary

if __name__ == "__main__":
    summary = summarize_feedback()
    print(summary)