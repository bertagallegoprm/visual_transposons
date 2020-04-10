
import requests

def get_sequences():
    """
    Get the TE sequences from the TAIR website
    """
    url = requests.get("https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_transposable_elements/TAIR10_TE.fas")
    return url.text

def get_names():
    """
    Get the TE names and attributes from the TAIR website
    """
    url = requests.get("https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_transposable_elements/TAIR10_Transposable_Elements.txt")
    return url.text


def save_to_file(text):
    file = open(f"{text}.txt", "w")
    file.writelines(text) 
    file.close()

  
def get_all_te_data():
    tair10_te_seq = get_sequences()
    tair10_te_attributes = get_names()
    save_to_file(tair10_te_seq)
    save_to_file(tair10_te_attributes)




if __name__ == "__main__":
