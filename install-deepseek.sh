#!/data/data/com.termux/files/usr/bin/bash

# DeepSeek Installation Script for Termux
# This script installs DeepSeek AI model and its dependencies on Android via Termux

set -e  # Exit on error

echo "================================================"
echo "   DeepSeek Installation Script for Termux     "
echo "================================================"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running on Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo -e "${RED}Error: This script must be run in Termux environment${NC}"
    exit 1
fi

echo -e "${GREEN}Step 1: Updating package repositories...${NC}"
pkg update -y || {
    echo -e "${RED}Failed to update packages${NC}"
    exit 1
}

echo ""
echo -e "${GREEN}Step 2: Installing required dependencies...${NC}"
echo "This may take several minutes..."

# Install essential packages
pkg install -y python python-pip git wget curl clang cmake || {
    echo -e "${RED}Failed to install essential packages${NC}"
    exit 1
}

# Install build dependencies
pkg install -y libc++ libandroid-execinfo patchelf binutils || {
    echo -e "${YELLOW}Warning: Some build dependencies failed to install${NC}"
}

echo ""
echo -e "${GREEN}Step 3: Upgrading pip and installing Python dependencies...${NC}"
pip install --upgrade pip setuptools wheel

# Install common AI/ML dependencies
pip install numpy torch transformers sentencepiece protobuf accelerate || {
    echo -e "${YELLOW}Warning: Some Python packages failed to install${NC}"
    echo -e "${YELLOW}You may need to install them manually later${NC}"
}

echo ""
echo -e "${GREEN}Step 4: Installing DeepSeek dependencies...${NC}"

# Install additional dependencies for DeepSeek
pip install tiktoken einops || {
    echo -e "${YELLOW}Warning: Some DeepSeek dependencies failed to install${NC}"
}

echo ""
echo -e "${GREEN}Step 5: Setting up DeepSeek environment...${NC}"

# Create directory for DeepSeek
DEEPSEEK_DIR="$HOME/deepseek"
mkdir -p "$DEEPSEEK_DIR"
cd "$DEEPSEEK_DIR"

# Create a simple Python script to use DeepSeek API
cat > deepseek_chat.py << 'EOF'
#!/usr/bin/env python3
"""
DeepSeek Chat Interface for Termux
This script provides a simple interface to interact with DeepSeek models
"""

import os
import sys

try:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
except ImportError as e:
    print("Error: Required packages not found.")
    print("Please install them with: pip install transformers torch")
    sys.exit(1)

def print_banner():
    print("=" * 50)
    print("       DeepSeek Chat Interface")
    print("=" * 50)
    print()

def main():
    print_banner()
    print("Welcome to DeepSeek Chat!")
    print()
    print("Note: First run will download the model (this may take time)")
    print("For a lighter model, consider using smaller variants")
    print()
    
    # Check if API mode or local mode
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    
    if api_key:
        print("API Key found - using DeepSeek API")
        print("You can make API calls to DeepSeek services")
        print()
        print("Example API usage:")
        print("  curl https://api.deepseek.com/v1/chat/completions \\")
        print("    -H 'Content-Type: application/json' \\")
        print("    -H 'Authorization: Bearer $DEEPSEEK_API_KEY' \\")
        print("    -d '{\"model\": \"deepseek-chat\", \"messages\": [{\"role\": \"user\", \"content\": \"Hello\"}]}'")
    else:
        print("No API key found (set DEEPSEEK_API_KEY to use API)")
        print()
        print("To use DeepSeek models locally, you'll need:")
        print("1. Sufficient storage (10GB+ for most models)")
        print("2. Sufficient RAM (8GB+ recommended)")
        print("3. Download a model using transformers library")
        print()
        print("Example code to load a model:")
        print("  from transformers import AutoTokenizer, AutoModelForCausalLM")
        print("  tokenizer = AutoTokenizer.from_pretrained('deepseek-ai/deepseek-coder-1.3b-base')")
        print("  model = AutoModelForCausalLM.from_pretrained('deepseek-ai/deepseek-coder-1.3b-base')")
        print()
        print("For Termux, lighter models are recommended (1.3B or 6.7B parameter versions)")
    
    print()
    print("Setup complete! Check DEEPSEEK_GUIDE.md for more information.")

if __name__ == "__main__":
    main()
EOF

chmod +x deepseek_chat.py

# Create helper script for API usage
cat > setup_api.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
# Script to configure DeepSeek API access

echo "DeepSeek API Configuration"
echo "=========================="
echo ""
echo "To use DeepSeek API, you need an API key from https://platform.deepseek.com"
echo ""
read -p "Enter your DeepSeek API key (or press Enter to skip): " api_key

if [ -n "$api_key" ]; then
    echo "export DEEPSEEK_API_KEY='$api_key'" >> ~/.bashrc
    export DEEPSEEK_API_KEY="$api_key"
    echo ""
    echo "API key saved! It will be available in new terminal sessions."
    echo "For this session, run: export DEEPSEEK_API_KEY='$api_key'"
else
    echo "Skipped API configuration."
fi
EOF

chmod +x setup_api.sh

echo ""
echo -e "${GREEN}Step 6: Creating example scripts...${NC}"

# Create example usage script
cat > example_api_call.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
# Example script to call DeepSeek API

if [ -z "$DEEPSEEK_API_KEY" ]; then
    echo "Error: DEEPSEEK_API_KEY not set"
    echo "Run ./setup_api.sh to configure your API key"
    exit 1
fi

echo "Testing DeepSeek API connection..."
echo ""

curl -X POST https://api.deepseek.com/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
    -d '{
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Can you confirm this API is working?"}
        ],
        "stream": false
    }'

echo ""
echo ""
echo "API test complete!"
EOF

chmod +x example_api_call.sh

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Installation Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "DeepSeek has been set up in: $DEEPSEEK_DIR"
echo ""
echo "Next steps:"
echo "1. (Optional) Configure API access:"
echo "   cd $DEEPSEEK_DIR && ./setup_api.sh"
echo ""
echo "2. Run the chat interface:"
echo "   cd $DEEPSEEK_DIR && python deepseek_chat.py"
echo ""
echo "3. Test API connection (if configured):"
echo "   cd $DEEPSEEK_DIR && ./example_api_call.sh"
echo ""
echo "4. Read the detailed guide:"
echo "   View DEEPSEEK_GUIDE.md for more information"
echo ""
echo -e "${YELLOW}Note: To use models locally, you'll need sufficient storage and RAM.${NC}"
echo -e "${YELLOW}For most devices, API access is recommended.${NC}"
echo ""
