
import requests
import datetime


def download_sequences_file():
    """
    Get the TE sequences from the TAIR website
    and store it in text file.
    """
    url = requests.get("https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_transposable_elements/TAIR10_TE.fas")  
    file = open("te_sequences.txt", "w")
    file.writelines(url.text) 
    file.close()


def download_attributes_file():
    """
    Get the TE names and attributes from the TAIR website
    and store it in text file.
    """
    url = requests.get("https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_transposable_elements/TAIR10_Transposable_Elements.txt")
    file = open("te_attributes.txt", "w")
    file.writelines(url.text) 
    file.close()


def print_download_date():
    last_download = str(datetime.date.today())
    file = open("last_download.txt", "w")
    file.write(last_download) 
    file.close()


if __name__ == "__main__":
    download_sequences_file()
    download_attributes_file()
    print_download_date()
