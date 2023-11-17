import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Adventure")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Variables del juego
snake_size = 20
snake_speed = 15
score = 0
# Variables globales
best_score = 0

enemies = []  # Lista para almacenar posiciones de enemigos

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

# ...

# Función principal del juego
# ...

# Función principal del juego
def game(num_enemies):
    global snake_speed, score,best_score

    snake = [(width // 2, height // 2)]
    snake_direction = (1, 0)

    # Nueva función para generar enemigos
    def spawn_enemy():
        x = random.randrange(0, width - snake_size, snake_size)
        y = random.randrange(0, height - snake_size, snake_size)
        return x, y

    # Nueva función para generar comida
    def spawn_food():
        while True:
            food_position = random.randrange(0, width - snake_size, snake_size), random.randrange(0, height - snake_size, snake_size)
            if food_position not in enemies and food_position not in snake:  # Modificación para evitar que aparezca en la serpiente
                return food_position

    # Inicializa algunos enemigos al comienzo del juego
    for _ in range(num_enemies):  # Disminuye la cantidad de enemigos
        enemies.append(spawn_enemy())

    food = spawn_food()  # Inicializa la comida

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        x, y = snake[0]
        x += snake_direction[0] * snake_size
        y += snake_direction[1] * snake_size
        

        # Lógica para verificar colisiones con enemigos
        for enemy in enemies:
            if (x, y) == enemy:
                score -= 1  # Pierde puntos al chocar con un enemigo
                enemies.remove(enemy)
                enemies.append(spawn_enemy())
                if score >= 0:
                    snake.pop()
             

        # Mueve la serpiente y elimina el último segmento
        snake.insert(0, (x, y))

        # Lógica para verificar colisión con comida
        if (x, y) == food:
            score += 1
            food = spawn_food()
               # Hace crecer la serpiente por 2 segmentos cada vez que la puntuación es un múltiplo de 5
            if score >= 0:
                snake.append(snake[-1])
            # Agrega un nuevo segmento al final de la serpiente
            #snake.append(snake[-1])  # Hace crecer la serpiente

        # Verificar colisiones
        if check_collision(snake, food):
            food = spawn_food()
        else:
            snake.pop()

        if x < 0 or x >= width or y < 0 or y >= height:
            if score > best_score:
                best_score = score
            game_over()

        if len(snake) > 1 and (x, y) in snake[1:]:
            if score > best_score:
                best_score = score
            game_over()

        screen.fill(black)
        draw_snake(snake)
        draw_enemies(enemies)
        draw_food(food)
        draw_score(score)

        pygame.display.flip()
        clock.tick(snake_speed)


# Función para dibujar la serpiente
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(
            screen, white, (segment[0], segment[1], snake_size, snake_size)
        )

# Nueva función para dibujar enemigos
def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.rect(screen, green, (enemy[0], enemy[1], snake_size, snake_size))

# Función para dibujar la comida
def draw_food(food):
    pygame.draw.rect(screen, red, (food[0], food[1], snake_size, snake_size))


# Función para generar comida de manera aleatoria
def spawn_food():
    x = random.randrange(0, width - snake_size, snake_size)
    y = random.randrange(0, height - snake_size, snake_size)
    return x, y


# Función para verificar colisiones con la comida
def check_collision(snake, food):
    return snake[0] == food


# Función para mostrar el puntaje
def draw_score(score):
    score_text = font.render(f"Puntuación: {score}", True, white)
    screen.blit(score_text, (10, 10))


# Función para mostrar el nivel
def draw_level(level):
    level_text = font.render(f"Level: {level}", True, white)
    screen.blit(level_text, (width - 100, 10))


# Función para mostrar la pantalla de Game Over
def game_over():
    global score, enemies,best_score
    # Restablece la puntuación y la lista de enemigos
    # Actualiza la mejor puntuación si la puntuación actual es mayor
    if score > best_score:
        best_score = score
    score = 0
    enemies = []
    game_over_text = font.render("Game Over", True, white)
    screen.blit(game_over_text, (width // 2 - 70, height // 2 - 20))
    pygame.display.flip()
    pygame.time.delay(3000)  # Espera 3 segundos antes de cerrar
    main_menu()


# Menú principal
def main_menu():
    global best_score
    selected_option = 0
    options = ["Fácil", "Medio", "Duro"]

    while True:
        screen.fill(black)
        title_text = font.render("Snake Adventure", True, white)
        screen.blit(title_text, (width // 2 - 150, height // 2 - 100))

        # Muestra la mejor puntuación en el menú principal
        best_score_text = font.render(f"Mejor Puntuación: {best_score}", True, white)
        screen.blit(best_score_text, (width // 2 - 100, height // 2 + len(options) * 50))

        for i, option in enumerate(options):
            text = font.render(option, True, white)
            pos = (width // 2 - 50, height // 2 + i * 50)
            screen.blit(text, pos)

            if i == selected_option:
                pygame.draw.rect(
                    screen,
                    white,
                    (pos[0] - 10, pos[1], text.get_width() + 20, text.get_height()),
                    2,
                )
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        num_enemies = 3  # Ajusta la cantidad de enemigos para Fácil
                    elif selected_option == 1:
                        num_enemies = 6  # Ajusta la cantidad de enemigos para Medio
                    elif selected_option == 2:
                        num_enemies = 9  # Ajusta la cantidad de enemigos para Duro

                    # llamada a la función game
                    game(num_enemies)


if __name__ == "__main__":
    main_menu()

