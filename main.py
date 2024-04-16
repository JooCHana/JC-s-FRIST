class Car:

    fdj='b型'
    def __init__(self.seat):
    self.seat=seat

    #类内方法
    def car_seat(self):
        print("这是{}车座...".format(Car.seat))

    def car_fdj(self):
        print("这是{}发动机...".format(Car.seat))

print(Car.seat)
print(Car.fdj)
# 第一年
carA=Car()
carA.car_seat()
carA.car_fdj()

carB=Car()
carB.car_seat()
carB.car_fdj()

# 第二年
Car.seat='aa'
Car.seat='bb'
carA=Car()
carA.car_seat()
carA.car_fdj()

carB=Car()
carB.car_seat()
carB.car_fdj()

# 第三年
Car.fdj='bb'
carA=Car()
carA.car_seat()
carA.car_fdj()

carB=Car()
carB.car_seat()
carB.car_fdj()