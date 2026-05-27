from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json

import numpy as np


@dataclass(frozen=True)
class SyntheticSignalConfig:
    sample_rate_hz: float = 10e6
    tone_offset_hz: float = 500e3
    sample_count: int = 262144
    noise_scale: float = 0.05
    random_seed: int = 42


@dataclass(frozen=True)
class SyntheticDatasetManifest:
    dataset_name: str
    sample_rate_hz: float
    sample_count: int
    tone_offset_hz: float
    random_seed: int

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)


def generate_iq(config: SyntheticSignalConfig) -> np.ndarray:
    rng = np.random.default_rng(config.random_seed)
    t = np.arange(config.sample_count) / config.sample_rate_hz

    tone = np.exp(2j * np.pi * config.tone_offset_hz * t)
    noise = config.noise_scale * (
        rng.standard_normal(config.sample_count)
        + 1j * rng.standard_normal(config.sample_count)
    )

    return tone + noise


def generate_dataset(output_dir: str | Path, dataset_name: str, config: SyntheticSignalConfig) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    iq = generate_iq(config)

    npy_path = output_path / f"{dataset_name}.npy"
    np.save(npy_path, iq)

    manifest = SyntheticDatasetManifest(
        dataset_name=dataset_name,
        sample_rate_hz=config.sample_rate_hz,
        sample_count=config.sample_count,
        tone_offset_hz=config.tone_offset_hz,
        random_seed=config.random_seed,
    )

    manifest_path = output_path / f"{dataset_name}.manifest.json"
    manifest_path.write_text(manifest.to_json(), encoding="utf-8")

    return npy_path
