# Voice-Based Agro Bot

A Python-powered agricultural assistant designed to provide crop and fertilizer recommendations using voice commands. The bot combines speech recognition, machine learning models, and agricultural datasets to help farmers and enthusiasts make informed decisions about crop and fertilizer selection.

## Features

- **Voice-Based Interaction**: Interact with the bot using voice commands for hands-free operation.
- **Crop Recommendation**: Suggests the best crop to grow based on soil and environmental data.
- **Fertilizer Recommendation**: Recommends appropriate fertilizers tailored to crop and soil needs.
- **ML Powered**: Utilizes machine learning models trained on agricultural datasets.
- **Easy-to-Extend**: Modular Python scripts that enable future enhancement.

## Repository Contents

- `voicebotadvanced.py`: Main script for voice-based user interaction and integration of recommendations.
- `croprecommend.py`: Provides crop recommendation logic.
- `fertiliserrecommend.py`: Fertilizer recommendation logic.
- `cropmodel.pkl`: Trained machine learning model for crop recommendation.
- `fertilizer_model.pkl`: Trained model for fertilizer recommendation.
- `crop_recommendation.csv`: Dataset used for crop suggestion.
- `fertilizer_recommendation.csv`: Dataset used for fertilizer suggestion.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries: `speech_recognition`, `scikit-learn`, `pandas`, `numpy`, etc.

Install dependencies using:
```bash
pip install -r requirements.txt
```
*(A `requirements.txt` file should be created containing the necessary libraries.)*

### Usage

1. **Run the voice bot:**
    ```bash
    python voicebotadvanced.py
    ```
2. **Follow the voice prompts** to provide crop/soil/environment details.
3. **Receive crop and fertilizer recommendations** vocally and on the console.

### Datasets and Models

- The `.csv` files provide the training/test data for the models.
- The `.pkl` files are pre-trained models used for prediction.

## Customization

- Extend the voice commands in `voicebotadvanced.py`.
- Update or retrain machine learning models as new datasets become available.
- Adjust datasets (`.csv` files) to suit local crops, soil types, and fertilizers.

## License

This repository does not specify a license yet.

## Author

- [anirudhaeran](https://github.com/anirudhaeran)

---

*For questions or contributions, feel free to open an issue or pull request.*
