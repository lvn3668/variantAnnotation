def genenamestring(exac_response):
    genenamestrings = [li['Gene'] for li in exac_response["vep_annotations"]]
    return genenamestrings


def majorconsequencestring(exac_response):
    majorconsequencestrings = [li['major_consequence'] for li in exac_response["vep_annotations"]]
    return majorconsequencestrings


def extractconsequencesfromvepannotations(exac_response):
    consequencestrings: list[string] = [li['Consequence'] for li in exac_response["vep_annotations"]]
    return consequencestrings


def extractallelesfromvepannotations(exac_response):
    Allelestrings: list[string] = [li['Allele'] for li in exac_response["vep_annotations"]]
    return Allelestrings

