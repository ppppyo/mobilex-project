import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.cheerbeat_generator import InputModel, OutputModel
from fastapi import HTTPException

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/api/vi/func/Cheerbeat')
async def call_cheerbeat_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    try:
        chain = build(
            name=NAME,
            llm=store.get(model.llm_type),
        )

        return OutputModel(
            output=chain.invoke({
                'input_context': model.word,
            }),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
