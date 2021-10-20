
def noofaltalleleobssupportedbypairedreaddata(numberofaltalleleobssupportedbypairedreaddata_PAIRED, infofielddict,
                                              vcfkey):
    """

    :param numberofaltalleleobssupportedbypairedreaddata_PAIRED:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    numberofaltalleleobssupportedbypairedreaddata_PAIRED[vcfkey] = infofielddict["PAIRED"]
    return numberofaltalleleobssupportedbypairedreaddata_PAIRED


def refallelephredqualsumspartialobsPQR(refallelephredqualitysumpartialobs_PQR, infofielddict, vcfkey):
    """

    :param refallelephredqualitysumpartialobs_PQR:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    refallelephredqualitysumpartialobs_PQR[vcfkey] = infofielddict["PQR"]
    return refallelephredqualitysumpartialobs_PQR


def altallelephredqualsumspartialobsPQA(altallelephredqualitysumpartialobs_PQA, vcfkey, infofielddict):
    """

    :param altallelephredqualitysumpartialobs_PQA:
    :param vcfkey:
    :param infofielddict:
    :return:
    """
    altallelephredqualitysumpartialobs_PQA[vcfkey] = infofielddict["PQA"]
    return altallelephredqualitysumpartialobs_PQA


def altalleleobscountpartialPAO(altalleleobscount_partial_PAO, infofielddict, vcfkey):
    """

    :param altalleleobscount_partial_PAO:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    altalleleobscount_partial_PAO[vcfkey] = infofielddict["PAO"]
    return altalleleobscount_partial_PAO


def typeofalleleTYPE(infofielddict, typeofallele_TYPE, vcfkey):
    """

    :param infofielddict:
    :param typeofallele_TYPE:
    :param vcfkey:
    :return:
    """
    typeofallele_TYPE[vcfkey] = infofielddict["TYPE"]
    return typeofallele_TYPE


def logoddsratioODDS(infofielddict, logoddsratio_ODDS, vcfkey):
    """

    :param infofielddict:
    :param logoddsratio_ODDS:
    :param vcfkey:
    :return:
    """
    logoddsratio_ODDS[vcfkey] = infofielddict["ODDS"]
    return logoddsratio_ODDS


def numofaltallleleobspersampleNUMALT(infofielddict, numofaltalleleobspersample_NUMALT, vcfkey):
    """

    :param infofielddict:
    :param numofaltalleleobspersample_NUMALT:
    :param vcfkey:
    :return:
    """
    numofaltalleleobspersample_NUMALT[vcfkey] = infofielddict["NUMALT"]
    return numofaltalleleobspersample_NUMALT


def noofsampleswithdataNS(infofielddict, numberofsampleswithdata_NS, vcfkey):
    """

    :param infofielddict:
    :param numberofsampleswithdata_NS:
    :param vcfkey:
    :return:
    """
    numberofsampleswithdata_NS[vcfkey] = infofielddict["NS"]
    return numberofsampleswithdata_NS


def meanmapqualrefalleleMQMR(infofielddict, meanmapqualrefallele_MQMR, vcfkey):
    """

    :param infofielddict:
    :param meanmapqualrefallele_MQMR:
    :param vcfkey:
    :return:
    """
    meanmapqualrefallele_MQMR[vcfkey] = infofielddict["MQMR"]
    return meanmapqualrefallele_MQMR


def meanmapqualaltalleleMQM(infofielddict, meanmapqualaltallele_MQM, vcfkey):
    """

    :param infofielddict:
    :param meanmapqualaltallele_MQM:
    :param vcfkey:
    :return:
    """
    meanmapqualaltallele_MQM[vcfkey] = infofielddict["MQM"]
    return meanmapqualaltallele_MQM


def meannoofaltallelespersampleMEANALT(infofielddict, meannoofaltallelespersample_MEANALT, vcfkey):
    """

    :param infofielddict:
    :param meannoofaltallelespersample_MEANALT:
    :param vcfkey:
    :return:
    """
    meannoofaltallelespersample_MEANALT[vcfkey] = infofielddict["MEANALT"]
    return meannoofaltallelespersample_MEANALT


def allelelengthLEN(allelelength_LEN, infofielddict, vcfkey):
    """

    :param allelelength_LEN:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    allelelength_LEN[vcfkey] = infofielddict["LEN"]
    return allelelength_LEN


