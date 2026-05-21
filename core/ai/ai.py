from typing import Any, AsyncGenerator

from openai import AsyncOpenAI


class AI:
    def __init__(self, api_url: str, api_key: str, model_name: str) -> None:
        self._connection = self._get_connection(api_url=api_url, api_key=api_key)
        self._model_name = model_name
        super().__init__()

    def _get_connection(self, api_url: str, api_key: str) -> AsyncOpenAI:
        return AsyncOpenAI(base_url=api_url, api_key=api_key)

    async def prompt(self, messages: list[Any]) -> AsyncGenerator[str, None]:
        stream = await self._connection.chat.completions.create(model=self._model_name, messages=messages, stream=True)
        
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content and content.strip() != "":
                yield f"data: {content}\n\n"
            