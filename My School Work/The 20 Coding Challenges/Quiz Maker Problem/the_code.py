import random


def key_to_define_users_grade(points, number_of_questions_user_wants_to_answer):
    # the line below is how we calculate percentage

    percentage = (points / number_of_questions_user_wants_to_answer) * 100
    # if it meeta a cetain condition you get a cetain grade
    if (percentage >= 95):
        print("You got", percentage, "% which is a grade 9")
    elif (percentage >= 85) and (percentage < 95):
        print("You got", percentage, "% which is a grade 8")
    elif (percentage >= 75) and (percentage < 85):
        print("You got", percentage, "% which is a grade 7")
    elif (percentage >= 65) and (percentage < 75):
        print("You got", percentage, "% which is a grade 6")
    elif (percentage >= 55) and (percentage < 65):
        print("You got", percentage, "% which is a grade 5")
    elif (percentage >= 45) and (percentage < 55):
        print("You got", percentage, "% which is a grade 4")
    elif (percentage >= 35) and (percentage < 45):
        print("You got", percentage, "% which is a grade 3")
    elif (percentage >= 25) and (percentage < 35):
        print("You got", percentage, "% which is a grade 2")
    elif (percentage >= 15) and (percentage < 25):
        print("You got", percentage, "% which is a grade 1")
    elif (percentage < 15):
        print("You got", percentage, "% which is a grade U")
    valid_choice = False
    # here you have a choice if you want to do a new quiz or you can quit the program and there is also validation for this
    while not valid_choice:
        print("Press 1 if you want to do a new quiz")
        print("Press 2 if want to quit the program ")
        users_choice = input("Which number do you choose\n")
        if (users_choice == "1"):
            valid_choice = True
            append_questions_from_file()
        elif (users_choice == "2"):
            print("Good bye")
            exit()
        else:
            print("Invalid choice")


def ask_and_check_users_answers_from_randomly_chosen_question(list_of_questions, list_of_answers, number_of_questions_user_wants_to_answer, number_of_questions_in_file):

    list_of_users_questions = []
    list_of_users_answers = []
    # the line under basically creates a list of random numbers which is basically random indexes
    # it will create a random list of numbers ranging from 0 - 50 bot only a cetain amount of times eg 10 times meaning it creates 10 random numbers which is in a list
    random_list_of_index_numbers = random.sample(
        range(number_of_questions_in_file + 1), number_of_questions_user_wants_to_answer)
    # we then loop through the random indexes and because the index is random we just get a index of the list of quetions and append it to a new list , same thing happens for the answers list
    for random_index in random_list_of_index_numbers:
        list_of_users_questions.append(list_of_questions[random_index])
        list_of_users_answers.append(list_of_answers[random_index])
    points = 0
    # here we have randomly chose the questions so we loop throuh the list and ask the user where they only have 3 attempts to type in the correct answer if they still get it wrong the correct answer is shown and we stop the while loop but this also stops the for loop so what we do is that we put a continue statement which continues the for loop
    for question in list_of_users_questions:
        answer_index = list_of_users_questions.index(question)
        attempts = 2
        valid_ans = False
        while not valid_ans:
            print(question)
            users_answer = input("What is the answer to this question\n")
            if (attempts == 0):
                print("The correct answer was: ",
                      list_of_users_answers[answer_index])
                valid_ans = True
            elif (users_answer != list_of_users_answers[answer_index]):
                print("Wrong answer, try again")
                attempts -= 1
            elif (users_answer == list_of_users_answers[answer_index]):
                print("Correct answer")
                points += 1
                valid_ans = True
        continue
    key_to_define_users_grade(points, number_of_questions_user_wants_to_answer)


def append_questions_from_file():
    # in a file i have questions which i got from the internet and another file with the answers with it
    number_of_questions_in_file = 0
    list_of_questions = []
    list_of_answers = []
    print("Welcome to Sanjeev's fun quiz")
    print("All questions are randomly chosen")
    print("You get 1 point for every correct answer")
    print("Answer questions in lower case letters and correct spelling")
    valid_num = False
    while not valid_num:
        # the user gets to choose how many questuons they want to answer and they must answer atleast 10 questions and for the input there is validation
        print("You must answer atleast 10 questions but you can answer up to 50 questions")
        number_of_questions_user_wants_to_answer = input(
            "How many questions would you like to answer\n")
        if (number_of_questions_user_wants_to_answer.isnumeric()) and (int(number_of_questions_user_wants_to_answer) >= 10) and (int(number_of_questions_user_wants_to_answer) <= 50):
            # we loop through the file with questions and append it to a list, the same thing happens in the file with ask_and_check_users_answers_from_randomly_chosen_question, we keep track of how many questions there are in total in the file
            # after that we call the function which randomly chooses the questions and asks the user
            valid_num = True
            number_of_questions_user_wants_to_answer = int(
                number_of_questions_user_wants_to_answer)
            questions_in_file = open("quiz questions.txt", "r")
            for question in questions_in_file:
                number_of_questions_in_file += 1
                list_of_questions.append(question.strip())
            answers_in_file = open("quiz questions answers.txt", "r")
            for answer in answers_in_file:
                list_of_answers.append(answer.strip())
            ask_and_check_users_answers_from_randomly_chosen_question(
                list_of_questions, list_of_answers, number_of_questions_user_wants_to_answer, number_of_questions_in_file)
        else:
            print("Invalid choice")


append_questions_from_file()
