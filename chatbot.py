import openai

openai.api_key = "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"

chat_history = []

while True: 
    prompt = input('Enter a prompt:')

    if prompt == "exit":
        break
    else:

        chat_history.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            stream=True,
            # max_tokens=100,
        )

        collected_messages = []

        for chunk in response:
            chunk_message = chunk["choices"][0]["delta"] # message
            collected_messages.append(chunk_message)
            full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
            print(full_reply_content)
            print("\033[H\033[J", end="")

        chat_history.append({"role": "assistant", "content": full_reply_content})
        print(full_reply_content)


