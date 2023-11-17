# Snake Game

Este es un clásico juego de Snake implementado en Python con PyGame.

## Descripción 

El objetivo del juego es controlar una serpiente que se mueve alrededor de la pantalla comiendo comida y evitando chocar contra los bordes o contra su propio cuerpo. Cada vez que la serpiente come un pedazo de comida, crece en longitud.

El juego tiene los siguientes elementos:

- La serpiente que controla el jugador con las flechas del teclado
- Comida generada aleatoriamente en la pantalla que la serpiente debe comer
- Enemigos generados aleatoriamente que le restan puntos a la serpiente si choca con ellos
- Puntuación que se incrementa cada vez que la serpiente come un pedazo de comida
- Pantalla de game over cuando la serpiente choca contra sí misma o un borde
- Menú principal con opciones para dificultad y configuración de velocidad
- Guardado de la mejor puntuación obtenida

## Requerimientos

- Python 3
- PyGame

## Controles

- Flecha arriba: Mueve la serpiente hacia arriba
- Flecha abajo: Mueve la serpiente hacia abajo  
- Flecha izquierda: Mueve la serpiente hacia la izquierda
- Flecha derecha: Mueve la serpiente hacia la derecha

## Instalación

1. Clona este repositorio
2. Instala las dependencias con `pip install -r requirements.txt` 
3. Ejecuta `python main.py`

## Personalización

El juego puede personalizarse editando variables como:

- Velocidad de la serpiente
- Tamaño de la serpiente y la comida 
- Colores de la serpiente, comida y fondo
- Cantidad de enemigos por nivel
- Comportamiento de colisión con enemigos

## Créditos

Este juego fue creado por Jhonatan Stiven Guzman Olaya como un proyecto de práctica.
