# YouTube Transcript RAG Application

An interactive web application that retrieves and synthesizes answers from YouTube video transcripts using Retrieval-Augmented Generation (RAG).

## Setup Instructions
1. Clone the repository and navigate to the project directory.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `streamlit run app.py`

## Usage
1. Input your OpenAI API Key in the sidebar.
2. Provide a YouTube Video ID (e.g., `Gfr50f6ZBvo`).
3. Click "Process Video" to ingest and vectorize the transcript.
4. Ask questions in the text input field to query the video context.