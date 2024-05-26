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

### Functionalities
