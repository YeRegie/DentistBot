# About GGSS - Gigi's smile support chatbot
The GGSS - Gigi's Smile Support 🦷, is a chatbot built on Streamlit, aimed at offering users' dental health guidance and assisting them with fundamental questions regarding symptoms and dental conditions. It harnesses the power of Gemini, Google's Generative AI model, to comprehend and address user inquiries accurately.

# Dev info
*Name: Regino C. Gallena
*Course and Section: BSCS 3 A- AI
*Institution: College of Information and Communications Technology, West Visayas State University
*Project Overview: A final project requirement for completion of the CCS 229 - Intelligent Systems
course in the Bachelor of Science in Computer Science program 
at the College of Information and Communications Technology, West Visayas State University.
## Project Setup

### Prerequisites

- Python 3.8+
- Pip
- An API key from Google Cloud with access to the Gemini model

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://yourrepository.git
   cd yourrepository
   ```

2. **Set up a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```

4. **Environment Variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your API key to the `.env` file:
     ```plaintext
     GEMINI_API_KEY='your_api_key_here'
     ```

### Running the Application

Execute the following command to run the app:
```bash
streamlit run your_script_name.py
```
### Functionalities

## Key Features 
1. **Interactive Dental Health Assistance:**

- Users can input their dental health-related questions, and the chatbot will provide accurate and relevant responses to help them understand their symptoms and conditions better.
  
2. **Step-by-Step Interaction:**

- The chatbot engages users with multiple prompts to gather detailed information before offering a conclusion or advice. This ensures a thorough understanding of the user's situation.
  
3. **Maintains Chat History:**

- All interactions are archived within a scrollable container, allowing users to review past conversations easily. This feature helps in maintaining continuity in the discussion.
  
4. **Reset Conversation:**

- Users can reset the conversation at any time to start a new session. This feature clears all previous chat history and allows users to commence a new interaction with the chatbot.
  
5. **Personalized Interaction:**

- The chatbot introduces itself as Gigi, the AI dentist, and provides a welcoming introduction to make the interaction more friendly and engaging.

## How It Works

1. **Launching the Chat:**

- Upon opening the application, users encounter a text input field where they can enter their dental inquiries.

2. **Multiple Prompts for Detailed Information:**

- The chatbot first asks about the user's dental history, followed by specific questions about their current dental issues. This step-by-step approach ensures comprehensive data collection before providing any conclusions.

3. **Accurate Responses Using Generative AI:**

-The chatbot utilizes Gemini, Google's Generative AI model, to generate accurate and helpful responses based on the user's input.

4. **Continuing the Conversation:**

- Users can continue to ask follow-up questions, and the chatbot will respond accordingly, maintaining the flow of the conversation without resetting.

5. **Resetting the Conversation:**

- If users wish to start a new session, they can reset the conversation, which clears the chat history and interaction count, allowing for a fresh start.





