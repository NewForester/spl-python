"""
    Python 3 solution to the Exercism 'rna_transcription' exercise
"""

def to_rna(dna_strand):
    """
    transcribe the nucleotides of a strand of DNA to their RNA complements
    """
    _nucleotide_complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    try:
        return ''.join([_nucleotide_complements[n] for n in dna_strand])
    except KeyError:
        return ''

##
## There is a str.maketrans function that might make the code easier to read
## but that does not handle invalid characters the way the exercise wants.
##
