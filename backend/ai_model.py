from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the Llama 2 7B Chat model and tokenizer
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Load the model without device_map (for CPU or single GPU)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    # Use device_map only if GPU is available
    device_map="auto" if torch.cuda.is_available() else None,
)


def analyze_logs_with_ai(file_path, query):
    """
    Analyze logs using the Llama 2 7B Chat model.
    """
    # Read the log file
    with open(file_path, 'r') as file:
        logs = file.read()

    # Prepare the prompt for the model
    prompt = f"""
    You are a log analysis assistant. Analyze the following logs and answer the user's query.
    
    Logs:
    {logs}
    
    Query: {query}
    
    Answer:
    """

    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    # Generate the response
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            max_length=10000,  # Adjust based on your needs
            num_return_sequences=1,
            temperature=0.7,  # Adjust for creativity
            top_p=0.9,       # Adjust for diversity
        )

    # Decode the output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response
