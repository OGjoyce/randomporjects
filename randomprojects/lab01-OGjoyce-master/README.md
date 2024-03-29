---
layout: post
title:  "Laboratorio 1"
date:   2017-01-27
category: lab
description: >
    El objetivo de este laboratorio es entrenar su intuición para trabajar con numeros en representación binaria y hexadecimal.
    Y tambien... jugar un poco...
---

#### Ejercicio 1: Alfabeto Binario

Para este ejercicio vamos a utilizar números en su representacion binaria de 4-bits. Si tomamos una pila de 5 números binarios de 4 bits, podemos
hacer patrones e imágenes. Para ayudarlos a visualizar esto, ustedes pueden pensar que los 0's  son blanco y los 1's son negro. Por ejemplo, el
siguiente patrón de bits se mira así:

<table style="text-align: center;">
  <tr>
    <th>Número Binario</th>
    <th>Imagen</th>
  </tr>
  <tr>
    <td>0b0110</td>
    <th rowspan="5"><img style="padding-top:30px;" src="/img/lab1_fig1.png" alt="fig1"></th>
  </tr>
  <tr>
    <td>0b1001</td>
  </tr>
  <tr>
    <td>0b1111</td>
  </tr>
  <tr>
    <td>0b1001</td>
  </tr>
  <tr>
    <td>0b1001</td>
  </tr>
</table>

En los archivos descargados, ustedes tienen el archivo BinaryAlphabet.class y binary.txt, estos archivos les ayudaran a visualizar el patrón
binario. En binary.txt, ustedes pueden escribir cinco lineas, cada una con cuatro 1's y 0's separados por espacio, que representan la
letra que quieren dibujar. Luego de eso, pueden ver el patrón generado ejecutando:

```shell
~ $ java BinaryAlphabet binary.txt
```

**Responder**

En el archivo ejercicio1.py, deben cambiar los valores de las variables globales (eso es lo único que deben hacer)  para responder
a las siguientes preguntas:

1. ¿Cuáles 5 números decimales producen el patrón de la letra "A" mostrada arriba? ¿Cuales 5 números hexadecimales?
2. ¿Qué letra se dibuja con 1, 1, 9, 9, 6? ¿Con 0xF8F88?
3. ¿Qué representación hexadecimal usarían para dibujar la letra S? ¿Qué representación hexadecimal usarían para dibujar la letra D?

Una vez hayan respondido las preguntas, pueden verificar su punteo ejecutando el siguiente comando:

```shell
~ $ make check-ej1
python check.py 1
Calificando Ejercicio: 1
....................
Nota: 40/40
```

Si todas las respuestas estan correctas en el ejercicio, entonces pueden subirl el ejercicio a GitHub:

```shell
~ $ git add ejercicio1.py
~ $ git commit -m "Ejericio 1 terminado"
~ $ git push origin master
```

***

#### Ejercicio 2: Cisco Binary Game

Hagan click [aquí](/assets/games/binary_game.swf) para encontrar el juego, pero si en algún caso tienen problemas con el juego, pueden probar
[este link](http://www.wordfreegames.com/game/binary-game.html). El objetivo es hacer coincidir el numero de la derecha con el representación
binaria sin signo de la izquierda. Esto requiere una combinación de clicking y typing. Y hay presión de tiempo para hacer las cosas mas divertidas.

![figura2](/img/lab1_fig2.png)

El juego progresivamente se va volviendo mas rápido y más difícil. Vean si pueden alcanzar arriba de 20,000 puntos y llegar al nivel 5.

Logren arriba de 18,000 puntos, pausen el juego, tomen un screen shot y guardenlo en su directorio de trabajo con el nombre (**_ejercicio2.png_**).

Para revisar si esta todo en orden, verifiquen su nota con:

```shell
~ $ make check-ej2
python check.py 2
Calificando Ejercicio: 2
....................
Nota: 10/10

```

Si obtienen los 10 puntos, hagan un commit y subanlo a GitHub:

```shell
~ $ git add ejercicio2.py
~ $ git commit -m "Ejericio 2 terminado"
~ $ git push origin master
```

***

#### Ejercicio 3: 1,000 $1 Bills

Si les entregamos mil billetes de $1 y diez sobres. Su trabajo es encontrar una manera de poner una cantidad X de billetes de dólar en cada uno de
los diez sobres, de modo que sin importar la cantidad que uno les pida (entre $1 y $1000), ustedes solo tienen que dar una combinación de esos
sobres asegurándose de dar siempre la cantidad correcta en efectivo.

**Responder**

Una vez tengan su respuesta, en el archivo ejercicio3.py, cambien las variables **_ENV_1 a ENV_10_** con la cantidad de billetes que debe tener
cada sobre. Tomen en cuenta que la suma de todos los billetes debe ser igual a $1,000

Verifiquen su trabajo ejecutando:

```shell
~ $ make check-ej3
python check.py 3
Calificando Ejercicio: 3
....................
Nota: 40/40

```

Una vez mas, deben subir el ejercicio terminado a GitHub.

```shell
~ $ git add ejercicio3.py
~ $ git commit -m "Ejericio 3 terminado"
~ $ git push origin master
```

***

#### Ejercicio 4: Pearls Before Swine

Esta es una versión de un juego bien cool que tiene una solución basada en number representation. Jueguen en el siguiente [link](/assets/games/
pearls3b.swf). Primero jueguen un par de veces y vean si pueden ganar algunos rounds.

![figura3](/img/lab1_fig3.png)

Después de haberlo intentado muchas veces, échenle un vistazo a este [articulo](http://en.wikipedia.org/wiki/Nim) de Wikipedia. Con este nuevo
conocimiento a la mano, ahora ustedes deben de ser capaces de vencer a Juan siempre. Pero siempre va a tomar un poco de practica. Sigan intentado
hasta que puedan ganar seguidamente.

Tomen un screen shot de su mejor partida y guardenla en su directorio con el nombre _**ejercicio4.png**_

Una vez tengan el screen shot en el directorio, pueden verificar la nota del ejercicio ejecutando:

```shell
~ $ make check-ej4
python check.py 4
Calificando Ejercicio: 4
....................
Nota: 10/10
```

o bien, la nota del laboratorio:

```shell
~ $ make check
python check.py
Calificando Todo:

Calificando Ejercicio: 1
....................
Nota: 40/40

Calificando Ejercicio: 2
....................
Nota: 10/10

Calificando Ejercicio: 3
....................
Nota: 40/40

Calificando Ejercicio: 4
....................
Nota: 10/10

TOTAL: 100/100
```

Recuerden hacer commit al terminar, y subir su respuesta final a GitHub:

```shell
~ $ git add *
~ $ git commit -m "Laboratorio 1 terminado"
~ $ git push origin master
```
Y lo mas  importante, agreguen a **_cc3-grades_** como contribuidor al repositorio, de lo contrario no podremos calificar su laboratorio y
tendran <b>0</b> en la nota. Finalmente, suban el link del repositorio al **_GES_**, esto tambien es necesario que les pongamos nota.
