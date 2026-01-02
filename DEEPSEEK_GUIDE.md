# DeepSeek Installation and Usage Guide for Termux

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation Methods](#installation-methods)
4. [Configuration](#configuration)
5. [Usage Options](#usage-options)
6. [Troubleshooting](#troubleshooting)
7. [FAQ](#faq)

## Introduction

DeepSeek is an advanced AI language model developed by DeepSeek AI. This guide will help you install and use DeepSeek on your Android device through Termux.

### What You Can Do With DeepSeek

- **Code Generation**: Generate, explain, and debug code
- **Chat Interface**: Have natural conversations with AI
- **Text Analysis**: Analyze and summarize documents
- **Programming Help**: Get assistance with coding problems
- **General Q&A**: Ask questions on various topics

## Prerequisites

### Device Requirements

- **RAM**: Minimum 4GB, 8GB+ recommended
- **Storage**: At least 10GB free space
- **Android Version**: 7.0 or higher
- **Termux**: Version 117 or higher (available in this repository)

### Network Requirements

- Stable internet connection for:
  - Initial package installation
  - API usage (if using DeepSeek API)
  - Model downloads (if running locally)

## Installation Methods

### Method 1: Automated Installation (Recommended)

```bash
# Download the installation script
curl -o install-deepseek.sh https://raw.githubusercontent.com/4evernever77777/termux-releases/main/install-deepseek.sh

# Make it executable
chmod +x install-deepseek.sh

# Run the installer
./install-deepseek.sh
```

The script will:
- Update Termux packages
- Install Python and dependencies
- Set up DeepSeek environment
- Create helper scripts

### Method 2: Manual Installation

If you prefer manual installation:

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and essential tools
pkg install -y python python-pip git wget curl

# Install build tools
pkg install -y clang cmake libc++

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install numpy torch transformers tiktoken einops sentencepiece

# Create DeepSeek directory
mkdir -p ~/deepseek
cd ~/deepseek
```

## Configuration

### Option 1: Using DeepSeek API (Recommended for Mobile)

The API approach is lighter on resources and doesn't require downloading large models.

1. **Get an API Key**
   - Visit [DeepSeek Platform](https://platform.deepseek.com)
   - Sign up for an account
   - Generate an API key

2. **Configure API Key**
   ```bash
   cd ~/deepseek
   ./setup_api.sh
   ```
   
   Or manually:
   ```bash
   echo "export DEEPSEEK_API_KEY='your-api-key-here'" >> ~/.bashrc
   source ~/.bashrc
   ```

3. **Test API Connection**
   ```bash
   cd ~/deepseek
   ./example_api_call.sh
   ```

### Option 2: Running Models Locally

For running models locally (requires more resources):

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Use a smaller model for mobile devices
model_name = "deepseek-ai/deepseek-coder-1.3b-base"

print("Downloading model (this may take time)...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Use half precision to save memory
    low_cpu_mem_usage=True
)

# Generate text
inputs = tokenizer("def hello_world():", return_tensors="pt")
outputs = model.generate(**inputs, max_length=100)
print(tokenizer.decode(outputs[0]))
```

**Recommended Models for Mobile:**
- `deepseek-ai/deepseek-coder-1.3b-base` - Lightweight (1.3B parameters)
- `deepseek-ai/deepseek-coder-6.7b-base` - Medium (6.7B parameters, requires 8GB+ RAM)

## Usage Options

### 1. API Usage with curl

```bash
curl -X POST https://api.deepseek.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {"role": "system", "content": "You are a helpful coding assistant."},
      {"role": "user", "content": "Write a Python function to calculate fibonacci numbers"}
    ]
  }'
```

### 2. API Usage with Python

Create a file `chat.py`:

```python
import os
import requests
import json

API_KEY = os.environ.get('DEEPSEEK_API_KEY')
API_URL = "https://api.deepseek.com/v1/chat/completions"

def chat(message, system_prompt="You are a helpful assistant."):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        "stream": False
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
if __name__ == "__main__":
    print("DeepSeek Chat Interface")
    print("-" * 40)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit', 'q']:
            break
            
        response = chat(user_input)
        print(f"\nDeepSeek: {response}")
```

Run it:
```bash
python chat.py
```

### 3. Local Model Usage

For local model inference:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model
model_name = "deepseek-ai/deepseek-coder-1.3b-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_code(prompt, max_length=200):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        temperature=0.7,
        do_sample=True,
        top_p=0.95
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example
code = generate_code("def calculate_fibonacci(n):")
print(code)
```

## Troubleshooting

### Common Issues

#### 1. Installation Fails

**Problem**: Package installation fails with errors

**Solutions**:
```bash
# Clear package cache
pkg clean

# Update repositories
pkg update

# Try installing packages one by one
pkg install -y python
pkg install -y python-pip
pkg install -y git
```

#### 2. Python Package Installation Fails

**Problem**: `pip install` fails with compilation errors

**Solutions**:
```bash
# Install build dependencies
pkg install -y clang cmake ninja

# Use pre-built wheels when available
pip install --prefer-binary numpy

# For torch issues, use CPU-only version
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

#### 3. Out of Memory Errors

**Problem**: Model fails to load due to insufficient memory

**Solutions**:
- Use smaller models (1.3B parameter version)
- Use API instead of local models
- Enable memory optimization:
  ```python
  model = AutoModelForCausalLM.from_pretrained(
      model_name,
      torch_dtype=torch.float16,
      low_cpu_mem_usage=True,
      device_map="auto"
  )
  ```

#### 4. API Connection Issues

**Problem**: Cannot connect to DeepSeek API

**Solutions**:
```bash
# Check if API key is set
echo $DEEPSEEK_API_KEY

# Test internet connection
ping -c 4 api.deepseek.com

# Check curl installation
pkg install -y curl

# Verify API key is valid
curl -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  https://api.deepseek.com/v1/models
```

#### 5. Permission Denied Errors

**Problem**: Cannot execute scripts

**Solutions**:
```bash
# Make scripts executable
chmod +x install-deepseek.sh
chmod +x ~/deepseek/*.sh

# Check file permissions
ls -la ~/deepseek/
```

### Storage Issues

If you're running out of storage:

```bash
# Clean pip cache
pip cache purge

# Clean pkg cache
pkg clean

# Remove unnecessary packages
pkg autoremove
```

## FAQ

### Q: Can I use DeepSeek offline?

**A:** Yes, if you download models locally. However, initial model download requires internet. API usage always requires internet connection.

### Q: How much data does API usage consume?

**A:** Approximately 1-5 KB per message, depending on length. Very efficient for mobile data.

### Q: Which approach is better: API or Local?

**A:** For mobile devices, **API is recommended** because:
- Less storage required
- Less RAM usage
- Access to latest models
- Better performance

Local models are good if you need offline access or have privacy concerns.

### Q: Can I use DeepSeek for free?

**A:** DeepSeek offers both free tier and paid plans. Check their pricing at [platform.deepseek.com](https://platform.deepseek.com).

### Q: How do I update DeepSeek?

**A:** For API: Updates are automatic on server side.
For local models:
```bash
pip install --upgrade transformers torch
```

### Q: Can I use DeepSeek with other apps?

**A:** Yes! You can:
- Create API endpoints
- Use it in your Python scripts
- Integrate with Termux-API
- Build custom interfaces

### Q: Is my data secure?

**A:** When using API, data is sent to DeepSeek servers. For sensitive data, use local models. Always review DeepSeek's privacy policy.

### Q: What if I get rate limited?

**A:** API has rate limits. If exceeded:
- Wait for limit reset
- Implement retry logic with delays
- Consider upgrading API plan

### Q: Can I fine-tune models on Termux?

**A:** Fine-tuning requires significant resources and is not recommended on mobile devices. Consider using cloud platforms for fine-tuning.

## Additional Resources

- **DeepSeek Official**: [https://www.deepseek.com](https://www.deepseek.com)
- **DeepSeek GitHub**: [https://github.com/deepseek-ai](https://github.com/deepseek-ai)
- **Termux Wiki**: [https://wiki.termux.com](https://wiki.termux.com)
- **Transformers Docs**: [https://huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)

## Getting Help

If you encounter issues:

1. Check this guide's [Troubleshooting](#troubleshooting) section
2. Search existing issues on this repository
3. Open a new issue with:
   - Termux version
   - Python version (`python --version`)
   - Error messages
   - Steps to reproduce

## Contributing

Found a better way to install or use DeepSeek on Termux? Contributions are welcome! Please submit a pull request with your improvements.

---

**Last Updated**: January 2026
**Version**: 1.0
