
def noofaltalleleobssupportedbypairedreaddata(numberofaltalleleobssupportedbypairedreaddata_PAIRED, infofielddict,
                                              vcfkey):
    numberofaltalleleobssupportedbypairedreaddata_PAIRED[vcfkey] = infofielddict["PAIRED"]
    return numberofaltalleleobssupportedbypairedreaddata_PAIRED


def refallelephredqualsumspartialobsPQR(refallelephredqualitysumpartialobs_PQR, infofielddict, vcfkey):
    refallelephredqualitysumpartialobs_PQR[vcfkey] = infofielddict["PQR"]
    return refallelephredqualitysumpartialobs_PQR


def altallelephredqualsumspartialobsPQA(altallelephredqualitysumpartialobs_PQA, vcfkey, infofielddict):
    altallelephredqualitysumpartialobs_PQA[vcfkey] = infofielddict["PQA"]
    return altallelephredqualitysumpartialobs_PQA


def altalleleobscountpartialPAO(altalleleobscount_partial_PAO, infofielddict, vcfkey):
    altalleleobscount_partial_PAO[vcfkey] = infofielddict["PAO"]
    return altalleleobscount_partial_PAO


def typeofalleleTYPE(infofielddict, typeofallele_TYPE, vcfkey):
    typeofallele_TYPE[vcfkey] = infofielddict["TYPE"]
    return typeofallele_TYPE


def logoddsratioODDS(infofielddict, logoddsratio_ODDS, vcfkey):
    logoddsratio_ODDS[vcfkey] = infofielddict["ODDS"]
    return logoddsratio_ODDS


def numofaltallleleobspersampleNUMALT(infofielddict, numofaltalleleobspersample_NUMALT, vcfkey):
    numofaltalleleobspersample_NUMALT[vcfkey] = infofielddict["NUMALT"]
    return numofaltalleleobspersample_NUMALT


def noofsampleswithdataNS(infofielddict, numberofsampleswithdata_NS, vcfkey):
    numberofsampleswithdata_NS[vcfkey] = infofielddict["NS"]
    return numberofsampleswithdata_NS


def meanmapqualrefalleleMQMR(infofielddict, meanmapqualrefallele_MQMR, vcfkey):
    meanmapqualrefallele_MQMR[vcfkey] = infofielddict["MQMR"]
    return meanmapqualrefallele_MQMR


def meanmapqualaltalleleMQM(infofielddict, meanmapqualaltallele_MQM, vcfkey):
    meanmapqualaltallele_MQM[vcfkey] = infofielddict["MQM"]
    return meanmapqualaltallele_MQM


def meannoofaltallelespersampleMEANALT(infofielddict, meannoofaltallelespersample_MEANALT, vcfkey):
    meannoofaltallelespersample_MEANALT[vcfkey] = infofielddict["MEANALT"]
    return meannoofaltallelespersample_MEANALT


def allelelengthLEN(allelelength_LEN, infofielddict, vcfkey):
    allelelength_LEN[vcfkey] = infofielddict["LEN"]
    return allelelength_LEN


def genotypeiterationsGTI(genotypeiterations_GTI, infofielddict, vcfkey):
    genotypeiterations_GTI[vcfkey] = infofielddict["GTI"]
    return genotypeiterations_GTI


def endplacementprobforrefalleleEPPR(endplacementprobref_EPPR, infofielddict, vcfkey):
    endplacementprobref_EPPR[vcfkey] = infofielddict["EPPR"]
    return endplacementprobref_EPPR


def endplacementprobabilityEPP(endplacementprob_EPP, infofielddict, vcfkey):
    endplacementprob_EPP[vcfkey] = infofielddict["EPP"]
    return endplacementprob_EPP


def altalleledepthratioDPRA(altalleledeptratio_DPRA, infofielddict, vcfkey):
    altalleledeptratio_DPRA[vcfkey] = infofielddict["DPRA"]
    return altalleledeptratio_DPRA


def readdepthforcalledgenotypeperbpDPB(infofielddict, readdepthforcalledgenotypeperbasepair_DPB, vcfkey):
    readdepthforcalledgenotypeperbasepair_DPB[vcfkey] = infofielddict["DPB"]
    return readdepthforcalledgenotypeperbasepair_DPB


def readdepthforcalledgenotypeininfofieldDP(infofielddict, readdepthforcalledgenotype_infofield_DP, vcfkey):
    readdepthforcalledgenotype_infofield_DP[vcfkey] = infofielddict["DP"]
    return readdepthforcalledgenotype_infofield_DP


def cigarstringCIGAR(cigarstring_CIGAR, infofielddict, vcfkey):
    cigarstring_CIGAR[vcfkey] = infofielddict["CIGAR"]
    return cigarstring_CIGAR


