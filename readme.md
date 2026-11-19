# PageRank Algorithm Demonstration
## Created by Adrian Bennett
### aab0125@auburn.edu — 904295194

## About
This project tasked us with implementing the PageRank algorithm that Google founders Larry Page & Sergey Brin invented to revolutionize page indexing and ultimately give their budding company Google footing.

To implement the algorithm I thought it made the most sense to create a Page and Link class that would represents node in this essentially weighted graph. With these classes in place, I randomly generated *N* pages and *M*links to initialize the graph space. After initialization the PageRank algorithm ran over the graph to rank the pages in terms of highest to lowest importance.

## Usage
In order to run the demonstration perform the following steps:
- 1. Activate the virtual environment: `source .venv/bin/activate`
- 2. Run the `demo.py` script with the command `python demo.py`
- 3. Observe the PageRank algorithm run live and calculate rankings of all pages.

Note: Settings for the `demo.py` script are hardcoded but have an easy to find settings section at the top of the `main` function. Tweak as you see fit.

