#!/usr/bin/env python3
"""
Local DeepSeek Model Usage Example
This script demonstrates how to use DeepSeek models locally on Termux
"""

import sys
import os

# Configuration constants
MODEL_OPTIONS = {
    "lightweight": "deepseek-ai/deepseek-coder-1.3b-base",
    "medium": "deepseek-ai/deepseek-coder-6.7b-base"
}
DEFAULT_MODEL = MODEL_OPTIONS["lightweight"]

# Generation parameters
MAX_LENGTH_EXAMPLE = 150
MAX_LENGTH_INTERACTIVE = 200
TEMPERATURE = 0.7
TOP_P = 0.95

def check_dependencies():
    """Check if required packages are installed"""
    missing = []
    
    try:
        import torch
    except ImportError:
        missing.append("torch")
    
    try:
        import transformers
    except ImportError:
        missing.append("transformers")
    
    if missing:
        print("Error: Missing required packages:", ", ".join(missing))
        print("\nInstall them with:")
        print(f"  pip install {' '.join(missing)}")
        return False
    
    return True

def main():
    """Main function to demonstrate local model usage"""
    print("=" * 60)
    print("  DeepSeek Local Model Example")
    print("=" * 60)
    print()
    
    if not check_dependencies():
        sys.exit(1)
    
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
    
    print("This example shows how to use DeepSeek models locally.")
    print()
    print("Note: First run will download the model (may take significant time)")
    print("Recommended models for mobile devices:")
    print(f"  1. {MODEL_OPTIONS['lightweight']} (Lightweight)")
    print(f"  2. {MODEL_OPTIONS['medium']} (Medium, needs 8GB+ RAM)")
    print()
    
    # Use lightweight model by default
    model_name = DEFAULT_MODEL
    
    print(f"Model: {model_name}")
    print()
    
    choice = input("Download and use this model? (y/n): ").strip().lower()
    
    if choice != 'y':
        print("\nTo use a different model, edit this script and change 'model_name'")
        print("Or use the API approach (recommended for mobile)")
        return
    
    print("\nLoading model... (this may take several minutes)")
    print("Please be patient...")
    
    try:
        # Load tokenizer
        print("Loading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Load model with optimizations for mobile
        print("Loading model...")
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,  # Use half precision
            low_cpu_mem_usage=True,
            device_map="auto"
        )
        
        print("\n✓ Model loaded successfully!")
        print()
        
        # Example usage
        print("=" * 60)
        print("Example: Code Generation")
        print("=" * 60)
        print()
        
        prompt = "def calculate_fibonacci(n):\n    "
        print(f"Prompt: {prompt}")
        print("\nGenerating code...\n")
        
        inputs = tokenizer(prompt, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=MAX_LENGTH_EXAMPLE,
                temperature=TEMPERATURE,
                do_sample=True,
                top_p=TOP_P,
                pad_token_id=tokenizer.eos_token_id
            )
        
        generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print("Generated code:")
        print("-" * 60)
        print(generated_code)
        print("-" * 60)
        print()
        
        # Interactive mode
        print("\nInteractive Mode")
        print("Type your code prompt (or 'exit' to quit):")
        print()
        
        while True:
            try:
                user_prompt = input("\nPrompt: ").strip()
                
                if user_prompt.lower() in ['exit', 'quit', 'q']:
                    break
                
                if not user_prompt:
                    continue
                
                inputs = tokenizer(user_prompt, return_tensors="pt")
                
                with torch.no_grad():
                    outputs = model.generate(
                        **inputs,
                        max_length=MAX_LENGTH_INTERACTIVE,
                        temperature=TEMPERATURE,
                        do_sample=True,
                        top_p=TOP_P,
                        pad_token_id=tokenizer.eos_token_id
                    )
                
                result = tokenizer.decode(outputs[0], skip_special_tokens=True)
                print("\nGenerated:")
                print("-" * 60)
                print(result)
                print("-" * 60)
                
            except KeyboardInterrupt:
                print("\n\nInterrupted. Type 'exit' to quit.")
                continue
        
        print("\nGoodbye!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Ensure you have enough storage (10GB+ free)")
        print("2. Ensure you have enough RAM (4GB+ recommended)")
        print("3. Try using the API approach instead (see README.md)")
        print("4. Check internet connection for model download")
        sys.exit(1)

if __name__ == "__main__":
    main()
