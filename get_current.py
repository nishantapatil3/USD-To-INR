from fixerio import Fixerio


def get_usd_inr():
    current = Fixerio(base='USD', symbols=['USD', 'INR'])
    return current.latest()


def main():
    current = get_usd_inr()
    print current

    print current["date"] + "T00:00:00Z"
    print current["rates"]

if __name__ == '__main__':
    main()
