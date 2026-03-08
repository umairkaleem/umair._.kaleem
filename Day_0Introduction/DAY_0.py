# print ("hello world")
# print ('''  "Ain’t got nobody in all this world,
#        Ain’t got nobody but ma self.
#        I’s gwine to quit ma frownin’
#        And put ma troubles on the shelf." ''')



    #    question---3
import platform
print(platform.architecture())
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()





#pyjokes is a library to get random jokes
# To use it, you need to install the library first using pip:


import pyjokes
joke = pyjokes.get_joke()
print(joke)