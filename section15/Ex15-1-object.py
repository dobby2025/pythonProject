'''
파일명: Ex15-1-object.py

클래스(class)
    클래스는 객체를 생성하기 위한 템플릿.
    객체를 만드는 설계도
    붕어빵 틀,  와플 기계
    객체화(인스턴스화) - 메모리에 올리는것

객체(object)
    현실 세계 존재하는 물리적인 것 또는 추상적인 개념을
    프로그램으로 표현한 것. (식별가능한 것)
    예) 물리적 객체 - 컴퓨터, 자동차, 마우스, 모니터, 키보드 등.
        추상적 객체 - 주문, 영수증, 게임유닛


객체 구성
    초기화용 - 생성자
    속성 - 변수
    기능 - 메서드(method)

'''

class Cumputer:

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.ram}')
        print(f'VGA = {self.vga}')
        print(f'SSD = {self.ssd}')


# 실행코드
desktop = Cumputer()    # Computer 객체생성
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()
print('=====================================')
desktop.cpu = 'i9'
desktop.hardware_info()
print('=====================================')
macbook = Cumputer()
macbook.set_spec('M2', '16GB', 'M2', '512GB')
macbook.hardware_info()






