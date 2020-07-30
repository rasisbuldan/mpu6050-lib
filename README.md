# mpu6050-lib
MPU6050 Python Implementation spinoff using smbus to provide device register read/write, hopefully faster reading on acceleration value.

## Usage
```python
import mpu6050

mpu = mpu6050.MPU6050(i2c_addr=0x68, g_range='2g', sample_rate='1000')

# Flat trim offset value
mpu.reset_offset()

# Get acceleration data
mpu.get_accel_data() # return acceleration value tuple (x,y,z)
```

## Benchmark
Initial version of this library on a par with Adafruit MPU6050 CircuitPython Library shown by this sequential read of acceleration value. Not bad.
![Starting Dark Mode](extras/bench-graph.png?raw=True)

## To do
- Implement FIFO buffer for consistent throughput
