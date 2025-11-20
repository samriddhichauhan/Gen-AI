from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "sshleifer/tiny-gpt2"

print("Loading model… this may take a few minutes. Please wait!")

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map={"": "cpu"},
    low_cpu_mem_usage=True
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.eos_token_id

print("Chatbot ready! Type 'exit' to stop.\n")

while True:
    prompt = input("You: ")
    if prompt.lower().strip() == "exit":
        print("Bot: Bye 👋")
        break

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        pad_token_id=tokenizer.pad_token_id,
    )

    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Bot:", reply, "\n")
