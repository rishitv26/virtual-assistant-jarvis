# ---------------- Importing Dependencies: --------------
from functions import *

speak("INITIALIZING JARVIS...")

# ----------------- User Initialization: ---------------
try:
    user = storage('return-data')[0]
except:
    user = ''

if 'user = ' in user:
    greet(user.split()[2])
else:
    speak('Hi, my name is JARVIS, what is your name?')
    username = input('Your name> ')
    print('\n')
    storage('add-data', f'user = {username}')
    user = storage('return-data')[0]
    greet(user.split()[2])

# ----------------- Primary Brain: ----------------

while True:
    query = command()

    if query is None:
        print('')

    # ------------------ Logic: ----------------
    # search wikipedia:

    elif 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.split()
        try:
            results = wikipedia.summary(filter_query(query), sentences=5)
        except:
            results = f'Sorry, could not find results regarding {filter_query(query)}'
        speak(results)

    # open a website using google:

    elif 'open' in query.lower() and '.' in query.lower() and 'google' in query.lower():
        """this function is very specific on what format you say, you must start with: 
        open (whatever website with domain-name) """

        speak(f'Opening {query.split()[1]}...')
        try:
            browse(query.split()[1])
        except:
            speak(f"Sorry, cant open {query.split()[1]}")

    # add people's email in contacts:

    elif 'add' in query.lower() and 'contacts' in query.lower():
        speak("Please type in an email address:")
        email = input('> ')
        speak("Give a convenient name to that email by saying it:")
        while True:
            nickname = command()
            speak('Is this what you would like to name it?')
            next = command()
            if next.lower() == 'yes':
                speak('ok')
                break
            if next.lower() == 'no':
                speak("Give a convenient name to that email by saying it:")
        storage('add-data', f'{nickname} {email}')

    # show saved contacts:

    elif 'show' in query.lower() and 'contacts' in query.lower():
        speak(show_contacts())

    # send emails via gmail:

    elif 'send' in query.lower() and 'mail' in query.lower():
        not_in_contacts = None
        speak('Who would you like to send an email? Please type it out:')
        who = input('(use nicknames from contacts)> ')
        contacts = show_contacts()
        for i in contacts:
            counter = 0
            if who in i:
                send_to = contacts[counter].split()[1]
                not_in_contacts = False
                break
            counter += 1
        if not_in_contacts is None:
            send_to = who

        speak('Your body:')
        body = command().capitalize() + '.'

        speak('Your subject:')
        subject = command()

        send_mail(send_to, body, subject)

    # tell the current time:

    elif 'the time' in query.lower():
        speak(f"Its currently {current_time()}")

    # open pycharm:

    elif 'open pycharm' in query.lower():
        path = 'C:/Program Files/JetBrains/PyCharm Community Edition 2021.1.3/bin/pycharm64.exe'
        speak("Opening Pycharm...")
        os.startfile(path)

    # exit Jarvis:

    elif 'exit' in query.lower() or 'quit' in query.lower():
        speak('Exiting JARVIS...')
        break