def genotypeiterationsGTI(genotypeiterations_GTI, infofielddict, vcfkey):
    """

    :param genotypeiterations_GTI:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    genotypeiterations_GTI[vcfkey] = infofielddict["GTI"]
    return genotypeiterations_GTI


def endplacementprobforrefalleleEPPR(endplacementprobref_EPPR, infofielddict, vcfkey):
    """

    :param endplacementprobref_EPPR:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    endplacementprobref_EPPR[vcfkey] = infofielddict["EPPR"]
    return endplacementprobref_EPPR


def endplacementprobabilityEPP(endplacementprob_EPP, infofielddict, vcfkey):
    """

    :param endplacementprob_EPP:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    endplacementprob_EPP[vcfkey] = infofielddict["EPP"]
    return endplacementprob_EPP


def altalleledepthratioDPRA(altalleledeptratio_DPRA, infofielddict, vcfkey):
    """

    :param altalleledeptratio_DPRA:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    altalleledeptratio_DPRA[vcfkey] = infofielddict["DPRA"]
    return altalleledeptratio_DPRA


def readdepthforcalledgenotypeperbpDPB(infofielddict, readdepthforcalledgenotypeperbasepair_DPB, vcfkey):
    """

    :param infofielddict:
    :param readdepthforcalledgenotypeperbasepair_DPB:
    :param vcfkey:
    :return:
    """
    readdepthforcalledgenotypeperbasepair_DPB[vcfkey] = infofielddict["DPB"]
    return readdepthforcalledgenotypeperbasepair_DPB


def readdepthforcalledgenotypeininfofieldDP(infofielddict, readdepthforcalledgenotype_infofield_DP, vcfkey):
    """

    :param infofielddict:
    :param readdepthforcalledgenotype_infofield_DP:
    :param vcfkey:
    :return:
    """
    readdepthforcalledgenotype_infofield_DP[vcfkey] = infofielddict["DP"]
    return readdepthforcalledgenotype_infofield_DP


def cigarstringCIGAR(cigarstring_CIGAR, infofielddict, vcfkey):
    """

    :param cigarstring_CIGAR:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    cigarstring_CIGAR[vcfkey] = infofielddict["CIGAR"]
    return cigarstring_CIGAR


def altalleleobsAO(alternatealleleobservations_AO, infofielddict, vcfkey):
    """

    :param alternatealleleobservations_AO:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    alternatealleleobservations_AO[vcfkey] = infofielddict["AO"]
    return alternatealleleobservations_AO


def totalnoofallelesincalledgenotypeAN(infofielddict, totalnumberofallelesincalledgenotype_AN, vcfkey):
    """

    :param infofielddict:
    :param totalnumberofallelesincalledgenotype_AN:
    :param vcfkey:
    :return:
    """
    totalnumberofallelesincalledgenotype_AN[vcfkey] = infofielddict["AN"]
    return totalnumberofallelesincalledgenotype_AN


def readplacementprobrefalleleRPPR(infofielddict, readplacementprobabilityforreference_RPPR, vcfkey):
    """

    :param infofielddict:
    :param readplacementprobabilityforreference_RPPR:
    :param vcfkey:
    :return:
    """
    readplacementprobabilityforreference_RPPR[vcfkey] = infofielddict["RPPR"]
    return readplacementprobabilityforreference_RPPR


def readplacementprobRPP(infofielddict, readplacementprobability_RPP, vcfkey):
    """

    :param infofielddict:
    :param readplacementprobability_RPP:
    :param vcfkey:
    :return:
    """
    readplacementprobability_RPP[vcfkey] = infofielddict["RPP"]
    return readplacementprobability_RPP


def noofconsecutiverepeatsofaltalleleRUN(infofielddict, numberofconsecutiverepeatsofaltallele_RUN, vcfkey):
    """

    :param infofielddict:
    :param numberofconsecutiverepeatsofaltallele_RUN:
    :param vcfkey:
    :return:
    """
    numberofconsecutiverepeatsofaltallele_RUN[vcfkey] = infofielddict["RUN"]
    return numberofconsecutiverepeatsofaltallele_RUN


def refalleleobservationcountRO(infofielddict, refalleleobscount_RO, vcfkey):
    """

    :param infofielddict:
    :param refalleleobscount_RO:
    :param vcfkey:
    :return:
    """
    refalleleobscount_RO[vcfkey] = infofielddict["RO"]
    return refalleleobscount_RO


