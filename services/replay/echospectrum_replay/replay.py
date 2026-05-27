from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass(frozen=True)
class WaterfallFrame:
    frame_id: str
    timestamp_utc: str
    center_frequency_hz: float
    fft_bins: list[float]


class ReplayArchive:
    def __init__(self) -> None:
        self.frames: list[WaterfallFrame] = []

    def add_frame(self, frame: WaterfallFrame) -> None:
        self.frames.append(frame)

    def replay_summary(self) -> dict:
        return {
            "frameCount": len(self.frames),
            "generatedUtc": datetime.now(UTC).isoformat(),
        }
