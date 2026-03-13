import logging
from functools import lru_cache
from pathlib import Path

logger = logging.getLogger(__name__)

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"


@lru_cache(maxsize=1)
def _read_prompts(prompts_dir: Path) -> tuple[str, str]:
    doctor = (prompts_dir / "doctor_instructions.prompt").read_text(encoding="utf-8")
    receptionist = (prompts_dir / "receptionist_instructions.prompt").read_text(encoding="utf-8")
    return doctor, receptionist

class PromptLoader:
    def __init__(self, prompts_dir: Path = PROMPTS_DIR):
        self.prompts_dir = prompts_dir
        self.DOCTOR_INSTRUCTIONS = ""
        self.RECEPTIONIST_INSTRUCTIONS = ""

    def load_prompts(self):
        try:
            self.DOCTOR_INSTRUCTIONS, self.RECEPTIONIST_INSTRUCTIONS = _read_prompts(self.prompts_dir)
            logger.info("Prompts loaded successfully.")
        except Exception as e:
            logger.exception("Error loading prompts.")
            raise

    def reload_prompts(self):
        _read_prompts.cache_clear()
        self.load_prompts()

prompt_loader = PromptLoader()