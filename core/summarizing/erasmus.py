from typing import AsyncGenerator

from core.summarizing.summarizer import Summarizer


class ErasmusSummarizer(Summarizer): 
    async def summarize(self, content: str) -> AsyncGenerator[str, None]:
        """summarizes the given Erasmus Mundus scholarship content and yields the summary as a stream of text chunks"""
        stream = self.ai.prompt([{
            "role": "user",
            "content": f"""Below, there is an Erasmus Mundus scholarship raw content, delimited by "START OF SCHOLARSHIP" and "END OF SCHOLARSHIP".
                            Create a MARKDOWN output that summarizes the given Erasmus Mundus scholarship.
                            Within this markdown, add a bullet point for each of the following information:
                                - **Title**: Name of the scholarship;<br>
                                - **Website URL**: <URL>. <br>
                                <hr>

                                Observe the following rules:
                                - Add the website URL between the angle brackets (<>)
                                - Add ";" and line breaks (<br>) between each bullet point
                                - Add the horizontal rule (<hr> <br>) at the end of the markdown
                                - Do not add additional html tags on the output markdown
                                - Do not include any information that is not present in the content.
                                - You MUST return ONLY the markdown output, without any additional text or explanations.
                                - Do not add markdown's opening and closing tags, such as "```markdown" or "```".

                            Scholarship raw content: 
                            \n\n{content}"""
        }])
          
        async for chunk in stream:
            if chunk.strip():
                yield chunk