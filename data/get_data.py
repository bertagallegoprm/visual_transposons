
import requests

def get_sequences():
    """
    Get the TE sequences from the TAIR website
    """
    url = requests.get("https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_transposable_elements/TAIR10_TE.fas")
    return url.text


def save_to_file(text):
    file = open(f"{text}.txt", "w")
    file.writelines(text) 
    file.close()



if __name__ == "__main__":
