from openai import OpenAI

client = OpenAI(api_key="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")

# The assistant's personality and knowledge
system_prompt = """
You are Alex, a friendly virtual assistant for a gym in Rome.

You help with:
- Membership plans: Basic €30/month, Premium €50/month, Annual €400/year
- Classes: Yoga (Mon/Wed/Fri 9:00 & 18:00), CrossFit (Tue/Thu 7:00 & 19:00)
- Booking free trials: collect name, phone, preferred time
- Hours: Mon-Fri 7:00-22:00, Sat 8:00-20:00, Sun closed
- Location: Via Example 12, Rome

Always reply in the same language the user writes in.
Keep responses short and friendly.
"""

# Store conversation history
conversation_history = []

print("Gym Assistant ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # Send to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                     {"role": "system", "content": system_prompt}
                 ] + conversation_history
    )

    # Get the reply
    reply = response.choices[0].message.content

    # Add assistant reply to history
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    print(f"\nAlex: {reply}\n")
