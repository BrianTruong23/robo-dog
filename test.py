

import replicate

import os

os.environ["REPLICATE_API_TOKEN"] = "r8_MU9HaMR9TIuM0sawmOodozfI6Lh3E5e3EfbnJ"

# Prompts
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "What is Python?"
# token = 'r8_MU9HaMR9TIuM0sawmOodozfI6Lh3E5e3EfbnJ'

# Generate LLM response
# output = replicate.run(
#     'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
#     input={
#         "prompt": f"{pre_prompt} {prompt_input} Assistant: {token}",
#         "temperature": 0.1,
#         "top_p": 0.9,
#         "max_length": 300,
#         "repetition_penalty": 1
#     }
# )


# Pre-prompt, User's input, and tokens
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "What is Streamlit?"



# Generate LLM response
output = replicate.run(
    'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
    input={
        "top_p": 1,
        "prompt": f"{pre_prompt} User: {prompt_input} \nAssistant:",
        "max_length": 500,
        "temperature": 0.75,
        "repetition_penalty": 1
    }
)
print(output)

full_response = ""

for item in output:
  full_response += item

print(full_response)