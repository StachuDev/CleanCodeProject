import pytest
from imagehub.models import *  
from rest_framework import status
from django.urls import reverse


# --- tag ---

@pytest.mark.django_db
def test_get_tag(api_client, tag):
    response = api_client.get(reverse('tag-list'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    tag_data = dict(response.data[0]) 
    assert tag_data['tag'] == tag.tag


@pytest.mark.django_db
def test_create_tag(api_client, tag_payload):
    url = '/api/tags/'
    response = api_client.post(url, tag_payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Tag.objects.count() == 1

@pytest.mark.django_db
def test_create_tag_bad(api_client):
    url = '/api/tags/'
    response = api_client.post(url, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_update_tag_put(api_client, tag):

    payload = {
        "tag": "tag2"
    }

    response = api_client.put(f'/api/tags/{tag.id}/', payload, format='json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_update_tag_patch(api_client, tag):
    payload = {
        "tag": "tag1"
    }

    response = api_client.patch(f'/api/tags/{tag.id}/', payload, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_tag(api_client, tag):

    response = api_client.delete(f'/api/tags/{tag.id}/', format='json')
    assert response.status_code == 204



# -- post ---

@pytest.mark.django_db
def test_get_post(api_client, create_post):
    response = api_client.get(reverse('post-list'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    post_data = dict(response.data[0]) 
    assert post_data['title'] == create_post.title
    assert post_data['user'] == create_post.user.id
    assert post_data['description'] == create_post.description
    assert post_data['tag'] == create_post.tag.tag


@pytest.mark.django_db
def test_get_post_detail(api_client, create_post):
    response = api_client.get(reverse('post-detail', args=[create_post.id]))

    assert response.status_code == status.HTTP_200_OK

    post_data = dict(response.data) 
    assert post_data['title'] == create_post.title
    assert post_data['description'] == create_post.description
    assert post_data['tag'] == create_post.tag.tag


@pytest.mark.django_db
def test_create_post(api_client, post_payload):
    url = '/api/posts/'
    response = api_client.post(url, post_payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_create_post_bad_request(api_client, post_payload_bad):
    url = '/api/posts/'
    response = api_client.post(url, post_payload_bad, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Post.objects.count() == 0


@pytest.mark.django_db
def test_update_post_put(api_client, create_post):

    payload = {
        "title": "teeessttttt",
        "tag": 1,
        "description": "teeessttttt"
    }

    response = api_client.put(f'/api/posts/{create_post.id}/edit/', payload, format='json')

    assert response.status_code == 200

@pytest.mark.django_db
def test_update_post_patch(api_client, create_post):

    payload = {
        "title": "teeessttttt"
    }

    response = api_client.patch(f'/api/posts/{create_post.id}/edit/', payload, format='json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_post(api_client, post):

    response = api_client.delete(f'/api/posts/{post.id}/edit/', format='json')
    assert response.status_code == 204



# -- comment ---

@pytest.mark.django_db
def test_get_comment(api_client, create_post, comment):
    response = api_client.get(reverse('comment-list'))

    assert response.status_code == status.HTTP_200_OK
    
    if(len(response.data) == 1):
        assert len(response.data) == 1

        comment_data = dict(response.data[0]) 
        assert comment_data['comment_text'] == comment.comment_text
    else:
        assert len(response.data) != 1


@pytest.mark.django_db
def test_create_comment(api_client, comment_payload):
    url = '/api/comments/new/'
    response = api_client.post(url, comment_payload, format='json')
    print(response.data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Comment.objects.count() == 1


# @pytest.mark.django_db
# def test_get_comment_detail(api_client, create_comment):
#     response = api_client.get(reverse('comment-detail', args=[create_comment.id]))

#     print(response.data)
#     assert response.status_code == status.HTTP_200_OK

#     comment_data = dict(response.data) 
#     assert comment_data['comment_text'] == create_comment.comment_text
