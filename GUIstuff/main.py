import pygame as py
from pygame.locals import *
import qna
import time
import pygame_widgets
from pygame_widgets.dropdown import Dropdown

# Colors
background_color = (45, 92, 199)
text_color = (255, 255, 255)
green_colour = (46,181,115)
yellow_colour = (255, 167, 16)
red_colour = (255,99,55)

# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION
# OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN
class Screen():
	# INITIALIZATION OF WINDOW HAVING TITLE,
	# WIDTH, HEIGHT AND COLOUR
	# HERE (0,0,255) IS A COLOUR CODE
	def __init__(self, title, width=1450, height=850,
				fill=background_color):
		# HEIGHT OF A WINDOW
		self.height = height
		# TITLE OF A WINDOW
		self.title = title
		# WIDTH OF A WINDOW
		self.width = width
		# COLOUR CODE
		self.fill = fill
		# CURRENT STATE OF A SCREEN
		self.CurrentState = False

	# DISPLAY THE CURRENT SCREEN OF
	# A WINDOW AT THE CURRENT STATE
	def makeCurrentScreen(self):
	
		# SET THE TITLE FOR THE CURRENT STATE OF A SCREEN
		py.display.set_caption(self.title)
		# SET THE STATE TO ACTIVE
		self.CurrentState = True
		# ACTIVE SCREEN SIZE
		self.screen = py.display.set_mode((self.width,
										self.height))

	# THIS WILL SET THE STATE OF A CURRENT STATE TO OFF
	def endCurrentScreen(self):
		self.CurrentState = False

	# THIS WILL CONFIRM WHETHER THE NAVIGATION OCCURS
	def checkUpdate(self, fill):
		# HERE FILL IS THE COLOR CODE
		self.fill = fill
		return self.CurrentState

	# THIS WILL UPDATE THE SCREEN WITH
	# THE NEW NAVIGATION TAB
	def screenUpdate(self):
		if self.CurrentState:
			self.screen.fill(self.fill)

	# RETURNS THE TITLE OF THE SCREEN
	def returnTitle(self):
		return self.screen

# NAVIGATION BUTTON CLASS

class Button():

	# INITIALIZATION OF BUTTON
	# COMPONENTS LIKE POSITION OF BUTTON,
	# COLOR OF BUTTON, FONT COLOR OF BUTTON, FONT SIZE,
	# TEXT INSIDE THE BUTTON
	def __init__(self, x, y, sx, sy, bcolour,
				fbcolour, font, fcolour, text):
		# ORIGIN_X COORDINATE OF BUTTON
		self.x = x
		# ORIGIN_Y COORDINATE OF BUTTON
		self.y = y
		# LAST_X COORDINATE OF BUTTON
		self.sx = sx
		# LAST_Y COORDINATE OF BUTTON
		self.sy = sy
		# FONT SIZE FOR THE TEXT IN A BUTTON
		self.fontsize = 25
		# BUTTON COLOUR
		self.bcolour = bcolour
		# RECTANGLE COLOR USED TO DRAW THE BUTTON
		self.fbcolour = fbcolour
		# BUTTON FONT COLOR
		self.fcolour = fcolour
		# TEXT IN A BUTTON
		self.text = text
		# CURRENT IS OFF
		self.CurrentState = False
		# FONT OBJECT FROM THE SYSTEM FONTS
		self.buttonf = py.font.SysFont(font, self.fontsize)

	# DRAW THE BUTTON FOR THE TWO
	# TABS MENU_SCREEN AND CONTROL TABS MENU
	def showButton(self, display):
		if(self.CurrentState):
			py.draw.rect(display, self.fbcolour,
						(self.x, self.y,
						self.sx, self.sy))
		else:
			py.draw.rect(display, self.fbcolour, 
						(self.x, self.y,
						self.sx, self.sy))
		# RENDER THE FONT OBJECT FROM THE SYSTEM FONTS
		textsurface = self.buttonf.render(self.text,
										False, self.fcolour)

		# THIS LINE WILL DRAW THE SURF ONTO THE SCREEN
		display.blit(textsurface, 
					((self.x + (self.sx/2) -
					(self.fontsize/2)*(len(self.text)/2) -
					5, (self.y + (self.sy/2) -
						(self.fontsize/2)-4))))

	# THIS FUNCTION CAPTURE WHETHER 
	# ANY MOUSE EVENT OCCUR ON THE BUTTON
	def focusCheck(self, mousepos, mouseclick):
		if(mousepos[0] >= self.x and mousepos[0] <= self.x +
				self.sx and mousepos[1] >= self.y and mousepos[1]
				<= self.y + self.sy):
			self.CurrentState = True
			# IF MOUSE BUTTON CLICK THEN
			# NAVIGATE TO THE NEXT OR PREVIOUS TABS
			return mouseclick[0]

		else:
			# ELSE LET THE CURRENT STATE TO BE OFF
			self.CurrentState = False
			return False


