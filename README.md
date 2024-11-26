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
The MatchID input file contains

### Data Simulator
The data simulation tool [here](https://github.com/Applied-Materials-Technology/data-simulator) uses the data in the "matchid2d" folder to generate a simulated data stream. The four images are places into a ring buffer and continuously output to the target directory.

### Robocopy
Data syncing

## Simulation Pipeline with MOOSE
Here we demonstrate a MOOSE simulation of a 2D plate with a hole in the centre. We note that this is the same simulation that was used to generate the simulated images in the "matchid2d" folder so the simulation should be directly comparable to the MatchID 2D output.


### Gmsh



## Full Worked Example in 2D
Here is a full worked example of running each part of the pipeline in order:

1.