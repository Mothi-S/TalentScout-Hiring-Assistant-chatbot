from ctransformers import AutoModelForCausalLM

def load_llm():
    llm = AutoModelForCausalLM.from_pretrained(
        "models/llama-2-7b-chat.ggmlv3.q8_0.bin",  # ✅ this is the model_path_or_repo_id
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5
    )
    return llm
