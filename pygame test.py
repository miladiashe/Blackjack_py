import pygame
pygame.init()

# 출처: https://kkamikoon.tistory.com/129 [컴퓨터를 다루다]

size = [1024, 768]
screen = pygame.display.set_mode(size)
# 화면을 정해진 크기로 설정한다.

pygame.display.set_caption("Blackjack")

font = pygame.font.Font('DungGeunMo.ttf', 30)
text_bg = pygame.image.load("fff.bmp")

# Loop until the user clicks the close button.
done = False
Next =  0
clock = pygame.time.Clock()

while not done:
    # 초기화가 끝나고 본격적인 게임 코딩.

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    # Main Event Loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.KEYDOWN:  # If user release what he pressed.
            # 다음으로 넘어간다
            Next = Next + 1
        elif event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill((255, 255, 255))

    '''
    Your Work.....
    '''
    screen.blit(text_bg, (10, 10))
    if Next == 0:
        text = font.render("블랙잭 게임에 오신 것을 환영합니다.", True, (28, 0, 0))
        screen.blit(text, (20, 20))
    if Next == 1:
        text2 = font.render('안녕하세요.', True, (28, 0, 0))
        screen.blit(text2, (20, 60))


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()

# 출처: https: // kkamikoon.tistory.com / 129[컴퓨터를다루다]