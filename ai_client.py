import ollama

response = ollama.chat(
    model="qwen2.5-coder:latest",
    messages=[
        {
            "role": "user",
            "content": "Hello! Tell me what you can do."
        }
    ]
)

print(response["message"]["content"])
import ollama

response = ollama.chat(
    model="qwen2.5-coder:latest",
    messages=[
        {
            "role": "user",
            "content": "Say only: Hello Jyoti, your AI is working."
        }
    ]
)

print(response["message"]["content"])
