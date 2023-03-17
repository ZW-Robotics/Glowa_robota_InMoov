from adafruit_servokit import ServoKit
from guizero import App, Slider, Text

servo_kit = ServoKit(channels=16)

def oczy_poziom(angle):
    servo_kit.servo[0].angle = int(angle) + 90

def oczy_pion(angle):
    servo_kit.servo[1].angle = int(angle) + 90

def szczęka(angle):
    servo_kit.servo[2].angle = int(angle) + 90

def głowa_poziom(angle):
    servo_kit.servo[3].angle = int(angle) + 90

def głowa_pion(angle):
    servo_kit.servo[4].angle = int(angle) + 90

app = App(title='Sterowanie serwomechanizmami InMoov', width=500, height=400)

text = Text(app, text="Oczy poziom")
slider = Slider(app, start=-90, end=90, command=oczy_poziom, width=300, height=25).text_size = 10

text = Text(app, text="Oczy pion")
slider = Slider(app, start=-90, end=90, command=oczy_pion, width=300, height=25).text_size = 10

text = Text(app, text="Szczęka")
slider = Slider(app, start=-90, end=90, command=szczęka, width=300, height=25).text_size = 10

text = Text(app, text="Głowa poziom")
slider = Slider(app, start=-90, end=90, command=głowa_poziom, width=300, height=25).text_size = 10

text = Text(app, text="Głowa pion")
slider = Slider(app, start=-90, end=90, command=głowa_pion, width=300, height=25).text_size = 10

app.display()

