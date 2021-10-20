# Author: Lalitha Viswanathan
# !/usr/bin/env/python3
# from requests.auth import HHTPDigestAuth


import argparse
import ast
import collections
import csv
import json
import re
import subprocess
import sys
import time
import urllib
import xml.etree.ElementTree as ET
from datetime import timedelta
from typing import Union, TextIO, Any

import requests
from requests.exceptions import HTTPError

from initializedictionaries.initializedicts import initdicts
from initializedictionaries.initializedicts import altalleleobscountformatfield
import vcfpackage.vcfparserfunctions as vcfpkg
import exacresponseutilities.exacutilities as exacpkg
import vepannotationutilities as veppkg


def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str


def flatten(x):
    if isinstance(x, dict):
        return [x]
    elif isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def printlistofdicts(listofdicts:list[dict]):
    """

    :param listofdicts: 
    """
    for dict in listofdicts:
        for ky in dict.keys():
            print(ky + "\t" + dict[ky])


def flatten(listofdictionaries: list[dict]):
    if isinstance(listofdictionaries, dict):
        return [listofdictionaries]
    elif isinstance(listofdictionaries, collections.Iterable):
        return [a for i in listofdictionaries for a in flatten(i)]
    else:
        return [listofdictionaries]


def get_all_values(nested_dictionary):
    dict_values = dict()
    # print("Inside function that prints all values from nested dict")
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key, ":", value)
            dict_values[key] = value
    return dict_values


