from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Data_ZeroBias_Run2017G_15March2018'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName =  'proto_runStudyHLT_cfg.py'
config.JobType.maxMemoryMB = 4000
##Running on 13 TeV Data 
config.Data.inputDataset = '/ZeroBias/Run2017G-LogError-PromptReco-v1/RAW-RECO'
#config.Data.inputDataset = '/ZeroBias1/Run2017C-LogError-PromptReco-v2/RAW-RECO'
#config.Data.inputDataset = '/ZeroBias/Run2017H-LogError-PromptReco-v1/RAW-RECO'

##Running on 5 TeV Data
#config.Data.inputDataset = '/ZeroBias/Run2017G-LogError-PromptReco-v1/RAW-RECO'

#13TeV##For Run2017C
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/PromptReco/Cert_299996-300088_13TeV_PromptReco_Collisions17_JSON_LowPU.txt'

#13TeV## For Run2017H
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_306896-307082_13TeV_PromptReco_Collisions17_JSON_LowPU.txt'

##5TeV##ForRun2017G

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/PromptReco/Cert_306546-306657_5TeV_PromptReco_Collisions17_JSON.txt'

#config.Data.runRange = '274108'
##Running on MC
#FB
#config.Data.inputDataset = '/SingleNeutrino/RunIISpring16DR80-FlatPU0to10_G4_FB_80X_mcRun2_asymptotic_v14-v2/GEN-SIM-RECO'
##QFBE
#config.Data.inputDataset = '/SingleNeutrino/RunIISpring16DR80-FlatPU0to10_G4_QFBE_80X_mcRun2_asymptotic_v14-v2/GEN-SIM-RECO'
#config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer16DR80-NoPU_RECO_80X_mcRun2_asymptotic_v14-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer16DR80-NoPU_RECO_80X_mcRun2_asymptotic_v14-v1/GEN-SIM-RECO'
#config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer16DR80-NoPU_RECO_FTFP_BERT_80X_mcRun2_asymptotic_v14-v1/GEN-SIM-RECO'

config.Data.inputDBS = 'global'
config.Data.outputDatasetTag = 'CRAB3_Data_ZeroBias_Run2017G_15March2018'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False

config.Site.storageSite ='T2_IN_TIFR' 
