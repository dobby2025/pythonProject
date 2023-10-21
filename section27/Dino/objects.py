import pygame

SCREEN = WIDTH, HEIGHT = (600, 200)


class Ground():
    def __init__(self):
        self.image = pygame.image.load('Assets/ground.png')  # 땅 이미지를 로드합니다.
        self.rect = self.image.get_rect()  # 이미지의 사각 영역을 가져옵니다.

        self.width = self.image.get_width()  # 이미지의 폭을 가져옵니다.
        self.x1 = 0  # 첫 번째 지면 이미지의 x 위치입니다.
        self.x2 = self.width  # 두 번째 지면 이미지의 x 위치입니다.
        self.y = 150  # 지면 이미지의 y 위치입니다.

    def update(self, speed):
        self.x1 -= speed  # 땅 이미지의 x 위치를 이동 속도에 따라 업데이트합니다.
        self.x2 -= speed

        if self.x1 <= -self.width:
            self.x1 = self.width  # 첫 번째 지면 이미지가 화면 왼쪽으로 벗어나면 다시 오른쪽으로 이동합니다.

        if self.x2 <= -self.width:
            self.x2 = self.width  # 두 번째 지면 이미지가 화면 왼쪽으로 벗어나면 다시 오른쪽으로 이동합니다.

    def draw(self, win):
        win.blit(self.image, (self.x1, self.y))  # 첫 번째 지면 이미지를 화면에 그립니다.
        win.blit(self.image, (self.x2, self.y))  # 두 번째 지면 이미지를 화면에 그립니다.


