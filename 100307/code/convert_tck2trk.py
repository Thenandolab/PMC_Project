# Script name: convert_tck2trk.py
# Date: Jan 11th 2023
# Purpose: convert .tck streamlines to .trk 

import os
import dipy
import nibabel as nib
from nibabel.streamlines import Field
from nibabel.orientations import aff2axcodes
from dipy.tracking.streamline import Streamlines
from dipy.io.streamline import save_tractogram
from dipy.io.stateful_tractogram import Space, StatefulTractogram
from dipy.io.image import load_nifti
from tck2trk import tck2trk
from datetime import datetime

fpath='/Users/nando/Desktop/HCP/subjects/100307/TOM_trackings'
dpath = '/Users/nando/Desktop/HCP/subjects/100307/dwi'

# Loop over all files in the directory
for file_name in os.listdir(fpath):
    # Check if the file is a .tck file
    if file_name.endswith('.tck'):
        # Remove the .tck extension to get the base name
        base_name = file_name[:-4]
        tck2trk(fpath, file_name, fpath, base_name + ".trk", dpath, "dwi.nii.gz")
