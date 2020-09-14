from csinscapp import *

app = CSinSCApp()

speech = Label()
speech.x = 10
speech.y = 62
speech.data = "Squirrel?"
speech.width = 100
app.add(speech)

pet = Image()
pet.x = 24
pet.y = 36
pet.data = "images/pet.png"
pet.width = 200
pet.height = 200
app.add(pet)

chatbox = Textbox()
chatbox.x = 10
chatbox.y = 280
chatbox.width = 230
chatbox.height = 18
app.add(chatbox)

submit = Button()
submit.x = 250
submit.y = 280
submit.data = "Chat!"
submit.width = 48
submit.height = 18
app.add(submit)

bow_image = Image()
bow_image.x = 24
bow_image.y = 36
bow_image.data = "images/bow.png"
bow_image.width = 200
bow_image.height = 200
bow_image.visible = False
app.add(bow_image)

# bow image
bow_on = False

bow_button = Button()
bow_button.x = 250
bow_button.y = 10
bow_button.data = "Bow on/off"
bow_button.width = 96
bow_button.height = 18
app.add(bow_button)

bow_image = Image()
bow_image.x = 24
bow_image.y = 36
bow_image.data = "images/bow.png"
bow_image.width = 200
bow_image.height = 200
bow_image.visible = False
app.add(bow_image)

# vest image
vest_on = False

vest_button = Button()
vest_button.x = 250
vest_button.y = 35
vest_button.data = "Vest on/off"
vest_button.width = 96
vest_button.height = 18
app.add(vest_button)

vest_image = Image()
vest_image.x = 24
vest_image.y = 36
vest_image.data = "images/vest.png"
vest_image.width = 200
vest_image.height = 200
vest_image.visible = False
app.add(vest_image)

app.run()

again = True

while again == True:

  event = app.wait_for_event(CLICK)

  if event.control == bow_button:
    if bow_on == False: 
      bow_image.visible = True      
      bow_on = True
    else:      
      bow_image.visible = False
      bow_on = False
  if event.control == vest_button:
    if vest_on == False: 
      vest_image.visible = True      
      vest_on = True
    else:      
      vest_image.visible = False
      vest_on = False      
  elif event.control == submit:
    if chatbox.data == "hello":
      speech.data = "Hello there!"
    else:
      speech.data = "Woof!"

  app.refresh()

app.stop()
