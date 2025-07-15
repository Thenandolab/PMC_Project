#!/bin/bash

# Make b0 from the diffusion data
fslroi /Users/nando/Desktop/HCP/subjects/100307/dwi/dwi.nii.gz \
/Users/nando/Desktop/HCP/subjects/100307/dwi/b0 0 1

# Make nodif brain
bet /Users/nando/Desktop/HCP/subjects/100307/dwi/b0 \
/Users/nando/Desktop/HCP/subjects/100307/dwi/nodif_brain -m -f 0.3

# Convert nifit to mif
mrconvert /Users/nando/Desktop/HCP/subjects/100307/dwi/dwi.nii.gz \
/Users/nando/Desktop/HCP/subjects/100307/dwi/dwi.mif \
-fslgrad /Users/nando/Desktop/HCP/subjects/100307/dwi/dwi.bvecs /Users/nando/Desktop/HCP/subjects/100307/dwi/dwi.bvals

# Define the directory where your tck files are
tck_dir="/Users/nando/Desktop/HCP/subjects/100307/TOM_trackings"

# Define the directory where your unfiltered tck files will be moved
unfiltered_dir="/Users/nando/Desktop/HCP/subjects/100307/unfiltered"

# Check if the unfiltered directory exists. If not, create it
[ ! -d "$unfiltered_dir" ] && mkdir -p "$unfiltered_dir"

# Loop over all tck files in the directory
for tck_file in $tck_dir/*.tck; do
    # Extract the base name of the tck file (without the extension)
    base_name=$(basename "$tck_file" .tck)

    # Define the name of the intermediate and output files
    intermediate_file="${tck_dir}/${base_name}_intermediate.tck"
    output_file="${tck_dir}/${base_name}_filtered.tck"

    # First, select streamlines that touch the first ROI
    tckedit $tck_file \
    $intermediate_file \
    -include /Users/nando/Desktop/HCP/subjects/100307/pmc_roi/pmc_seed.nii.gz \
    -ends_only

    # Then, from those, select streamlines that also touch the second ROI
    tckedit $intermediate_file \
    $output_file \
    -include /Users/nando/Desktop/HCP/subjects/100307/greymatter_roi/grey_matter_seed.nii.gz \
    -ends_only

    # Optional: remove the intermediate file
    rm $intermediate_file

    # Move the original tck file to the unfiltered directory
    mv "$tck_file" "$unfiltered_dir"

    # Visualize the output (optional)
    # mrview /Users/nando/Desktop/HCP/subjects/100307/dwi/dwi.mif -tractography.load $output_file
done
