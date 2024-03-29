'''
initial game: silver background, blue circle, move up, down, left, right
game2: adding mouse functions
'''
import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Codemy.com Pygame Tutorial')
clock = pygame.time.Clock()
running = True

dt = 0 			# delta time variable
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)	# player position variable

while running:
	# poll for events
	# pygame.QUIT event means that the user clicked the 'X' to close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Pick the screen color
	screen.fill('silver')

	# Render the game here
	pygame.draw.circle(screen, '#033660', player_pos, 40)

	# Move the circle
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		player_pos.y -= 300 * dt
	if keys[pygame.K_DOWN]:
		player_pos.y += 300 * dt
	if keys[pygame.K_LEFT]:
		player_pos.x -= 300 * dt
	if keys[pygame.K_RIGHT]:
		player_pos.x += 300 * dt
	# Check to see if mouse has been pressed
	if pygame.mouse.get_pressed()[0]:
		# Move the circle
		if event.type == pygame.MOUSEMOTION:
			pos = pygame.mouse.get_pos()
			player_pos.x = pos[0]
			player_pos.y = pos[1]

	# # Use the mouse
	# if event.type == pygame.MOUSEBUTTONDOWN:								# Mouse button event returns dict: {'pos':(x,y), 'button': 1,2,3,..., 'touch': True, False, 'window': None}
	# 	pos = pygame.mouse.get_pos()
	# 	# Move the circle
	# 	player_pos.x = pos[0]
	# 	player_pos.y = pos[1]
	# if event.type == pygame.MOUSEBUTTONUP:
	# 	pos = pygame.mouse.get_pos()
	# 	pygame.draw.circle(screen, 'red', player_pos, 40)
	# if event.type == pygame.MOUSEMOTION:
	# 	pos = pygame.mouse.get_pos()
	# 	player_pos.x = pos[0]
	# 	player_pos.y = pos[1]
	# 	print(event)										# Mouse motion event returns dict: {'pos':(x,y), 'rel': (x,y), 'buttons': (0,0,0), 'touch': True, False, 'window': None}

	# Flip the display to output work to the screen
	pygame.display.flip()

	# Set the clock stuff / delta time in seconds since the last frame
	# Used for framerate-independent physics
	dt = clock.tick(60) / 1000

pygame.quit()