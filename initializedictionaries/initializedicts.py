import string

def initdicts():
    numberofconsecutiverepeatsofaltallele_RUN: dict[string, string] = noofconsecutiverepeatsofaltallele()
    readplacementprobability_RPP: dict[string, string] = readplacementprob_RPP()
    readplacementprobabilityforreference_RPPR: dict[string, string] = readplacementprobref_RPPR()
    readsplacedleft_RPL: dict[string, string] = readsplacedleftRPL()
    readsplacedright_RPR: dict[string, string] = readsplacedrightRPR()
    endplacementprob_EPP: dict[string, string] = endplacementprobEPP()
    endplacementprobref_EPPR: dict[string, string] = endplacementprobrefEPPR()
    altalleledeptratio_DPRA: dict[string, string] = altalleledepthratio()
    logoddsratio_ODDS: dict[string, string] = logoddsratio()
    typeofallele_TYPE: dict[string, string] = typeofallele()
    numaltalleles_AC: dict[string, string] = numofaltalleles()
    totalnumberofallelesincalledgenotype_AN: dict[string, string] = totalnoofallelesincalledgenotype()
    meannoofaltallelespersample_MEANALT: dict[string, string] = meannoofaltallelespersample()
    numofaltalleleobspersample_NUMALT: dict[string, string] = noofaltallelespersample()
    allelelength_LEN: dict[string, string] = allelelength()
    meanmapqualrefallele_MQMR: dict[string, string] = meanmapqualrefallele()
    meanmapqualaltallele_MQM: dict[string, string] = meanmapqualaltallele()
    genotypequality_GQ: dict[string, string] = genotypequality()
    genotypeiterations_GTI: dict[string, string] = genotypeiterations()
    allelebalanceatheterozygoussites_AB: dict[string, string] = allelebalanceatheterozygoussites()
    allelebalanceprobabilityatheterozygousites_ABP: dict[string, string] = allelebalprobatheterozygoussites()
    readdepthforcalledgenotype_infofield_DP: dict[string, string] = readdepthcalledgenotype_infofield()
    readdepthforcalledgenotypeperbasepair_DPB: dict[string, string] = readdepthforcalledgenotypeperbp()
    refalleleobscount_RO: dict[string, string] = refalleleobservationcount()
    infofielddescriptions: dict[string, string] = infofielddescription()
    estimatedallelefrequency_AF: dict[string, string] = estimatedallelefreq()
    alternatealleleobservations_AO: dict[string, string] = altalleleobservations()
    cigarstring_CIGAR: dict[string, string] = cigarstring()
    numberofsampleswithdata_NS: dict[string, string] = numberofsampleswithdata()
    sumofqualityofaltobs_QA: dict[string, string] = sumqualityaltobservations()
    sumofqualityofrefobs_QR: dict[string, string] = sumqualityrefobservations()
    sumofqualityofrefobs_formatfield_QR: dict[string, string] = sumqualityrefobservations_formatfield()
    sumofqualityofaltobs_formatfield_QA: dict[string, string] = sumqualityaltobservations_formatfield()
    variantphased: dict[string, string] = variantphasing()
    variantploidy: dict[string, string] = variant_ploidy()
    variantzygosity: dict[string, string] = variant_zygosity()
    calledgenotype_GT: dict[string, string] = calledgenotype()
    altalleleobscount_partial_PAO: dict[string, string] = altalleleobscount()
    refalleleobscount_partial_PRO: dict[string, string] = refallelepartialobscount()
    propofallelesproperlypaired: dict[string, string] = proportionofallelesproperlypaired()
    propofrefallelesproperlypaired: dict[string, string] = proportionofrefallelesproperlypaired()
    minreaddepth: dict[string, string] = minimumreaddepth()
    sumqualitiesrefallelecount: dict[string, string] = sumqualitiesrefallelecounts()
    minreaddepthgvcfblock: dict[string, string] = minreaddepthingvcfblock()
    numberofaltalleleobssupportedbypairedreaddata_PAIRED = numofaltallelessupportedbypairedreaddata()
    numberofrefalleleobssupportedbypairedreaddata_PAIREDR = numofrefallelesupportedbypairedreaddata()
    altallelephredqualitysumpartialobs_PQA = altallelesphredqualsumofpartialobs()
    refallelephredqualitysumpartialobs_PQR = refallelesphredqualsumofpartialobs()
    strandbalanceprobability_altallele_SAP = strandbalanceprobaltallele()
    strandbalanceprobability_altallele_SAR = strandbalanceprobrefallele()
    numberofrefobsonfwdstrand_SRF = numberofrefallelesobsonfwdstrand()
    numberofrefobsonfwdstrand_SRR = numberofrefallelesobsonrevstrand()
    numberofaltobservationsonfwdstrand_SAF = numberofaltalleleobsonfwdstrand()
    numberofaltobservationsonfwdstrand_SAR = numberofaltallelesobsonreversestrand()
    readdepthforcalledgenotype_formatfield_DP = readdepthforcalledgenotypeinformatfield()
    numberofobsforeachallele_DPR = noofobsforeachalleleDPR()
    refalleleobscount_formatfield_RO = refalleleobscountformatfield()
    exacannotationsforeachvariant = exacannotationsforeachvariantinvcf()
    return (
        numberofconsecutiverepeatsofaltallele_RUN, readplacementprobability_RPP,
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
        exacannotationsforeachvariant)


