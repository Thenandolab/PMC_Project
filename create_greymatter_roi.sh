#!/bin/bash

subjects=("100307" "102311" "115017" "118831" "120010" "121719" "122822" "128127" 
          "133625" "135528" "144832" "146129" "147636" "147737" "148032" "148133" 
          "150625" "150726" "151021" "151223" "151324" "151728" "158338" "162228" 
          "162935" "183337" "185846" "202113" "283543" "286347" "322224" "392447" 
          "557857" "715647" "774663" "832651" "878877" "987983" "993675" "996782")

for subject in "${subjects[@]}"
do
  cd /Users/nando/Desktop/HCP/subjects/$subject/pmc_roi

  fslmaths aparc_aseg.nii.gz -thr 8 -uthr 13 -bin gm1
  fslmaths aparc_aseg.nii.gz -thr 16 -uthr 39 -bin gm2
  fslmaths aparc_aseg.nii.gz -thr 48 -uthr 71 -bin gm3
  fslmaths aparc_aseg.nii.gz -thr 73 -uthr 176 -bin gm4
  fslmaths aparc_aseg.nii.gz -thr 178 -uthr 212 -bin gm5
  fslmaths aparc_aseg.nii.gz -thr 214 -uthr 218 -bin gm6
  fslmaths aparc_aseg.nii.gz -thr 220 -uthr 222 -bin gm7
  fslmaths aparc_aseg.nii.gz -thr 224 -uthr 702 -bin gm8
  fslmaths aparc_aseg.nii.gz -thr 704 -uthr 1022 -bin gm9
  fslmaths aparc_aseg.nii.gz -thr 1024 -uthr 1024 -bin gm10
  fslmaths aparc_aseg.nii.gz -thr 1026 -uthr 5000 -bin gm11
  fslmaths aparc_aseg.nii.gz -thr 5003 -uthr 14175 -bin gm12

  fslmaths gm1.nii.gz -add gm2.nii.gz -add gm3.nii.gz -add gm4.nii.gz -add gm5.nii.gz -add gm6.nii.gz -add gm7.nii.gz -add gm8.nii.gz -add gm9.nii.gz -add gm10.nii.gz -add gm11.nii.gz -add gm12.nii.gz -bin grey_matter_seed
done
