from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass(frozen=True)
class FieldBriefing:
    briefing_id: str
    language: str
    summary: str
    generated_utc: str


def generate_field_briefing(summary: str, language: str = "en") -> FieldBriefing:
    return FieldBriefing(
        briefing_id=f"briefing-{int(datetime.now(UTC).timestamp())}",
        language=language,
        summary=summary,
        generated_utc=datetime.now(UTC).isoformat(),
    )
