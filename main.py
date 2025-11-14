import pygame
pygame.init()
screen = pygame.display.set_mode((1530,800))
clock = pygame.time.Clock()
screen.fill([120,180,240])
player_x = 300
player_y = 350
player_h = 50
player_w = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("Up")
            player_y -=10
        # goes up
        if keys[pygame.K_w]:
            print("Up")
            player_y -=10
            # goes up
        if keys[pygame.K_DOWN]:
            print("down")
            player_y +=10
            # goes down
        if keys[pygame.K_s]:
            print("down")
            player_y +=10
            # goes down
        if keys[pygame.K_RIGHT]:
            print("right")
            player_x +=10
            #goes right
        if keys[pygame.K_d]:
            print("right")
            player_x +=10
            # goes right
        if keys[pygame.K_LEFT]:
            print("left")
            player_x -=10
            # goes left
        if keys[pygame.K_a]:
            print("left")
            player_x -=10
            #goes left
    screen.fill([120, 180, 240])
    player = pygame.Rect(player_x,player_y,player_w,player_h)
    pygame.draw.rect(screen,(67,0,0),player)
    pygame.display.flip()
    clock.tick(60)
