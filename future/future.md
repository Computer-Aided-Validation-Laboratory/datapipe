### Extension: Auto-masking
We do not commonly use automasking so this feature can be built after the rest of the pipeline is working. If auto masking is used we will also require a single \*.tiff image containing the mask which is automatically named by MatchID as "Job.m2inp_MaskShape_0.tiff". Note that as the name of the job file can change it is best to identify this file using the sub-string "MaskShape" associated with the extension \*.tiff.

An example MatchID input file with automasking is given in

Comparison of the example MatchID input files ("Job_man_roi.m2inp" and "Job_auto_mask.m2inp") shows that the auto mask version contains an additional block of text at the end of the file which gives the full path to the mask file.