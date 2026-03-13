from google.adk.agents.llm_agent import LllmAgent
from src.services.medical_assistant.prompts import DOCTOR_INSTRUCTIONS
from src.core.config import settings

doctor_agent = LllmAgent(
    name="DoctorAgent",
    model=settings.GEMINI_CHAT_MODEL,
    instruction=DOCTOR_INSTRUCTIONS,
    description="Analyzes patient symptoms and provides medical advice.",
    output_key="symptoms_analysis",
    
)