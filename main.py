from modules.chatbot import WellnessBot
from modules.mood_tracker import log_mood, plot_mood
from modules.journal import write_journal, read_journals
from modules.sentiment import analyze_sentiment

print("🌿 Welcome to Your Mental Wellness Companion")
bot = WellnessBot()

while True:
    user_input = input("\n🗣️ You: ")
    if user_input.lower() == "exit":
        print("👋 Take care!")
        break

    if user_input.lower().startswith("mood "):
        try:
            mood_value = int(user_input.split()[1])
            log_mood(mood_value)
            print("✅ Mood saved.")
        except:
            print("⚠️ Use: mood [1-10]")
        continue

    elif user_input.lower() == "show mood":
        plot_mood()
        continue

    elif user_input.lower().startswith("journal "):
        entry = user_input[8:]
        write_journal(entry)
        sentiment = analyze_sentiment(entry)
        print(f"🧠 Sentiment: {sentiment}")
        continue

    elif user_input.lower() == "read journal":
        read_journals()
        continue

    response = bot.get_response(user_input)
    print(f"🤖 Bot: {response}")