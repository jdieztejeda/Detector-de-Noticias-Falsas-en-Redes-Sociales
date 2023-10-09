# Detector de Noticias Falsas en Redes Sociales

## Descripción del Proyecto

Este proyecto se enfoca en la detección de noticias falsas en las redes sociales utilizando técnicas de Big Data y modelado de Inteligencia Artificial (IA). A lo largo de esta introducción, exploraremos cómo recopilamos los datos de diversas plataformas, procesamos esos datos con Apache Spark, desarrollamos modelos de IA y probamos la efectividad del detector en diferentes contextos.

## Recopilación de Datos

Para obtener información de diversas redes sociales, empleamos una variedad de enfoques:

- **Kaggle**: Sacamos de Kaggle diferentes datasets de noticias tanto falsas como verdaderas para poder entrenar al modelo.

- **Twitter**: Conectamos con la API de Twitter para obtener tweets relacionados con noticias de diversos temas.

- **Reddit**: Empleamos la API de Reddit para acceder a comentarios de comunidades y publicaciones específicasde diversos temas .

## Procesamiento de Datos con Apache Spark

Los datos recopilados se procesaron con Apache Spark para unificarlos en un solo dataframe, lo que facilitó su posterior análisis y entrenamiento de modelos.

## Desarrollo de Modelos de IA

Desarrollamos dos modelos de IA para detectar noticias falsas:

- **Modelo en Python**: Creamos un modelo en Python utilizando Arboles de decisión y el algoritmo de Random Forest, lo que nos brindó un mayor rendimiento en contextos específicos.

## Análisis de Datos de Entrenamiento

Antes de construir los modelos, realizamos un análisis exhaustivo sobre equilibrio de los datos, ya que la informaciñon que usa el modelo tiene que estar balanceada.

## Etiquetado de Comentarios en Redes Sociales

Utilizamos los modelos de IA desarrollados para etiquetar las noticias recopiladas de las redes sociales como posibles fake news o noticias legitimas. Esta clasificación resulta valiosa para comprender y analizar la cantidad de informacion falsa que hay en las redes sociales.

## Visualización

Tiene un peso muy importante la representación de los resultados obtenidos después del análisis. La visualización de los resultados que hemos obtenido con el análisis de las noticias sacadas de las fuentes de datos en streaming las visualizamos con las librerías que ofrece Python de Seaborn y Matplotlib. Los resultados que sacamos del modelo nos los mostraba en forma de array, por lo que tuvimos que convertir ese array con las soluciones en un dataframe para poder visualizarlo y que las librerías puedan interpretar los resultados. De esta forma, conseguimos sacar las gráficas que estábamos buscando con los resultados obtenidos del análisis del modelo sobre las noticias sacadas de las redes sociales.

## Conclusiones

Los beneficios de este proyecto se verán reflejados en la veracidad del contenido que consumimos. Nuestra meta es informar al usuario, ya sea una persona natural o jurídica, acerca de un tema particular o una publicación. Esta tarea nos ha planteado una problemática interesante, ya que al identificar qué temas son más vulnerables que otros, podemos determinar la sensibilidad en torno a estos temas o la posible manipulación que podría surgir en el futuro.

La desinformación y la manipulación son cuestiones críticas en la era de la información, y este proyecto busca implementar una solución para abordar este desafío. Nuestra herramienta no solo puede identificar noticias falsas, sino que también puede ayudar a los usuarios a ser más críticos y conscientes del contenido que consumen en las redes sociales y otras plataformas en línea. A medida que avanzamos en esta era digital, la importancia de combatir la desinformación se vuelve cada vez más evidente, y este proyecto es un paso hacia un entorno de información más confiable y veraz.


## Contribución y Contacto

¡Apreciamos las contribuciones! Si deseas colaborar con este proyecto o tienes preguntas, no dudes en contactarnos.

**Proyecto Realizado por:**
Javier Diez Tejeda
Ismael Tse Perdomo Rodríguez
Roberto Tortoledo Arroyo


Gracias por tu interés en nuestro proyecto de Detector de Noticias Falsas en Redes Sociales.
