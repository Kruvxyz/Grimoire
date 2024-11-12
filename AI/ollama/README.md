# Ollama Notebook Guide
This notebook provides an overview of Ollama, a versatile tool for running and interacting with language models. This guide covers the following topics:

1. Installation and Setup
2. Downloading and Running Models
2.1. Listing Available Models
2.2. Downloading Models from Hugging Face
3. Using Ollama in Python

## Installation and Setup
Prerequisites
* Operating System: macOS, Linux, or Windows Subsystem for Linux (WSL)
* Python: Version 3.6 or higher
* Git: Ensure Git is installed for cloning repositories

## Installation Steps
1. Install Ollama
```
# For macOS (using Homebrew)
brew install ollama

# For Linux (using script)
curl -sSfL https://ollama.ai/install.sh | sh
```

3. Verify Installation
```
ollama --version
```
You should see the installed version of Ollama displayed.

## Downloading and Running Models
### Downloading a Model
To download a model, use the ollama pull command followed by the model name:
```
ollama pull llama2
```

### Running a Model
Once the model is downloaded, you can run it using:
```
ollama run llama2
```

### Listing Available Models
To see a list of models available in your local Ollama environment, use:
```
ollama list
```

### Downloading Models from Hugging Face
Ollama supports running models directly from Hugging Face repositories.

### Running a Model from Hugging Face
```
# General syntax
ollama run hf.co/{username}/{repository}
```
### Example:
```
ollama run hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF
```
### Specifying Quantization
You can specify the desired quantization level for the model:
```
# General syntax with quantization
ollama run hf.co/{username}/{repository}:{quantization}
```
### Example:
```
ollama run hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:IQ3_M
```

## Using Ollama in Python
You can integrate Ollama into your Python projects to leverage language models programmatically.

### Installation
Ensure you have the ollama Python package installed:
```
pip install ollama
```

### Sample Usage
```
import ollama

# Initialize the Ollama client
client = ollama.Client()

# Generate text using a specific model
response = client.generate(
    model='llama3',
    prompt='Once upon a time,'
)

# Print the generated text
print(response)
```

## Additional Resources
* Ollama Documentation: https://ollama.ai/docs
* Hugging Face Models: https://huggingface.co/models
* GitHub Repository: https://github.com/jmorganca/ollama

## Troubleshooting
* Model Compatibility: Ensure the models you download are compatible with Ollama.
* Network Issues: If you encounter download issues, check your network connection or proxy settings.
* Python Version: Make sure you're using a compatible version of Python (3.6 or higher).
