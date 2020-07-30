# Benchmark
import timeit
import matplotlib.pyplot as plt

n_samples = 5000

# Object initialization
SETUP_ADAFRUIT = ''' 
import time
import board
import busio
import adafruit_mpu6050
i2c = busio.I2C(board.SCL, board.SDA)
mpu_adafruit = adafruit_mpu6050.MPU6050(i2c)  
'''

SETUP_LOCAL = ''' 
import mpu6050
mpu = mpu6050.MPU6050(0x68, '2g', 1000)
'''

LOOP_ADAFRUIT = '''
try:
    mpu_adafruit.acceleration
except:
    pass
'''

LOOP_LOCAL = '''
try:
    mpu.get_accel_data()
except:
    pass
'''

# Benchmarking
local_times = []
adafruit_times = []

for n_sample in range(1,n_samples,50):
    # Local library times
    local_times.append(min(timeit.repeat(
        setup=SETUP_LOCAL,
        stmt=LOOP_LOCAL,
        repeat=2,
        number=n_sample
    )))

    # Adafruit library times
    adafruit_times.append(min(timeit.repeat(
        setup=SETUP_ADAFRUIT,
        stmt=LOOP_ADAFRUIT,
        repeat=2,
        number=n_sample
    )))


# Matplotlib plot
fig = plt.figure()
ax1 = fig.add_subplot(111, label='Local lib')
ax2 = fig.add_subplot(111, label='Adafruit lib')

x_boundary = [0, n_samples]
y_boundary = [0, max(local_times+adafruit_times) + 20]
x_data = list(range(1,n_samples,50))

p1, = ax1.plot(x_data, local_times, 'bo-')
ax1.set_xlim(x_boundary)
ax1.set_ylim(y_boundary)

p2, = ax2.plot(x_data, adafruit_times, 'rx--')
ax2.set_xlim(x_boundary)
ax2.set_ylim(y_boundary)

ax.legend((p1,p2), ('Local library','Adafruit library'), loc='upper right')
plt.show()