from django.http import HttpResponse

# Define a list of tuples containing questions and their corresponding options
quiz = [
    ("You have 20 seconds to answer.Who was the first president of Kenya?", ["Jomo Kenyatta", "Uhuru Kenyatta", "Moi Daniel", "Mwai kibaki"]),
    ("Congratulations.You have earned 50 points.When did Kenya get independence?", ["1955", "1963", "1980", "1961"])
    ("Congratulations.You have earned 100 points.What is the capital city of Kenya?", ["Nakuru", "Nairobi", "Mombasa", "Kisumu"])
]

# Define a dictionary to store correct answers
correct_answers = {
    "Who was the first president of Kenya?": "1",
    "When did Kenya get independence?": "2"
}

def ussd_callback(request):
    # Get the POST data from the request
    session_id = request.POST.get("sessionId")
    phone_number = request.POST.get("phoneNumber")
    service_code = request.POST.get("serviceCode")
    text = request.POST.get("text")

    # If text is not provided or is empty, display the main menu
    if not text:
        response = "CON Welcome to Omoka draw. Please select an option to win upto 21,500:\n"
        response += "1. Start Quiz\n"
        response += "2. Withdraw to M-pesa\n"
        response += "3. Terms & Conditions"
    else:
        # Check user input for menu options
        if text == '1':
            # Start the quiz
            response = "CON " + quiz[0][0] + "\n"
            for i, option in enumerate(quiz[0][1], start=1):
                response += f"{i}. {option}\n"
            response += "Enter your answer:"
        elif text == '2':
            # Process withdrawal if user selects option 2
            amount = 100
            phone = phone_number
            # Call function to initiate M-Pesa payment
            # initiate_mpesa_payment(phone, amount, access_token)
            response = "END {} Pay verification fee to get your loan within 24hrs\n".format(phone)
        elif text == '3':
            # Display terms and conditions if user selects option 3
            response = "END Terms & Conditions: These are the terms and conditions.\n"
        elif text.isdigit():
            # Check if the user entered a digit (quiz answer)
            question_index = int(text) - 1  # Convert user input to index
            current_question, options = quiz[question_index]
            correct_answer = correct_answers[current_question]
            if text == correct_answer:
                # User entered the correct answer, ask the next question
                if question_index < len(quiz) - 1:
                    next_question, next_options = quiz[question_index + 1]
                    response = f"CON {next_question}\n"
                    for i, option in enumerate(next_options, start=1):
                        response += f"{i}. {option}\n"
                    response += "Enter your answer:"
                else:
                    # End of quiz, provide feedback
                    response = "END Congratulations! You've earned 150 points with 100% correct annswers\n Enter your pin to get a chance to win 21,500 within the hour\n"
            else:
                # User entered the wrong answer, end the session
                response = "END Wrong answer. Quiz ended.\n"
        else:
            # User entered an invalid option, end the session
            response = "END Invalid selection. Session ended.\n"

    # Send response to USSD gateway
    return HttpResponse(response, content_type='text/plain')
