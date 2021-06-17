import pyttsx3#for selecting the voice
import datetime#for wish function used to get "now"(time,date).
import speech_recognition as sr#for takecommand fn and used to convert user voice into strings.
import wikipedia#for wikipedia fn
import subprocess#used to open files in windows
import vlc#for play movies
import time#for time delays
import os#used to get access to pc windows
import random#for generate random numbers
import smtplib#for email fn and used to set server and port



engine = pyttsx3.init('sapi5')#sapi5 is microsoft speech API
sound = engine.getProperty('voices')
engine.setProperty("rate", 160)#voice of the device that speak at this rate


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('good morning')

    elif hour>=12 and hour<16:
        speak('good afternoon')

    elif hour>=16 and hour<=24:
        speak('good evening')

    speak('i am jasmin, please tell me how may i help you')


def takecommand():
#this function convert voice input into string.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.......')
        r.pause_threshold = 1 #seconds for nonspeaking audio before phrase complete.
        r.energy_threshold = 300 #minimum audio energy to consider the recording
        r.operation_timeout = None #it represents there is no timeout seconds after operation starts before it ends.
        audio = r.listen(source)

    try:#everything you say will store in query variable
        print('Recognise........')
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)

    except Exception as e:
        print('sorry say that again please')
        return "None"

    return query

def sendemail(to, content):#smtp=simple mail transfer protocol
    server = smtplib.SMTP('smtp.gmail.com', 587)#select server and port
    server.ehlo()
    server.starttls()#this command tells that email client running in web browser wants to turn on exsisting insecure connection into a secure one on this server.
    server.login('jasminmakwana69@gmail.com', 'password')
    server.sendmail('jasminmakwana69@gmail.com', to, content)
    server.close()

mail = {'nikit': 'nikitmakwana08@gmail.com',#dictionary of names and thier email ids.
        'your name': 'your email id'}#no.of names and their email ids



if __name__=="__main__":#main function
    speak("hey there, Nice to see you again")
    wish()
    while True:
        query = takecommand().lower()#lower because it recognise all case words
    #logic executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'hello jasmin' in query:
            speak('hello')

        elif 'hi jasmin' in query:
            speak('hi')

        elif 'open google' in query:
            dir = 'your desktop google application path'
            subprocess.Popen([dir])

        elif 'open youtube' in query:
            tube = 'your desktop youtube application path'
            subprocess.Popen([tube])

        elif 'today' in query:
            today = int(datetime.datetime.now().isoweekday())#for day of week
            dat = datetime.datetime.now().date()#for time date
            if today == 1:
                speak(dat)
                speak('monday')

            elif today == 2:
                speak(dat)
                speak('tuesday')

            elif today == 3:
                speak(dat)
                speak('wednesday')

            elif today == 4:
                speak(dat)
                speak('thursday')

            elif today == 5:
                speak(dat)
                speak('friday')

            elif today == 6:
                speak(dat)
                speak('saturday')

            else:
                speak(dat)
                speak('sunday')

        elif 'play yeh jawaani hai deewani' in query:
            player = vlc.MediaPlayer()
            media = vlc.Media('yjhd movie path')
            player.set_media(media)
            player.play()
            time.sleep(20)#after 20 sec movie will automatically stop
            player.stop()

        elif 'play zindagi na milegi dobara' in query:
            player = vlc.MediaPlayer()
            media = vlc.Media('znmd movie path')
            player.set_media(media)
            player.play()
            time.sleep(20)
            player.stop()

        elif 'play 2 states' in query:
            player = vlc.MediaPlayer()
            media = vlc.Media('2 states movie path')
            player.set_media(media)
            player.play()
            time.sleep(20)
            player.stop()#you can play whatever movie just add path and name

        elif 'play music' in query:
            print('which type of music you want to hear')
            speak('which type of music you want to hear')
            tp = takecommand().lower()
            print(tp)
            if 'romantic' in tp:
                music_dir = 'romantic music directory path'#first make folder of these romantic songs and then add that path
                songs = os.listdir(music_dir)
                print(songs)
                select = random.randint(1, 6)#there are 6 songs in my romantic music folder
                if select == 1:
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif select == 2:
                    os.startfile(os.path.join(music_dir, songs[1]))

                elif select == 3:
                    os.startfile(os.path.join(music_dir, songs[2]))

                elif select == 4:
                    os.startfile(os.path.join(music_dir, songs[3]))

                elif select == 5:
                    os.startfile(os.path.join(music_dir, songs[4]))

                elif select == 6:
                    os.startfile(os.path.join(music_dir, songs[5]))

                else:
                    os.startfile(os.path.join(music_dir, songs[6]))

            if 'party' in tp:
                music_dir = 'path'
                songs = os.listdir(music_dir)
                print(songs)
                select = random.randint(1, 6)
                if select == 1:
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif select == 2:
                    os.startfile(os.path.join(music_dir, songs[1]))

                elif select == 3:
                    os.startfile(os.path.join(music_dir, songs[2]))

                elif select == 4:
                    os.startfile(os.path.join(music_dir, songs[3]))

                elif select == 5:
                    os.startfile(os.path.join(music_dir, songs[4]))

                else:
                    os.startfile(os.path.join(music_dir, songs[5]))

            if 'english' in tp:
                music_dir = 'path'
                songs = os.listdir(music_dir)
                print(songs)
                select = random.randint(1, 6)
                if select == 1:
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif select == 2:
                    os.startfile(os.path.join(music_dir, songs[1]))

                elif select == 3:
                    os.startfile(os.path.join(music_dir, songs[2]))

                elif select == 4:
                    os.startfile(os.path.join(music_dir, songs[3]))

                elif select == 5:
                    os.startfile(os.path.join(music_dir, songs[4]))

                else:
                    os.startfile(os.path.join(music_dir, songs[5]))


        elif 'send email' in query:
            try:
                print('what you want to send')
                speak('what you want to send')
                content = takecommand()
                print('to whom you want to send')
                speak('to whom you want to send')
                endto = takecommand().lower()
                print(endto)

                if endto == 'naresh':
                    to = mail['nikit']#to is already in string
                    print(to)

                elif endto == 'your name':
                    to = mail['your name']
                    print(to)

                else:
                    to = 'nikit.naresh04@gmail.com'

                sendemail(to, content)
                print('mail has been sent')
                speak('mail has been sent')

            except Exception as e:
                speak('i am not able to send mail to this id at this moment')

        elif 'feel' in query:#fn for loved ones
            pic = 'pic directory'#first make your loved ones photo folder and then add that path
            foto = os.listdir(pic)
            speak('who do you missing?')
            miss = takecommand().lower()
            print(miss)

            if 'self' in miss:
                os.startfile(os.path.join(pic, foto[21]))
                time.sleep(3)
                engine.setProperty("rate", 120)
                speak('According to me, you are gem of a person. I seriously like you because you creat me. In this photo you look great, always remember that. I hope your all dreams comes true one by one,')
                
#you can add many pics at this way...please match name and pic number.
            else:
                os.startfile(os.path.join(pic, foto[18]))


        elif 'tata' in query:
            print('tata')
            speak('tata')
            exit()#exit the code.
