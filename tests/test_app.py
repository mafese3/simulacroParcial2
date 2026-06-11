"""
Suite de pruebas para la aplicación Flask – Sultanes Nazaríes de Granada.

Convenciones:
  - Patrón AAA: Arrange → Act → Assert en cada test.
  - Nombre de función = descripción técnica corta.
  - Docstring      = descripción legible para `pytest -v`.
"""

import pytest
from app import app as flask_app


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def app():
    """Instancia de la app Flask configurada para pruebas."""
    flask_app.config.update({"TESTING": True})
    yield flask_app


@pytest.fixture
def client(app):
    """Cliente HTTP de pruebas proporcionado por Flask."""
    return app.test_client()


# =============================================================================
# GET /health
# =============================================================================

def test_health_returns_200(client):
    """GET /health responde con código HTTP 200."""
    # Arrange
    endpoint = "/health"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200


def test_health_response_body(client):
    """GET /health devuelve exactamente {"status": "ok"}."""
    # Arrange
    endpoint = "/health"
    expected_body = {"status": "ok"}

    # Act
    response = client.get(endpoint)
    body = response.get_json()

    # Assert
    assert body == expected_body


# =============================================================================
# GET /
# =============================================================================

def test_index_returns_200(client):
    """GET / responde con código HTTP 200."""
    # Arrange
    endpoint = "/"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200


def test_index_contains_known_content(client):
    """GET / contiene el título principal de la página en el HTML."""
    # Arrange
    expected_text = "Emires y sultanes nazaríes de Granada"

    # Act
    response = client.get("/")
    html = response.data.decode("utf-8")

    # Assert
    assert expected_text in html, (
        f"No se encontró '{expected_text}' en el HTML. "
        "Verifica que el archivo templates/index.html no ha sido modificado."
    )


def test_index_content_type_is_html(client):
    """GET / responde con Content-Type text/html."""
    # Arrange
    endpoint = "/"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.content_type.startswith("text/html"), (
        f"Se esperaba 'text/html' pero se obtuvo '{response.content_type}'."
    )


# =============================================================================
# GET /health – content-type
# =============================================================================

# Justificación: el endpoint /health es consumido por el healthcheck de Kubernetes;
# debe responder JSON para que cualquier cliente lo parsee sin configuración extra.
def test_health_content_type_is_json(client):
    """GET /health responde con Content-Type application/json."""
    # Arrange
    endpoint = "/health"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.content_type.startswith("application/json"), (
        f"Se esperaba 'application/json' pero se obtuvo '{response.content_type}'."
    )
