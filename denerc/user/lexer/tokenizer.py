"""
Copyright (c) 2022 Dener and Dener Contributors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from uuid import uuid4
from enum import Enum
from typing import NamedTuple


# latin letters and numbers allowed
ALLOWED_VALUE_NAMES = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


# these are special tokens not allowed for use in stuff like constant names.
class Tokens(Enum):
    OPAREN = '('
    CPAREN = ')'
    OBRACE = '{'
    CBRACE = '}'
    OBRACKET = '['
    CBRACKET = ']'
    SEMICOLON = ';'
    COLON = ':'
    QUOTE = '"'
    PERIOD = '.'
    ASTERISK = '*'
    MOCHE = '!'
    COMMA = ','
    GT = '>'
    LT = '<'
    UNDERSCORE = '_'


class Token(NamedTuple):
    id: str
    value: str
    type: int | None = None


class Tokenizer:
    def __init__(self, content: str, working_file: str = 'main.de'):
        self._content = content
        self._working_file = working_file

    def _recover(self, tks: list[Token]) -> str:
        return ''.join(token.value for token in tks)

    def start_tokenization(self) -> list[Token]:
        tkizer: list[str] = []
        tk_values = [tk.value for tk in Tokens]

        for text in self._content:
            token_id = str(uuid4())
            if text not in [tk_values, ALLOWED_VALUE_NAMES]:
                tkizer.append(Token(id=token_id, value=text, type=0))
                continue

            tkizer.append(Token(id=token_id, value=text, type=1))

        return tkizer
