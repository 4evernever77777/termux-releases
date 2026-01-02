#!/usr/bin/env python3
"""
Enhanced DeepSeek Chat Interface for Termux
A user-friendly chat interface for interacting with DeepSeek AI
"""

import os
import sys
import json

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import requests
        return True
    except ImportError:
        print("Error: 'requests' package not found.")
        print("Install it with: pip install requests")
        return False

def print_banner():
    """Display welcome banner"""
    print("\n" + "=" * 50)
    print("       DeepSeek Chat Interface v1.0")
    print("=" * 50)
    print()

def print_help():
    """Display help message"""
    print("Commands:")
    print("  /help    - Show this help message")
    print("  /clear   - Clear conversation history")
    print("  /exit    - Exit the chat")
    print("  /model   - Show current model")
    print("  /system  - Change system prompt")
    print()

class DeepSeekChat:
    def __init__(self):
        self.api_key = os.environ.get('DEEPSEEK_API_KEY')
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.model = "deepseek-chat"
        self.conversation_history = []
        self.system_prompt = "You are a helpful AI assistant."
        
        if not self.api_key:
            print("Warning: DEEPSEEK_API_KEY environment variable not set")
            print("Please set it up using: ./setup_api.sh")
            print("Or manually: export DEEPSEEK_API_KEY='your-key-here'")
            sys.exit(1)
    
    def send_message(self, message, stream=False):
        """Send a message to DeepSeek API"""
        try:
            import requests
        except ImportError:
            print("Error: 'requests' package not installed")
            print("Install with: pip install requests")
            return None
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.conversation_history)
        messages.append({"role": "user", "content": message})
        
        data = {
            "model": self.model,
            "messages": messages,
            "stream": stream,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                assistant_message = result['choices'][0]['message']['content']
                
                # Add to conversation history
                self.conversation_history.append({"role": "user", "content": message})
                self.conversation_history.append({"role": "assistant", "content": assistant_message})
                
                # Keep only last 10 exchanges to avoid token limits
                if len(self.conversation_history) > 20:
                    self.conversation_history = self.conversation_history[-20:]
                
                return assistant_message
            else:
                return f"Error {response.status_code}: {response.text}"
                
        except requests.exceptions.Timeout:
            return "Error: Request timed out. Please try again."
        except requests.exceptions.ConnectionError:
            return "Error: Cannot connect to API. Check your internet connection."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("Conversation history cleared.")
    
    def change_system_prompt(self, new_prompt):
        """Change the system prompt"""
        self.system_prompt = new_prompt
        print(f"System prompt updated to: {new_prompt}")
    
    def run(self):
        """Run the interactive chat loop"""
        print_banner()
        print(f"Using model: {self.model}")
        print("Type /help for commands, /exit to quit")
        print("-" * 50)
        print()
        
        while True:
            try:
                user_input = input("\n\033[1;36mYou:\033[0m ")
                
                if not user_input.strip():
                    continue
                
                # Handle commands
                if user_input.startswith('/'):
                    command = user_input.lower().strip()
                    
                    if command == '/exit' or command == '/quit':
                        print("\nGoodbye! 👋")
                        break
                    elif command == '/help':
                        print_help()
                        continue
                    elif command == '/clear':
                        self.clear_history()
                        continue
                    elif command == '/model':
                        print(f"Current model: {self.model}")
                        continue
                    elif command.startswith('/system'):
                        new_prompt = input("Enter new system prompt: ")
                        if new_prompt.strip():
                            self.change_system_prompt(new_prompt.strip())
                        continue
                    else:
                        print(f"Unknown command: {command}")
                        print("Type /help for available commands")
                        continue
                
                # Send message to API
                print("\n\033[1;32mDeepSeek:\033[0m ", end="", flush=True)
                response = self.send_message(user_input)
                
                if response:
                    print(response)
                else:
                    print("Failed to get response")
                    
            except KeyboardInterrupt:
                print("\n\nInterrupted. Type /exit to quit or continue chatting.")
                continue
            except EOFError:
                print("\n\nGoodbye! 👋")
                break

def main():
    """Main entry point"""
    if not check_dependencies():
        sys.exit(1)
    
    chat = DeepSeekChat()
    chat.run()

if __name__ == "__main__":
    main()
