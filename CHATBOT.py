import random
import json

# Define the rules and responses for the chatbot
rules = {
    'hello': ['NAMASTE!', 'HELLO!', 'VANAKAM!', 'Greetings!'],
    'how are you': ['I am doing well, thank you!', 'I am fine, how about you?', 'All good!'],
    'what is your name': ['I am a rule-based chatbot.', 'You can call me ChatBot.', 'My name is ChatBot.'],
    'what is your age': ['I am a chatbot, I do not have an age.', 'I am ageless!', 'I exist in the digital realm, no age for me!'],
    'bye': ['Goodbye!', 'See you!', 'Bye!', 'Take care!']
}

def get_response(user_input):
    for rule, responses in rules.items():
        if rule in user_input.lower():
            return random.choice(responses)
    return "I'm sorry, I don't understand that."

def add_rule(rule, response):
    rules[rule.lower()] = [response]

def save_rules_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(rules, file)

def load_rules_from_file(filename):
    global rules
    with open(filename, 'r') as file:
        rules = json.load(file)

# Main chat loop
print("Bot: Hi, I'm a rule-based chatbot. How can I assist you?")
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break

    if user_input.lower() == 'add rule':
        new_rule = input("Enter the new rule: ")
        new_response = input("Enter the response for the rule: ")
        add_rule(new_rule, new_response)
        print("Bot: Rule added successfully!")
        continue

    if user_input.lower() == 'save':
        filename = input("Enter the filename to save the rules: ")
        save_rules_to_file(filename)
        print("Bot: Rules saved successfully!")
        continue

    if user_input.lower() == 'load':
        filename = input("Enter the filename to load the rules: ")
        load_rules_from_file(filename)
        print("Bot: Rules loaded successfully!")
        continue

    response = get_response(user_input)
    print("Bot:", response)
