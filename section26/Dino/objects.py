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