def snppos2rsid(chr_id, chr_pos, org='HUMAN'):
    esearch = subprocess.Popen(
        ['esearch', '-db', 'snp', '-query', '"{}[CHR]" AND {}[ORGN] AND {}[CPOS]'.format(chr_id, org, chr_pos)],
        stdout=subprocess.PIPE)
    efetch_command = ['efetch', '-format', 'docsum']
    efetch_snp_report = subprocess.Popen(efetch_command, stdin=esearch.stdout, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    root = ET.fromstring(efetch_snp_report.stdout.read().decode('utf-8'))
    result = root.findall('./DocumentSummary/SNP_ID')
    result = ['rs' + r.text for r in result]
    return ','.join(result)


def getensembltouniprotids(ensemblids):
    url = 'https://www.uniprot.org/uploadlists/'
    params = {
        'from': 'ENSEMBL_ID',
        'to': 'ACC+ID',
        'format': 'tab',
        'query': ensemblids
    }

    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read()
    print("ensembl to chembl id")
    print(response.decode('utf-8'))
    return response.decode('utf-8')


def getchemblidsfromuniprotids(uniprotids):
    url = 'https://www.uniprot.org/uploadlists/'
    params = {
        'from': 'ACC+ID',
        'to': 'CHEMBL_ID',
        'format': 'tab',
        'query': uniprotids
    }

    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        response = f.read()
    print("uniprot to chembl id")
    print(response.decode('utf-8'))
    return response.decode('utf-8')


def getdrugbanktargetsfromchemblids(chembltouniprotfile, chemblid):
    with open(chembltouniprotfile, newline='') as chembltouniprotmappingfile:
        chembltouniprot = csv.DictReader(chembltouniprotmappingfile, delimiter='\t')
        for record in chembltouniprot:
            print(record)


def main(numberofconsecutiverepeatsofaltallele_RUN: dict = None,
         readplacementprobability_RPP: dict = None,
         readplacementprobabilityforreference_RPPR: dict = None,
         readsplacedleft_RPL: dict = None, readsplacedright_RPR: dict = None, endplacementprob_EPP: dict = None,
         endplacementprobref_EPPR: dict = None,
         altalleledeptratio_DPRA: dict = None,
         logoddsratio_ODDS: dict = None,
         typeofallele_TYPE: dict = None, numaltalleles_AC: dict = None,
         totalnumberofallelesincalledgenotype_AN: dict = None,
         meannoofaltallelespersample_MEANALT: dict = None,
         numofaltalleleobspersample_NUMALT: dict = None,
         allelelength_LEN: dict = None, meanmapqualaltallele_MQM: dict = None, meanmapqualrefallele_MQMR: dict = None,
         genotypequality_GQ: dict = None,
         genotypeiterations_GTI: dict = None,
         allelebalanceatheterozygoussites_AB: dict = None,
         allelebalanceprobabilityatheterozygousites_ABP: dict = None,
         readdepthforcalledgenotype_infofield_DP: dict = None,
         readdepthforcalledgenotypeperbasepair_DPB: dict = None, refalleleobscount_RO: dict = None,
         infofielddescriptions: dict = None, estimatedallelefrequency_AF: dict = None,
         alternatealleleobservations_AO: dict = None,
         cigarstring_CIGAR: dict = None,
         numberofsampleswithdata_NS: dict = None, sumofqualityofaltobs_QA: dict = None,
         sumofqualityofrefobs_QR: dict = None, sumofqualityofrefobs_formatfield_QR: dict = None,
         sumofqualityofaltobs_formatfield_QA: dict = None,
         variantphased: dict = None,
         variantploidy: dict = None, variantzygosity: dict = None,
         calledgenotype_GT: dict = None, altalleleobscount_partial_PAO: dict = None,
         refalleleobscount_partial_PRO: dict = None,
         propofallelesproperlypaired: dict = None, propofrefallelesproperlypaired: dict = None,
         minreaddepth: dict = None,
         sumqualitiesrefallelecount: dict = None, minreaddepthgvcfblock: dict = None,
         numberofaltalleleobssupportedbypairedreaddata_PAIRED: dict = None,
         numberofrefalleleobssupportedbypairedreaddata_PAIREDR: dict = None,
         altallelephredqualitysumpartialobs_PQA: dict = None, refallelephredqualitysumpartialobs_PQR: dict = None,
         strandbalanceprobability_altallele_SAP: dict = None, strandbalanceprobability_altallele_SAR: dict = None,
         numberofrefobsonfwdstrand_SRF: dict = None,
         numberofrefobsonfwdstrand_SRR: dict = None, numberofaltobservationsonfwdstrand_SAF: dict = None,
         numberofaltobservationsonfwdstrand_SAR: dict = None,
         readdepthforcalledgenotype_formatfield_DP: dict = None
         ):
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", "-i", type=str, required=True)
    parser.add_argument("--outputfile", "-o", type=str, required=True)
    parser.add_argument("--chembldrugbankmapping" "-d", type=str, required=True)
    variant: list[string] = []
    variantdictofdict: dict[str, dict[str, Union[str, dict]]] = {}
    variant_dict = {}
    variantlist = []

    headerlinenumber = 0
    variantlinenumber = 0
    url = 'http://exac.hms.harvard.edu/rest/variant/variant/'
    qurl = ''

    ############################################################################
    # Code starts here (to clean up before this)

    (numberofconsecutiverepeatsofaltallele_RUN, readplacementprobability_RPP,
     readplacementprobabilityforreference_RPPR,
     readsplacedleft_RPL, readsplacedright_RPR, endplacementprob_EPP, endplacementprobref_EPPR,
     altalleledeptratio_DPRA,
     logoddsratio_ODDS,
     typeofallele_TYPE, numaltalleles_AC, totalnumberofallelesincalledgenotype_AN,
     meannoofaltallelespersample_MEANALT,
     numofaltalleleobspersample_NUMALT,
     allelelength_LEN, meanmapqualaltallele_MQM, meanmapqualrefallele_MQMR, genotypequality_GQ,
     genotypeiterations_GTI,
     allelebalanceatheterozygoussites_AB,
     allelebalanceprobabilityatheterozygousites_ABP, readdepthforcalledgenotype_infofield_DP,
     readdepthforcalledgenotypeperbasepair_DPB, refalleleobscount_RO,
     infofielddescriptions, estimatedallelefrequency_AF, alternatealleleobservations_AO, cigarstring_CIGAR,
     numberofsampleswithdata_NS, sumofqualityofaltobs_QA,
     sumofqualityofrefobs_QR, sumofqualityofrefobs_formatfield_QR, sumofqualityofaltobs_formatfield_QA,
     variantphased,
     variantploidy, variantzygosity,
     calledgenotype_GT, altalleleobscount_partial_PAO, refalleleobscount_partial_PRO, propofallelesproperlypaired,
     propofrefallelesproperlypaired, minreaddepth, sumqualitiesrefallelecount, minreaddepthgvcfblock,
     numberofaltalleleobssupportedbypairedreaddata_PAIRED, numberofrefalleleobssupportedbypairedreaddata_PAIREDR,
     altallelephredqualitysumpartialobs_PQA, refallelephredqualitysumpartialobs_PQR,
     strandbalanceprobability_altallele_SAP, strandbalanceprobability_altallele_SAR, numberofrefobsonfwdstrand_SRF,
     numberofrefobsonfwdstrand_SRR, numberofaltobservationsonfwdstrand_SAF, numberofaltobservationsonfwdstrand_SAR,
     readdepthforcalledgenotype_formatfield_DP, numberofobsforeachallele_DPR, refalleleobscount_formatfield_RO,
     exacannotationsforeachvariant
     ) = initdicts()
    genotypelength: dict[string, string] = dict()
    sumqualaltobservations: dict[string, string] = dict()
    altalleleobscount_formatfield_AO = altalleleobscountformatfield()

    line: object
    filehandle: TextIO = open('Challenge_data.vcf', 'r')
    results: TextIO = open('annotatedvcf.txt', 'w')
    results.close()
    linewithchromosomeinfo()
    # Split the INFO line
    for line in filehandle.readlines():
        if line.startswith("##") is True & line.startswith("##INFO") is True:
            try:
                substring: string = re.search(r"\<(.*?)\>", line).group(1)
                # print(substring)
            except AttributeError:
                substring = ""
            # split the string on comma and then equals
            if len(substring) > 0:
                fieldsininfostring: list = substring.split(r",")
                field: string
                for field in fieldsininfostring:
                    # for every field in ID field, populate ID and DESCRIPTION
                    value: string
                    key: string
                    (key, value) = field.split("=")
                    if key == "ID":
                        infofielddescriptions[value] = ""
                        fieldname: string = value
                    if key == "DESCRIPTION":
                        infofielddescriptions[fieldname] = value

        # write out the CHROM line and parse all the fields therein
        if line.startswith("#CHROM") is True:
            # results.write(line)
            chromlinekeys = line.split("\t")

        if line.startswith("#") is False:
            # split every vcf call on tab
            # chromosome number and position are the keys into each dict
            variant = line.split("\t")
            # build the key
            vcfkey: string = variant[0] + "_" + variant[1]
            variant_dict: dict(string, string) = dict(zip(chromlinekeys, variant))
            print("VCF KEY is " + vcfkey)
            # split the info field
            infofield: list = variant_dict['INFO'].replace('\n', '').split(";")
            infofielddict: dict(string, string) = {k: v for k, v in (x.split('=') for x in infofield)}
            variant_dict['INFO_DICT'] = infofielddict
            variantdictofdict[vcfkey] = variant_dict
            genotypequality_GQ[vcfkey] = variant[6]
            # write out allele balance (number of reads supporting homozygous to heterozygous calls at this position)
            allelebalanceatheterozygoussites_AB = vcfpkg.altallelebalanceathetzygoussites(
                allelebalanceatheterozygoussites_AB,
                infofielddict, vcfkey)
            # deviation between allele balance ref and allele balance alt using hoeffing's inequality
            allelebalanceprobabilityatheterozygousites_ABP = vcfpkg.allelebalanceprobatheterozygoussites(
                allelebalanceprobabilityatheterozygousites_ABP, infofielddict, vcfkey)
            # write out individual INFO fields into dicts
            numaltalleles_AC = vcfpkg.numofaltallelesAC(infofielddict, numaltalleles_AC, vcfkey)
            estimatedallelefrequency_AF = vcfpkg.estimatedallelefreqAF(estimatedallelefrequency_AF, infofielddict,
                                                                       vcfkey)
            refalleleobscount_RO = vcfpkg.refalleleobservationcountRO(infofielddict, refalleleobscount_RO, vcfkey)
            numberofconsecutiverepeatsofaltallele_RUN = vcfpkg.noofconsecutiverepeatsofaltalleleRUN(infofielddict,
                                                                                                    numberofconsecutiverepeatsofaltallele_RUN,
                                                                                                    vcfkey)
            readplacementprobability_RPP = vcfpkg.readplacementprobRPP(infofielddict, readplacementprobability_RPP,
                                                                       vcfkey)
            readplacementprobabilityforreference_RPPR = vcfpkg.readplacementprobrefalleleRPPR(infofielddict,
                                                                                              readplacementprobabilityforreference_RPPR,
                                                                                              vcfkey)
            totalnumberofallelesincalledgenotype_AN = vcfpkg.totalnoofallelesincalledgenotypeAN(infofielddict,
                                                                                                totalnumberofallelesincalledgenotype_AN,
                                                                                                vcfkey)
            alternatealleleobservations_AO = vcfpkg.altalleleobsAO(alternatealleleobservations_AO, infofielddict,
                                                                   vcfkey)
            cigarstring_CIGAR = vcfpkg.cigarstringCIGAR(cigarstring_CIGAR, infofielddict, vcfkey)
            readdepthforcalledgenotype_infofield_DP = vcfpkg.readdepthforcalledgenotypeininfofieldDP(infofielddict,
                                                                                                     readdepthforcalledgenotype_infofield_DP,
                                                                                                     vcfkey)
            readdepthforcalledgenotypeperbasepair_DPB = vcfpkg.readdepthforcalledgenotypeperbpDPB(infofielddict,
                                                                                                  readdepthforcalledgenotypeperbasepair_DPB,
                                                                                                  vcfkey)
            altalleledeptratio_DPRA = vcfpkg.altalleledepthratioDPRA(altalleledeptratio_DPRA, infofielddict, vcfkey)
            endplacementprob_EPP = vcfpkg.endplacementprobabilityEPP(endplacementprob_EPP, infofielddict, vcfkey)
            endplacementprobref_EPPR = vcfpkg.endplacementprobforrefalleleEPPR(endplacementprobref_EPPR, infofielddict,
                                                                               vcfkey)
            genotypeiterations_GTI = vcfpkg.genotypeiterationsGTI(genotypeiterations_GTI, infofielddict, vcfkey)
            allelelength_LEN = vcfpkg.allelelengthLEN(allelelength_LEN, infofielddict, vcfkey)
            meannoofaltallelespersample_MEANALT = vcfpkg.meannoofaltallelespersampleMEANALT(infofielddict,
                                                                                            meannoofaltallelespersample_MEANALT,
                                                                                            vcfkey)
            meanmapqualaltallele_MQM = vcfpkg.meanmapqualaltalleleMQM(infofielddict, meanmapqualaltallele_MQM, vcfkey)
            meanmapqualrefallele_MQMR = vcfpkg.meanmapqualrefalleleMQMR(infofielddict, meanmapqualrefallele_MQMR,
                                                                        vcfkey)
            numberofsampleswithdata_NS = vcfpkg.noofsampleswithdataNS(infofielddict, numberofsampleswithdata_NS, vcfkey)
            numofaltalleleobspersample_NUMALT = vcfpkg.numofaltallleleobspersampleNUMALT(infofielddict,
                                                                                         numofaltalleleobspersample_NUMALT,
                                                                                         vcfkey)
            logoddsratio_ODDS = vcfpkg.logoddsratioODDS(infofielddict, logoddsratio_ODDS, vcfkey)
            typeofallele_TYPE = vcfpkg.typeofalleleTYPE(infofielddict, typeofallele_TYPE, vcfkey)
            altalleleobscount_partial_PAO = vcfpkg.altalleleobscountpartialPAO(altalleleobscount_partial_PAO,
                                                                               infofielddict,
                                                                               vcfkey)
            altallelephredqualitysumpartialobs_PQA = vcfpkg.altallelephredqualsumspartialobsPQA(
                altallelephredqualitysumpartialobs_PQA, vcfkey, infofielddict)
            refallelephredqualitysumpartialobs_PQR = vcfpkg.refallelephredqualsumspartialobsPQR(
                refallelephredqualitysumpartialobs_PQR, infofielddict, vcfkey)
            numberofaltalleleobssupportedbypairedreaddata_PAIRED = vcfpkg.noofaltalleleobssupportedbypairedreaddata(
                numberofaltalleleobssupportedbypairedreaddata_PAIRED, infofielddict, vcfkey)
            numberofrefalleleobssupportedbypairedreaddata_PAIREDR = infofielddict["PAIREDR"]
            refalleleobscount_partial_PRO[vcfkey] = infofielddict["PRO"]
            sumofqualityofaltobs_QA[vcfkey] = infofielddict["QA"]
            sumofqualityofrefobs_QR[vcfkey] = infofielddict["QR"]
            refalleleobscount_RO[vcfkey] = infofielddict["RO"]
            alternatealleleobservations_AO[vcfkey] = infofielddict["AO"]
            readsplacedleft_RPL[vcfkey] = infofielddict["RPL"]
            readsplacedright_RPR[vcfkey] = infofielddict["RPR"]
            readplacementprobability_RPP[vcfkey] = infofielddict["RPP"]
            readplacementprobabilityforreference_RPPR[vcfkey] = infofielddict["RPPR"]
            formatfield: string = variant_dict['FORMAT'].replace('\n', '').split(":")
            formatvaluesfield: string = variant_dict['normal'].replace('\n', '').split(":")
            formatfieldcounter: int = 0

            for field in formatfield:
                if field == 'GT':
                    calledgenotype_GT[vcfkey] = formatvaluesfield[formatfieldcounter]
                    # find if homozygous ref, heterozygous, homozygous alt
                    # check ploidy
                    variantphased = assignphasingtovariants(formatfieldcounter, formatvaluesfield, variantphased,
                                                            vcfkey)
                    variantploidy = calculateploidy(formatfieldcounter, formatvaluesfield, variantphased, variantploidy,
                                                    vcfkey)
                    variantzygosity = calculatezygosity(field, variantploidy, variantzygosity, vcfkey)
                elif field == 'GQ':
                    genotypequality_GQ = vcfpkg.assignGenotypeQualityGQ(formatfieldcounter, formatvaluesfield,
                                                                        genotypequality_GQ, vcfkey)
                elif field == 'DP':
                    readdepthforcalledgenotype_formatfield_DP = vcfpkg.readdepthforcalledgenotype_DP(formatfieldcounter,
                                                                                                     formatvaluesfield,
                                                                                                     readdepthforcalledgenotype_formatfield_DP,
                                                                                                     vcfkey)
                elif field == 'DPR':
                    numberofobsforeachallele_DPR = vcfpkg.numberofobservationsforeachallele_DPR(formatfieldcounter,
                                                                                                formatvaluesfield,
                                                                                                numberofobsforeachallele_DPR,
                                                                                                vcfkey)
                elif field == 'QR':
                    sumofqualityofrefobs_formatfield_QR = vcfpkg.sumofqualityscoresforrefallelesinformatfield_QR(
                        formatfieldcounter, formatvaluesfield,
                        sumofqualityofrefobs_formatfield_QR, vcfkey)
                elif field == 'QA':
                    sumofqualityofaltobs_formatfield_QA = vcfpkg.sumofqualityscoresforaltalleleobservations_DQA(
                        formatfieldcounter, formatvaluesfield,
                        sumofqualityofaltobs_formatfield_QA, vcfkey)
                elif field == 'RO':
                    refalleleobscount_formatfield_RO = vcfpkg.refalleleobservationcountsinformatfield_RO(
                        formatfieldcounter,
                        formatvaluesfield,
                        refalleleobscount_formatfield_RO,
                        vcfkey)
                elif field == 'AO':
                    altalleleobscount_formatfield_AO = vcfpkg.altalleleobservationcountinformatfield_AO(
                        altalleleobscount_formatfield_AO, formatfieldcounter,
                        formatvaluesfield, vcfkey)
                separator = "\t"
                formatfieldcounter = formatfieldcounter + 1

            print(vcfkey + "\t" + allelebalanceatheterozygoussites_AB[vcfkey] + "\t" +
                  allelebalanceprobabilityatheterozygousites_ABP[vcfkey] + "\t" + numaltalleles_AC[vcfkey] + "\t" +
                  estimatedallelefrequency_AF[vcfkey] + "\t" + refalleleobscount_RO[vcfkey] + "\t" +
                  numberofconsecutiverepeatsofaltallele_RUN[vcfkey] + "\t" +
                  readplacementprobability_RPP[vcfkey] + "\t" + readplacementprobabilityforreference_RPPR[
                      vcfkey] + "\t" +
                  totalnumberofallelesincalledgenotype_AN[vcfkey] + "\t" +
                  alternatealleleobservations_AO[vcfkey] + "\t" + cigarstring_CIGAR[vcfkey] + "\t" +
                  readdepthforcalledgenotype_infofield_DP[vcfkey] + "\t" +
                  readdepthforcalledgenotypeperbasepair_DPB[vcfkey] + "\t" + altalleledeptratio_DPRA[
                      vcfkey] + "\t" + endplacementprob_EPP[vcfkey] + "\t" +
                  endplacementprobref_EPPR[vcfkey] + "\t" + genotypeiterations_GTI[vcfkey] + "\t" +
                  allelelength_LEN[vcfkey] + "\t" +
                  meannoofaltallelespersample_MEANALT[vcfkey] + "\t" +
                  meanmapqualaltallele_MQM[vcfkey] + "\t" + meanmapqualrefallele_MQMR[vcfkey] + "\t" +
                  numberofsampleswithdata_NS[vcfkey] + "\t" +
                  numofaltalleleobspersample_NUMALT[vcfkey] + "\t" +
                  logoddsratio_ODDS[vcfkey] + "\t" + typeofallele_TYPE[vcfkey] + "\t" +
                  altalleleobscount_partial_PAO[vcfkey] + "\t" +
                  altallelephredqualitysumpartialobs_PQA[vcfkey] + "\t" +
                  refallelephredqualitysumpartialobs_PQR[
                      vcfkey] + "\t" + numberofaltalleleobssupportedbypairedreaddata_PAIRED[vcfkey] + "\n")
            results = open('annotatedvcf.txt', 'a+')
            results.write(vcfkey + "\t" +
                          allelebalanceatheterozygoussites_AB[vcfkey] + "\t" +
                          allelebalanceprobabilityatheterozygousites_ABP[vcfkey] + "\t" + numaltalleles_AC[
                              vcfkey] + "\t" +
                          estimatedallelefrequency_AF[vcfkey] + "\t" + refalleleobscount_RO[vcfkey] + "\t" +
                          numberofconsecutiverepeatsofaltallele_RUN[vcfkey] + "\t" +
                          readplacementprobability_RPP[vcfkey] + "\t" + readplacementprobabilityforreference_RPPR[
                              vcfkey] + "\t" +
                          totalnumberofallelesincalledgenotype_AN[vcfkey] + "\t" +
                          alternatealleleobservations_AO[vcfkey] + "\t" + cigarstring_CIGAR[vcfkey] + "\t" +
                          readdepthforcalledgenotype_infofield_DP[vcfkey] + "\t" +
                          readdepthforcalledgenotypeperbasepair_DPB[vcfkey] + "\t" + altalleledeptratio_DPRA[
                              vcfkey] + "\t" + endplacementprob_EPP[vcfkey] + "\t" +
                          endplacementprobref_EPPR[vcfkey] + "\t" + genotypeiterations_GTI[vcfkey] + "\t" +
                          allelelength_LEN[vcfkey] + "\t" +
                          meannoofaltallelespersample_MEANALT[vcfkey] + "\t" +
                          meanmapqualaltallele_MQM[vcfkey] + "\t" + meanmapqualrefallele_MQMR[vcfkey] + "\t" +
                          numberofsampleswithdata_NS[vcfkey] + "\t" +
                          numofaltalleleobspersample_NUMALT[vcfkey] + "\t" +
                          logoddsratio_ODDS[vcfkey] + "\t" + typeofallele_TYPE[vcfkey] + "\t" +
                          altalleleobscount_partial_PAO[vcfkey] + "\t" +
                          altallelephredqualitysumpartialobs_PQA[vcfkey] + "\t" +
                          refallelephredqualitysumpartialobs_PQR[
                              vcfkey] + "\t" + numberofaltalleleobssupportedbypairedreaddata_PAIRED[vcfkey] + "\n")
            results.close()

            try:
                print("Getting annotations from exac")
                print("http://exac.hms.harvard.edu/rest/variant/variant/" + variant_dict['#CHROM'] + '-' + variant_dict[
                    'POS'] + '-' + variant_dict["REF"] + '-' + variant_dict["ALT"])
                response = requests.get(
                    "http://exac.hms.harvard.edu/rest/variant/variant/" + variant_dict['#CHROM'] + '-' + variant_dict[
                        'POS'] + '-' + variant_dict["REF"] + '-' + variant_dict["ALT"])
                exac_response = response.json()
                response.raise_for_status()
                exac_response = json.loads(response.text)
                exacannotationsforeachvariant[vcfkey] = get_all_values(exac_response)
                keys_list = list(exacannotationsforeachvariant[vcfkey].keys())
                valuestring = {str(value) for value in exacannotationsforeachvariant[vcfkey].values()}
                # print(valuestring)
                keysstring = "\t".join(keys_list)
                # print(keysstring)
                # # Adding additional annotations from ExAC as per SNPEff
                if "vep_annotations" in exac_response:
                    # initializefieldsinvepannotations()
                    ccdsstring: list[string] = []
                    hgvspstring: list[string] = []
                    enspstring: list[string] = []
                    somaticstring: list[string] = []
                    canonicalstring: list[string] = []
                    print(exac_response["vep_annotations"])
                    #######################
                    li: string
                    Allelestrings = exacpkg.extractallelesfromvepannotations(exac_response)
                    consequencestrings = exacpkg.extractconsequencesfromvepannotations(exac_response)
                    majorconsequencestrings = exacpkg.majorconsequencestring(exac_response)
                    genenamestrings = exacpkg.genenamestring(exac_response)
                    symbolStrings = [li['SYMBOL'] for li in exac_response["vep_annotations"]]
                    codonstrings = [li['Codons'] for li in exac_response["vep_annotations"]]
                    motifnametrings = [li['MOTIF_NAME'] for li in exac_response["vep_annotations"]]
                    hgncidstrings = [li['HGNC_ID'] for li in exac_response["vep_annotations"]]
                    Feature_typestrings = [li['Feature_type'] for li in exac_response["vep_annotations"]]
                    Featurestrings = [li['Feature'] for li in exac_response["vep_annotations"]]
                    biotypestrings = [li['BIOTYPE'] for li in exac_response["vep_annotations"]]
                    CDSPositionstrings = [li['CDS_position'] for li in exac_response["vep_annotations"]]
                    cDNAPositionstrings = [li['cDNA_position'] for li in exac_response["vep_annotations"]]
                    proteinPositionstrings = [li['Protein_position'] for li in exac_response["vep_annotations"]]
                    exonstrings = [li['EXON'] for li in exac_response["vep_annotations"]]
                    intronstrings = [li['INTRON'] for li in exac_response["vep_annotations"]]
                    HGVScstrings = [li['HGVSc'] for li in exac_response["vep_annotations"]]
                    HGVSpstrings = [li['HGVSp'] for li in exac_response["vep_annotations"]]
                    siftstrings: list[string] = [li['SIFT'] for li in exac_response["vep_annotations"]]
                    ccdsstring: list[string] = [li['CCDS'] for li in exac_response["vep_annotations"]]
                    polyphenstring: list[string] = [li['PolyPhen'] for li in exac_response["vep_annotations"]]
                    hgvspstring: list[string] = []
                    enspstring: list[string] = [li['ENSP'] for li in exac_response["vep_annotations"]]
                    existingvariationstring: list[string] = [li['Existing_variation'] for li in
                                                             exac_response["vep_annotations"]]
                    swissprotstring: list[string] = [li['SWISSPROT'] for li in exac_response["vep_annotations"]]
                    uniparcstring: list[string] = [li['UNIPARC'] for li in exac_response["vep_annotations"]]
                    domainstring: list[string] = [li['DOMAINS'] for li in exac_response["vep_annotations"]]
                    tremblstring: list[string] = [li['TREMBL'] for li in exac_response["vep_annotations"]]
                    motifposstring: list[string] = []
                    clinicalsignificancestring: list[string] = [li['CLIN_SIG'] for li in
                                                                exac_response["vep_annotations"]]
                    pubmedstring: list[string] = [li['PUBMED'] for li in exac_response["vep_annotations"]]
                    motifscorechange: list[string] = [li['MOTIF_SCORE_CHANGE'] for li in
                                                      exac_response["vep_annotations"]]
                    gmafstring: list[string] = [li['GMAF'] for li in
                                                exac_response["vep_annotations"]]
                    somaticstring: list[string] = [li['SOMATIC'] for li in
                                                   exac_response["vep_annotations"]]
                    canonicalstring: list[string] = [li['CANONICAL'] for li in exac_response["vep_annotations"]]
                    asnmafstring: list[string] = [li['ASN_MAF'] for li in exac_response["vep_annotations"]]
                    amrmafstring: list[string] = [li['AMR_MAF'] for li in exac_response["vep_annotations"]]
                    #######################
                    # Create Annotation String#
                    vepannotationsfromexac = zip(to_utf8(Allelestrings), to_utf8(consequencestrings),
                                                 to_utf8(majorconsequencestrings), to_utf8(genenamestrings),
                                                 to_utf8(symbolStrings), to_utf8(codonstrings),
                                                 to_utf8(motifnametrings),
                                                 to_utf8(hgncidstrings), to_utf8(Feature_typestrings),
                                                 to_utf8(Featurestrings), to_utf8(biotypestrings),
                                                 to_utf8(HGVScstrings), to_utf8(HGVSpstrings),
                                                 to_utf8(exonstrings), to_utf8(intronstrings),
                                                 to_utf8(HGVScstrings), to_utf8(HGVSpstrings),
                                                 to_utf8(siftstrings), to_utf8(ccdsstring),
                                                 to_utf8(proteinPositionstrings), to_utf8(polyphenstring),
                                                 to_utf8(enspstring), to_utf8(existingvariationstring),
                                                 to_utf8(swissprotstring), to_utf8(uniparcstring),
                                                 to_utf8(domainstring), to_utf8(tremblstring),
                                                 to_utf8(clinicalsignificancestring), to_utf8(pubmedstring),
                                                 to_utf8(motifscorechange), to_utf8(gmafstring),
                                                 to_utf8(somaticstring), to_utf8(canonicalstring),
                                                 to_utf8(asnmafstring), to_utf8(amrmafstring),
                                                 to_utf8(CDSPositionstrings), to_utf8(cDNAPositionstrings))
                    finalData = setfinaldata()
                    print("VEP Annotations from Exac ")
                    print(list(vepannotationsfromexac))
                    vepannotations = "\t".join(list(vepannotationsfromexac))
                    print(vepannotations)
                    lengthlist = len(genenamestrings)
                    print("Getting annotations from Ensembl")
                    for counter in range(lengthlist):
                        ensgs = genenamestrings[counter]
                        print("Ensembl Gene Id " + ensgs)
                        rsid = existingvariationstring[counter]
                        # print("Request string is " + "http://david.abcc.ncifcrf.gov/api.jsp?type=ENSEMBL_GENE_ID&ids="+ensgs+"&tool=chartReport&annot=GOTERM_BP_FAT,GOTERM_CC_FAT,GOTERM_MF_FAT,INTERPRO,PIR_SUPERFAMILY,SMART,BBID,BIOCARTA,KEGG_PATHWAY,COG_ONTOLOGY,SP_PIR_KEYWORDS,UP_SEQ_FEATURE,GENETIC_ASSOCIATION_DB_DISEASE,OMIM_DISEASE")
                        string = setdavidannotationsrestapiendpoint(ensgs)
                        print(string)
                        server = setemsemblserverrestapi()
                        ext = "/eqtl/id/homo_sapiens/" + ensgs + "?statistic=p-value;variant_name=" + rsid
                        r = requests.get(server + ext, headers={"Content-Type": "application/json"})
                        if not r.ok:
                            r.raise_for_status()
                            sys.exit()
                        decoded = r.json()
                        print("Results from Ensembl")
                        print(repr(decoded))
                        print(printlistofdicts(decoded))
                        uniprotid = getensembltouniprotids(ensgs)
                        if uniprotid == string.empty:
                            continue
                        else:
                            getdrugbanktargetsfromchemblids(chembltouniprotfile, uniprotid)
                            # get drugbank id from uniprot id
                else:
                    finalData = ''
                    # # Get TYPE from INFO Field of VCF
                    # annotation_string += "TYPE=" + variant_dict['INFO_DICT']['TYPE'] + ","
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')


def initializefieldsinvepannotations():
    veppkg.allelesinvepannotations()
    veppkg.consequencesinvepannotations()
    veppkg.majorconsequencesinvepannotations()
    veppkg.genenamesinvepannotations()
    veppkg.hgncidsinvepannotations()
    veppkg.featuretypesinvepannotations()
    veppkg.featuresinvepannotations()
    veppkg.biotypeinvepannotations()
    veppkg.exonsinvepannotations()
    veppkg.intronsinvepannotations()
    veppkg.hgvscrefsinvepannotations()
    veppkg.hgvsprefsinvepannotations()
    veppkg.cdsPositionsinvepannotations()
    veppkg.cdnapositionsinvepannotations()
    veppkg.proteinpositionsinvepannotations()
    veppkg.symbolsinvepannotations()
    veppkg.codonsinvepannotations()
    veppkg.siftmethodinvepannotations()
    veppkg.asnmafinvepannotations()
    veppkg.amrmafinvepannotations()
    veppkg.existingvariationsinvepannotations()
    veppkg.swissprotinvepannotations()
    veppkg.uniparcreferencesinvepannotations()
    veppkg.domainsinvepannotations()
    veppkg.tremblreferencesinvepannotations()
    veppkg.motifpositionsinvepannotations()
    veppkg.clinicalsignificanceinvepannotations()
    veppkg.pubmedreferencesinvepannotations()
    veppkg.motifscoreinvepannotations()
    veppkg.gmafreferencesinvepannotations()
    veppkg.polyphenannotationsinvepannotations()


def setfinaldata():
    """

    :return: 
    """
    finalData = ''
    return finalData


def setdavidannotationsrestapiendpoint(ensgs):
    """

    :rtype: object
    :param ensgs: 
    :return: 
    """
    string: Union[
        str, Any] = "http://david.abcc.ncifcrf.gov/api.jsp?type=ENSEMBL_GENE_ID&ids=" + ensgs + "&tool=geneReportFull"
    return string


def setemsemblserverrestapi():
    server = "https://rest.ensembl.org"
    return server


def calculatezygosity(field, variantploidy, variantzygosity, vcfkey):
    if len(re.findall('[1-9]+', field)) == 0:
        variantzygosity[vcfkey] = "homozygousref"
    elif (
            len(re.findall("1")) == variantploidy[vcfkey]
            |
            len(re.findall("2")) == variantploidy[vcfkey]
            |
            len(re.findall("3")) == variantploidy[vcfkey]
            |
            len(re.findall("4")) == variantploidy[vcfkey]
            |
            len(re.findall("5")) == variantploidy[vcfkey]
            |
            len(re.findall("6")) == variantploidy[vcfkey]
            |
            len(re.findall("7")) == variantploidy[vcfkey]
            |
            len(re.findall("8")) == variantploidy[vcfkey]
            |
            len(re.findall("9")) == variantploidy[vcfkey]
    ):
        variantzygosity[vcfkey] == "homozygousalt"
    else:
        variantzygosity[vcfkey] == "heterozygous"
    return variantzygosity


def calculateploidy(formatfieldcounter, formatvaluesfield, variantphased, variantploidy, vcfkey):
    if (variantphased[vcfkey]) == "unphased":
        variantploidy[vcfkey] = formatvaluesfield[formatfieldcounter].count('/')
    else:
        variantploidy[vcfkey] = formatvaluesfield[formatfieldcounter].count('|')
    return variantploidy


def assignphasingtovariants(formatfieldcounter, formatvaluesfield, variantphased, vcfkey):
    # check if phased
    # move out these logic into packages
    if "/" in formatvaluesfield[formatfieldcounter]:
        variantphased[vcfkey] = "unphased"
    else:
        variantphased[vcfkey] = "phased"
    return variantphased


def linewithchromosomeinfo():
    chromelinekeys = []


# print(variantdictofdict['7117']['INFO'])
# while i < len(variantListForRestAPI):
#     slicedVariantList = variantListForRestAPI[i:50]
#     print("http://exac.hms.harvard.edu/rest/bulk/variant/variant" + json.dumps(slicedVariantList))
#     response = requests.post("http://exac.hms.harvard.edu/rest/variant/variant" + json.dumps(slicedVariantList))
#     print(response.status_code, "***STATUS CODE***")

def gettypeofvariants(d, consequencestr):
    """

    :type consequencestr: object
    """
    # print(d)
    for k, v in d.items():
        if type(v) is dict:
            gettypeofvariants(v, consequencestr)
        elif k.equals("Consequence"):
            # print("Inside else")
            consequencestr.append(":").v
    return consequencestr


def to_utf8(d):
    # print(type(d))
    utf8string = [str(items) for items in d]
    # print(utf8string)
    return utf8string


def utf8(d):
    # print ast.literal_eval(json.dumps(d))
    d1 = ast.literal_eval(json.dumps(d))
    return d1


def printDict(dict):
    dict = ast.literal_eval(json.dumps(dict))
    for key, value in dict.items():
        if type(value) is dict:
            printDict(value)
        else:
            print("{0} : {1}".format(str(key), str(value)))


if __name__ == "__main__":
    start_time = time.monotonic()
    main()
    end_time = time.monotonic()
    print(timedelta(seconds=end_time - start_time))
    names = {}
    # for namess in sysstdin.readlines():
    #     namess = namess.strip()
