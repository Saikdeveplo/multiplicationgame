import random
import time

print("Welcome to the Multiplication Game!")
print("Try to answer as many multiplication problems as you can.")

score = 0
num_problems = 10
high_score = 0
total_time = 0

for i in range(num_problems):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2

    print(f"Problem #{i+1}: {num1} x {num2} = ?")

    start_time = time.time()
    user_answer = input()
    end_time = time.time()
    elapsed_time = end_time - start_time

    user_answer = int(user_answer)

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

    total_time += elapsed_time

if score > high_score:
    high_score = score
    print(f"Congratulations! You set a new high score of {high_score}.")

print(f"You got {score} out of {num_problems} correct.")
print(f"Your total time was {round(total_time)} seconds.")
