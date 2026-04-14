from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitors: dict) -> None:
        if visitors.get("vaccine") is None:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_raw = visitors["vaccine"].get("expiration_date")

        if expiration_raw is None:
            raise OutdatedVaccineError("Vaccine has no expiration date")

        if isinstance(expiration_raw, str):
            expiration = date.fromisoformat(expiration_raw)
        else:
            expiration = expiration_raw

        if expiration < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitors.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
