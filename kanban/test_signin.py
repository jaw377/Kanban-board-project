import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_signup_view_get(client):
    url = reverse('signup')  
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context  
    assert b'<form' in response.content  

@pytest.mark.django_db
def test_signup_view_post_valid(client):
    url = reverse('signup')
    valid_data = {
        'username': 'jakob',
        'password': 'Ambrose17',
    }
    response = client.post(url, data=valid_data)
    # Should redirect after successful form submission
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup_view_post_invalid(client):
    url = reverse('signup')
    invalid_data = {
        'username': 'dom',  
        'password': 'dog',
    }
    response = client.post(url, data=invalid_data)
    # Should return 200 with form errors
    assert response.status_code == 200
    assert 'form' in response.context
    form = response.context['form']
    assert form.errors
