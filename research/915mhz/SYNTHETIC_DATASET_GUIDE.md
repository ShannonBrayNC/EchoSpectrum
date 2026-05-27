# Synthetic RF Dataset Guide

EchoSpectrum uses deterministic synthetic RF datasets for:
- CI validation
- replay testing
- AI classifier training
- FFT reproducibility
- hardware-independent development

## Goals

The synthetic pipeline ensures:
- repeatable FFT outputs
- no SDR hardware dependency
- safe offline development
- lawful generated datasets

## Example Usage

```python
from services.ingest.echospectrum_ingest.synthetic import (
    SyntheticSignalConfig,
    generate_dataset,
)

config = SyntheticSignalConfig(
    sample_rate_hz=10e6,
    tone_offset_hz=500e3,
    sample_count=262144,
    random_seed=42,
)

generate_dataset(
    output_dir="datasets/generated",
    dataset_name="ism_915_reference",
    config=config,
)
```

## Generated Outputs

- `.npy` IQ sample file
- `.manifest.json` metadata file

## Safety Model

All generated datasets are synthetic and contain no captured private RF traffic.
