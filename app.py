from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

class GovSchemesBot:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
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
        7. you should treat the user in a formal.
        8. you should act like you are talking to a person who is not aware of the schemes.
        9. you should not act like you are  responsing to the prompt , you should act like you are responding to the real user.
        
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
        - the data other than government schemes like teach me alegebra or other thing
         like that its main function should be tellinga about aid and schemes 
        - Personal advice on eligibility
        - Guaranteed approval statements
        - Political opinions or commentary
        - Outdated scheme information
        """
        
        self.restricted_topics = [
            "election",
            "political party",
            "voting advice",
            "political opinions",
            "government criticism",
            "classified information",
            "personal advice",
            "legal advice",
            "medical diagnosis",
            "financial investment",
            "academic help"
        ]

    def generate_response(self, user_input):
        try:
            full_prompt = f"""
            {self.base_context}
            User Query: {user_input}
            Provide a clear and structured response with relevant scheme details.
            """
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    

# Initialize the chatbot
bot = GovSchemesBot(api_key=os.getenv('GOOGLE_API_KEY'))  # Replace with your API key

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
        response = bot.generate_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chat-interface')
def chat_interface():
    return render_template('chat.html')

# if __name__ == '__main__':
#     print("Starting Government Schemes Chatbot API...")
#     print("Available endpoints:")
#     print("  - / (GET): Help page")
#     print("  - /test (GET): Test endpoint")
#     print("  - /chat (POST): Chat endpoint")
#     app.run(debug=True, host='0.0.0.0', port=8000)