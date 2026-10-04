"""
Civic Awareness & Rights Advisory Module
Provides situational rights evaluation, Indian law mappings (BNS, BNSS, BSA, Special Acts),
interactive quiz evaluation, and evidence guidance for ordinary citizens.
"""
from .situations_db import SITUATIONS_DB, SITUATION_CATEGORIES
from .scenarios_db import SCENARIOS_DB, SCENARIO_CATEGORIES
from .rights_evaluator import RightsEvaluator
from .quiz_engine import QuizEngine

__all__ = [
    "SITUATIONS_DB",
    "SITUATION_CATEGORIES",
    "SCENARIOS_DB",
    "SCENARIO_CATEGORIES",
    "RightsEvaluator",
    "QuizEngine",
]
