import openai
import time

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Function to get OpenAI response
def get_openai_response(prompt):
    try:
        # Request a completion from GPT-3/4
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use other engines like "gpt-4" if you have access
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to give motivational messages
def motivational_message():
    prompts = [
        "Give me a motivational message.",
        "I need some inspiration, can you motivate me?",
        "Tell me something that will lift my spirits."
    ]
    return get_openai_response(prompts[0])

# Function to translate text
def translate_text(text, target_language="en"):
    prompt = f"Translate this text to {target_language}: {text}"
    return get_openai_response(prompt)

# Function to compare previous results with new ones
def compare_results(prev_result, new_result):
    prompt = f"Compare the following results:\nPrevious Result: {prev_result}\nNew Result: {new_result}\nWhich is better?"
    return get_openai_response(prompt)

# Function to answer questions
def answer_question(question):
    prompt = f"Answer this question: {question}"
    return get_openai_response(prompt)

def main():
    print("Welcome to the AI Assistant!")
    print("You can ask me questions, get motivational messages, or translate text. Type 'exit' to stop.")

    # User interaction loop
    while True:
        user_input = input("Enter your command: ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif "motivation" in user_input:
            print("Assistant: " + motivational_message())
        elif "translate" in user_input:
            text_to_translate = input("Enter the text to translate: ")
            target_language = input("Enter target language (default is English): ").strip() or "en"
            print("Assistant: " + translate_text(text_to_translate, target_language))
        elif "compare" in user_input:
            prev_result = input("Enter previous result: ")
            new_result = input("Enter new result: ")
            print("Assistant: " + compare_results(prev_result, new_result))
        else:
            print("Assistant: " + answer_question(user_input))

if __name__ == "__main__":
    main()
