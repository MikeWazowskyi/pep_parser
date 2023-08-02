# PEP parser

[![Scrapy CI](https://github.com/MikeWazowskyi/pep_parser/actions/workflows/scrapy_ci.yml/badge.svg)](https://github.com/MikeWazowskyi/pep_parser/actions/workflows/scrapy_ci.yml)

## Description

Implementation of a simple Scrapy parser for page with Python's PEPs, which collect number, name and status of every PEP.

## Instructions for running

1. Clone the repository and navigate to it in the command line::

   ``` git clone https://github.com/MikeWazowskyi/pep_parcer```

   ``` cd pep_parcer```

2. Create and activate a virtual environment:

   ``` python -m venv venv```

   *unix/MacOS:
   ``` source venv/bin/activate```

   Windows:
   ``` ./venv/Scripts/activate```

3. Install requirements:

   ``` python -m pip install --upgrade pip```

   ``` python -m pip install -r requirements.txt```

4. Run parser:

   ``` scrapy crawl pep```

## Results

Parsing results are available in results/ directory:
* pep_<datetime>.csv contains information about PEP's number, name and status.
* status_summary_<datetime>.csv contains summary information about PEPs status.

## About Author:
https://github.com/MikeWazowskyi
