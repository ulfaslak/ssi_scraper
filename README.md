# Scraper for SSI COVID19 data

Minimal script that automatically collects new data from `https://www.ssi.dk/sygdomme-beredskab-og-forskning/sygdomsovervaagning/c/covid19-overvaagning/arkiv-med-overvaagningsdata-for-covid19`.
It first looks to see if a repository is already downloaded, then downloads it if not.

## Usage

First download this repository
```bash
$ git clone https://github.com/ulfaslak/ssi_scraper
```

Then `cd` into it
```bash
$ cd ssi_scraper
```

Finally, execute the script
```bash
$ python scrape_ssi_data.py
```

The script now starts populating the `data` folder.
