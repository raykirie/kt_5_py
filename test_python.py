import pytest
import asyncio


async def some_async_function():
    return 42


async def some_async_function_that_raises():
    raise ValueError("Some error message")

@pytest.mark.asyncio
async def test_promise_resolution():
    expected_value = 42
    result = await some_async_function()
    assert result == expected_value

@pytest.mark.asyncio
async def test_promise_rejection():
    expected_exception = ValueError("Some error message")
    
    with pytest.raises(ValueError) as exc_info:
        await some_async_function_that_raises()

    assert str(exc_info.value) == str(expected_exception)
