import pytest

from news.models import Comment, News


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Author')


@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client


@pytest.fixture
def news():
    news = News.objects.create(
        title='news title',
        text='news text',
    )
    return news


@pytest.fixture
def comment(news, author):
    comment = Comment.objects.create(
        news=news,
        author=author,
        text='comment text',
    )
    return comment


@pytest.fixture
def news_id(news):
    return (news.pk,)


@pytest.fixture
def news_with_comment_id(news, comment):
    return (news.pk,)
