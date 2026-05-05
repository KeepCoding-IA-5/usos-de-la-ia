from ollama import chat, ChatResponse

response: ChatResponse = chat(
    model="gemma4:latest",
    messages=[
        {"role": "user", "content": "Di un color que no sea rojo"},
    ],
)

ciudad= response.message.content
response2: ChatResponse = chat(
    model="gemma4:latest",
    messages=[
        {"role": "user", "content": "Si el color que te iondico no es rojo diq ue esta mal, color: "+ ciudad},
    ],
)
print(response2.message.content)