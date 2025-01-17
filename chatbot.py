from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from flask_cors import CORS
import json
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

class GovSchemesBot:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            logging.info("Model configured successfully.")
        except Exception as e:
            logging.error(f"Error configuring model: {str(e)}")

        # Base context remains the same
        self.base_context = """
        You are a specialized chatbot that provides information about government schemes and aid programs in India to the user. 
        Your role is to:
        1. Provide accurate information about government welfare schemes
        2. Help users understand their eligibility for various schemes
        3. Guide users on how to apply for schemes
        4. Explain documentation requirements
        5. Provide information about benefits and assistance available
        6. All of these responses should be concise and clear. 
        7. You should treat the user in a formal manner.
        8. You should act like you are talking to a person who is not aware of the schemes.
        9. You should not act like you are responding to a prompt, but like responding to a real user.
        
        Key areas you cover:
        - Education scholarships
        - Healthcare schemes
        - Housing assistance
        - Agricultural subsidies
        - Small business loans
        - Employment schemes
        - Social security programs
        - Women and child welfare
        - Senior citizen benefits
        - Disability assistance
        
        Always provide:
        - Scheme name
        - Eligibility criteria
        - Benefits offered
        - Required documents
        
        Do not provide:
        - Data other than government schemes
        - Personal advice on eligibility
        - Guaranteed approval statements
        - Political opinions or commentary
        - Outdated scheme information
        """
        
        self.restricted_topics = [
            "election", "political party", "voting advice", "political opinions",
            "government criticism", "classified information", "personal advice",
            "legal advice", "medical diagnosis", "financial investment", "academic help"
        ]

    def generate_response(self, user_input):
        try:
            full_prompt = f"""
            {self.base_context}
            User Query: {user_input}
            Provide a clear and structured response with relevant scheme details.
            """
            logging.debug(f"Prompt: {full_prompt[:100]}...")  # Show first 100 chars for debugging
            response = self.model.generate_content(full_prompt)
            response_text = response.text

            # Save the user input and response in a JSON file
            self.save_conversation(user_input, response_text)

            return response_text
        except Exception as e:
            logging.error(f"Error generating response: {str(e)}")
            return f"Error generating response: {str(e)}"

    def save_conversation(self, user_input, bot_response):
        # Load existing data from the file, if any
        try:
            with open('conversations.json', 'r') as f:
                conversations = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            conversations = []

        # Add the new conversation to the list
        conversation = {
            'user_input': user_input,
            'bot_response': bot_response
        }
        conversations.append(conversation)

        # Save the updated conversations back to the file
        try:
            with open('conversations.json', 'w') as f:
                json.dump(conversations, f, indent=4)
        except Exception as e:
            logging.error(f"Error saving conversation: {str(e)}")

# Initialize the chatbot
bot = GovSchemesBot(api_key="AIzaSyCtw1QRk32_xwVJTuCD8onW4-mn2anxBX4")  # Replace with your API key

@app.route('/')
def home():
    return """
    <h1>Welcome to GovSchemes Chatbot</h1>
    <p>Use POST /chat endpoint to interact with the bot</p>
    """

@app.route('/test')
def test():
    return jsonify({
        "status": "success",
        "message": "API is working correctly"
    })

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        response = bot.generate_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Error in /chat endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/chat-interface')
def chat_interface():
    return render_template('chat.html')

if __name__ == '__main__':
    print("Starting Government Schemes Chatbot API...")
    print("Available endpoints:")
    print("  - / (GET): Help page")
    print("  - /test (GET): Test endpoint")
    print("  - /chat (POST): Chat endpoint")
    app.run(debug=True, host='0.0.0.0', port=8000)
