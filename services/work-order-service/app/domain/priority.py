from abc import ABC, abstractmethod


class PriorityStrategy(ABC):
    @abstractmethod
    def calculate(self, complaint: str, urgency: str) -> str:
        raise NotImplementedError


class DefaultPriorityStrategy(PriorityStrategy):
    def calculate(self, complaint: str, urgency: str) -> str:
        normalized_urgency = urgency.strip().lower()
        normalized_complaint = complaint.strip().lower()

        if normalized_urgency == "high":
            return "high"
        if "freio" in normalized_complaint or "vazamento" in normalized_complaint:
            return "high"
        if normalized_urgency == "medium":
            return "medium"
        return "low"