def altalleleobscountformatfield():
    """

    :return: 
    """
    altalleleobscount_formatfield_AO: dict[string, string] = dict()
    return altalleleobscount_formatfield_AO


def noofobsforeachalleleDPR():
    """

    :return: 
    """
    numberofobsforeachallele_DPR: dict[string, string] = dict()
    return numberofobsforeachallele_DPR


def exacannotationsforeachvariantinvcf():
    """

    :return: 
    """
    exacannotationsforeachvariant: dict[string, string] = dict()
    return exacannotationsforeachvariant


def refalleleobscountformatfield():
    """

    :return: 
    """
    refalleleobscount_formatfield_RO: dict[string, string] = dict()
    return refalleleobscount_formatfield_RO


def readdepthforcalledgenotypeinformatfield():
    """

    :return: 
    """
    readdepthforcalledgenotype_formatfield_DP: dict[string, string] = dict()
    return readdepthforcalledgenotype_formatfield_DP


def numberofaltallelesobsonreversestrand():
    """

    :return: 
    """
    numberofaltobservationsonreversestrand_SAR: dict[string, string] = dict()
    return numberofaltobservationsonreversestrand_SAR


def numberofaltalleleobsonfwdstrand():
    """

    :return: 
    """
    numberofaltobservationsonfwdstrand_SAF: dict[string, string] = dict()
    return numberofaltobservationsonfwdstrand_SAF


def numberofrefallelesobsonrevstrand():
    """

    :return: 
    """
    numberofrefobsonreversestrand_SRR: dict[string, string] = dict()
    return numberofrefobsonreversestrand_SRR


def numberofrefallelesobsonfwdstrand():
    """

    :return: 
    """
    numberofrefobsonfwdstrand_SRF: dict[string, string] = dict()
    return numberofrefobsonfwdstrand_SRF


def strandbalanceprobrefallele():
    """

    :return: 
    """
    strandbalanceprobability_refallele_SRP: dict[string, string] = dict()
    return strandbalanceprobability_refallele_SRP


def strandbalanceprobaltallele():
    """

    :return: 
    """
    strandbalanceprobability_altallele_SAP: dict[string, string] = dict()
    return strandbalanceprobability_altallele_SAP


def refallelesphredqualsumofpartialobs():
    """

    :return: 
    """
    refallelephredqualitysumpartialobs_PQR: dict[string, string] = dict()
    return refallelephredqualitysumpartialobs_PQR


def altallelesphredqualsumofpartialobs():
    """

    :return: 
    """
    altallelephredqualitysumpartialobs_PQA: dict[string, string] = dict()
    return altallelephredqualitysumpartialobs_PQA


def numofrefallelesupportedbypairedreaddata():
    """

    :return: 
    """
    numberofrefalleleobssupportedbypairedreaddata_PAIREDR: dict[string, string] = dict()
    return numberofrefalleleobssupportedbypairedreaddata_PAIREDR


def numofaltallelessupportedbypairedreaddata():
    """

    :return: 
    """
    numberofaltalleleobssupportedbypairedreaddata_PAIRED: dict[string, string] = dict()
    return numberofaltalleleobssupportedbypairedreaddata_PAIRED


def minreaddepthingvcfblock():
    """

    :return: 
    """
    mindepthingvcfblock: dict[string, string] = dict()
    return mindepthingvcfblock


def sumqualitiesrefallelecounts():
    """

    :return: 
    """
    sumqualityrefallelecount: dict[string, string] = dict()
    return sumqualityrefallelecount


def minimumreaddepth():
    """

    :return: 
    """
    minreaddepth: dict[string, string] = dict()
    return minreaddepth


def proportionofrefallelesproperlypaired():
    """

    :return: 
    """
    proprefallelesproperlypaired: dict[string, string] = dict()
    return proprefallelesproperlypaired


def proportionofallelesproperlypaired() -> dict:
    propaltallelesproprerlypaired: dict[string, string] = dict()
    return propaltallelesproprerlypaired


def variant_zygosity() -> dict:
    variantzygosity: dict[string, string] = dict()
    return variantzygosity


def variant_ploidy() -> dict:
    variantploidy: dict[string, string] = dict()
    return variantploidy


def variantphasing() -> dict:
    variantphased: dict[string, string] = dict()
    return variantphased


def sumqualityaltobservations_formatfield() -> dict:
    sumofqualityofaltobs_formatfield_QA: dict[string, string] = dict()
    return sumofqualityofaltobs_formatfield_QA


def sumqualityrefobservations_formatfield() -> dict:
    sumofqualityofrefobs_formatfield_QR: dict[string, string] = dict()
    return sumofqualityofrefobs_formatfield_QR


def sumqualityrefobservations() -> dict:
    sumofqualityofrefobs_QR: dict[string, string] = dict()
    return sumofqualityofrefobs_QR


