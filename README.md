# ArtistToMusic

**ArtistToMusic** is a simple  Command-line program that generates YouTube links for all songs by a specific artist.

## Features

- **Automatic link generation**: Fetches YouTube links for all songs by a given artist.
- **Simple to use**: Just input the artist's name to get the links.

## How it works

Once you run the tool, simply enter the name of the artist and let the tool do the rest. When it’s finished, you’ll receive a .txt file with all the links, one per line.

To download the songs, I recommend using [Youtube-dl-gui](https://github.com/oleksis/youtube-dl-gui)

## Installation

Clone the repository:

```bash
  git clone https://github.com/doplerer/ArtistToMusic.git
```

Create a Virtual Environment & activate it

```bash
  python -m venv venv
  # .\.venv\Scripts\Activate.ps1 For Windows
  # source venv/bin/activate MacOs & Linux
```

Install required dependencies
```bash
  pip install -r requirements.txt
```
Run the tool!
```bash
  python main.py
```
## Authors

- [@doplerer](https://www.github.com/doplerer)

