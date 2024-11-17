from colorama import init, Fore, Style

init(autoreset=True)

services = [
    "https://t.me/{username}",
    "https://vk.com/{username}",
    "https://ok.ru/{username}",
    "https://dzen.ru/{username}",
    "https://github.com/{username}",
    "https://www.instagram.com/{username}",
    "https://twitter.com/{username}",
    "https://rutube.ru/channel/{username}",
    "https://music.yandex.ru/users/{username}",
    "https://www.youtube.com/{username}",
    "https://www.linkedin.com/in/{username}",
    "https://www.reddit.com/user/{username}",
    "https://www.pinterest.com/{username}",
    "https://soundcloud.com/{username}",
    "https://www.tumblr.com/{username}",
    "https://steamcommunity.com/id/{username}",
    "https://www.medium.com/@{username}",
    "https://www.flickr.com/people/{username}",
    "https://dev.to/{username}",
    "https://stackoverflow.com/users/{username}",
    "https://about.me/{username}",
    "https://keybase.io/{username}",
    "https://dribbble.com/{username}",
    "https://www.behance.net/{username}",
    "https://twitch.tv/{username}",
    "https://forum.ru-board.com/{username}",
    "https://pikabu.ru/@{username}"
]

def main():
    print(Fore.CYAN + Style.BRIGHT + "Введите никнейм:")
    username = input().strip()
    
    if not username:
        print(Fore.RED + "Вы не ввели никнейм!")
        return
    
    print(Fore.GREEN + Style.BRIGHT + "\nВот ссылки с вашим никнеймом:\n")
    for service in services:
        print(Fore.YELLOW + service.format(username=username))
        print(Fore.MAGENTA + "-" * 50)

if __name__ == "__main__":
    main()