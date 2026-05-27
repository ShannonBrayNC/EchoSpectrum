# AI Signal Classification

EchoSpectrum includes an AI-assisted signal classification research layer.

## Goals

- lawful receive-only interpretation
- explainable spectrum tagging
- anomaly awareness
- synthetic-data training support
- metadata-only analysis

## Initial Classification Families

| Label | Region |
|---|---|
| possible_915mhz_ism | 902-928 MHz |
| possible_24ghz_ism | 2.4 GHz ISM |
| possible_58ghz_ism | 5.8 GHz ISM |
| possible_adsb | 1090 MHz ADS-B |
| unknown_receive_only_signal | fallback |

## Safety Boundaries

EchoSpectrum classification:
- does not decode private communications
- does not perform interception
- does not classify protected/private content
- operates on metadata and observation heuristics only

## Future Enhancements

- CNN spectrum classifiers
- waterfall image classification
- anomaly detection
- replay analysis
- federated sensor classification
- AI-generated engineering summaries
