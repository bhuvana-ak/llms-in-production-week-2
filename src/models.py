from guardrails.hub import ValidSQL,ToxicLanguage, DetectPII
from pydantic import BaseModel, Field


class LLMResponse(BaseModel):
    """
    LLM Response that is validated using Guardrails.ai
    """

    generated_sql: str = Field(
        description="Generate PostgreSQL for the given natural language instruction.",
        validators=[
            ValidSQL(on_fail="reask"),
            ToxicLanguage(on_fail="fix"), 
            DetectPII(pii_entities=["EMAIL_ADDRESS", "PHONE_NUMBER"], on_fail="exception")
        ],
    )
