
import matplotlib.pyplot as plt

# Figure 객체 생성
figure = plt.figure()

axes = figure.add_subplot(223) # 행, 열, 번호
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
y = [1200, 800, 500, 400, 700, 800]
axes.plot(x, y, linestyle='--', marker='^', color='red')
plt.show()