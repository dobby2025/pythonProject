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
        
    def update(self):
        # 공룡이 생존하는경우
        if self.alive:
            # 달리기 애니메이션 처리합니다.
            self.counter += 1
            if self.counter >= 4:
                self.index = (self.index + 1) % len(self.run_list)
                self.image = self.run_list[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.bottom = self.base
                self.counter = 0
        else:
            # 죽은 상태의 이미지를 표시합니다.
            self.image = self.dead_image

    def draw(self, win):
        # 현재 공룡 이미지를 게임 화면의 위치에 그립니다.
        win.blit(self.image, self.rect)









