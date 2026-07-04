from colorama import Fore, Style, init

init(autoreset=True)

def name(): return input(f"{Fore.YELLOW}Please enter your{Fore.GREEN} name{Fore.YELLOW}: {Fore.BLUE}")

def mood(name):
    mood = input(Fore.YELLOW + f"How is your {Fore.GREEN}mood{Fore.YELLOW} today? {Fore.BLUE}").lower()

    if "good" in mood: print(Fore.YELLOW + f"Wish you a happy day ahead, {name}! 😊")
    elif "bad" in mood: print(Fore.YELLOW + f"Hope your day gets better soon, {name}!")
    else: print(Fore.YELLOW + f"I understand, {name}.")

def hobby():
    hobby = input(Fore.YELLOW + f"What is {Fore.GREEN}a favorite hobby{Fore.YELLOW} of yours?{Fore.BLUE} ").upper()
    print(Fore.GREEN + hobby + Fore.YELLOW + " is a nice hobby of yours!")

def chat_again():
    while True:
        chat_again = input(Fore.YELLOW + f"Do you want to chat again? ({Fore.GREEN}yes{Fore.YELLOW}/{Fore.RED}no{Fore.YELLOW}) " + Fore.BLUE).lower().strip()
        if chat_again == "yes": return True
        elif chat_again == "no": return False 
        else: print(Fore.RED + f"Invalid response. {Fore.YELLOW}Please enter one of the responses shown in the question above.")   

def main():
    while True:
        print(Fore.YELLOW + f"Welcome to {Fore.GREEN}tAI{Fore.YELLOW}!")
        user_name = name()
        mood(user_name)
        hobby()

        if chat_again() == False: break

    print(Fore.YELLOW + "Thank you for chatting with me!")
    print(f"{Fore.RED}B{Fore.GREEN}y{Fore.BLUE}e{Fore.YELLOW}!")

if __name__ == "__main__": main()