def estimatedallelefreqAF(estimatedallelefrequency_AF, infofielddict, vcfkey):
    """

    :param estimatedallelefrequency_AF:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    estimatedallelefrequency_AF[vcfkey] = infofielddict["AF"]
    return estimatedallelefrequency_AF


def numofaltallelesAC(infofielddict, numaltalleles_AC, vcfkey):
    """

    :param infofielddict:
    :param numaltalleles_AC:
    :param vcfkey:
    :return:
    """
    numaltalleles_AC[vcfkey] = infofielddict["AC"]
    return numaltalleles_AC


def allelebalanceprobatheterozygoussites(allelebalanceprobabilityatheterozygousites_ABP, infofielddict, vcfkey):
    """

    :param allelebalanceprobabilityatheterozygousites_ABP:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    allelebalanceprobabilityatheterozygousites_ABP[vcfkey] = infofielddict["ABP"]
    return allelebalanceprobabilityatheterozygousites_ABP


def altallelebalanceathetzygoussites(allelebalanceatheterozygoussites_AB, infofielddict, vcfkey):
    """

    :param allelebalanceatheterozygoussites_AB:
    :param infofielddict:
    :param vcfkey:
    :return:
    """
    allelebalanceatheterozygoussites_AB[vcfkey] = infofielddict["AB"]
    return allelebalanceatheterozygoussites_AB


def altalleleobservationcountinformatfield_AO(altalleleobscount_formatfield_AO, formatfieldcounter, formatvaluesfield,
                                              vcfkey):
    """

    :param altalleleobscount_formatfield_AO:
    :param formatfieldcounter:
    :param formatvaluesfield:
    :param vcfkey:
    :return:
    """
    altalleleobscount_formatfield_AO[vcfkey] = formatvaluesfield[formatfieldcounter]
    return altalleleobscount_formatfield_AO


def refalleleobservationcountsinformatfield_RO(formatfieldcounter, formatvaluesfield, refalleleobscount_formatfield_RO,
                                               vcfkey):
    """

    :param formatfieldcounter:
    :param formatvaluesfield:
    :param refalleleobscount_formatfield_RO:
    :param vcfkey:
    :return:
    """
    refalleleobscount_formatfield_RO[vcfkey] = formatvaluesfield[formatfieldcounter]
    return refalleleobscount_formatfield_RO


def sumofqualityscoresforaltalleleobservations_DQA(formatfieldcounter, formatvaluesfield,
                                                   sumofqualityofaltobs_formatfield_QA, vcfkey):
    """

    :param formatfieldcounter:
    :param formatvaluesfield:
    :param sumofqualityofaltobs_formatfield_QA:
    :param vcfkey:
    :return:
    """
    sumofqualityofaltobs_formatfield_QA[vcfkey] = formatvaluesfield[formatfieldcounter]
    return sumofqualityofaltobs_formatfield_QA


def sumofqualityscoresforrefallelesinformatfield_QR(formatfieldcounter, formatvaluesfield,
                                                    sumofqualityofrefobs_formatfield_QR, vcfkey):
    """

    :param formatfieldcounter:
    :param formatvaluesfield:
    :param sumofqualityofrefobs_formatfield_QR:
    :param vcfkey:
    :return:
    """
    sumofqualityofrefobs_formatfield_QR[vcfkey] = formatvaluesfield[formatfieldcounter]
    return sumofqualityofrefobs_formatfield_QR


def numberofobservationsforeachallele_DPR(formatfieldcounter, formatvaluesfield, numberofobsforeachallele_DPR, vcfkey):
    """

    :param formatfieldcounter:
    :param formatvaluesfield:
    :param numberofobsforeachallele_DPR:
    :param vcfkey:
    :return:
    """
    numberofobsforeachallele_DPR[vcfkey] = list(formatvaluesfield[formatfieldcounter])
    return numberofobsforeachallele_DPR


def readdepthforcalledgenotype_DP(formatfieldcounter, formatvaluesfield, readdepthforcalledgenotype_formatfield_DP,
                                  vcfkey):
    """

    :param formatfieldcounter:
    :param formatvaluesfield:
    :param readdepthforcalledgenotype_formatfield_DP:
    :param vcfkey:
    :return:
    """
    readdepthforcalledgenotype_formatfield_DP[vcfkey] = list(formatvaluesfield[formatfieldcounter])
    return readdepthforcalledgenotype_formatfield_DP


def assignGenotypeQualityGQ(formatfieldcounter, formatvaluesfield, genotypequality_GQ, vcfkey):
    """

    :param formatfieldcounter:
    :param formatvaluesfield:
    :param genotypequality_GQ:
    :param vcfkey:
    :return:
    """
    genotypequality_GQ[vcfkey] = formatvaluesfield[formatfieldcounter]
    return genotypequality_GQ

