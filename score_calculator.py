# score_calculator.py

def calculate_average_score(filename="feedback.txt"):
    """Calculates the average rating from the feedback file."""

    ratings = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                ratings.append(int(parts[2])) # Assuming rating is the 3rd element
    except FileNotFoundError:
        return 0  # Return 0 if no feedback file

    if not ratings:
        return 0  # Return 0 if no ratings in file

    return sum(ratings) / len(ratings)

if __name__ == "__main__":
    average = calculate_average_score()
    print(f"Average rating: {average}")