def altalleleobsAO(alternatealleleobservations_AO, infofielddict, vcfkey):
    alternatealleleobservations_AO[vcfkey] = infofielddict["AO"]
    return alternatealleleobservations_AO


def totalnoofallelesincalledgenotypeAN(infofielddict, totalnumberofallelesincalledgenotype_AN, vcfkey):
    totalnumberofallelesincalledgenotype_AN[vcfkey] = infofielddict["AN"]
    return totalnumberofallelesincalledgenotype_AN


def readplacementprobrefalleleRPPR(infofielddict, readplacementprobabilityforreference_RPPR, vcfkey):
    readplacementprobabilityforreference_RPPR[vcfkey] = infofielddict["RPPR"]
    return readplacementprobabilityforreference_RPPR


def readplacementprobRPP(infofielddict, readplacementprobability_RPP, vcfkey):
    readplacementprobability_RPP[vcfkey] = infofielddict["RPP"]
    return readplacementprobability_RPP


def noofconsecutiverepeatsofaltalleleRUN(infofielddict, numberofconsecutiverepeatsofaltallele_RUN, vcfkey):
    numberofconsecutiverepeatsofaltallele_RUN[vcfkey] = infofielddict["RUN"]
    return numberofconsecutiverepeatsofaltallele_RUN


def refalleleobservationcountRO(infofielddict, refalleleobscount_RO, vcfkey):
    refalleleobscount_RO[vcfkey] = infofielddict["RO"]
    return refalleleobscount_RO


def estimatedallelefreqAF(estimatedallelefrequency_AF, infofielddict, vcfkey):
    estimatedallelefrequency_AF[vcfkey] = infofielddict["AF"]
    return estimatedallelefrequency_AF


def numofaltallelesAC(infofielddict, numaltalleles_AC, vcfkey):
    numaltalleles_AC[vcfkey] = infofielddict["AC"]
    return numaltalleles_AC


def allelebalanceprobatheterozygoussites(allelebalanceprobabilityatheterozygousites_ABP, infofielddict, vcfkey):
    allelebalanceprobabilityatheterozygousites_ABP[vcfkey] = infofielddict["ABP"]
    return allelebalanceprobabilityatheterozygousites_ABP


def altallelebalanceathetzygoussites(allelebalanceatheterozygoussites_AB, infofielddict, vcfkey):
    allelebalanceatheterozygoussites_AB[vcfkey] = infofielddict["AB"]
    return allelebalanceatheterozygoussites_AB


def altalleleobservationcountinformatfield_AO(altalleleobscount_formatfield_AO, formatfieldcounter, formatvaluesfield,
                                              vcfkey):
    altalleleobscount_formatfield_AO[vcfkey] = formatvaluesfield[formatfieldcounter]
    return altalleleobscount_formatfield_AO


def refalleleobservationcountsinformatfield_RO(formatfieldcounter, formatvaluesfield, refalleleobscount_formatfield_RO,
                                               vcfkey):
    refalleleobscount_formatfield_RO[vcfkey] = formatvaluesfield[formatfieldcounter]
    return refalleleobscount_formatfield_RO


def sumofqualityscoresforaltalleleobservations_DQA(formatfieldcounter, formatvaluesfield,
                                                   sumofqualityofaltobs_formatfield_QA, vcfkey):
    sumofqualityofaltobs_formatfield_QA[vcfkey] = formatvaluesfield[formatfieldcounter]
    return sumofqualityofaltobs_formatfield_QA


def sumofqualityscoresforrefallelesinformatfield_QR(formatfieldcounter, formatvaluesfield,
                                                    sumofqualityofrefobs_formatfield_QR, vcfkey):
    sumofqualityofrefobs_formatfield_QR[vcfkey] = formatvaluesfield[formatfieldcounter]
    return sumofqualityofrefobs_formatfield_QR


def numberofobservationsforeachallele_DPR(formatfieldcounter, formatvaluesfield, numberofobsforeachallele_DPR, vcfkey):
    numberofobsforeachallele_DPR[vcfkey] = list(formatvaluesfield[formatfieldcounter])
    return numberofobsforeachallele_DPR


def readdepthforcalledgenotype_DP(formatfieldcounter, formatvaluesfield, readdepthforcalledgenotype_formatfield_DP,
                                  vcfkey):
    readdepthforcalledgenotype_formatfield_DP[vcfkey] = list(formatvaluesfield[formatfieldcounter])
    return readdepthforcalledgenotype_formatfield_DP


def assignGenotypeQualityGQ(formatfieldcounter, formatvaluesfield, genotypequality_GQ, vcfkey):
    genotypequality_GQ[vcfkey] = formatvaluesfield[formatfieldcounter]
    return genotypequality_GQ

