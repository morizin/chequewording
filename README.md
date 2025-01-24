# Number to Words Converter

## Overview
Python utility to convert numeric values to words, supporting multiple currencies and large numbers.

## Features
- Converts numbers to words
- Supports multiple currencies
- Handles positive and negative numbers
- Supports up to Crore (10 million)

## Installation
```bash
git clone https://github.com/yourusername/number-to-words.git
cd number-to-words
```

## Usage
```python
converter = NumberToWords()
print(converter.convert_to_words(1234567, 'Dollar'))
# Output: Twelve Lakh Thirty Four Thousand Five Hundred Sixty Seven Dollar Only
```

## Quick Start
```bash
python number_to_words.py
```

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request
```

<antArtifact identifier="requirements" type="text/markdown" title="Project Requirements">
# No external dependencies required
```

<antArtifact identifier="license" type="text/markdown" title="MIT License">
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

<antArtifact identifier="gitignore" type="text/markdown" title="Git Ignore File">
# Python
__pycache__/
*.py[cod]
.python-version
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```