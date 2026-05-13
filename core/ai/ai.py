from openai import OpenAI


class AI:
    def __init__(self, api_url: str, api_key: str, model_name: str) -> None:
        self._connection = self._get_connection(api_url=api_url, api_key=api_key)
        self._model_name = model_name
        super().__init__()

    def _get_connection(self, api_url: str, api_key: str) -> OpenAI:
        return OpenAI(base_url=api_url, api_key=api_key)

    def prompt(self, messages: list[dict[str, str]]) -> str:
        request = self._connection.chat.completions.create(model=self._model_name, messages=messages)
        answer = request.choices[0].message.content
        
        return answer if answer is not None else "No answer could be provided."