def sumqualityaltobservations() -> dict:
    sumofqualityofaltobs_QA: dict[string, string] = dict()
    return sumofqualityofaltobs_QA


def numberofsampleswithdata() -> dict:
    numberofsampleswithdata_NS: dict[string, string] = dict()
    return numberofsampleswithdata_NS


def cigarstring() -> dict:
    cigarstring_CIGAR: dict[string, string] = dict()
    return cigarstring_CIGAR


def altalleleobservations() -> dict:
    alternatealleleobservations_AO: dict[string, string] = dict()
    return alternatealleleobservations_AO


def estimatedallelefreq() -> dict:
    estimatedallelefrequency_AF: dict[string, string] = dict()
    return estimatedallelefrequency_AF


def infofielddescription() -> dict:
    infofielddescriptions: dict[string, string] = dict()
    return infofielddescriptions


def refallelepartialobscount() -> dict:
    refalleleobscount_partial_PRO: dict[string, string] = dict()
    return refalleleobscount_partial_PRO


def altalleleobscount() -> dict:
    altalleleobscount_partial_PAO: dict[string, string] = dict()
    return altalleleobscount_partial_PAO


def refalleleobservationcount() -> dict:
    refalleleobscount_RO: dict[string, string] = dict()
    return refalleleobscount_RO


def readdepthforcalledgenotypeperbp() -> dict:
    readdepthforcalledgenotypeperbasepair_DPB: dict[string, string] = dict()
    return readdepthforcalledgenotypeperbasepair_DPB


def readdepthcalledgenotype_infofield() -> dict:
    readdepthforcalledgenotype_infofield_DP: dict[string, string] = dict()
    return readdepthforcalledgenotype_infofield_DP


def allelebalprobatheterozygoussites() -> dict:
    allelebalanceprobabilityatheterozygousites_ABP: dict[string, string] = dict()
    return allelebalanceprobabilityatheterozygousites_ABP


def allelebalanceatheterozygoussites() -> dict:
    allelebalanceatheterozygoussites_AB: dict[string, string] = dict()
    return allelebalanceatheterozygoussites_AB


def genotypeiterations() -> dict:
    genotypeiterations_GTI: dict[string, string] = dict()
    return genotypeiterations_GTI


def genotypequality() -> dict():
    genotypequality_GQ: dict[string, string] = dict()
    return genotypequality_GQ


def calledgenotype() -> dict():
    calledgenotype_GT: dict[string, string] = dict()
    return calledgenotype_GT


def meanmapqualaltallele() -> dict():
    meanmapqualaltallele_MQM: dict[string, string] = dict()
    return meanmapqualaltallele_MQM


def meanmapqualrefallele() -> dict():
    meanmapqualrefallele_MQMR: dict[string, string] = dict()
    return meanmapqualrefallele_MQMR


def allelelength() -> dict():
    allelelength_LEN: dict[string, string] = dict()
    return allelelength_LEN


def noofaltallelespersample() -> dict():
    numofaltalleleobspersample_NUMALT: dict[string, string] = dict()
    return numofaltalleleobspersample_NUMALT


def meannoofaltallelespersample() -> dict():
    meannoofaltallelespersample_MEANALT: dict[string, string] = dict()
    return meannoofaltallelespersample_MEANALT


def totalnoofallelesincalledgenotype() -> dict():
    totalnumberofallelesincalledgenotype_AN: dict[string, string] = dict()
    return totalnumberofallelesincalledgenotype_AN


def numofaltalleles() -> dict():
    numaltalleles_AC: dict[string, string] = dict()
    return numaltalleles_AC


def typeofallele() -> dict():
    typeofallele_TYPE: dict[string, string] = dict()
    return typeofallele_TYPE


def logoddsratio() -> dict():
    logoddsratio_ODDS: dict[string, string] = dict()
    return logoddsratio_ODDS


def altalleledepthratio() -> dict():
    altalleledeptratio_DPRA: dict[string, string] = dict()
    return altalleledeptratio_DPRA


def endplacementprobrefEPPR() -> dict():
    endplacementprobref_EPPR: dict[string, string] = dict()
    return endplacementprobref_EPPR


def endplacementprobEPP():
    endplacementprob_EPP: dict[string, string] = dict()
    return endplacementprob_EPP


def readsplacedrightRPR():
    readsplacedright_RPR: dict[string, string] = dict()
    return readsplacedright_RPR


def readsplacedleftRPL():
    readsplacedleft_RPL: dict[string, string] = dict()
    return readsplacedleft_RPL


def readplacementprobref_RPPR():
    readplacementprobabilityforreference_RPPR: dict[string, string] = dict()
    return readplacementprobabilityforreference_RPPR


def readplacementprob_RPP():
    readplacementprobability_RPP: dict[string, string] = dict()
    return readplacementprobability_RPP


def noofconsecutiverepeatsofaltallele():
    """

    :rtype: object
    """
    numberofconsecutiverepeatsofaltallele_RUN: dict[string, string] = dict()
    return numberofconsecutiverepeatsofaltallele_RUN
