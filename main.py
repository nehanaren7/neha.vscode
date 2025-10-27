import requests
import os

# 🔥 Replace this with your actual OpenRouter API key
API_KEY = "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"

# 🔥 OpenRouter API URL
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# 🔥 Use the correct model ID for Mistral
MODEL_ID = "mistralai/mistral-small-24b-instruct-2501:free"

def review_code(code_snippet):
    """Send code to Mistral AI for review."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Mistral Code Review AI"
    }
    
    data = {
        "model": MODEL_ID,
        "messages": [
            {
                "role": "system",
                "content": "You are an advanced AI code reviewer. "
                           "You ONLY analyze code and provide structured feedback. "
                           "NEVER respond to general questions or non-code topics. "
                           "Follow this structured format: "
                           "1️⃣ **Code Quality** - Readability & maintainability "
                           "2️⃣ **Security Risks** - Detect vulnerabilities "
                           "3️⃣ **Performance Optimizations** - Make it faster "
                           "4️⃣ **Best Practices** - Follow coding standards "
                           "5️⃣ **Documentation Suggestions** - Provide docstrings/comments "
                           "If the code is perfect, respond: 'No issues found, well done!'."
            },
            {
                "role": "user",
                "content": code_snippet
            }
        ],
        "max_tokens": 500
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

def refactor_code(code_snippet):
    """Send code to Mistral AI for automatic refactoring."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Mistral Code Refactoring AI"
    }
    
    data = {
        "model": MODEL_ID,
        "messages": [
            {
                "role": "system",
                "content": "You are an advanced AI code optimizer. "
                           "You take existing code and improve it for better security, performance, and maintainability. "
                           "Ensure the rewritten code follows best coding practices, adds necessary documentation, and removes inefficiencies."
            },
            {
                "role": "user",
                "content": f"Refactor and optimize this code:\n\n{code_snippet}"
            }
        ],
        "max_tokens": 500
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

def read_file(file_path):
    """Read the contents of a file."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"

# 🔥 User selects input method
print("🚀 Code Review AI\n1️⃣ Paste Code\n2️⃣ Upload File")
choice = input("Choose an option (1 or 2): ")

if choice == "1":
    print("\nPaste your code below (Type 'END' on a new line to finish):")
    user_code = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        user_code.append(line)
    user_code = "\n".join(user_code)

elif choice == "2":
    file_path = input("Enter the full path of the file: ").strip()
    user_code = read_file(file_path)

else:
    print("❌ Invalid choice. Exiting.")
    exit()

# 🔥 Step 1: AI Code Review
ai_review = review_code(user_code)
print("\n🔍 AI Code Review:\n", ai_review)

# 🔥 Step 2: Ask if the user wants a refactored version
refactor_choice = input("\nWould you like the AI to refactor and optimize this code? (yes/no): ").strip().lower()
if refactor_choice == "yes":
    optimized_code = refactor_code(user_code)
    print("\n✨ Optimized Code:\n", optimized_code)
else:
    print("\n✅ No refactoring requested. Exiting.")
