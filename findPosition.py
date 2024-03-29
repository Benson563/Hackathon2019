import pyautogui,time

#a script to automate the moving of mouse to center of screen and click on plan for hulu
def printPosition():

    #the code below prints the x,y coordinates. Recommended display size is 3840x2160
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionString, end='')
            print('\b' * len(positionString), end='', flush=True)

    except KeyboardInterrupt:
        print('\nDone.')

if __name__ == '__main__':
    printPosition()