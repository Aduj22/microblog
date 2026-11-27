"""
Tests for the application version route
"""

def test_version_unknown(client):
    """
    Test that the version defaults to unknown
    """
    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'unknown'
    assert response.content_type == 'text/plain; charset=utf-8'


def test_version_configured(client):
    """
    Test that the configured application version is returned
    """
    client.application.config['APP_VERSION'] = '11.0.0'

    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'11.0.0'
    assert response.content_type == 'text/plain; charset=utf-8'
