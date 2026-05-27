from services.ai.echospectrum_ai.classifier import (
    SignalObservation,
    classify_observation,
)


def test_915mhz_classification():
    observation = SignalObservation(
        center_frequency_hz=915e6,
        bandwidth_hz=125e3,
        peak_power_dbfs=-42,
        sample_rate_hz=10e6,
    )

    result = classify_observation(observation)

    assert result.label == "possible_915mhz_ism"
    assert result.confidence > 0.5


def test_24ghz_classification():
    observation = SignalObservation(
        center_frequency_hz=2.44e9,
        bandwidth_hz=20e6,
        peak_power_dbfs=-55,
        sample_rate_hz=20e6,
    )

    result = classify_observation(observation)

    assert result.label == "possible_24ghz_ism"


def test_unknown_classification():
    observation = SignalObservation(
        center_frequency_hz=7.2e9,
        bandwidth_hz=5e6,
        peak_power_dbfs=-60,
        sample_rate_hz=20e6,
    )

    result = classify_observation(observation)

    assert result.label == "unknown_receive_only_signal"
