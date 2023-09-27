import asyncio
import socketio

sio = socketio.AsyncClient()
def setRightMotorPwn(pwm):
    print('set right pwm')

def setLeftMotorPWM(pwm):
    print('set Left Motor pwm')

def leftMotorForward():
    print('left motor forward')

def leftMotorBack():
    print('left motorBack')

def rightMotorForward():
    print('right motor forward')

def rightMotorback():
    print('right motor back')

def handleMoveForward(speed):
    leftMotorPwm(100,speed)
    rightMotorPWM(100,speed)
    leftMotorForward()
    rightMotorForward()
    print('forward')

def handleMoveBackward(speed):
    leftMotorPwm(100,speed)
    rightMotorPWM(100,speed)
    leftMotorBack()
    rightMotorback()
    print('backward')

def handleSpinLeft(speed):
    leftMotorPwm(100,speed)
    rightMotorPWM(100,speed)
    leftMotorBack()
    rightMotorForward()
    print('spinleft')

def handleSpinRight(speed):
    leftMotorPwm(100,speed)
    rightMotorPWM(100,speed)
    leftMotorForward()
    rightMotorForward()
    print('spinright')

def handleForwardRight(turnPercentage,speed):
    rightMotorPWM(turnpercentage,speed)
    leftMotorPWM(100, speed)
    leftMotorForward()
    rightMotorForward()

def handleForwardLeft(turnPercentage, speed):
    rightMotorPWM(100,speed)
    leftMotorPWM(turnPercentage, speed)
    leftMotorForward()
    rightMotorForward()

def handleBackRight(turnPercentage, speed):
    leftMotorPWM(100,speed)
    rightMotorPWM(turnPercentage, speed)
    leftMotorForward()
    rightMotorForward()

def handleBackLeft(turnPercentage, speed):
    leftMotorPWM(turnPercentage,speed)
    rightMotorPWM(100, speed)
    leftMotorForward()
    rightMotorForward()

def handleControls(controls):
    speed = (controls['speed']*6)+200
    turnPercentage = controls['angle'] / 0.9

def handleStop():


    print(controls)
    if (controls['direction'] == 'moveForward'):
        handleMoveForward(pwm,speed)
    elif (controls['direction'] == 'moveBack'):
        handleMoveBackward()
    elif (controls['direction'] == 'spinLeft'):
        handleSpinLeft()
    elif (controls['direction']) == 'spinRight':
        handleSpinRight()
    elif (controls['direction'] == 'forwardright'):
        handleForwardRight()
    elif (controls['direction'] == 'forwardLeft'):
        handleForwardLeft()
    elif (controls['direction'] == 'backLeft'):
        handleBackLeft()
    elif (controls['direction'] == 'backright'):
        handleBackRight()
    else:
        print('stop')


@sio.event
async def connect():
    print('connection established')
    await sio.emit('registerBot', {"Id": '12345678', "password":'RobotWorld1!'})


@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.on('setControls')
async def my_message(data):
    print(data['direction'])
    handleControls(data)

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('https://rawbotz.com')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
