from pathlib import Path

import numpy as np

from services.ingest.echospectrum_ingest.synthetic import (
    SyntheticSignalConfig,
    generate_dataset,
    generate_iq,
)


def test_synthetic_generation_is_deterministic():
    config = SyntheticSignalConfig(random_seed=123)

    iq_a = generate_iq(config)
    iq_b = generate_iq(config)

    assert np.allclose(iq_a, iq_b)


def test_dataset_files_created(tmp_path: Path):
    config = SyntheticSignalConfig(random_seed=99)

    npy_path = generate_dataset(
        output_dir=tmp_path,
        dataset_name="test_dataset",
        config=config,
    )

    manifest_path = tmp_path / "test_dataset.manifest.json"

    assert npy_path.exists()
    assert manifest_path.exists()
