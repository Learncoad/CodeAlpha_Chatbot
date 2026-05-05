# Basic Chatbot

def Response(userInput):
    userInput = userInput.lower().strip()

    #greeting
    if userInput in ["hello",'hi','hey']:
        return "Hi!!"
    
    #asking about bot
    elif userInput in ["how are you", "how are you doing"]:
        return "I'm fine, thanks!"
    
    #name
    elif "your name" in userInput:
        return "I am a simple chatbot."
    
    #help
    elif "help" in userInput:
        return "You can say hello, ask how I am, or type bye to exit."
    
    #exit
    elif userInput in ["bye", "exit", "quit"]:
        return "Goodbye!"
    
    #fallback
    else:
        return "Sorry, I didn't understand that."
    
def Chatbot():
    print("Chatbot: Hi! Type something (type 'bye' to 'exit')")

    while True:
        userinput = input("You: ")

        response = Response(userinput)
        print("Chatbot: ", response)

        if userinput.lower() in ['bye','exit','quit']:
            break

if __name__ == '__main__':
    Chatbot()
