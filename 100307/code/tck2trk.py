# Script name: tck2trk.py
# Date: Jan 12th 2023
# Purpose: convert .tck streamlines to .trk
# Author: Zoe
# Credit: The nibabel transformation (mth="nib") is adpated from app-convert-tck-to-trk
# https://github.com/brainlife/app-convert-tck-to-trk/blob/1.0/convert_tck_to_trk.py
# Note: The nib transformation is significantly faster than dipy. Keeping the dipy 
# method here as a reference for when working with dipy

import os
import nibabel as nib
from nibabel.streamlines import Field
from nibabel.orientations import aff2axcodes
from dipy.tracking.streamline import Streamlines
from dipy.io.streamline import save_tractogram
from dipy.io.stateful_tractogram import Space, StatefulTractogram
from dipy.io.image import load_nifti
def tck2trk(
    tck_path, #Path to the tck file
    tck_fn, #Name of the tck file
    trk_path, #Path to trk file
    trk_fn, #Name of the trk file
    dwi_path, #Path to the diffusion data
    dwi_fn, #Name of the diffusion data in nifti format
    mth="nib" #Transform method: nib or dipy
    ):
    dwi_file=os.path.join(dwi_path,dwi_fn)
    tck_file=os.path.join(tck_path,tck_fn)
    trk_file=os.path.join(trk_path,trk_fn)
    if mth=="nib":
        nii = nib.load(dwi_file)        
        header = {}
        header[Field.VOXEL_TO_RASMM] = nii.affine.copy()
        header[Field.VOXEL_SIZES] = nii.header.get_zooms()[:3]
        header[Field.DIMENSIONS] = nii.shape[:3]
        header[Field.VOXEL_ORDER] = "".join(aff2axcodes(nii.affine))
        tck = nib.streamlines.load(tck_file)
        nib.streamlines.save(tck.tractogram, trk_file, header=header)
    elif mth=="dipy":
        _, _, dmri_img = load_nifti(dwi_file, return_img=True)
        streamlines= Streamlines(nib.streamlines.load(tck_file).streamlines)
        sft = StatefulTractogram(streamlines, dmri_img, Space.RASMM)
        save_tractogram(sft, trk_file)