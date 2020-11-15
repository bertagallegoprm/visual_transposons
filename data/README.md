# Data 

The data is available at the [Arabidopsis Information Resource (TAIR) website](https://www.arabidopsis.org/download/index-auto.jsp?dir=%2Fdownload_files%2FGenes%2FTAIR10_genome_release%2FTAIR10_transposable_elements), where it appears the date of the last release. 

There are two types of data:
- `data/te_attributes.txt`. Names and attributes (family and subfamily, orientation, location in the genome).
- `data/te_sequences.txt`. Sequences.

The date of the last download can be found in `data/last_download.txt`.

- To run the code and get the data:

```
python3 get_data.py 
```

See `database` for specific instructions on how to create the database schema and load the TE attributes into it.