class Dino():
    def __init__(self, x, y):
        self.x, self.base = x, y  # 공룡의 x 좌표와 기본 y 좌표(바닥)를 설정합니다.

        # 달리기 및 점프 애니메이션 프레임을 저장할 리스트를 초기화합니다.
        self.run_list = []
        self.duck_list = []

        # 달리기 애니메이션의 프레임 이미지를 로드하고 크기를 조정하여 리스트에 추가합니다.
        for i in range(1, 4):
            img = pygame.image.load(f'Assets/Dino/{i}.png')
            img = pygame.transform.scale(img, (52, 58))
            self.run_list.append(img)

        # 앉기 애니메이션의 프레임 이미지를 로드하고 크기를 조정하여 리스트에 추가합니다.
        for i in range(4, 6):
            img = pygame.image.load(f'Assets/Dino/{i}.png')
            img = pygame.transform.scale(img, (70, 38))
            self.duck_list.append(img)

        # 죽음 애니메이션의 이미지를 로드하고 크기를 조정합니다.
        self.dead_image = pygame.image.load(f'Assets/Dino/8.png')
        self.dead_image = pygame.transform.scale(self.dead_image, (52, 58))

        self.reset()  # 공룡의 초기 상태를 설정하는 메서드를 호출합니다.

        self.vel = 0  # 공룡의 수직 속도를 초기화합니다.
        self.gravity = 1  # 중력 가속도를 설정합니다.
        self.jumpHeight = 15  # 점프 높이를 설정합니다.
        self.isJumping = False  # 현재 점프 중인지 여부를 나타내는 플래그입니다.

    def reset(self):
        """
        공룡의 초기 상태를 설정합니다. 이 메서드는 게임이 처음 시작하거나 공룡이 죽었을 때 호출됩니다.
        """
        self.index = 0  # 공룡의 애니메이션 프레임 인덱스를 초기화합니다.
        self.image = self.run_list[self.index]  # 현재 이미지를 달리기 애니메이션의 첫 번째 프레임으로 설정합니다.
        self.rect = self.image.get_rect()  # 이미지의 사각형 영역을 가져와서 설정합니다.
        self.rect.x = self.x  # 공룡의 x 좌표를 설정합니다.
        self.rect.bottom = self.base  # 공룡의 바닥 높이를 설정합니다.

        self.alive = True  # 공룡의 생존 여부를 True로 설정합니다.
        self.counter = 0  # 카운터를 초기화합니다. 이 카운터는 애니메이션 프레임 전환을 제어합니다.

    def update(self, jump, duck):
        # 공룡이 생존하는 경우:
        if self.alive:
            if not self.isJumping and jump:
                # 점프를 시작하고 수직 속도를 설정합니다.
                self.vel = -self.jumpHeight
                self.isJumping = True

            # 중력에 따라 수직 속도를 조절합니다.
            self.vel += self.gravity
            if self.vel >= self.jumpHeight:
                self.vel = self.jumpHeight

            # 공룡의 y 위치를 업데이트하고 바닥에 도착하면 점프 중인지 여부를 설정합니다.
            self.rect.y += self.vel
            if self.rect.bottom > self.base:
                self.rect.bottom = self.base
                self.isJumping = False

            if duck:
                # 덕 상태 애니메이션을 처리합니다.
                self.counter += 1
                if self.counter >= 6:
                    self.index = (self.index + 1) % len(self.duck_list)
                    self.image = self.duck_list[self.index]
                    self.rect = self.image.get_rect()
                    self.rect.x = self.x
                    self.rect.bottom = self.base
                    self.counter = 0

            elif self.isJumping:
                # 점프 중인 경우 달리기 상태 애니메이션을 재설정합니다.
                self.index = 0
                self.counter = 0
                self.image = self.run_list[self.index]
            else:
                # 달리기 애니메이션을 처리합니다.
                self.counter += 1
                if self.counter >= 4:
                    self.index = (self.index + 1) % len(self.run_list)
                    self.image = self.run_list[self.index]
                    self.rect = self.image.get_rect()
                    self.rect.x = self.x
                    self.rect.bottom = self.base
                    self.counter = 0

            # 공룡의 마스크를 이미지에서 생성합니다.
            self.mask = pygame.mask.from_surface(self.image)

        # 공룡이 죽은 경우:
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
        super(Ptera, self).__init__()

        self.image_list = []
        for i in range(2):
            scale = 0.65
            img = pygame.image.load(f'Assets/Ptera/{i + 1}.png')
            w, h = img.get_size()
            img = pygame.transform.scale(img, (int(w * scale), int(h * scale)))
            self.image_list.append(img)

        self.index = 0
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect(center=(x, y))

        self.counter = 0

    def update(self, speed, dino):

        if dino.alive:
            # 조류를 왼쪽으로 이동시킵니다.
            self.rect.x -= speed

            # 조류가 화면 왼쪽 끝을 벗어나면 제거합니다.
            if self.rect.right <= 0:
                self.kill()

            # 일정한 프레임마다 이미지를 변경하여 조류가 움직이는 것처럼 보이게 합니다.
            self.counter += 1
            if self.counter >= 6:
                self.index = (self.index + 1) % len(self.image_list)
                self.image = self.image_list[self.index]
                self.counter = 0

            # 마스크를 업데이트합니다.
            self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        # 조류 이미지를 게임 화면에 그립니다.
        win.blit(self.image, self.rect)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Cloud, self).__init__()
        self.image = pygame.image.load(f'Assets/cloud.png')
        self.image = pygame.transform.scale(self.image, (60, 18))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, speed, dino):
        if dino.alive:
            # 구름을 왼쪽으로 이동시킵니다.
            self.rect.x -= speed

            # 구름이 화면 왼쪽 끝을 벗어나면 제거합니다.
            if self.rect.right <= 0:
                self.kill()

    def draw(self, win):
        # 구름 이미지를 게임 화면에 그립니다.
        win.blit(self.image, self.rect)


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super(Star, self).__init__()
        image = pygame.image.load(f'Assets/stars.png')
        self.image_list = []
        for i in range(3):
            img = image.subsurface((0, 20 * (i), 18, 18))
            self.image_list.append(img)
        self.image = self.image_list[type - 1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, speed, dino):
        if dino.alive:
            # 별을 왼쪽으로 이동시킵니다.
            self.rect.x -= speed

            # 별이 화면 왼쪽 끝을 벗어나면 제거합니다.
            if self.rect.right <= 0:
                self.kill()

    def draw(self, win):
        # 별 이미지를 게임 화면에 그립니다.
        win.blit(self.image, self.rect)
