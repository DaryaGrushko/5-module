#Дополнительное практическое задание по модулю: "Классы и объекты."
#Задание "Свой YouTube"

import time
class User:
    def __init__(self, nickname, password, age):

        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title, duration = 0, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return (self.title)

class UrTube:

    def __init__(self, users=[], videos=[], current_user =''):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname='', password=''):
        #self.current_user = None

        if nickname=='':
            return 0
        else:
            for user in self.users:
                if nickname in user.nickname:
                    if user.password != hash(password):
                        print ('Введен неверный пароль')
                    else:
                        if user.age<18:
                            print ('Вам нет 18 лет, пожалуйста, покиньте страницу')
                        else:
                            self.current_user = nickname

    def register(self, nickname, password, age):
        #print('==================', '[', ur.current_user, ']','-', nickname, password, age)
        call = 0
        if self.users != []:
            for user in self.users:
                if nickname in user.nickname:

                    print (f'Пользователь {nickname} уже существует')
                    call = 1
                else:

                    print ('Нет такого пользователя')
                    if call != 1 :
                        self.users.append(User(nickname, hash(password), age))
        else:
                    self.users.append(User(nickname, hash(password), age))
        UrTube.log_in(self, nickname, password)
        return self.current_user

    def log_out(self):
        self.current_user = None

    def add(self, *args, **kwargs):
        for ar in args:
            self.videos.append(ar)

    def get_videos(self, search_word):
        findlist = []
        for vid in self.videos:
            if search_word.lower() in vid.title.lower():
                findlist.append(vid.title)
        return findlist

    def watch_video(self, name_film):
        if self.current_user!='':
            flag = 0
            for vid in self.videos:
                if name_film in vid.title:
                    sec = 1
                    while sec < int(vid.duration)+1:
                        print (sec , end = ' ')
                        sec+=1
                        time.sleep(1)
                    print('Конец видео')
                    flag = 1

            if flag == 0:
                print('Такого фильма нет')

        else:
            print ('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')


ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin55555', 'F8098FM8fjm9jmi', 55)




print( ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')