# INITIALIZATION OF THE PYGAME
py.init()

# INITIALIZATION OF SYSTEM FONTS
py.font.init()
font = py.font.Font(None, 36)

# CREATING THE OBJECT OF THE
# CLASS Screen FOR MENU SCREEN
menuScreen = Screen("Home")

# CREATING THE OBJECT OF THE
# CLASS Screen FOR CONTROL SCREEN
flashCards = Screen("Flash Cards")

# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
win = menuScreen.makeCurrentScreen()


# MENU BUTTON
MENU_BUTTON = Button(625, 600, 150, 50, background_color,
					(255, 167, 16), None,
					text_color, "Begin")

# CONTROL BUTTON
CONTROL_BUTTON = Button(1200, 150, 150, 50,
						background_color, (255, 167, 16),
						None,
						text_color, "Done")


toggle = False

##Menu
welcome_color = background_color
welcometext_color = (255, 167, 16)  # RGB color for the text on the button
welcomefont = py.font.Font(None, 100)  # You can choose a different font if you prefer
welcomecard_text = "WELCOME"

def draw_welcome():
    # Get the surface from the control_bar screen when it's active
    if menuScreen.checkUpdate(background_color):
        screen = menuScreen.screen

        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, welcome_color, (card_x, card_y, card_width, card_height))

        text_surface = welcomefont.render(welcomecard_text, True, welcometext_color)
        text_rect = text_surface.get_rect(center=(card_x + card_width // 2, card_y + card_height // 2))
        screen.blit(text_surface, text_rect)

##FlashCard
card_width = 800
card_height = 500
card_x = 300
card_y = 100
card_color = text_color
writing = (0,0,0)
text_color = (255, 255, 255)  # RGB color for the text on the button
font = py.font.Font(None, 36)  # You can choose a different font if you prefer
card_text = "What is the capital of italy"

def draw_card():
    # Get the surface from the control_bar screen when it's active
    if flashCards.checkUpdate(background_color):
        screen = flashCards.screen

        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, card_color, (card_x, card_y, card_width, card_height))

        lines = card_text.split('\n')  # Split the text into lines

        y_position = card_y
        for line in lines:
            text_surface = font.render(line, True, writing)
            text_rect = text_surface.get_rect(center=(card_x + card_width // 2, y_position + card_height // 2))
            screen.blit(text_surface, text_rect)
            y_position += text_rect.height  # Move down for the next line

##Score
score_width = 100
score_height = 100
score_x = 0
score_y = 0
score_color = background_color
text_color = (255, 167, 16)  # RGB color for the text on the button
font = py.font.Font(None, 30)  # You can choose a different font if you prefer

def draw_score(score_text):
    # Get the surface from the control_bar screen when it's active
    if flashCards.checkUpdate(background_color):
        screen = flashCards.screen
	
        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, score_color, (score_x, score_y, score_width, score_height))

        text_surface = font.render(score_text, True, text_color)
        text_rect = text_surface.get_rect(center=(score_x + score_width // 2, score_y + score_height // 2))
        screen.blit(text_surface, text_rect)

##Flip Button
button_width = 200
button_height = 75
buttonflip_x = 350
buttonflip_y = 700
buttonflip_color = (255, 167, 16)
text_color = (255, 255, 255)  # RGB color for the text on the button
buttonflip_text = "FLIP"

def draw_flipButton():
    if flashCards.checkUpdate(background_color):
        screen = flashCards.screen

        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, buttonflip_color, (buttonflip_x, buttonflip_y, button_width, button_height))

        text_surface = font.render(buttonflip_text, True, text_color)
        text_rect = text_surface.get_rect(center=(buttonflip_x + button_width // 2, buttonflip_y + button_height // 2))
        screen.blit(text_surface, text_rect)

##Correct and Next Button
buttoncorrect_x = 600
buttoncorrect_y = 700
buttoncorrect_color = (46,181,115)
buttoncorrect_text = "Correct!"

def draw_CorrectButton():
    if flashCards.checkUpdate(background_color):
        screen = flashCards.screen

        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, buttoncorrect_color, (buttoncorrect_x, buttoncorrect_y, button_width, button_height))

        text_surface = font.render(buttoncorrect_text, True, text_color)
        text_rect = text_surface.get_rect(center=(buttoncorrect_x + button_width // 2, buttoncorrect_y + button_height // 2))
        screen.blit(text_surface, text_rect)

##Incorrect and Next Button
buttonincorrect_x = 850
buttonincorrect_y = 700
buttonincorrect_color = (255,99,55)
buttonincorrect_text = "Incorrect :(!"

def draw_IncorrectButton():
    if flashCards.checkUpdate(background_color):
        screen = flashCards.screen

        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, buttonincorrect_color, (buttonincorrect_x, buttonincorrect_y, button_width, button_height))

        text_surface = font.render(buttonincorrect_text, True, text_color)
        text_rect = text_surface.get_rect(center=(buttonincorrect_x + button_width // 2, buttonincorrect_y + button_height // 2))
        screen.blit(text_surface, text_rect)

# dropdown 
dropdown = Dropdown(
	win=menuScreen.screen,
	x=100,
	y=50,
	width=100,
	height=50,
	name='Select Quiz',
	choices=qna.get_quizes("FileHandeling Section/qnas"),
	borderRadius=0,
	colour = yellow_colour,
	#values=qna.get_values(len(qna.get_quizes("FileHandeling Section/qnas"))),
	direction='down',
	textHAlign='centre',
	textColour = text_color,
	inactiveColour = yellow_colour,
	pressedColour = green_colour,
	hoverColour = (255, 200, 20)
)


# other useful functions 
def update_score(d):
	corr, tot = qna.get_num_correct(d)
	return str(corr) + "/" + str(tot)

def show_picture(display, path):
	try:
		image = py.image.load(path)
		top_margin = (card_height*0.1)/2
		old_width, old_height = image.get_size()
		new_height = card_height-2*top_margin
		new_width = old_width * (new_height/old_height)
		image = py.transform.scale(image,(new_width,new_height))

		image_y = card_y+top_margin
		image_x = (card_width-new_width)/2 + card_x
		display.screen.blit(image, (image_x, image_y))
	except py.error as e:
		print("Error loading the image:", str(e))

# initialiazing before running
buttonflip_clicked = False
buttoncorrect_clicked = False
buttonincorrect_clicked = False


side = True #when the side of the flashcard is true, then it is a question side, if false it is an answer side
running = True
image_display = False


last_flip_click_time = 0
last_correct_click_time = 0
last_incorrect_click_time = 0

# MAIN LOOPING
while running:

	# CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
	events = py.event.get()
	for event in events:
		# IF CLICKED THEN CLOSE THE WINDOW
		if(event.type == py.QUIT):
			running = False
	
	# CALLING OF screenUpdate 
	# function FOR MENU SCREEN
	menuScreen.screenUpdate()
	# CALLING THE FUNCTION OF CONTROL BAR
	flashCards.screenUpdate()
	
    
	# STORING THE MOUSE EVENT TO
	# CHECK THE POSITION OF THE MOUSE
	mouse_pos = py.mouse.get_pos()
	# CHECKING THE MOUSE CLICK EVENT
	mouse_click = py.mouse.get_pressed()
	# KEY PRESSED OR NOT
	keys = py.key.get_pressed()

	# MENU BAR CODE TO ACCESS
	# CHECKING MENU SCREEN FOR ITS UPDATE
	if menuScreen.checkUpdate(background_color):
		dropdown.enable()
		dropdown.show()

		if dropdown.getSelected() is not None:
			choice = dropdown.getSelected()
			control_barbutton = MENU_BUTTON.focusCheck(mouse_pos, mouse_click)
			MENU_BUTTON.showButton(menuScreen.returnTitle())

			if control_barbutton:
				q,a,d = qna.initialise("FileHandeling Section/qnas/"+choice)
				ques,ans,num,found = qna.get_next(q,a,d)
				card_text = ques
				win = flashCards.makeCurrentScreen()
				menuScreen.endCurrentScreen()	
    
	# CONTROL BAR CODE TO ACCESS
	# CHECKING CONTROL SCREEN FOR ITS UPDATE
	elif flashCards.checkUpdate(background_color):
		dropdown.hide()
		dropdown.disable()
		
		return_back = CONTROL_BUTTON.focusCheck(mouse_pos, mouse_click)
		CONTROL_BUTTON.showButton(flashCards.returnTitle())
		if return_back:
			flashCards.endCurrentScreen()
			win = menuScreen.makeCurrentScreen()
			image_display = False
	
	draw_welcome()
	draw_card()
	draw_flipButton()
	draw_CorrectButton()
	draw_IncorrectButton()
	if flashCards.checkUpdate(background_color):
		draw_score(update_score(d))


	if event.type == py.MOUSEBUTTONDOWN and event.button == 1 and flashCards.checkUpdate(background_color):
		mouse_x, mouse_y = py.mouse.get_pos()

		if buttonflip_x <= mouse_x <= buttonflip_x + button_width and buttonflip_y <= mouse_y <= buttonflip_y + button_height:
			# Check for debouncing the flip button
			current_time = py.time.get_ticks()
			if current_time - last_flip_click_time > 500:  # Adjust the debounce time (500 milliseconds)
				last_flip_click_time = current_time
				buttonflip_clicked = True

		if buttoncorrect_x <= mouse_x <= buttoncorrect_x + button_width and buttoncorrect_y <= mouse_y <= buttoncorrect_y + button_height:
			# Check for debouncing the correct button
			current_time = py.time.get_ticks()
			if current_time - last_correct_click_time > 500:  # Adjust the debounce time (500 milliseconds)
				last_correct_click_time = current_time
				buttoncorrect_clicked = True

		if buttonincorrect_x <= mouse_x <= buttonincorrect_x + button_width and buttonincorrect_y <= mouse_y <= buttonincorrect_y + button_height:
			# Check for debouncing the incorrect button
			current_time = py.time.get_ticks()
			if current_time - last_incorrect_click_time > 500:  # Adjust the debounce time (500 milliseconds)
				last_incorrect_click_time = current_time
				buttonincorrect_clicked = True

	if buttonflip_clicked and side:
		# if the flip button is clicked, then the writing must change to the answer of the variable, the writing is in variable card_text
		if qna.check_image(ans):
			image_display = True
			image_path = ans[1:]
			card_text = ""
		else:
			card_text = ans
		side = False # now the side is an answer
		buttonflip_clicked = False # allow it to be clicked again
		time.sleep(0.1)
	
	if buttonflip_clicked and not side:
		#it is currently on the answer and you now want to make the card_text writing the question
		image_display = False
		card_text = ques
		side = True # now the side is an question
		buttonflip_clicked = False # allow it to be clicked again
		time.sleep(0.1)

	if buttoncorrect_clicked:
		#if the button correct is clicked, gett the next array index and put the question into card_text
		side = True
		d = qna.correct(num,d)
		ques,ans,num,found = qna.get_next(q,a,d)
		card_text = ques
		buttoncorrect_clicked = False # allow it to be clicked again
		image_display = False
		if not found:	
			flashCards.endCurrentScreen()
			win = menuScreen.makeCurrentScreen()
		time.sleep(0.1)

	if buttonincorrect_clicked:
		#if the incorrect button is clicked, get the next array index and put the question on the screen
		#dont update the score
		side = True
		ques,ans,num,found = qna.get_next(q,a,d)
		card_text = ques
		buttonincorrect_clicked = False # allow it to be clicked again
		image_display = False
		time.sleep(0.1)
	
	if image_display:
		show_picture(flashCards,image_path)

	pygame_widgets.update(events)

	py.display.update()
	
# CLOSE THE PROGRAM
py.quit()
