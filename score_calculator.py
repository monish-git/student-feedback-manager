# score_calculator.py

def compute_average_score():
    total = 0
    count = 0

    try:
        with open("feedback_data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    score = float(parts[1])
                    total += score
                    count += 1
    except FileNotFoundError:
        print("No feedback data found.")
        return

    if count == 0:
        print("No valid feedback entries.")
    else:
        print(f"Average score: {total / count:.2f}")

if __name__ == "__main__":
    compute_average_score()

