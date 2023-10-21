import random
import pygame

from objects import Ground, Dino, Cactus, Cloud, Ptera, Star

# pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN = WIDTH, HEIGHT = (600, 200)

# 화면 생성 및 프레임 설정
win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
clock = pygame.time.Clock()
FPS = 60

# 색깔 정의
WHITE = (225, 225, 225)  # 흰색
BLACK = (0, 0, 0)  # 검정색
GRAY = (32, 33, 36)  # 회색

# 시작 이미지 로드 및 크기 조절
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

# 숫자 이미지 로드 및 크기 조절
numbers_img = pygame.image.load('Assets/numbers.png')
numbers_img = pygame.transform.scale(numbers_img, (120, 12))

# 점프 사운드 로드
jump_fx = pygame.mixer.Sound('Sounds/jump.wav')

# 죽음 사운드 로드
die_fx = pygame.mixer.Sound('Sounds/die.wav')

# 체크포인트 사운드 로드
checkpoint_fx = pygame.mixer.Sound('Sounds/checkPoint.wav')

# 게임 객체 및 그룹 초기화
ground = Ground()  # 지면
dino = Dino(50, 160)  # 공룡

cactus_group = pygame.sprite.Group()  # 선인장 그룹
ptera_group = pygame.sprite.Group()  # 테라 그룹
cloud_group = pygame.sprite.Group()  # 구름 그룹
stars_group = pygame.sprite.Group()  # 별 그룹


# FUNCTIONS ******************************************************************
def reset():
    # 전역 변수를 사용하기 위해 global 키워드 사용
    global counter, SPEED, score, high_score

    # 현재 점수(score)가 최고 점수(high_score)보다 높으면 최고 점수를 업데이트
    if score and score >= high_score:
        high_score = score

    # 게임 상태 초기화
    counter = 0  # 카운터 초기화
    SPEED = 5  # 게임 속도 초기화
    score = 0  # 현재 점수 초기화

    # 선인장, 테라, 구름, 별 그룹 초기화
    cactus_group.empty()
    ptera_group.empty()
    cloud_group.empty()
    stars_group.empty()

    # 공룡 객체 리셋
    dino.reset()


# CHEATCODES *****************************************************************

# GODMODE -> immortal jutsu ( can't die )
# DAYMODE -> Swap between day and night
# LYAGAMI -> automatic jump and duck
# IAMRICH -> add 10,000 to score
# HISCORE -> highscore is 99999
# SPEEDUP -> increase speed by 2

keys = []  # 사용자 입력 키를 저장하는 빈 리스트
GODMODE = False  # 게임 내의 "신" 모드 (무적 모드)를 나타내는 변수
DAYMODE = False  # 게임 내의 낮과 밤 모드를 전환하는 변수
LYAGAMI = False  # "LYAGAMI" 입력에 의해 자동 점프 및 웅크리기 기능을 활성화하는 변수

# VARIABLES ******************************************************************

counter = 0  # 게임 루프 반복 횟수를 계산하는 변수
enemy_time = 100  # 적 캐릭터(선인장, 테라)가 생성되는 주기
cloud_time = 500  # 구름이 생성되는 주기
stars_time = 175  # 별이 생성되는 주기

SPEED = 5  # 게임의 초기 속도
jump = False  # 공룡의 점프 동작 여부를 나타내는 변수
duck = False  # 공룡의 웅크리기 동작 여부를 나타내는 변수

score = 0  # 현재 점수를 나타내는 변수
high_score = 0  # 최고 점수를 나타내는 변수

start_page = True  # 게임 시작 화면 여부를 나타내는 변수
mouse_pos = (-1, -1)  # 마우스의 현재 위치를 나타내는 변수

running = True  # 게임 루프를 계속 실행할지 여부를 나타내는 변수

