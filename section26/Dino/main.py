'''
pygame
    파이썬 언어를 기반으로 한 오픈 소스 게임 개발 라이브러리이다.
'''
import random

import pygame

from objects import Ground, Dino, Cactus, Ptera

# pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN = WIDTH, HEIGHT = (600, 200)

# 화면 생성 및 프레임 설정
win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
clock = pygame.time.Clock()
FPS = 60

# 색깔 정의
WHITE = (255, 255, 255) # 흰색
BLACK = (0, 0, 0)   # 검정색
GRAY = (32, 33, 36)

start_img = pygame.image.load('Assets/start_img.png')
start_img = pygame.transform.scale(start_img, (60, 64))

# 게임 오버 이미지 로드 및 크기 조절
game_over_img = pygame.image.load('Assets/game_over.png')
game_over_img = pygame.transform.scale(game_over_img, (200, 36))

# 리플레이 이미지 로드 및 크기 조절
replay_img = pygame.image.load('Assets/replay.png')
replay_img = pygame.transform.scale(replay_img, (40, 36))

# 리플레이 버튼의 위치 설정
replay_rect = replay_img.get_rect()
replay_rect.x = WIDTH // 2 - 20
replay_rect.y = 100

DAYMODE = True     # 게임 내의 낮과 밤 모드 전환변수
start_page = True  # 게임 시작 화면 여부를 나타내는 변수
jump = False       # 공룡의 점프 동작 여부를 나타내는 변수
duck = False       # 공룡의 웅크리기 동작 여부를 나타내는 변수

ground = Ground()
dino = Dino(50, 160)

SPEED = 5   # 게임의 초기 속도

counter = 0 # 게임 루프 반복횟수 계산하는 변수

key_pressed = 0
MOVESPEED = 3
enemy_time = 100

cactus_group = pygame.sprite.Group()    # 선인장 그룹
ptera_group = pygame.sprite.Group()     # 테라 그룹

def reset():
    global counter, SPEED

    # 게임 상태 초기화
    counter = 0 # 카운터 초기화
    SPEED = 5
    
    # 선인장, 테라 그룹 초기화
    cactus_group.empty()
    ptera_group.empty()
    
    # 공룡 객체 리셋
    dino.reset()


running = True  # 게임 실행여부 변수
while running:  # 게임 루프 시작

    if DAYMODE:
        win.fill(WHITE)
    else:
        win.fill(GRAY)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # 종료 이벤트가 발생하면 게임 루프 종료
            running = False
        
        if event.type == pygame.KEYDOWN:
            # Esc 또는 Q키를 누르면 게임 종료
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

            if event.key == pygame.K_SPACE:
                if start_page:
                    start_page = False  # 스페이스 키로 게임 시작 화면 닫음
                elif dino.alive:
                    jump = True
                else:
                    reset()

            if event.key == pygame.K_UP:
                jump = True
            if event.key == pygame.K_DOWN:
                duck = True

            if event.key == pygame.K_LEFT:
                key_pressed = -MOVESPEED
            elif event.key == pygame.K_RIGHT:
                key_pressed = MOVESPEED
            else:
                key_pressed = 0

        if event.type == pygame.KEYUP:  # 키를 뗏을 때의 이벤트 처리
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                jump = False    # 스페이스 키 또는 화살표 위 키를 떼면 점프 중지

            if event.key == pygame.K_DOWN:
                duck = False

            if event.key == pygame.K_LEFT:
                key_pressed = 0

            if event.key == pygame.K_RIGHT:
                key_pressed = 0



    if start_page:
        print('시작 화면')
        win.blit(start_img, (50, 100))
    else:
        print('# 게임 진행 화면')

        counter += 1
        if counter % 100 == 0:
            SPEED += 0.1   # 일정 주기마다 게임속도 증가


        # 적 캐릭터(선인장) 생성 및 관리
        if counter % int(enemy_time) == 0:

            if random.randint(1, 10) == 5:
                y = random.choice([85, 130])
                ptera = Ptera(WIDTH, y)
                ptera_group.add(ptera)
            else:
                type = random.randint(1, 4)
                cactus = Cactus(type)
                cactus_group.add(cactus)

        for cactus in cactus_group:
            if pygame.sprite.collide_mask(dino, cactus):
                SPEED = 0
                dino.alive = False

        for ptera in ptera_group:
            if pygame.sprite.collide_mask(dino, ptera):
                SPEED = 0
                dino.alive = False


        ground.update(SPEED)
        ground.draw(win)

        dino.update(jump, duck, key_pressed)
        dino.draw(win)

        cactus_group.update(SPEED, dino)
        cactus_group.draw(win)

        ptera_group.update(SPEED, dino)
        ptera_group.draw(win)

        if not dino.alive:
            win.blit(game_over_img, (WIDTH // 2 - 100, 55))
            win.blit(replay_img, replay_rect)

    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 4)  # 화면 테두리 그리기
    clock.tick(FPS)     # 게임 루프의 주기를 제어합니다.
    pygame.display.update()     # 화면을 업데이트 합니다.

pygame.quit()   #게임 루프를 종료하고 pygame을 종료한다.