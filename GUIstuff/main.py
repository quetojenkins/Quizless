import pygame as py
from pygame.locals import *
import qna
import time
import pygame_widgets
from pygame_widgets.dropdown import Dropdown

# INITIALIZATION OF THE PYGAME
py.init()

# INITIALIZATION OF SYSTEM FONTS
py.font.init()

# Colors
background_color = (45, 92, 199)
text_color = (255, 255, 255)
green_colour = (46,181,115)
yellow_colour = (255, 167, 16)
red_colour = (255,99,55)
SCREEN_WIDTH, SCREEN_HEIGHT = 1450, 850
globalFont = py.font.SysFont("calibri", 30)

# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION
# OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN
class Screen():
	# INITIALIZATION OF WINDOW HAVING TITLE,
	# WIDTH, HEIGHT AND COLOUR
	# HERE (0,0,255) IS A COLOUR CODE
	def __init__(self, title, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
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

import pygame as py

class Button:
	def __init__(self, x, y, width, height, button_color, font, font_color, text):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.button_color = button_color
		self.font = globalFont
		self.font_color = font_color
		self.text = text
		self.button_rect = py.Rect(self.x, self.y, self.width, self.height)
		self.hidden = False  # Add a hidden attribute

	def showButton(self, display):
		if not self.hidden:
			py.draw.rect(display, self.button_color, self.button_rect)
			text_surface = self.font.render(self.text, True, self.font_color)
			text_rect = text_surface.get_rect()
			text_rect.center = self.button_rect.center
			display.blit(text_surface, text_rect)

	def focusCheck(self, mousepos, mouseclick):
		if(mousepos[0] >= self.x and mousepos[0] <= self.x +
				self.width and mousepos[1] >= self.y and mousepos[1]
				<= self.y + self.height):
			self.CurrentState = True
			# IF MOUSE BUTTON CLICK THEN
			# NAVIGATE TO THE NEXT OR PREVIOUS TABS
			return mouseclick[0]
		else:
			# ELSE LET THE CURRENT STATE TO BE OFF
			self.CurrentState = False
			return False
	
	def hide(self):
		self.hidden = True
		# You can also modify other attributes, such as the dimensions or transparency, to hide the button.

	def unhide(self):
		self.hidden = False




font = globalFont

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
# MENU BUTTON
MB_WIDTH, MB_HEIGHT = 180, 55
MENU_BUTTON = Button(SCREEN_WIDTH // 2 - MB_WIDTH // 2, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.2, MB_WIDTH, MB_HEIGHT, 
                     (255, 167, 16),"Calibri", 
                     text_color, "BEGIN")



# CONTROL BUTTON
CONTROL_BUTTON = Button(1200, 300, 150, 50,
						(255, 167, 16), None,
						text_color, "DONE")


toggle = False

##Menu
welcome_color = background_color
welcometext_color = (255, 167, 16)  # RGB color for the text on the button
welcomefont = py.font.SysFont("calibri", 100)  # You can choose a different font if you prefer
welcomecard_text = "WELCOME"

def draw_welcome():
    # Get the surface from the control_bar screen when it's active
    if menuScreen.checkUpdate(background_color):
        screen = menuScreen.screen

        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, welcome_color, (card_x, card_y, card_width, card_height))

        text_surface = welcomefont.render(welcomecard_text, True, welcometext_color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.05))
        screen.blit(text_surface, text_rect)

##FlashCard
card_width = 800
card_height = 500
card_x = 300
card_y = 100
card_color = text_color
writing = (0,0,0)
text_color = (255, 255, 255)  # RGB color for the text on the button
cardFont = py.font.SysFont("calibri", 29)  # You can choose a different font if you prefer
card_text = "What is the capital of italy"

