import time
from selfcaffeinate import SelfCaffeinate


def main():
    print("Self caffeinating")
    SLEEP_PERIOD = 60
    sc = SelfCaffeinate()
    for i in range(0, 60):
        print("Sleeping {}".format(SLEEP_PERIOD))
        time.sleep(SLEEP_PERIOD)


if __name__ == "__main__":
    main()
