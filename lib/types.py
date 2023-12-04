from typing import Literal, TypedDict

__all__ = ["Question", "Evaluation"]


class Question(TypedDict):
    question: str
    type: Literal["personal", "role-specific", "behavioral", "situational"]


class Evaluation(TypedDict):
    evaluation: Literal["good", "average", "bad"]
    feedback: str | None
    reason: str | None
    samples: list[str] | None
