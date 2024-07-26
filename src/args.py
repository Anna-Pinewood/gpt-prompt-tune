from dataclasses import dataclass, field


@dataclass
class ScriptArguments:
    api_key: str = field(
        metadata={"help": "API key for the LLM API"},
    )
    dataset_path: str = field(
        metadata={"help": "Path to the dataset"},
    )
