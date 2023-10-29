# Импорт необходимых модулей
import pygame
import time

# Инициализация Pygame
pygame.init()

# Установка размеров окна
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Простая хоррор-игра")

# Инициализация часов и других переменных
clock = pygame.time.Clock()
done = False
font = pygame.font.Font(None, 36)

# Загрузка изображений и настройка текста
txt_1 = font.render("Дверь 1 или 2 (Нажми на кнопку на клавиатуре)?", True, (255, 255, 255))
txt_note = font.render("Записка", True, (0, 0, 0))
txt_key = font.render("Ключи в 4-й комнате. 3 или 4?(Нажми на кнопку на клавиатуре)", True, (0, 0, 0))
txt_room3 = font.render("Ключи найдены!", True, (0, 0, 0))
txt_room4 = font.render("Выберите 3 или 4", True, (0, 0, 0))

# Установка начальных значений для отображения элементов
note_visible = False
text_visible = True
room_choice = None

# Загрузка изображений фона и звуковых эффектов
bg_1 = pygame.image.load('1.jpg')
bg_1 = pygame.transform.scale(bg_1, (800, 600))
bg_2 = pygame.image.load('i.jpg')
bg_2 = pygame.transform.scale(bg_2, (800, 600))
scary_1 = pygame.image.load('1.jpg')
scary_1 = pygame.transform.scale(scary_1, (800, 600))
scary_3 = pygame.image.load('4.jpg')
scary_3 = pygame.transform.scale(scary_3, (800, 600))
scary_4 = pygame.image.load('2.jpg')
scary_4 = pygame.transform.scale(scary_4, (800, 600))
scary_5 = pygame.image.load('5.jpg')
scary_5 = pygame.transform.scale(scary_5, (800, 600))
note_img = pygame.image.load('note.png')
note_img = pygame.transform.scale(note_img, (200, 200))

# Инициализация звуковых эффектов
pygame.mixer.init()
scream_sound = pygame.mixer.Sound('krik.wav')
win_sound = pygame.mixer.Sound('win.wav')
lose_sound = pygame.mixer.Sound('lose.wav')

# Инициализация фоновой музыки
pygame.mixer.music.load('fon.wav')
pygame.mixer.music.play(-1)

# Инициализация флагов и состояний игры
er = 1
game_over = False

# Главный игровой цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Действия при выборе двери 1
            if event.key == pygame.K_1:
                er = 0
                screen.blit(scary_1, (0, 0))
                pygame.display.flip()
                time.sleep(3)
                screen.blit(scary_3, (0, 0))
                scream_sound.play()
                game_over = True
                note_visible = False
                text_visible = True
                room_choice = None
            # Действия при выборе двери 2
            elif event.key == pygame.K_2:
                note_visible = True
                text_visible = False
                bg_1 = bg_2
                room_choice = 2
            # Действия при выборе комнаты 3
            elif event.key == pygame.K_3 and room_choice == 2:
                note_visible = False
                text_visible = False
                lose_sound.play()
                bg_1 = scary_4
                room_choice = 4
            # Действия при выборе комнаты 4
            elif event.key == pygame.K_4 and room_choice == 2:
                note_visible = False
                text_visible = False
                win_sound.play()
                bg_1 = scary_5
                room_choice = 3

    # Отображение фона и текста
    if er == 1:
        screen.blit(bg_1, (0, 0))
        if text_visible:
            screen.blit(txt_1, (250, 250))

    # Отображение скримера
    if game_over:
        screen.blit(scary_3, (0, 0))

    # Обработка клика на записке
    if note_visible and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if 300 < event.pos[0] < 500 and 200 < event.pos[1] < 400:
            text_visible = True

    # Отображение записки и текста на ней
    if note_visible:
        screen.blit(note_img, (300, 200))
        if text_visible:
            screen.blit(txt_note, (200, 250))
            screen.blit(txt_key, (200, 300))

    # Обновление экрана и установка FPS
    pygame.display.flip()
    clock.tick(60)

# Выход из Pygame
pygame.quit()
