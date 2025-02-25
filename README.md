pip install flask flask-cors boto3 pandas matplotlib

clone the repo
cd ai-loganalyzer
npm install axios react-chartjs-2 chart.js
python app.py - from backend folder
npm start - from frontend folder

install dependency
cd backend
pip install -r requirements.txt
cd ../frontend
npm install
cd backend
python app.py
cd frontend
npm start

To integrate the **Meta Llama 2 7B Chat model** (`meta-llama/Llama-2-7b-chat-hf`) into the `ai_model.py` file, we'll use the Hugging Face `transformers` library. This will allow us to load the model and use it for log analysis.

Below is the updated `ai_model.py` with the Llama 2 model integration:

---



---

### **Steps to Use the Llama 2 Model**

1. **Install Required Libraries**:
   Install the `transformers` library and other dependencies:
   ```bash
   pip install transformers torch
   ```

2. **Hugging Face Authentication**:
   - The Llama 2 model requires authentication to access. You need a Hugging Face account and an access token.
   - Log in to Hugging Face and generate a token: [Hugging Face Tokens](https://huggingface.co/settings/tokens).
   - Install the `huggingface_hub` library and log in:
     ```bash
     pip install huggingface_hub
     huggingface-cli login
     ```
   - Enter your Hugging Face token when prompted.

3. **Run the Backend**:
   - Start the Flask backend:
     ```bash
     python app.py
     ```

4. **Test the AI Integration**:
   - Upload a log file and ask a query like:
     ```
     Show all errors from the past week.
     ```
   - The Llama 2 model will analyze the logs and provide a response.

---

### **Example Workflow**

1. **Upload a Log File**:
   - Use the file upload button to upload a log file.

2. **Ask a Query**:
   - Enter a query in the chat box, e.g.,:
     ```
     What are the most frequent errors in the logs?
     ```

3. **Get the Response**:
   - The Llama 2 model will process the logs and return a response.

4. **Download Reports**:
   - Use the download buttons to generate and download reports in CSV or PDF format.

---

### **Notes**

- **Hardware Requirements**:
  - The Llama 2 7B model requires a GPU with at least 16GB of VRAM for optimal performance. If you don't have a GPU, you can use a smaller model or run it on CPU (though it will be slower).
  
- **Cost-Effective Alternative**:
  - If running the model locally is too resource-intensive, consider using an API-based solution like OpenAI's GPT or Hugging Face's Inference API.

- **Environment Variables**:
  - Store sensitive credentials (e.g., Hugging Face token) in environment variables for security.

---

This updated code provides a complete integration of the Llama 2 model for log analysis. You can deploy it as-is, and it should work seamlessly with the React frontend and Flask backend.
