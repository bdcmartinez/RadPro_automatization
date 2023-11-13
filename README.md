# RadPro_automatization
# Radiación Ionizante - Calculadora Automatizada

## Descripción
Este programa es una herramienta automatizada diseñada para interactuar con el sitio web "http://www.radprocalculator.com/Gamma.aspx". Utiliza Selenium, una herramienta de automatización de navegadores, para recoger datos de radiación de varios radioisótopos. Es especialmente útil en campos como la investigación nuclear o médica para el análisis de la radiación de diferentes isotopos.

## Funcionalidades
- **Inicialización Automática del Navegador**: Inicia una sesión en Chrome y abre la URL del calculador de radiación.
- **Configuración de Parámetros de Radiación**: Permite la selección y configuración de unidades de dosis, unidades de actividad, tipo de armadura, distancia, y selección de isotopos.
- **Recopilación de Datos de Radiación**: Calcula y recopila datos de radiación para diferentes configuraciones de espesor de armadura y radioisótopos.
- **Almacenamiento de Datos**: Los datos recopilados se almacenan en listas de NumPy para su posterior análisis.

## Requisitos
- Python 3.x
- Selenium WebDriver
- Navegador Chrome
- Librerías: time, pandas, numpy

## Uso
1. Ejecute el script `python <nombre_del_script>.py`.
2. El script iniciará automáticamente el navegador Chrome y navegará a la página de cálculo.
3. El script interactuará con la página web, configurará los parámetros deseados y recopilará los datos de radiación.
4. Los datos recopilados se almacenarán en listas de NumPy para su análisis.

## Notas Importantes
- Este script depende de la estructura actual del sitio web mencionado; cualquier cambio en el sitio puede requerir una actualización del script.
- Asegúrese de tener la última versión de Chrome y Selenium WebDriver instalados para evitar problemas de compatibilidad.

## Licencia
[Incluir detalles de la licencia aquí, si los hay]

## Contacto
[Incluir información de contacto o del autor aquí]

---

Este README proporciona una descripción general del funcionamiento y propósito del programa. Para más detalles, por favor revise el código fuente o contacte al desarrollador.
