# Sistema de Registro de Visitantes

Aplicación de escritorio desarrollada con Python y Tkinter para gestionar el flujo de visitantes en una oficina.

## Requisitos
- Python 3.x (sin librerías externas)

## Cómo ejecutar
```bash
python main.py
```

## Arquitectura
El proyecto sigue una arquitectura modular por capas:
- `modelos/` → Clase Visitante (atributos)
- `servicios/` → Lógica CRUD
- `ui/` → Interfaz gráfica con Tkinter
- `main.py` → Punto de entrada