import pytest


def test_root_non_async(api):
    response = api.get('/')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"msg": "Hello, World!"}


def test_hello_non_async(api):
    response = api.get('/hello')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"msg": "Welcome to Banana World"}


@pytest.mark.asyncio
async def test_root(async_api):
    response = await async_api.get('/')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"msg": "Hello, World!"}


@pytest.mark.asyncio
async def test_hello(async_api):
    response = await async_api.get('/hello')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"msg": "Welcome to Banana World"}