def draw_card():
    # Get the surface from the control_bar screen when it's active
    if flashCards.checkUpdate(background_color):
        screen = flashCards.screen

        # Draw the rectangle on the control_bar screen
        py.draw.rect(screen, card_color, (card_x, card_y, card_width, card_height))

        lines = card_text.split('\n')  # Split the text into lines

        # Calculate the initial y_position to center the lines within the card height
        total_lines_height = sum(cardFont.size(line)[1] for line in lines)
        y_position = card_y + (card_height - total_lines_height) // 2

        for line in lines:
            text_surface = cardFont.render(line, True, writing)
            text_rect = text_surface.get_rect(center=(card_x + card_width // 2, y_position + text_surface.get_height() // 2))
            screen.blit(text_surface, text_rect)
            y_position += text_surface.get_height()  # Move down for the next line

##Score
score_width = 100
score_height = 100
score_x = 0
score_y = 0
score_color = background_color
text_color = (255, 167, 16)  # RGB color for the text on the button
font = globalFont  # You can choose a different font if you prefer

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
MENU_WIDTH, MENU_HEIGHT = 400, 30  # Adjust menu width
MENU_FONT_SIZE = 20
SCROLL_SPEED = 20  # Adjust this value for faster or slower scrolling

# Calculate the center position for the scrollable list
MENU_X = (SCREEN_WIDTH - MENU_WIDTH) // 2
MENU_Y = (SCREEN_HEIGHT - MENU_HEIGHT) // 2 + 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 167, 16)

menu_items = qna.get_quizes("FileHandeling Section/qnas")
is_dropdown_open = False
scroll_offset = 0
option = "Select a quiz"
list_len = len(menu_items)
max_visible = 4
invisible_items = [0,max_visible]
dropDownFont = py.font.SysFont("calibri", MENU_FONT_SIZE)
def draw_drop(option):
	if menuScreen.checkUpdate(background_color):
		screen = menuScreen.screen
	
		if is_dropdown_open:
			for i, item in enumerate(menu_items):
				if i >= invisible_items[0] and i <= invisible_items[1]:
					text = dropDownFont.render(item, True, WHITE)
					text_rect = text.get_rect()
					text_rect.topleft = (MENU_X + 10, MENU_Y + MENU_HEIGHT + i * MENU_FONT_SIZE - scroll_offset)
					screen.blit(text, text_rect)

		# Draw the dropdown box with text
		py.draw.rect(screen, YELLOW, (MENU_X, MENU_Y, MENU_WIDTH, MENU_HEIGHT))
		text = dropDownFont.render(option, True, WHITE)  # Text inside the rectangle
		text_rect = text.get_rect()
		text_rect.center = (MENU_X + MENU_WIDTH // 2, MENU_Y + MENU_HEIGHT // 2)  # Center the text
		screen.blit(text, text_rect)

def get_selected_item(mouse_pos):
    for i, item in enumerate(menu_items):
        item_rect = py.Rect(MENU_X, MENU_Y + MENU_HEIGHT + i * MENU_FONT_SIZE, MENU_WIDTH, MENU_FONT_SIZE)
        item_rect.y -= scroll_offset
        if item_rect.collidepoint(mouse_pos):
            return item
    return None

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

keys = py.key.get_pressed()

# if keys[K_c]:
#     # Perform the action associated with the 'n' key
# 	buttoncorrect_clicked = True

# if keys[K_i]:
#     # Perform the action associated with the 'n' key
# 	buttonincorrect_clicked = True

# if keys[K_SPACE]:
#     # Perform the action associated with the 'n' key
# 	buttonflip_clicked = True


side = True #when the side of the flashcard is true, then it is a question side, if false it is an answer side
running = True
image_display = False

last_flip_click_time = 0
last_correct_click_time = 0
last_incorrect_click_time = 0

# MAIN LOOPING
while running:

	if option == "Select a quiz":
		MENU_BUTTON.hide()

	# CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
	events = py.event.get()
	for event in events:
		# IF CLICKED THEN CLOSE THE WINDOW
		if(event.type == py.QUIT):
			running = False

		if event.type == py.MOUSEBUTTONDOWN:
			if event.button == 1:  # Left mouse button
				mouse_pos = event.pos
				if MENU_X <= mouse_pos[0] < MENU_X + MENU_WIDTH and MENU_Y <= mouse_pos[1] < MENU_Y + MENU_HEIGHT:
					# Toggle dropdown
					is_dropdown_open = not is_dropdown_open
				elif is_dropdown_open:
					selected_item = get_selected_item(mouse_pos)
					if selected_item is not None:
						option = selected_item
						MENU_BUTTON.unhide()
						is_dropdown_open = False
		
		if event.type == py.MOUSEWHEEL and is_dropdown_open:
			# Scroll the dropdown, adjusting the scroll offset by SCROLL_SPEED
			if event.y != 0:
				max_scroll = len(menu_items) * MENU_FONT_SIZE
				if invisible_items[1] != list_len - 1 or (invisible_items[1] == list_len - 1 and SCROLL_SPEED * event.y < 0):
					scroll_offset = max(0, min(max_scroll, scroll_offset + SCROLL_SPEED * event.y))
				invisible_items[0] = abs(scroll_offset/(SCROLL_SPEED * event.y))
				if SCROLL_SPEED * event.y > 0 and invisible_items[1] < list_len -1:
					invisible_items[1] += 1
				elif SCROLL_SPEED * event.y < 0 and invisible_items[1] > max_visible and not invisible_items[1] - invisible_items[0] <= max_visible:
						invisible_items[1] -= 1
	
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
		if option is not None:
			control_barbutton = MENU_BUTTON.focusCheck(mouse_pos, mouse_click)
			MENU_BUTTON.showButton(menuScreen.returnTitle())

			if control_barbutton:
				q,a,d = qna.initialise("FileHandeling Section/qnas/"+option)
				ques,ans,num,found = qna.get_next(q,a,d)
				card_text = ques
				win = flashCards.makeCurrentScreen()
				menuScreen.endCurrentScreen()	
    
	# CONTROL BAR CODE TO ACCESS
	# CHECKING CONTROL SCREEN FOR ITS UPDATE
	elif flashCards.checkUpdate(background_color):
		
		return_back = CONTROL_BUTTON.focusCheck(mouse_pos, mouse_click)
		CONTROL_BUTTON.showButton(flashCards.returnTitle())
		if return_back:
			flashCards.endCurrentScreen()
			win = menuScreen.makeCurrentScreen()
			MENU_BUTTON.hide()
			image_display = False
	
	draw_welcome()
	draw_card()
	draw_flipButton()
	draw_CorrectButton()
	draw_IncorrectButton()
	draw_drop(option)
	if flashCards.checkUpdate(background_color):
		draw_score(update_score(d))

	if keys[K_c]:
    	# Perform the action associated with the 'n' key
		current_time = py.time.get_ticks()
		if current_time - last_flip_click_time > 500:  # Adjust the debounce time (500 milliseconds)
				last_flip_click_time = current_time
				buttoncorrect_clicked = True

	if keys[K_i]:
    	# Perform the action associated with the 'n' key
		current_time = py.time.get_ticks()
		if current_time - last_flip_click_time > 500:  # Adjust the debounce time (500 milliseconds)
				last_flip_click_time = current_time
				buttonincorrect_clicked = True

	if keys[K_SPACE]:
    	# Perform the action associated with the 'n' key
		current_time = py.time.get_ticks()
		if current_time - last_flip_click_time > 500:  # Adjust the debounce time (500 milliseconds)
				last_flip_click_time = current_time
				buttonflip_clicked = True
	
	if keys[K_q]:
		running = False
	
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
