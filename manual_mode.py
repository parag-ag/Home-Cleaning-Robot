def start_manual_mode(robot):
    print("f - forward, b - backward, s - stop, r - turn-right, l - turn-left, e - exit")
    while 1:
        ins = input()
        if ins == 'f':
            robot.forward()
        elif ins == 'b':
            robot.backward(1)
        elif ins == 's':
            robot.stop()
        elif ins == 'r':
            robot.turn_right(1)
        elif ins == 'l':
            robot.turn_left(1)
        elif ins == 'e':
            robot.stop_cleaning()
            robot.stop()
            break
        else:
            print('Invalid Instruction Given!!') 