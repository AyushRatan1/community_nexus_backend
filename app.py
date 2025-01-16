import google.generativeai as genai

class GovSchemesBot:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Base context for the chatbot
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
        
        # List of restricted topics
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

    def is_restricted_topic(self, user_input):
        """Check if the user input contains restricted topics"""
        return any(topic.lower() in user_input.lower() for topic in self.restricted_topics)

    def generate_response(self, user_input):
        """Generate a response based on user input"""
        if self.is_restricted_topic(user_input):
            return ("I apologize, but I cannot provide information about that topic. "
                   "I can only provide factual information about government schemes and aid programs. "
                   "How can I help you with information about government welfare schemes?")

        # Construct the full prompt
        full_prompt = f"""
        {self.base_context}
        
        User Query: {user_input}
        
        Provide a clear and structured response with relevant scheme details and application information.
        If multiple schemes are relevant, list the most appropriate ones.
        If the query is not about government schemes, politely redirect to scheme-related information.
        """

        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return ("I apologize, but I encountered an error. Please try rephrasing your question "
                   "about government schemes and benefits.")

def run_chatbot():
    # Initialize the chatbot with your API key
    api_key = "AIzaSyCtw1QRk32_xwVJTuCD8onW4-mn2anxBX4"  # Replace with your actual API key
    bot = GovSchemesBot(api_key)
    
    print("Government Schemes Assistant: Hello! I can help you with information about government schemes and aid programs. "
          "What would you like to know? (Type 'exit' to end the conversation)")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'exit':
            print("\nGovernment Schemes Assistant: Thank you for using our service. Goodbye!")
            break
            
        response = bot.generate_response(user_input)
        print(f"\nGovernment Schemes Assistant: {response}")

if __name__ == "__main__":
    run_chatbot()