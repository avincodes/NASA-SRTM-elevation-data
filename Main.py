#%%

#%%
import srtmchoose, srtmdownload, srtmparse, srtmwrite

# Prompt user for target coordinates, level of detail, and units of altitude.
parameters = srtmchoose.srtmChoose()
target = parameters.chooseTarget()
detail = parameters.chooseDetail()
unitscale = parameters.chooseUnits()

# Download, unzip, and parse HGT file
downloader = srtmdownload.srtmDownloader()
parser = srtmparse.srtmParser()

if detail == 1:
    downloader.downloadFileL1(target)
    hgtcontents = parser.parseFileL1(target+".hgt")
else:
    downloader.downloadFileL3(target)
    hgtcontents = parser.parseFileL3(target+".hgt")

# Read data from file into numpy array and save as a CSV file. There are three columns with X, Y, and Z dimensions for each point
writer = srtmwrite.srtmWriter()
writer.srtmWriteFile(hgtcontents, detail, unitscale)

# This csv file can be imported directly into Rhinoceros 5 software to create a 3D point cloud of the topography.

#%%

#%%

#%%

#%%
