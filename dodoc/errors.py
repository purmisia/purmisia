"""
Copyright (c) 2022 Dodo Software Foundation and Dodo Contributors.

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

class CompilerError(Exception):
    """
    A Dodo Compiler Error
    """
    def __init__(self, code: int, message: str):
        super().__init__(f'PANIC!: Compiler failed to compile under code {code} with message:\n\n{message}')

class UnsupportedOS(CompilerError):
    """
    Raised when DodoC is ran on an unsupported OS.
    """

class SyntacticError(CompilerError):
    """
    Raised when an error with syntazx occurs.
    """

class InvalidToken(CompilerError):
    """
    Raised when a provided token is invalid.
    """
