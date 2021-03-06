import FWCore.ParameterSet.Config as cms

rootTupleGenEventInfo = cms.EDProducer("BristolNTuple_GenEventInfo",
    GenEventInfoInputTag = cms.InputTag('generator'),
    StorePDFWeights      = cms.bool(True),
    PUWeightsInputTag    = cms.InputTag('eventWeightPU'),
    PDFWeightsInputTag   = cms.InputTag('pdfWeights','cteq66'),
    pileupInfo           = cms.InputTag('addPileupInfo'),
    Prefix               = cms.string('Event.'),
    Suffix               = cms.string(''),
    ttbarDecayFlags      = cms.VInputTag(
                                         cms.InputTag( 'ttFullHadronicFilter' ),
                                         cms.InputTag( 'ttSemiLeptonicElectronFilter' ),
                                         cms.InputTag( 'ttSemiLeptonicMuonFilter' ),
                                         cms.InputTag( 'ttSemiLeptonicTauFilter' ),
                                         cms.InputTag( 'ttFullLeptonicEEFilter' ),
                                         cms.InputTag( 'ttFullLeptonicMuMuFilter' ),
                                         cms.InputTag( 'ttFullLeptonicTauTauFilter' ),
                                         cms.InputTag( 'ttFullLeptonicETauFilter' ),
                                         cms.InputTag( 'ttFullLeptonicEMuFilter' ),
                                         cms.InputTag( 'ttFullLeptonicMuTauFilter' ),
                ),
    isTTbarMC = cms.bool(False),
)
