
import requests

def get_sequences_file():
    """
    Get the TE sequences from the TAIR website
    and store it in a text file.
    """
    url = requests.get("https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_transposable_elements/TAIR10_TE.fas")
    sequences = url.text
    fas_file = open("TAIR10_TE.txt", "w")
    fas_file.writelines(sequences) 
    fas_file.close()



if __name__ == "__main__":
    get_sequences_file()