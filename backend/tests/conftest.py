import pytest
from imagehub.models import Tag, Post, Comment, Subcomment, PostLike
from users.models import Account
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client(account):
    client = APIClient()
    refresh = RefreshToken.for_user(account)
    client.credentials(HTTP_AUTHORIZATION='Bearer '+str(refresh.access_token))
    return client


@pytest.fixture
def api_client_unauthorized():
    client = APIClient()
    return client


#users fixtures
@pytest.fixture
def account() -> Account:
    return Account.objects.create(username="ABC", email='abc@aaa.com', password='password')



#imagehub textures

@pytest.fixture
def tag() -> Tag:
    return Tag.objects.create(tag="tag")

@pytest.fixture
def post(account, tag) -> Post:
    return Post.objects.create(user=account, title="tytuł", description="opis", create_date='2023-10-10', image='ścieżka do brazka', tag=tag)


@pytest.fixture
def comment(post, account) -> Comment:
    return Comment.objects.create(post=post, user=account, comment_text="komentarz", create_date='2023-10-10')


@pytest.fixture
def subcomment(post, account, comment) -> Subcomment:
    return Subcomment.objects.create(parrent_comment=comment, user=account, comment_text="komentarz2", create_date='2023-10-10')


@pytest.fixture
def like(post, account) -> PostLike:
    return PostLike.objects.create(type=1, user=account, post=post)




# -- for views ---
@pytest.fixture
def tag_payload():
    payload = {
        "tag": "tag"
    }
    return payload


@pytest.fixture
def post_payload():
    payload = {
        "title": "Lewis Hamilton",
        "user": 5,
        "description": "Desc...",
        "tag": 1
    }
    return payload


@pytest.fixture
def post_payload_bad():
    payload = {
        "user": 1,
        "description": "Desc...",
        "tag": 1
    }
    return payload


@pytest.fixture
def comment_payload(post):
    payload = {
        "post": post.id,
        "comment_text": "Lewis Hamilton"
    }
    return payload



@pytest.fixture
def create_post(account, tag):
    payload = {
        "id": 100,
        "title": "Lewis Hamilton",
        "user": account,
        "description": "Desc...",
        "tag": tag
    }
    record = Post.objects.create(**payload)
    return record

@pytest.fixture
def create_comment(account, post):
    payload = {
        "id": 100,
        "comment_text": "AAAAAAAAAAA",
        "user": account,
        "post": post
    }
    record = Comment.objects.create(**payload)
    return record
