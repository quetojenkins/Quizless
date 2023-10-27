import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Increase screen size
MENU_WIDTH, MENU_HEIGHT = 200, 30  # Adjust menu width
MENU_FONT_SIZE = 20
SCROLL_SPEED = 20  # Adjust this value for faster or slower scrolling

# Calculate the center position for the scrollable list
MENU_X = (SCREEN_WIDTH - MENU_WIDTH) // 2
MENU_Y = (SCREEN_HEIGHT - MENU_HEIGHT) // 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Create the main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrollable Dropdown Box")

# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Initialize the font
font = pygame.font.Font(None, MENU_FONT_SIZE)

# Dropdown menu options
menu_items = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Option 8", "Option 9", "Option 10", "Option 11"]
is_dropdown_open = False
scroll_offset = 0
option = ""

# Calculate the maximum number of visible items
list_len = len(menu_items)
max_visible = 6
invisible_items = [0,max_visible]

def draw_drop(option):
    screen.fill(WHITE)
    
    if is_dropdown_open:
        for i, item in enumerate(menu_items):
            if i >= invisible_items[0] and i <= invisible_items[1]:
                text = font.render(item, True, BLACK)
                text_rect = text.get_rect()
                text_rect.topleft = (MENU_X + 10, MENU_Y + MENU_HEIGHT + i * MENU_FONT_SIZE - scroll_offset)
                screen.blit(text, text_rect)

    # Draw the dropdown box with text
    pygame.draw.rect(screen, GRAY, (MENU_X, MENU_Y, MENU_WIDTH, MENU_HEIGHT))
    text = font.render(option, True, BLACK)  # Text inside the rectangle
    text_rect = text.get_rect()
    text_rect.center = (MENU_X + MENU_WIDTH // 2, MENU_Y + MENU_HEIGHT // 2)  # Center the text
    screen.blit(text, text_rect)

def get_selected_item(mouse_pos):
    for i, item in enumerate(menu_items):
        item_rect = pygame.Rect(MENU_X, MENU_Y + MENU_HEIGHT + i * MENU_FONT_SIZE, MENU_WIDTH, MENU_FONT_SIZE)
        item_rect.y -= scroll_offset
        if item_rect.collidepoint(mouse_pos):
            return item
    return None

def main():
    global is_dropdown_open, scroll_offset, invisible_items, list_len, option

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    if MENU_X <= mouse_pos[0] < MENU_X + MENU_WIDTH and MENU_Y <= mouse_pos[1] < MENU_Y + MENU_HEIGHT:
                        # Toggle dropdown
                        is_dropdown_open = not is_dropdown_open
                    elif is_dropdown_open:
                        selected_item = get_selected_item(mouse_pos)
                        if selected_item is not None:
                            option = selected_item
                            is_dropdown_open = False
            
            if event.type == pygame.MOUSEWHEEL and is_dropdown_open:
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

        draw_drop(option)
        pygame.display.flip()
        clock.tick(200)

if __name__ == "__main__":
    main()
