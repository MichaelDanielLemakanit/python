def analyze_performance():
    # Store subject names for better feedback
    subjects = ["Math", "English", "Science", "History", "Geography"]
    marks = []

    # 1. Input marks for five subjects
    print("Enter the marks for the following subjects:")
    for subject in subjects:
        while True:
            try:
                score = float(input(f"{subject}: "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Please enter a valid score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # 2. Calculate the average
    average_score = sum(marks) / len(marks)

    # 3. Determine the Grade
    if average_score >= 70:
        grade = "A"
    elif average_score >= 50:
        grade = "B"
    else:
        grade = "C"

    # 4. Display Results
    print("\n--- Performance Report ---")
    print(f"Average Mark: {average_score:.2f}")
    print(f"Final Grade: {grade}")

    # 5. Check for Retakes (Scores below 40)
    print("\nStatus:")
    needs_retake = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"-> Must retake: {subjects[i]} (Score: {marks[i]})")
            needs_retake = True
    
    if not needs_retake:
        print("Pass: No retakes required.")

# Run the program
analyze_performance()