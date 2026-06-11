# Sultanes Nazaríes de Granada

Aplicación web Flask que muestra información sobre los emires y sultanes nazaríes de Granada.

![CI](https://github.com/mafese3/simulacroParcial2/actions/workflows/ci-cd.yml/badge.svg)

## Rutas

| Ruta | Descripción |
|---|---|
| `GET /` | Página principal con la lista de sultanes |
| `GET /health` | Endpoint de salud: devuelve `{"status": "ok"}` |

## Requisitos

- Python 3.12
- Docker (opcional)

## Ejecución local

```bash
pip install -r requirements.txt
flask run
```

## Tests

```bash
pytest tests/ -v
```
