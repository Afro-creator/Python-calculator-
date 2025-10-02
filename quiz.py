questions = [
    {
    "question": "What is the Capital of France?",
    "options": ["A. Paris", "B. London", "C. Nairobi", "D. Eiffel"],
    "answer": "A"
    },
    {
    "question": "Which data type is immutable in Python?",
    "options": ["A. List", "B. Sets", "C. Tuples", "D. Dictionary"],
    "answer": "C"
    },
    {
    "question": "What is the largest planet in our solar system?",
    "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
    "answer": "B"   

    },
    {
    "question": "Who wrote 'Romeo and Juliet'?",
    "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
    "answer": "C"
    },
    {
    "question": "What is the chemical symbol for water?",   
    "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
    "answer": "B"
    },
    {
    "question": "What year did the Titanic sink?",
    "options": ["A. 1912", "B. 1905", "C. 1898", "D. 1923"],
    "answer": "A"       
    },
    {
    "question": "What is the hardest natural substance on Earth?",  
    "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Silver"],
    "answer": "C"
    },
    {
    "question": "Who painted the Mona Lisa?",
    "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
    "answer": "C"
    },
    {
    "question": "What is the smallest prime number?",
    "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
    "answer": "C"
    },
    {
    "question": "Which element has the chemical symbol 'O'?",
    "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Silver"],
    "answer": "B"
    },
    {
    "question": "What is the main ingredient in guacamole?",
    "options": ["A. Tomato", "B. Avocado", "C. Onion", "D. Pepper"],
    "answer": "B"   
    },
    {
    "question": "Who is known as the 'Father of Computers'?",
    "options": ["A. Charles Babbage", "B. Alan Turing", "C. John von Neumann", "D. Steve Jobs"],
    "answer": "A"
    },
    {
    "question": "What is the largest mammal in the world?",
    "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
    "answer": "B"
    },
    {
    "question": "Which planet is known as the Red Planet?",
    "options": ["A. Venus", "B. Mars", "C. Jupiter",    "D. Saturn"],
    "answer": "B"
    },
    {
    "question": "What is the boiling point of water at sea level?",
    "options": ["A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"],
    "answer": "B"
    },
    {
    "question": "Who discovered penicillin?",   
    "options": ["A. Marie Curie", "B. Alexander Fleming", "C. Louis Pasteur", "D. Gregor Mendel"],
    "answer": "B"
    },
    {
    "question": "What is the currency of Japan?",
    "options": ["A. Yen", "B. Dollar", "C. Euro", "D. Peso"],
    "answer": "A"
    },
    {   
    "question": "Which organ in the human body is primarily responsible for detoxification?",
    "options": ["A. Kidney", "B. Liver", "C. Lungs", "D. Heart"],
    "answer": "B"
    },
    {
    "question": "What is the tallest mountain in the world?",
    "options": ["A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Lhotse"],
    "answer": "C"
    },
    {
    "question": "Who is the author of '1984'?",
    "options": ["A. Aldous Huxley", "B. George Orwell", "C. Ray Bradbury", "D. J.K. Rowling"],
    "answer": "B"
    },
    {
    "question": "What is the primary language spoken in Brazil?",
    "options": ["A. Spanish", "B. Portuguese", "C. French", "D. English"],
    "answer": "B"   
    },
    {
    "question": "What is the smallest country in the world by land area?",  
    "options": ["A. Monaco", "B. Nauru", "C. Vatican City", "D. San Marino"],
    "answer": "C"
    },
    {
    "question": "Which gas is most abundant in the Earth's atmosphere?",
    "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Argon"],
    "answer": "B"
    },
    {
    "question": "What is the main ingredient in traditional Japanese miso soup?",   
    "options": ["A. Tofu", "B. Seaweed", "C. Miso paste", "D. Rice"],
    "answer": "C"
    },
    {
    "question": "Who was the first person to walk on the moon?",
    "options": ["A. Yuri Gagarin", "B. Buzz Aldrin", "C. Neil Armstrong", "D. Michael Collins"],
    "answer": "C"
    },
    {"question": "What is the largest desert in the world?",
    "options": ["A. Sahara", "B. Arabian", "C. Gobi", "D. Antarctic"],
    "answer": "D"   
    },
    {"question": "Which planet has the most moons?",
    "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
    "answer": "C"
    },
    {"question": "What is the hardest rock?",
    "options": ["A. Granite", "B. Marble", "C. Diamond", "D. Quartz"],
    "answer": "C"
    },
    {"question": "What is the main ingredient in hummus?",
    "options": ["A. Lentils", "B. Chickpeas", "C. Beans", "D. Peas"],
    "answer": "B"
    },
    {"question": "Who developed the theory of relativity?",
    "options": ["A. Isaac Newton", "B. Nikola Tesla", "C. Albert Einstein", "D. Galileo Galilei"],
    "answer": "C"   
    }
]

import random 
random.shuffle(questions) # Shuffle questions to ensure random order each time
def run_quiz(questions):
    score = 0 # Initialize score

    for q in questions:
        print(q["question"]) # Display the question
        for option in q["options"]: # Display the options
            print(option) # Display each option
        
        while True:
            answer = input("Your answer (A, B, C, or D): ").strip().upper() # Get user input and standardize it
            if answer in ['A', 'B', 'C', 'D']: # Validate input
                break # Exit loop if input is valid
            else:
                print("Invalid input. Please enter A, B, C, or D only.") # Prompt for valid input

        if answer == q["answer"]: # Check if the answer is correct
            print("Correct!\n") # Print feedback
            score += 1 # Increment score for correct answer
        else: # If the answer is wrong
            print(f"Wrong! The correct answer is {q['answer']}.\n") # Print the correct answer

    print(f"Quiz Over! You scored {score} out of {len(questions)}.") # Print final score
    percentage = (score / len(questions)) * 100 # Calculate percentage
    print(f"Your percentage score is {percentage:.2f}%") # Print percentage score

run_quiz(questions) # Start the quiz 

while True:
    retry = input("Do you want to retake the quiz? (yes/no): ").lower() # Ask if the user wants to retake the quiz
    if retry == 'yes':
            random.shuffle(questions) # Shuffle questions for a new order
            run_quiz(questions) # Restart the quiz
    elif retry == 'no':
            break # Exit the loop and end the quiz
    else:
            print("Please answer with 'yes' or 'no'.") # Prompt for valid input