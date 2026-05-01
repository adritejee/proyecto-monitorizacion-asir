# Sistema de monitorización de variables de proceso

## Descripción
Este proyecto consiste en el desarrollo de un sistema de monitorización de variables de proceso en un entorno Linux, capaz de generar datos simulados, almacenarlos en MySQL y visualizarlos mediante Grafana.

## Tecnologías utilizadas
- Python
- MySQL
- Grafana
- systemd
- Linux (Ubuntu Server)

## Estructura del proyecto
- scripts/simulacion_proceso.py → script principal
- scripts/simulacion_v1.py → versión inicial
- scripts/simulacion_v2.py → versión intermedia

## Funcionamiento
El sistema genera datos de forma periódica, los almacena en MySQL y los muestra en Grafana mediante dashboards. Además, permite la configuración de alertas para detectar valores fuera de rango.

## Repositorio
Este repositorio contiene el código fuente del sistema desarrollado en el proyecto.

## Autor
Adrián Tejedor  
Proyecto TFG – Administración de Sistemas Informáticos en Red (ASIR)
