from typing import AsyncGenerator

from core.summarizing.summarizer import Summarizer


class ErasmusSummarizer(Summarizer): 
    async def summarize(self, content: str) -> AsyncGenerator[str, None]:
        stream = self.ai.prompt([{
            "role": "user",
            "content": f"""Below, there are several Erasmus Mundus scholarships raw content, separated by "START OF PROJECT" and "END OF PROJECT".
                            Create a MARKDOWN output that summarizes the given Erasmus Mundus scholarships.
                            Within this markdown, add a section for each scholarship and include the following information:
                                - Name of the scholarship
                                - Description
                                - Its website URL

                                Observe the following rules:
                                - Do not include any information that is not present in the content.
                                - You MUST return ONLY the markdown output, without any additional text or explanations.

                            Scholarships raw content: \n\n{content}"""
        }])
          
        async for chunk in stream:
            yield chunk