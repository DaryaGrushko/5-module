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

    def __init__(self, users=[], videos=[], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname='', password=''):

        #print ('1. НАЧИНАЕМ ВХОД В УЧЕТКУ', nickname, password)
        #print('self.users = ', self.users)
        if nickname=='':
            return 0
        else:
            for user in self.users:
                #print ('user = ', user)
                if nickname in user.nickname:
                    #print('2 - нашли ПОЛЬЗОВАТЕЛЯ ', nickname)
                    if user.password != hash(password):
                        print ('Введен неверный пароль')
                    else:
                        #print('3 - проверили пароль, совпал ')
                        #print ('передали age = ', user.age)
                        self.current_user = User(nickname, hash(password), user.age)
                        #print('4. вошли. Текущий пользователь : ', self.current_user)
                        #print ('***********self.current_user = ', self.current_user, 'age = ', self.current_user.age, 'nickname = ', self.current_user.nickname, 'password = ', self.current_user.password)
                        return self.current_user

    def register(self, nickname, password, age):
        #print('=начало регистрации=====', 'тек польз[', ur.current_user, ']','- переданы:', nickname, password, age)
        call = 0
        if self.users != []:

            for user in self.users:

                #print ('№1 -  Регистрация. Начинаем перебор по записям в User: первый цикл ' , user.nickname,', ', user.password,', ', user.age)
                if nickname in user.nickname:
                    print (f'Пользователь {nickname} уже существует')
                    return self.current_user
                else:
                    #print ('Нет такого пользователя')
                    self.users.append(User(nickname,hash(password),age))
                    #print('ДОБАВЛЕН - ', '[', nickname, ']', '-', nickname, password, age)
                    #print ('User = ',  self.users)
                    #print('~~~Сейчас буду входить в учетку:', nickname, password)
                    UrTube.log_in(self, nickname, password)
                    break
        else:
                    self.users.append(User(nickname, hash(password), age))
                    #self.users.append({'nickname': nickname, 'password': hash(password), 'age': age})
                    #print('ДОБАВЛЕН2 - ', '[', nickname, ']', '-', nickname, password, age)
                    #print('User = ',  self.users)
                    #print('~~~Сейчас буду входить в учетку:', nickname, password)
                    UrTube.log_in(self, nickname, password)
        return self.current_user

    def log_out(self):
        self.current_user = None

    def add(self, *args, **kwargs):
        #print ('=============я в add');
        #print ('список  с видео сохраненными self.videos = ', self.videos)
        #print ('*args = ', *args)

        for ar in args:
            flag = 0
            #print('ar=', ar, ', ar.title =', ar.title, ', ar.duration =', ar.duration, ', ar.time_now =', ar.time_now, ', ar.adult_mode =', ar.adult_mode)
            if self.videos!=[]:
                for video in self.videos:
                    #print('Начинаем перебор видео video=', video)
                    if ar.title == video.title:
                        #print ('Такой фильм уже есть')
                        flag = 1
                #print ('flag = ', flag)
                if flag !=1: # Нашелся фильм с таким именем
                    self.videos.append(Video(ar.title, ar.duration, ar.time_now, ar.adult_mode))
                    #print('2- Видео "', ar, '" добавлено')
                    break
            else:
                self.videos.append(Video(ar.title, ar.duration, ar.time_now, ar.adult_mode))
                #print('Видео "', ar, '" добавлено')



    def get_videos(self, search_word):
        #print ('==============я в get_videos============ищем = ', search_word)
        findlist = []
        for video in self.videos:
            #print ('video = ', video)
            if search_word.lower() in video.title.lower():
                findlist.append(video.title)
        return findlist

    def watch_video(self, name_film):
        #print ('==я в watch_video')
        #print('5. Проверяем учетку перед просмотром видео. Пользователь текущий:', self.current_user)
        if self.current_user!= None:
            flag = 0
            #print('5. Проверяем учетку перед просмотром видео. Пользователь текущий:', self.current_user)
            #print ('self.current_user.age = ', self.current_user.age)
            if self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            else:
                #print ('~~~~~~~ что смотреть будем?')
                for video in self.videos:
                    if name_film in video.title:
                        flag = 1
                        #print('~~~~~~~ видео  -',  name_film)
                        for sec in range(video.duration+1):
                            print (sec , end = ' ')
                            sec+=1
                            time.sleep(1)

                        print('Конец видео')
                if flag != 1:
                    print('Такого фильма нет')
        else:
            print ('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 1, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 2, adult_mode=True)
v4 = Video('Для чего ', 2)

# Добавление видео
ur.add(v1, v2)

ur.add(v3)
ur.add(v4)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('20'))
print ('----------------')

# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')
print ('----------------')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')
print ('----------------')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')
print ('----------------')
# Проверка входа в другой аккаунт

ur.register('vasya_pupkin55555', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')
