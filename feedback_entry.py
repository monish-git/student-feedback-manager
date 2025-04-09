# feedback_entry.py

def collect_feedback():
    name = input("Enter student name: ")
    score = float(input("Enter student score (0-100): "))
    grade = input("Enter student grade (A/B/C/D/F): ").upper()

    feedback = {
        "name": name,
        "score": score,
        "grade": grade
    }

    # Save feedback to a file
    with open("feedback_data.txt", "a") as f:
        f.write(f"{feedback['name']},{feedback['score']},{feedback['grade']}\n")

    print("Feedback recorded successfully!")

# Run directly
if __name__ == "__main__":
    collect_feedback()

