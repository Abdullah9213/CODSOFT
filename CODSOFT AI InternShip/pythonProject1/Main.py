from Chatbot import chatbot


my_chatbot = chatbot()


def chat():
    user_input = input("You: ")

    while True:
        user_input = user_input.lower()
        if user_input != "goodbye" and user_input != "exit" and user_input != "":
            chatbot_response, probability = my_chatbot.get_response(user_input)

            print("Chatbot: ", chatbot_response)
            print("Probability: ", probability * 100,'%')
            user_input = input("You: ")
        elif user_input == "":
            print("Invalid input")
            user_input = input("You: ")
        else:
            print("Goodbye!")
            return 0


def main():
    chat()


if __name__ == "__main__":
    main()
