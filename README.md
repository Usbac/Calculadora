# Calculadora

<p align="center">
<img src="https://k62.kn3.net/7/F/1/4/D/D/E55.png">
</p>
  
  
Esta calculadora recibe una operación Infija, la convierte a Postfija y posteriormente la resuelve devolviendo el resultado. 
Escrito en [Python](https://www.python.org) usando la librería de Tkinter.

Debido a algunas limitantes, como no aceptar números negativos o operadores con solo números a la derecha (ej: -5+4), la calculadora sigue estando en estado Beta, por ende su funcionalidad y diseño esta propenso a cambios.

*Ejemplo Operación Infija:* 5 + (4 - 20)

*Ejemplo Operación Postfija:* 5 4 20 - +

## Conversión
Para convertir una operación, se siguen unos pasos específicos pero muy simples. Se recorre la Operación Infija (izq. a der.) y se siguen estas reglas:

* Si el elemento es un numero se guarda en la primera Pila.
* Si el elemento es un operador se guarda en la segunda Pila.
* Si el elemento es un paréntesis cerrado ‘)’ se desapilan los elementos de la segunda Pila y se apilan en la primera hasta encontrar el paréntesis abierto ‘(’ (pero evitando introducir este).
* Si el elemento es un numero con mayor jerarquia que el ultimo numero de la segunda Pila, se desapilan los elementos de la segunda Pila y se apilan en la primera, hasta que su ultimo elemento tenga menor o igual jerarquia al elemento actual, y posteriormente de apila en la segunda Pila el elemento pendiente.

## Características

* Conversión de Infija a Postfija
* Opciones para introducir funciones trigonométricas básicas (Seno, Coseno y Tangente)
* La operación convertida (Postfija) se imprime en la consola después de mostrar el resultado.
* Interfaz gráfica simple y agradable.
