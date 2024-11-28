# Datapipe
Example simulated experimental data for testing digital twin data pipelines. Here we use a MOOSE solid mechanics simulation of a 2D plate with a hole to generate synthetically deformed images that can be processed with MatchID.

## Experimental Data Processing with MatchID 2D
Here we will use a simple 2D example that has a single camera. For this case we only need a MatchID input file (\*.m2inp), a *reference image* (\*.tiff) and one or more *deformed images* (\*.tiff).

The name of the MatchID input file (\*.m2inp) does not matter only the extension is required to identify the file and only a single input file will be needed per data process operation. Note that the MatchID input file is a human readable text file and contains full paths to the reference image and deformed images. If the input file is transferred to another computer along with the associated images then the full paths in the input file will need to be updated. See "MatchID Input Files" below for more detail about the structure of the MatchID input file and where these paths might need to be changed.

The image files are numbered consecutively and the first image in numeric order can be assumed to be the *reference image*. The remaining numbered *.tiff images can be assumed to be deformed images. Note that MatchID uses an image naming and numbering convention as follows: "Image_XXXX_C.tiff". Where XXXX is an integer starting at zero and left padded with zeros and C is an integer giving the camera number that was used to take the image starting at zero. Therefore "Image_0021_0.tiff" is image 21 taken with camera 0. Note that for 2D DIC we only have one camera so for all images C will be 0.

The files for running MatchID can be found in the "matchid2d" directory of this repository with an example input file given as "Job_man_roi.m2inp". The reference image in this folder is "Image_0000_0.tiff" i.e. the first image in the sequence. The deformed images are the remaining \*.tiff files in this folder with names of the form "Image_000X_0.tiff" where X is an integer.

MatchID can be called from the windows command line using the following syntax:
```shell
matchid.exe "full\path\to\*.m2inp"
```

For example:
```shell
matchid.exe "F:\datapipe\data\imagesdef\Job_man_roi.m2inp"
```

### MatchID Input Files (\*.m2inp)
The MatchID input file is a human readable text file that contains a large amount of parameters which specify how the data should be processed. These will need to be captured as meta-data at some point but for now we will focus on the parameters which are required to run the MatchID input file and obtain a result. Note that the MatchID input file uses \% as a comment character.

Note that this section is specific to MatchID 2D input files. An additional description will be provided for MatchID stereo input files (\*.m3inp) once the 2D pipeline is working.

Here we need to make sure that all full paths in the MatchID input file are consistent with the locations that the images have been moved to in the data pipeline. The full path to the reference image is specified in the following block:
```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% s_Filename Reference Image
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
<Reference$image>=<F:\datapipe\data\imagesdef\Image_0000_0.tiff>
```

The deformed images are then specified in the next block, for example:
```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% <Deformed$image> =
%%%%%% 	 <s_FullPathOfDeformedImage; i_NumberOfROIs;i_IndexOfROI_1;i_IndexSeed;s_GuessROI1;  i_ArrayOfGuessValuesROI1; ...; i_IndexOfROI_N; ...; i_ArrayOfGuessValuesROI1>
%%%%%%
%%%%%% Remarks:
%%%%%% i_IndexSeed: 0 refers to the InitialSubset. Other indices should comply with the ones in the extra seed list.
%%%%%% i_ArrayOfGuessValuesROI:
%%%%%% 	 if (s_GuessROI == None) i_ArrayOfGuessValuesROI should be omitted.
%%%%%% 	 if (s_GuessROI == Translation) i_ArrayOfGuessValuesROI= [i_guess_Horizontal;i_guess_Vertical]
%%%%%% 	 if (s_GuessROI == Complete) i_ArrayOfGuessValuesROI= [i_guess_H_1; i_guess_V_1; i_guess_H_2; i_guess_V_2;i_guess_H_3; i_guess_V_3]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
<Deformed$image>=<F:\datapipe\data\imagesdef\Image_0001_0.tiff;2;0;0;None>
```

Finally the output path is specified in thre following block further down the file:
```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% s_Path of output files
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
<Output$path>=<F:\datapipe\data\imagesdef>
```
By default this is set to the directory containing the reference and deformed images but can be changed if needed.

To make the data pipeline work the input file will need to automatically updated to have consistent full paths to the data to be processed.

### Data Simulator
The data simulation tool [here](https://github.com/Applied-Materials-Technology/data-simulator) uses the data in the "matchid2d" folder to generate a simulated data stream. The four images are places into a ring buffer and continuously output to the target directory. The same ring buffer is used to replicate rows of the \*.csv file as a single file or as one file per frame.

### Robocopy
Data syncing

## Simulation Pipeline with MOOSE
Here we demonstrate a MOOSE simulation of a 2D plate with a hole in the centre. We note that this is the same simulation that was used to generate the simulated images in the "matchid2d" folder so the simulation should be directly comparable to the MatchID 2D output.

This simulation will run on a linux machine and you will need to install a suitable MOOSE build such as `proteus` here: https://github.com/aurora-multiphysics/proteus. 




## Full Worked Example in 2D
Here is a full worked example of running each part of the pipeline in order:

1.