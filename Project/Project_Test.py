import pygame
import random

#ประกาศใฃ้งาน pygame
pygame.init()
#หัวข้อเกม
pygame.display.set_caption('Plane Of bullet')

WIDTH = 1500
HIGHT = 900
WHITE = (255,255,255)
RED = (255,0,0)

#ความเร็วการเคลื่อนที่
SPEED = 40
BALL_SPEED = 40
#FPS
FPS = 120
clock = pygame.time.Clock()

#ขนาดของหน้าจอเกม
screen = pygame.display.set_mode((WIDTH,HIGHT))

#แสดงหน้าจอเกม
screen.fill(WHITE)

#ตั่งค่าข้อความและฟอนต์
#custom_font = pygame.font.Font('Noto_Serif_Thai/NotoSerifThai.ttf',20)
#title_text = custom_font.render('Hello Pygame',True,RED)
#โหลดภาพ
blackgound = pygame.image.load('Plane/BG.png')
Plane = pygame.image.load('Plane/Plane/Fly (1).png')
ball = pygame.image.load('Plane/Bullet/Bullet (1).png')
restart_button_img = pygame.image.load('Image/Button.png')

#ปรับขนาดภาพ
blackgound = pygame.transform.scale(blackgound,(WIDTH,HIGHT))
Plane = pygame.transform.scale(Plane,(WIDTH//6,HIGHT//6))

#ปรับพิกัดต่างๆเช่น จุดกึ่งกลาง
blackgound_rect = blackgound.get_rect()
blackgound_rect.centerx = WIDTH // 2
Plane_rect = Plane.get_rect()
Plane_rect.centery = HIGHT//2
ball_rect = ball.get_rect()
#ball_rect.center = (WIDTH+50),HIGHT//2
#ball_rect.center = WIDTH//2,HIGHT//2
ball_rect.y = random.randint(0,HIGHT-32)
ball_rect.x = 1450

#ระบบนับคะแนน
score = 0
font = pygame.font.Font('Font/PixelDigivolve-mOm9.ttf',65)
score_txt = font.render('Score : '+str(score),True,WHITE)
score_rect = score_txt.get_rect()
score_rect.topleft=(10,10)

#ระบบเวลา
countdown_time = 2  #ตั้งค่าจำนวณวลานับถอยหลัง
game_over = False
remaining_seconds = clock.tick(60) #แปลงเวลาจากมิลลิวินาทีเป็นวินาที


running = True
restart_game = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # กด 'SPACE' เพื่อเริ่มเกมใหม่
                restart_game = True
        #ตรวจสอบการชน
    if Plane_rect.colliderect(ball_rect):
        #ball_rect.top = random.randint(0,HIGHT-32)
        score += 2
        score_txt = font.render('Score : '+str(score),True,WHITE)
        ball_rect.y = random.randint(0,HIGHT-100)
        ball_rect.x = 1450
        
    if event.type == pygame.MOUSEBUTTONDOWN: #ตรวจจับเมาส์
        mous_x = event.pos[0]
        mous_y = event.pos[1]
        #print(mous_x,',',mous_y,',')
        Plane_rect.centerx = mous_x
        Plane_rect.centery = mous_y

    # ตรวจสอบเวลา
    countdown_time -= remaining_seconds / 4300
    if countdown_time > 0:
        #remaining_seconds -= clock.tick(60)
        timer_txt = font.render("Time: {:.0f}".format(countdown_time),True,WHITE)
        timer_rect = timer_txt.get_rect(topright=(WIDTH - 10, 10))
    else:
        game_over = True

    # เกมจบแล้วแสดงข้อความ "Game Over" และจบเกม
    if game_over:
        game_over_text = font.render('Game Over', True, RED)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HIGHT // 5))
        screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()

        # ระบุข้อความและตำแหน่งของผลสรุปคะแนน
        score_summary_text = font.render('Your Score: {}'.format(score), True, WHITE)
        score_summary_rect = score_summary_text.get_rect(center=(WIDTH // 2, HIGHT // 2 + 100))
        # แสดงผลคะแนนและข้อความสรุปในหน้าจอเกม
        screen.blit(score_summary_text, score_summary_rect)

    if game_over:
        screen.blit(game_over_text, game_over_rect)
        if restart_game:  # ถ้ากดปุ่มเริ่มเกมใหม่
            score = 0
            countdown_time = 2
            game_over = False
            restart_game = False
            Plane_rect.center = HIGHT//3.5,WIDTH//3.5  # ตำแหน่งเริ่มต้นของเครื่องบิน
            ball_rect.y = random.randint(0, HIGHT - 100)
            ball_rect.x = 1450
            continue  # ไปที่การวนลูปต่อไปโดยไม่ทำการเฟรมปัจจุบัน

        #สร้างปุ่มเริ่มเกมใหม่
        restart_button = pygame.Rect(WIDTH // 2 - 100, HIGHT // 3 + 50, 200, 50)
        restart_text = font.render('Press " SPACE " to restart', True, WHITE)
        restart_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_rect)
        pygame.display.flip()

    #รอจนกว่าผู้เล่นจะกดปุ่มเริ่มเกมใหม่
    '''
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # ในที่นี้เมื่อกดปุ่ม Space
                    game_over = False  # เริ่มเกมใหม่
                    countdown_time = 2
                    score = 0
    '''
    #รับค่าจากผู้เล่น
    if game_over == False:
        keys = pygame.key.get_pressed() #ตรวจจับปุ่มที่กด
        if keys[pygame.K_UP] and Plane_rect.top > 0:
            Plane_rect.y -= SPEED
        if keys[pygame.K_DOWN] and Plane_rect.bottom < HIGHT:
            Plane_rect.y += SPEED
        if keys[pygame.K_LEFT] and Plane_rect.left > 0:
            Plane_rect.x -= SPEED
        if keys[pygame.K_RIGHT] and Plane_rect.right < WIDTH:
            Plane_rect.x += SPEED
        if keys[pygame.K_w] and Plane_rect.top > 0:
            Plane_rect.y -= SPEED
        if keys[pygame.K_s] and Plane_rect.bottom < HIGHT:
            Plane_rect.y += SPEED
        if keys[pygame.K_a] and Plane_rect.left > 0:
            Plane_rect.x -= SPEED
        if keys[pygame.K_d] and Plane_rect.right < WIDTH:
            Plane_rect.x += SPEED

            #การเคลื่อนที่ของลูกบอล
        if ball_rect.x > -100:
           ball_rect.x -= BALL_SPEED
        #print(ball_rect.x)
        else:
            ball_rect.y = random.randint(0,HIGHT-100)
            ball_rect.x = 1450

    #แสดงภาพ
    screen.fill(WHITE)
    #screen.blit(title_text,(80,100)) #แสดงผลฟอนต์ 80,100 คือพิกัด
    screen.blit(blackgound,blackgound_rect) #แสดงผลพื้นหลัง
    screen.blit(Plane,Plane_rect) #แสดงผลเครื่องบิน
    screen.blit(ball,ball_rect)#แสดงผลลูกกระสุน
    screen.blit(score_txt,score_rect)
    screen.blit(timer_txt,timer_rect)

    #แสดงขอบเขตวัตถุ
    pygame.draw.rect(screen,RED,Plane_rect,2)
    pygame.draw.rect(screen,RED,ball_rect,2)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
