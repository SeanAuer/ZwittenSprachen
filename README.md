

# ZwittenSprachen

ZwittenSprachen is a command-line language study tool designed for rapid recall of vocabulary through flashcard-style decks. It supports multiple formats for deck input and is designed for expansion to a GUI via SwiftUI.

## Features

- Supports decks in YAML, JSON, and CSV formats
- CLI-based interactive study session
- Commands for flipping, navigating, and transposing cards
- Modular Python backend
- SwiftUI front-end directory scaffolded for future development

## Usage

1. Placeholder / example decks in `examples/example_data/` directory.
2. Supported formats:
   - `.yaml`: dictionary-style key-value pairs
   - `.json`: standard JSON dictionary
   - `.csv`: two-column format (first column = prompt, second = definition)
3. Run the CLI study tool:

```bash
python ZwittenSprachen/zwitten_sprachen.py
```

4. In-session commands:
   - `f`: Flip card
   - `Enter`: Go to next card
   - `b`: Go back one card
   - `q`: Quit session
   - `t`: Transpose (flip prompt/definition direction)

## Project Structure

```
ZwittenSprachen/
│
├── examples/
│   └── example_data/
│       ├── german_nouns.yaml
│       ├── french_nouns.csv
│       └── german_verbs.json
│
├── swift_ui/
│   └── ZwittenSprachenApp.xcodeproj/
│
├── ZwittenSprachen/
│   ├── __init__.py
│   ├── zwitten_sprachen.py
│   ├── deck_loader.py
│   ├── session_manager.py
│   └── ai_generator.py
│
├── requirements.txt
└── README.md
```

## Dependencies

- Python 3.8+
- pandas
- PyYAML

Install with:

```bash
pip install -r requirements.txt
```

## Roadmap

- Randomize prompt drawing
- Combinations of decks
- User profiles for perpetual custom decks at application start 
- Implement SwiftUI-based GUI
- Add user scoring and spaced repetition
- Quiz / Test mode - track user responses and provide score
- Enable deck export and sharing