while running:  # 게임 루프 시작

    jump = False  # 점프 동작 여부 초기화

    # DAYMODE가 활성화되어 있으면 화면을 흰색으로, 그렇지 않으면 회색으로 채움
    if DAYMODE:
        win.fill(WHITE)
    else:
        win.fill(GRAY)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 종료 이벤트가 발생하면 게임 루프 종료
            running = False

        if event.type == pygame.KEYDOWN:  # 키를 눌렀을 때의 이벤트 처리
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False  # ESC 또는 Q 키를 누르면 게임 종료

            if event.key == pygame.K_SPACE:
                if start_page:
                    start_page = False  # 스페이스 키로 게임 시작 화면을 닫음
                elif dino.alive:
                    jump = True  # 게임 중이면 공룡을 점프시키고 점프 효과음 재생
                    jump_fx.play()
                else:
                    reset()  # 게임 오버 시 리셋

            if event.key == pygame.K_UP:
                jump = True  # 화살표 위 키로 점프

            if event.key == pygame.K_DOWN:
                duck = True  # 화살표 아래 키로 웅크리기

            key = pygame.key.name(event.key)
            keys.append(key)
            keys = keys[-7:]

            # 입력된 키를 연결하여 특정한 입력을 감지하여 기능 활성화/비활성화
            if ''.join(keys).upper() == 'GODMODE':
                GODMODE = not GODMODE

            if ''.join(keys).upper() == 'DAYMODE':
                DAYMODE = not DAYMODE

            if ''.join(keys).upper() == 'LYAGAMI':
                LYAGAMI = not LYAGAMI

            if ''.join(keys).upper() == 'SPEEDUP':
                SPEED += 2

            if ''.join(keys).upper() == 'IAMRICH':
                score += 10000

            if ''.join(keys).upper() == 'HISCORE':
                high_score = 99999

        if event.type == pygame.KEYUP:  # 키를 뗐을 때의 이벤트 처리
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                jump = False  # 스페이스 키 또는 화살표 위 키를 떼면 점프 중지

            if event.key == pygame.K_DOWN:
                duck = False  # 화살표 아래 키를 떼면 웅크리기 중지

        if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 버튼이 눌렸을 때의 이벤트 처리
            mouse_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:  # 마우스 버튼을 뗐을 때의 이벤트 처리
            mouse_pos = (-1, -1)

    if start_page:  # 시작 화면 표시
        win.blit(start_img, (50, 100))
    else:
        if dino.alive:  # 게임 진행 중인 경우
            counter += 1

            # 적 캐릭터(선인장, 테라) 생성 및 관리
            if counter % int(enemy_time) == 0:
                if random.randint(1, 10) == 5:
                    y = random.choice([85, 130])
                    ptera = Ptera(WIDTH, y)
                    ptera_group.add(ptera)
                else:
                    type = random.randint(1, 4)
                    cactus = Cactus(type)
                    cactus_group.add(cactus)

            # 구름 생성 및 관리
            if counter % cloud_time == 0:
                y = random.randint(40, 100)
                cloud = Cloud(WIDTH, y)
                cloud_group.add(cloud)

            # 별 생성 및 관리
            if counter % stars_time == 0:
                type = random.randint(1, 3)
                y = random.randint(40, 100)
                star = Star(WIDTH, y, type)
                stars_group.add(star)

            if counter % 100 == 0:
                SPEED += 0.1  # 일정 주기마다 게임 속도 증가
                enemy_time -= 0.5  # 일정 주기마다 적 생성 주기 감소

            if counter % 5 == 0:
                score += 1  # 일정 주기마다 점수 증가

            if score and score % 100 == 0:
                checkpoint_fx.play()  # 일정 점수 달성 시 체크포인트 효과음 재생

            if not GODMODE:
                for cactus in cactus_group:
                    if LYAGAMI:
                        dx = cactus.rect.x - dino.rect.x
                        if 0 <= dx <= (70 + (score // 100)):
                            jump = True  # 적에게 가까워지면 자동으로 점프

                    if pygame.sprite.collide_mask(dino, cactus):
                        SPEED = 0
                        dino.alive = False
                        die_fx.play()  # 적과 충돌 시 게임 오버 처리 및 효과

                # 테라 그룹 내의 각 테라 캐릭터와 충돌 감지
                for ptera in ptera_group:
                    if LYAGAMI:
                        dx = ptera.rect.x - dino.rect.x
                        if 0 <= dx <= 70:
                            if dino.rect.top <= ptera.rect.top:
                                jump = True
                            else:
                                duck = True
                        else:
                            duck = False

                    if pygame.sprite.collide_mask(dino, ptera):
                        SPEED = 0
                        dino.alive = False  # 테라와 충돌 시 게임 오버 처리
                        die_fx.play()  # 게임 오버 효과음 재생

        ground.update(SPEED)  # 땅을 업데이트하고 이동 속도에 맞춰 그립니다.
        ground.draw(win)

        cloud_group.update(SPEED - 3, dino)  # 구름 그룹을 업데이트하고 이동 속도에 맞춰 그립니다.
        cloud_group.draw(win)

        stars_group.update(SPEED - 3, dino)  # 별 그룹을 업데이트하고 이동 속도에 맞춰 그립니다.
        stars_group.draw(win)

        cactus_group.update(SPEED, dino)  # 선인장 그룹을 업데이트하고 이동 속도에 맞춰 그립니다.
        cactus_group.draw(win)

        ptera_group.update(SPEED - 1, dino)  # 테라 그룹을 업데이트하고 이동 속도에 맞춰 그립니다.
        ptera_group.draw(win)

        dino.update(jump, duck)  # 공룡 캐릭터를 업데이트합니다.
        dino.draw(win)

        # 점수를 화면에 표시합니다.
        string_score = str(score).zfill(5)
        for i, num in enumerate(string_score):
            win.blit(numbers_img, (520 + 11 * i, 10), (10 * int(num), 0, 10, 12))

        if high_score:
            win.blit(numbers_img, (425, 10), (100, 0, 20, 12))
            string_score = f'{high_score}'.zfill(5)
            for i, num in enumerate(string_score):
                win.blit(numbers_img, (455 + 11 * i, 10), (10 * int(num), 0, 10, 12))

        if not dino.alive:
            win.blit(game_over_img, (WIDTH // 2 - 100, 55))  # 게임 오버 메시지를 화면에 표시합니다.
            win.blit(replay_img, replay_rect)  # 다시 시작 이미지를 화면에 표시합니다.

            # 다시 시작 이미지가 마우스 클릭 위치와 충돌하는지 확인하고 게임을 재시작합니다.
            if replay_rect.collidepoint(mouse_pos):
                reset()

    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 4)  # 화면 테두리를 그립니다.
    clock.tick(FPS)  # 게임 루프의 주기를 제어합니다.
    pygame.display.update()  # 화면을 업데이트합니다.

pygame.quit()   #게임 루프를 종료하고 pygame을 종료합니다.