# Huffman Python Project

Este proyecto implementa un codificador y decodificador de Huffman en Python. El algoritmo de Huffman es un método de compresión de datos sin pérdida que utiliza un árbol binario para representar los caracteres de una cadena de texto de manera eficiente.

## Estructura del Proyecto

```
huffman-python
├── src
│   ├── huffman
│   │   ├── __init__.py
│   │   ├── encoder.py
│   │   └── decoder.py
│   └── main.py
├── tests
│   └── test_huffman.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener `pip` instalado y ejecuta:

```
pip install -r requirements.txt
```

## Uso

1. Ejecuta el programa principal:

```
python src/main.py
```

2. Introduce la cadena de texto que deseas codificar.

3. El programa mostrará la representación codificada de la cadena y la decodificará de vuelta a su forma original.

## Pruebas

Para ejecutar las pruebas unitarias, utiliza `pytest`:

```
pytest tests/test_huffman.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o un pull request en el repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.