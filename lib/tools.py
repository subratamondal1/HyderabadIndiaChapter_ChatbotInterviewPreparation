from typing import Literal, Optional

from openai import OpenAI
from openai._base_client import HttpxBinaryResponseContent

from lib.configs import OPENAI_API_KEY

__all__ = ["BaseTool"]


class BaseTool:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError
