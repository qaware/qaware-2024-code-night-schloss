from pydantic import BaseModel
from pydantic.class_validators import Optional


class Sendung(BaseModel):
    # TODO: Füge relevante Daten hinzu
    sendung_id: int
    erfassungszeitpunkt: Optional[str]

    def to_dict(self):
        return {
            # TODO: Füge relevante Daten hinzu
            "sendung_id": self.sendung_id,
            "erfassungszeitpunkt": self.erfassungszeitpunkt
        }
