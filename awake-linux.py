from pyautogui import moveTo, position
from time import sleep

version = "1.0"

logo = f"""

##############################################
#  █████╗ ██╗    ██╗ █████╗ ██╗  ██╗███████╗ #
# ██╔══██╗██║    ██║██╔══██╗██║ ██╔╝██╔════╝ #
# ███████║██║ █╗ ██║███████║█████╔╝ █████╗   #
# ██╔══██║██║███╗██║██╔══██║██╔═██╗ ██╔══╝   #
# ██║  ██║╚███╔███╔╝██║  ██║██║  ██╗███████╗ #
# ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ #
##############################################
For Linux by dertfin1 | v{version}
"""


def main():
    while True:
        pos = [position().x, position().y]
        moveTo(pos[0] + 1, pos[1] + 1)
        sleep(3 * 60)
        moveTo(pos[0], pos[1])
        sleep(3*60)


print("Program can't run as module!")

if __name__ == '__main__':
    print(logo)
    main()
