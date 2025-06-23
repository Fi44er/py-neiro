import numpy as np
import matplotlib.pyplot as plt

# source venv/bin/activate

N = 5
b = 3

x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for _ in range(N)] + b
C1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10) / 10 for _ in range(N)] - 0.1 + b
C2 = [x1, x2]

f = [0 + b, 1 + b]

w2 = 0.5
w3 = -b * w2
w = np.array([-w2, w2, w3])
w = np.array([-0.3, 0.3])
for i in range(N):
    x = np.array([C2[0][i], C2[1][i]])
    y = np.dot(x, w)
    if y >= 0:
        print("Class C1")
    else:
        print("Class C2")

plt.scatter(C1[0][:], C1[1][:], s=10, c="red")
plt.scatter(C2[0][:], C2[1][:], s=10, c="blue")
plt.plot(f)
plt.grid(True)
plt.savefig("neiro1.png")
