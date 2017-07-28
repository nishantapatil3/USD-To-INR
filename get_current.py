from fixerio import Fixerio
from get_exchange_info import *


def get_usd_inr():
    current = Fixerio(base='USD', symbols=['USD', 'INR'])
    return current.latest()


def main():
    current = get_google_exchange()
    print current

    

if __name__ == '__main__':
    main()
