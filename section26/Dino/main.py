'''
pygame
    파이썬 언어를 기반으로 한 오픈 소스 게임 개발 라이브러리이다.
'''
import pygame

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

DAYMODE = False     # 게임 내의 낮과 밤 모드 전환변수
start_page = True   # 게임 시작 화면 여부를 나타내는 변수


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

    
    if start_page:
        print('시작 화면')
        win.blit(start_img, (50, 100))
    else:
        print('# 게임 진행 화면')

    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 4)  # 화면 테두리 그리기
    clock.tick(FPS)     # 게임 루프의 주기를 제어합니다.
    pygame.display.update()     # 화면을 업데이트 합니다.



pygame.quit()   #게임 루프를 종료하고 pygame을 종료한다.