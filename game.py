import pygame
import random

main_score = 0


# устанавливаем фон игры
def set_fone(fon):
    if fon == 'Белый':
        return 255, 255, 255
    elif fon == 'Жёлтый':
        return 238, 221, 130
    elif fon == 'Красный':
        return 240, 128, 128
    elif fon == 'Зеленый':
        return 60, 179, 113
    elif fon == 'Синий':
        return 135, 206, 250
    else:
        return 245, 245, 220


# выбор скорости игры
def set_speed(speed):
    if speed == 'Легкий':
        return 500
    elif speed == 'Средний':
        return 250
    elif speed == 'Тяжелый':
        return 100
    else:
        return 50


# изменяем данные по кол-во очков
def set_score(score):
    global main_score
    main_score = score


# отправляем очки с предыдущей игры
def get_score():
    return main_score


# стартуем всю игру
def start(fon, speed, volume):
    FON = set_fone(fon)
    SPEED = set_speed(speed)
    BLACK = (0, 0, 0)

    HEIGHT = 450  # высота окна
    WIDTH = 700  # ширина окна
    FPS = 30  # частота обновления кадра

    # создаем окно и игру
    pygame.init()  # самый старт всего
    # создаем окно для игры
    screen = pygame.display.set_mode((WIDTH, HEIGHT), not pygame.RESIZABLE)
    # обновление экрана
    pygame.display.update()
    # название для игры
    pygame.display.set_caption("DinoGame")
    # создание времени работы( для ФПС )
    clock = pygame.time.Clock()
    # музыка
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(volume * 0.01)
    pygame.mixer.music.play()

    # загружаю динозаврика
    dino = pygame.image.load('dino.png')
    final_dino = pygame.transform.scale(dino, (50, 50))  # установка 50Х50
    # создаем кактус и изменяем размер
    cactus = pygame.image.load('cactus.png')
    final_cactus = pygame.transform.scale(cactus, (50, 50))
    # создаем картинку облака
    cloud = pygame.image.load('cloud.png')
    final_cloud = pygame.transform.scale(cloud, (50, 50))
    # создаем картинку птеродактеля
    pterod = pygame.image.load('pterod.png')
    final_pterod = pygame.transform.scale(pterod, (50, 50))
    # сидячий дино
    sit = pygame.image.load('sit.png')
    final_sit = pygame.transform.scale(sit, (50, 50))
    # дино бежит
    dino_run = pygame.image.load('dino_run.png')
    final_run = pygame.transform.scale(dino_run, (50, 50))

    # отрисовка текста
    font = pygame.font.Font(None, 25)  # стиль шрифта и размер его

    # слежка за временем для анимации дино
    time = 0
    # количесто очков
    score = 0

    # координаты для птеродактеля
    pterod_pos = {
        "x": 1000,
        "y": 150,
        "speed": 15
    }
    # координаты для облака
    cloud_pos = {
        "x": 100,
        "y": 100,
        "speed": 7
    }
    # Координаты для кактуса
    cactus_pos = {
        "x": 700,  # Икс координата
        "y": 300,  # Игрик координата
        "speed": 15  # Скорость кактуса
    }
    # Координаты для дино
    dino_pos = {
        "x": 200,
        "y": 300
    }
    # переменные для прыжка
    is_up = False  # переменная для прыжка вверх
    is_down = False  # переменная для падения
    # проверка на сидит ли дино
    is_sit = False
    # переменная для прыжка скорость
    index = 40
    # переменная для камня
    stone_pos = {
        'x': 400
    }

    # цикл игры
    running = True  # значит, что игра будет работать
    while running:  # пока переменная = True - игра работает
        # изменяем скорость игры каждые 200 очков
        if score % SPEED == 0:
            pterod_pos["speed"] += 2
            cloud_pos["speed"] += 2
            cactus_pos["speed"] += 2
        clock.tick(FPS)  # контрлирует скорость игра
        # ввод каждого события в игру
        for event in pygame.event.get():
            # если мы нажали на крестик
            if event.type == pygame.QUIT:
                # заканчиваем игру
                running = False
            # обработка нажатия кнопок
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # прыжок
                    if not is_up and not is_down:  # когда дино не прыгает
                        is_up = True  # начать прыжок
                    # присид
                if event.key == pygame.K_DOWN:
                    is_sit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                        is_sit = False
        # расчеты игр
        # ведём отсчет игры
        time = time + 1
        # движение кактуса влево со скоростью Speed
        cactus_pos["x"] = cactus_pos["x"] - cactus_pos["speed"]
        # если кактус уехал за границу
        if cactus_pos["x"] < -50:
            # телепортируем вправо
            cactus_pos["x"] = random.randint(600, 1400)
        # движение облака
        cloud_pos["x"] = cloud_pos["x"] - cloud_pos["speed"]
        if cloud_pos["x"] < -50:
            cloud_pos["x"] = 700
        # движение птеродактеля
        pterod_pos["x"] = pterod_pos["x"] - pterod_pos["speed"]
        if pterod_pos["x"] < -50:
            pterod_pos["x"] = random.randint(1500, 2000)
        stone_pos["x"] = stone_pos["x"] - cactus_pos["speed"]
        # если кактус уехал за границу
        if stone_pos["x"] < -50:
            # телепортируем вправо
            stone_pos["x"] = 700
        # проверка на столкновение с кактусом
        if dino_pos["x"] + 50 > cactus_pos["x"] and cactus_pos["x"] + 50 > dino_pos["x"]:
            if dino_pos["y"] + 40 > cactus_pos["y"]:
                # остановка игры
                running = False
        # подсчет очков
        score += 1
        score_text = font.render(str(score), True, BLACK)  # текст, сглаживание, цвет
        text = font.render('Ваш счет: ', True, BLACK)
        # если дино подерыгнул
        if is_up:
            # изменяем координату У
            dino_pos["y"] = dino_pos["y"] - index
            # изменяем скорость прыжка
            index = index - 1
            # если дино достигает 200 пикселей
            if dino_pos["y"] < 200:
                index = 0  # дино останавливается в полете
                is_up = False  # теперь дино вверх не летить
                is_down = True  # начинает падать вниз
        # если ДИНО падает вниз
        if is_down:
            dino_pos["y"] = dino_pos["y"] + index
            # увеличиваем скорость падения
            index = index + 1
            # Когда дино упал на землю
            if dino_pos["y"] > 300:
                # корректируем позицию
                dino_pos["y"] = 300
                # устанавливаем скорость
                index = 40
                # останавливаем процессы
                is_up = False
                is_down = False
        # создание цветов
        screen.fill(FON)
        # отрисовка земли
        pygame.draw.rect(screen, BLACK, [
            0,  # Х координата
            320,  # У координата
            700,  # ширина
            1,  # высота
        ])
        pygame.draw.rect(screen, BLACK, [
            stone_pos['x'],  # Х координата
            380,  # У координата
            20,  # ширина
            5,  # высота
        ])
        # отрисовка дино
        if is_sit:
            screen.blit(final_sit, (dino_pos["x"], dino_pos["y"]))
        else:
            if time >= 15:
                screen.blit(final_dino, (dino_pos["x"], dino_pos["y"]))
            else:
                screen.blit(final_run, (dino_pos["x"], dino_pos["y"]))
        if time == 30:
            time = 0
        # отрисовка кактуса
        screen.blit(final_cactus, (cactus_pos["x"], cactus_pos["y"]))
        # отрисовка облака
        screen.blit(final_cloud, (cloud_pos["x"], cloud_pos["y"]))
        # отрисовка птеродактеля
        screen.blit(final_pterod, (pterod_pos["x"], pterod_pos["y"]))
        # отрисовка текста
        screen.blit(score_text, (120, 20))
        screen.blit(text, (20, 20))
        # вывод их на экран
        pygame.display.flip()
    # изменяем кол-во очков для меню
    set_score(score)
    # ЗАКРЫТИЕ ИГРЫ
    pygame.quit()
