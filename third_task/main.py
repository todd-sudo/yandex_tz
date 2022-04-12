from bot import send_news_channel
from config import CHANNEL_NAME


def main():
    send_news_channel(channel_name=CHANNEL_NAME)
    print("#готоводело")


if __name__ == '__main__':
    main()
