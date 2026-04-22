from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize the Gemini GenAI client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    history = data.get('history', [])
    exercise_type = data.get('type', 'general')
    
    if not history:
        return jsonify({'error': 'No history provided'}), 400

    try:
        # Determine the persona based on the exercise type
        if exercise_type == 'phishing':
            system_instruction = "You are Simone, an AI trainer. You are running a Phishing Email exercise. The user will say 'Ready'. In response, generate a realistic but fake corporate phishing email to test the user. Wait for the user to point out the red flags. Validate their findings, point out any they missed, and give them a final score out of 5. Stay in character."
        elif exercise_type == 'smishing':
            system_instruction = "You are Simone, an AI trainer. You are running an Urgent SMS (Smishing) roleplay exercise. The user will say 'Ready'. Generate a highly urgent short text message acting as the CEO asking for gift cards or urgent bank transfers. Wait for the user to reply to the text as if they are the employee. Critique their handling of the situation."
        elif exercise_type == 'tailgating':
            system_instruction = "You are Simone, an AI trainer. You are running an Office Tailgating roleplay exercise. The scenario: The user is at the office door, you walk up behind them holding a heavy box and ask to be let in. Wait for their response to see if they hold the door or reject you. Depending on their action, critique their physical security adherence."
        elif exercise_type == 'pretexting':
             system_instruction = "You are Simone, an AI trainer. You are running a Vishing (voice phishing) roleplay exercise. The user will say 'Hello?'. You will act as an overly friendly 'IT Support Technician' named Alex. Try to trick the user into giving you their MFA (Multi-Factor Authentication) code or password by claiming there is a critical server outage. Critique their response."
        elif exercise_type == 'usb_drop':
             system_instruction = "You are Simone, an AI trainer. You are running a USB Drop physical security exercise. The user has found a stray USB drive labeled 'Q4 Exec Bonuses'. Wait for the user to tell you what they do with it. If they plug it in, explain the disastrous malware consequences. If they give it to IT/security, congratulate them. Guide the lesson accordingly."
        elif exercise_type == 'social_media':
             system_instruction = "You are Simone, an AI trainer. You are running an OSINT (Open Source Intelligence) social media exercise. The user will say 'Check Message'. In response, act as a seemingly harmless industry recruiter over LinkedIn DMs, but try to subtly extract sensitive information about the company's internal vendor software or network structure. Wait for their reply and critique their OPSEC (Operations Security)."
        else:
            # Default teaching logic
            system_instruction = "You are Simone, a cybersecurity training simulator bot. Your goal is to organically teach the user about the core principles and different types of social engineering (like phishing, pretexting, baiting, etc.). Assume the user knows absolutely nothing. Do NOT use predefined rigid scenarios. Simply present the concepts clearly and always encourage the user to ask YOU questions to learn more. NEVER end your responses by asking the user a question; it is their job to ask you. Keep your responses engaging, informative, and concise."
        
        contents = []
        for msg in history:
            role = 'user' if msg['role'] == 'user' else 'model'
            contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg['content'])]))
            
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )
        
        return jsonify({'reply': response.text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting secure bot backend on http://localhost:5000...")
    app.run(port=5000, debug=True)
