'''
파일명: objects.py
'''

import pygame

SCREEN = WIDTH, HEIGHT = (600, 200)

class Ground():
    def __init__(self):
        self.image = pygame.image.load('Assets/ground.png') # 땅 이미지 로드

        self.width = self.image.get_width()     # 이미지 폭 가져오기
        self.x1 = 0
        self.x2 = self.width
        self.y = 150
    
    def update(self, speed):
        self.x1 -= speed    # 땅 이미지 x 위치를 이동 속도에 따라 업데이트
        self.x2 -= speed

        if self.x1 <= -self.width:
            self.x1 = self.width

        if self.x2 <= -self.width:
            self.x2 = self.width

    def draw(self, win):
        win.blit(self.image, (self.x1, self.y))     # 지면 이미지 화면에 그리기
        win.blit(self.image, (self.x2, self.y))  # 지면 이미지 화면에 그리기


class Dino():

    def __init__(self, x, y):
        self.x, self.base = x, y    # 공룡의 x, y(바닥) 좌표 설정합니다.

        # 달리기 및 점프 애니메이션 프레임을 저장할 리스트를 초기화 합니다.
        self.run_list = []
        self.duck_list = []

        # 달리기 이미지 로드하고 리스트에 추가
        for i in range(1, 4):
            img = pygame.image.load(f'Assets/Dino/{i}.png')
            img = pygame.transform.scale(img, (52, 58))
            self.run_list.append(img)
        
        # 앉기 이미지 로드하고 리스트에 추가
        for i in range(4, 6):
            img = pygame.image.load(f'Assets/Dino/{i}.png')
            img = pygame.transform.scale(img, (70, 38))
            self.duck_list.append(img)

        self.dead_image = pygame.image.load(f'Assets/Dino/8.png')
        self.dead_image = pygame.transform.scale(self.dead_image, (52, 58))

        self.reset()

        self.vel = 0        # 공룡의 수직속도를 초기화합니다.
        self.gravity = 1    # 중력 가속도를 설정합니다.
        self.jumpHeight = 15    # 점프 높이를 설정합니다.
        self.isJumping = False  # 현재 점프 중인지 여부를 나타내는 플래그 입니다.

    def reset(self):
        """
        공룡의 초기 상태 설정하는 메서드
        """
        self.index = 0
        self.image = self.run_list[self.index]
        self.rect = self.image.get_rect()   # 이미지 사각형 영역을 가져옵니다.
        self.rect.x = self.x    # 공룡의 x좌표를 설정합니다.
        self.rect.bottom = self.base   # 공룡의 바닥 높이를 설정합니다.
        
        self.alive = True   # 공룡의 생존여부
        self.counter = 0    # 애니메이션 프레임 전환용으로 사용합니다.
        
    def update(self, jump, duck, key_pressed):
        # 공룡이 생존하는경우
        if self.alive:

            self.x += key_pressed

            if not self.isJumping and jump:
                self.vel = -self.jumpHeight
                self.isJumping = True

            # 중력에 따라 수직 속도를 조절합니다.
            self.vel += self.gravity
            if self.vel >= self.jumpHeight:
                self.vel = self.jumpHeight

            self.rect.y += self.vel
            if self.rect.bottom > self.base:
                self.rect.bottom = self.base
                self.isJumping = False

            if self.isJumping:
                self.index = 0
                self.counter = 0
                self.image = self.run_list[self.index]
            elif duck:  # 웅크리기 상태일때
                # 달리기 애니메이션 처리합니다.
                self.counter += 1
                if self.counter >= 6:
                    self.index = (self.index + 1) % len(self.duck_list)
                    self.image = self.duck_list[self.index]
                    self.rect = self.image.get_rect()
                    self.rect.x = self.x
                    self.rect.bottom = self.base
                    self.counter = 0

            else:
                # 달리기 애니메이션 처리합니다.
                self.counter += 1
                if self.counter >= 4:
                    self.index = (self.index + 1) % len(self.run_list)
                    self.image = self.run_list[self.index]
                    self.rect = self.image.get_rect()
                    self.rect.x = self.x
                    self.rect.bottom = self.base
                    self.counter = 0

            #공룡의 마스크를 이미지에서 생성합니다.
            self.mask = pygame.mask.from_surface(self.image)

        else:
            # 죽은 상태의 이미지를 표시합니다.
            self.image = self.dead_image

    def draw(self, win):
        # 현재 공룡 이미지를 게임 화면의 위치에 그립니다.
        win.blit(self.image, self.rect)




class Cactus(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        # 다양한 선인장 이미지를 리스트에 저장합니다.
        self.image_list = []
        for i in range(5):
            scale = 0.65
            img = pygame.image.load(f'Assets/Cactus/{i + 1}.png')
            w, h = img.get_size()
            img = pygame.transform.scale(img, (int(w * scale), int(h * scale)))
            self.image_list.append(img)

        # 초기 이미지를 설정하고 위치를 초기화합니다.
        self.image = self.image_list[type - 1]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + 10
        self.rect.bottom = 165

    def update(self, speed, dino):
        if dino.alive:
            # 선인장을 왼쪽으로 이동하고 화면 밖으로 나가면 삭제합니다.
            self.rect.x -= speed
            if self.rect.right <= 0:
                self.kill()

            # 충돌 검사를 위한 마스크 생성합니다.
            self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        # 현재 선인장 이미지를 게임 화면의 위치에 그립니다.
        win.blit(self.image, self.rect)


class Ptera(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image_list = []
        for i in range(2):
            scale = 0.65
            img = pygame.image.load(f'Assets/Ptera/{i + 1}.png')
            w, h = img.get_size()
            img = pygame.transform.scale(img, int(w * scale), int(h * scale))
            self.image_list.append(img)

        self.index = 0
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect(center = (x, y))

        self.counter = 0

    def update(self, speed, dino):

        if dino.alive:
            # 익룡을 왼쪽으로 이동시킵니다.
            self.rect.x -= speed

            # 익룡이 화면 왼쪽 끝을 벗어나면 제거합니다.
            if self.rect.right <= 0:
                self.kill()

            # 일정한 프레임마다 이미지를 변경하여 조류가 움직이는 것처럼 보이게 합니다.
            self.counter += 1
            if self.counter >= 6:
                self.index = (self.index + 1) % len(self.image_list)
                self.image = self.image_list[self.index]
                self.counter = 0

            self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        #익룡 화면에 그리기
        win.blit(self.image, self.rect)







