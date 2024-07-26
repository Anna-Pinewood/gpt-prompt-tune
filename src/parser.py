import ast
from langchain_core.output_parsers import BaseOutputParser
import json
import re


class ReviewOutputParser(BaseOutputParser):
    """Custom parser for first thoughts then structured output."""

    def parse(self, text: str):
        """Extract the structured output after specified cutoff like
        "Result:\n", "Output:\n", etc."""
        json_start = text.rfind("```json")
        json_end = text.rfind("```")
        json_str = text[json_start + 7:json_end].strip()

        try:
            parsed_data = ast.literal_eval(json_str)
        except SyntaxError:
            raise ValueError(
                "Invalid JSON format in the output. Maybe output is too loong to be completed correctly.")

        if not isinstance(parsed_data, list) or not all(isinstance(item, dict) for item in parsed_data):
            raise ValueError("Parsed data is not a list of dictionaries")

        return parsed_data

    @property
    def _type(self) -> str:
        return "review_output_parser"
