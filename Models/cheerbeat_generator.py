from typing import Literal

from pydantic import BaseModel, Field

MAX_LENGTH = 500000


class InputModel(BaseModel):
    word: str = Field(
        alias='word',
        description='입력할 가사를 넣어주세요!',
        default='음냐음냐',
        min_length=5000,
        max_length=5000,
        pattern=rf'^[a-z|가-힣]{{{MAX_LENGTH}}}$',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='suno',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='응원가 생성 짜잔!',
    )
