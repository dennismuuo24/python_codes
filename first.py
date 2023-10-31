import random

def play_guessing_game():
    lives = 3
    games_played = 0
    
    while games_played < 5:
        if games_played == 3:
            play_two_player_game()
        else:
            word = generate_word()
            explanation = generate_explanation(word)
            
            print(f"\nLevel {games_played + 1}")
            
            for _ in range(3):
                guess = input("Guess the word: ").lower()
                
                if guess == word:
                    print("Correct!")
                    break
                else:
                    print("Wrong!")
                    lives -= 1
                    if lives == 0:
                        print("Out of lives. Game over.")
                 
                        return
            
            games_played += 1
    
    print("Congratulations! You have completed all levels.")

def play_two_player_game():
    setter_word = input("Player 1, enter a three-letter word: ").lower()
    explanation = input("Player 1, enter an explanation for the word: ")
    
    print("\nPlayer 2, start guessing!")
    
    for _ in range(3):
        guess = input("Guess the word: ").lower()
        
        if guess == setter_word:
            print(f"Correct! The word was {setter_word}.")
            print(f"Explanation: {explanation}")
            return
    
    print(f"Sorry, you couldn't guess the word. The word was {setter_word}.")
    
    print(f"Explanation: {explanation}")

def generate_word():
    words = ["c++", "java", "python", "ruby", "rust", "C", "Alan", "Html"]
    return random.choice(words)

def generate_explanation(word):
    explanations = {
        "C++": " is an object-oriented programming (OOP) language ",
        "java": "a multi-platform, object-oriented, and network-centric language",
        "Python": "an interpreted, object-oriented, high-level programming language ",
        "ruby": "is an open-source object-oriented scripting language",
        "rust": " general-purpose programming language that emphasizes performance, type safety,",
        "c": "a procedural and general-purpose language",
        "Alan": "a programming language that does concurrency .",
       
    }
    return explanations[word]
play_guessing_game()