from __future__ import annotations

from typing import Optional

from typing_extensions import Literal, Required, TypedDict

__all__ = ["Question", "Evaluation"]


class Question(TypedDict):
    question: Required[str]
    type: Required[Literal["personal", "role-specific", "behavioral", "situational"]]


class Evaluation(TypedDict):
    evaluation: Required[Literal["good", "average", "bad"]]
    feedback: Optional[str]
    reason: Optional[str]
    samples: Optional[list[str]]
