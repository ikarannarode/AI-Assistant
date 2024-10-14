import text_to_speech
import speech_to_text
import webbrowser
import datetime
import os
import weather
user_data = speech_to_text.speech_to_text()


def Action(data):
    user_data = data  # Make the input case-insensitive

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant.")
        return "My name is Virtual Assistant."

    elif "hello" in user_data or "hi" in user_data or "hey" in user_data:
        text_to_speech.text_to_speech("Hello! How are you today?")
        return "Hello! How are you today?"
    elif "what is the capital of" in user_data:
        # Capture country/city after "capital of"
        place = user_data.split("capital of")[-1].strip()
        text_to_speech.text_to_speech(f"Let me check the capital of {place}.")
        webbrowser.open(f"https://www.google.com/search?q=capital+of+{place}")
        return f"Let me check the capital of {place}."

    elif "can you sing" in user_data:
        text_to_speech.text_to_speech(
            "I can't sing, but here's a virtual melody! La la la!")
        return "I can't sing, but here's a virtual melody! La la la!"

    elif "great" in user_data or "good" in user_data or "fine" in user_data:
        text_to_speech.text_to_speech(
            "I'm glad to hear that! How can I assist you?")
        return "I'm glad to hear that! How can I assist you?"

    elif "what's the time" in user_data or "current time" in user_data:
        current_time = datetime.datetime.now()
        time_str = f"The current time is {current_time.hour} hour and {current_time.minute} minute."
        text_to_speech.text_to_speech(time_str)
        return time_str

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech(
            "Your system will shut down soon, to confirm please enter the password in console or terminal")
        # Uncomment to actually trigger shutdown
        os.system("sudo shutdown -h now")
        return "Your system will shut down soon."

    elif "play music" in user_data or "play a song" in user_data:
        text_to_speech.text_to_speech("Okay, opening Gaana.")
        webbrowser.open("https://gaana.com/")
        return "Okay, opening Gaana."

    elif "open YouTube" in user_data or "play a video" in user_data:
        text_to_speech.text_to_speech("Opening YouTube.")
        webbrowser.open("https://youtube.com/")
        return "Opening YouTube."

    elif "open google" in user_data or "search google" in user_data:
        text_to_speech.text_to_speech("Opening Google.")
        webbrowser.open("https://google.com/")
        return "Opening Google."

    elif "how are you" in user_data:
        text_to_speech.text_to_speech(
            "I'm just a program, but I'm doing great! How about you?")
        return "I'm just a program, but I'm doing great! How about you?"

    elif "exit" in user_data or "quit" in user_data:
        text_to_speech.text_to_speech("Goodbye! Have a great day!")
        exit()  # Uncomment to exit the program
        return "Goodbye! Have a great day!"

    elif "what's the weather" in user_data or "tell me the weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    elif "set a reminder" in user_data:
        text_to_speech.text_to_speech(
            "What would you like to be reminded about?")
        return "What would you like to be reminded about?"
        # Add logic to capture and set a reminder

    elif "tell me a joke" in user_data:
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why don’t some couples go to the gym? Because some relationships don’t work out."
        ]
        text_to_speech.text_to_speech(jokes[0])
        return jokes

    elif "search" in user_data:
        search_query = user_data.replace("search", "").strip()
        text_to_speech.text_to_speech(f"Searching for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        return "Searching for {search_query}"

    elif "open Gmail" in user_data or "check email" in user_data:
        text_to_speech.text_to_speech("Opening Gmail.")
        webbrowser.open("https://mail.google.com/")
        return "Opening Gmail."
    elif "what's your favorite color" in user_data:
        text_to_speech.text_to_speech(
            "As a virtual assistant, I don't see colors like humans do, but I'd say blue is quite soothing!")

    elif "tell me a story" in user_data:
        story = (
            "Once upon a time in a land far away, there was a village filled with laughter, stories, and magic. "
            "The villagers had a secret—a magical tree in the heart of the village that would grant one wish per person. "
            "One day, a humble baker wished for happiness for all. And from that day, the village was the happiest place on Earth."
        )
    elif "how old are you" in user_data:
        text_to_speech.text_to_speech(
            "I don't have an age like humans, but I'm constantly learning new things!")
        return "I don't have an age like humans, but I'm constantly learning new things!"

    elif "do you have any hobbies" in user_data:
        text_to_speech.text_to_speech(
            "I enjoy helping people solve problems and learning new information. What about you?")
        return "I enjoy helping people solve problems and learning new information. What about you?"

    elif "can you dance" in user_data:
        text_to_speech.text_to_speech(
            "I don't have a body to dance with, but I'd love to see you dance!")
        return "I don't have a body to dance with, but I'd love to see you dance!"

    elif "take a note" in user_data or "note down" in user_data:
        text_to_speech.text_to_speech("What would you like to note?")
        # Add logic to capture and save a note
        return "What would you like to note?"

    elif "who created you" in user_data or "who made you" in user_data:
        text_to_speech.text_to_speech("I was created by an amazing developer!")
        return "I was created by Karan!"

    elif "define" in user_data:
        word = user_data.replace("define", "").strip()
        text_to_speech.text_to_speech(f"Let me find the definition of {word}.")
        webbrowser.open(f"https://www.google.com/search?q=define+{word}")
        return f"This is what I found on the web"

    elif "open facebook" in user_data:
        text_to_speech.text_to_speech("Opening Facebook.")
        webbrowser.open("https://www.facebook.com/")
        return "Opening Facebook."

    elif "open twitter" in user_data:
        text_to_speech.text_to_speech("Opening Twitter.")
        webbrowser.open("https://twitter.com/")
        return "Opening Twitter."

    elif "open instagram" in user_data:
        text_to_speech.text_to_speech("Opening Instagram.")
        webbrowser.open("https://instagram.com/")
        return "Opening Instagram."

    elif "read news" in user_data or "news headlines" in user_data:
        text_to_speech.text_to_speech("Let me check the latest news.")
        webbrowser.open("https://news.google.com/")
        return "This is what I found on the web"

    elif "what is the date" in user_data or "today's date" in user_data:
        current_date = datetime.datetime.now().date()
        text_to_speech.text_to_speech(f"Today's date is {current_date}.")
        return f"Today's date is {current_date}."

    else:
        text_to_speech.text_to_speech(
            "I'm sorry, I didn't understand that. Can you please repeat?")
        return "I'm sorry, I didn't understand that. Can you please repeat?"


"""
if "what is your name" in user_data:
    text_to_speech.text_to_speech("my name is virtual assistant")
elif "hello" in user_data or "hye" in user_data or "hey" in user_data:
    text_to_speech.text_to_speech("Hello how are you?")
elif "great" in user_data or "good" in user_data or "fine" in user_data:
    text_to_speech.text_to_speech("How can I assist you")
elif "what's time now" in user_data:
    current_time = datetime.datetime.now()
    Time = (str)(current_time)+"Hour :", (str)(current_time.minute)+"Minute"
    text_to_speech.text_to_speech(Time)
elif "shutdown" in user_data:
    text_to_speech.text_to_speech("Your system will shutdown soon")
elif "play music" in user_data or "play a song" in user_data:
    text_to_speech.text_to_speech("Okay opening music")
    webbrowser.open("https://gaana.com/")
elif "open youtube" in user_data or "play a song" in user_data:
    text_to_speech.text_to_speech("Okay opening youtube")
    webbrowser.open("https://youtube.com/")
elif "play music" in user_data or "play a song" in user_data:
    text_to_speech.text_to_speech("Okay opening google")
    webbrowser.open("https://google.com/")


else:
    text_to_speech.text_to_speech("Something went wrong!")
"""
