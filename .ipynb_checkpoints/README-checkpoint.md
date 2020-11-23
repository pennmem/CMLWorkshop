# CML Workshop

These are notes for the Computational Memory Lab's Workshop on Cognitive Electrophysiology.  They are also a good introduction to performing EEG analyses, and you can use them as a resource for learning these tools and methods.

# Making use of this tutorial

This tutorial can be made use of on your own system after obtaining the
CMLExamples data set (contact kahana-sysadmin@sas.upenn.edu to receive
access to these files) or directly on the Rhino computing cluster if you
have access to this. Instructions are provided below to set up either
your local machine or an environment on Rhino for affiliates of the 
Computational Memory Lab.

Though this workshop assumes a basic knowledge of Python and command line
tools, we have linked recommended resources in the Pre-launch section for getting started with
python and common data analysis tools. Though this material isn't strictly
part of the Workshop, we recommend reviewing it before proceeding to the
materials included here unless you are confident in you experience with
numpy, pandas, scipy, and basic python syntax. If those words don't mean
anything to you (or you want to brush up), please check out this section!

# Initial Setup

To start working with any materials contained or linked here, you'll need to
set up tools for writing and running Python code. If you are affiliated with
the Computational Memory Lab and have access to Rhino, our computing cluster,
you can skip down to the Getting started on Rhino section. Otherwise, you
can follow the instructions below to set up python on your own computer.

## Command line access

All subsequent stages of these instructions will assume familiarity with and access
to a *NIX command line. If this is unfamiliar to you, please use the resources below
to get yourself oriented.

If you are using Rhino, an apple computer running OSX, or a Linux computer,
you will already have access to a command line. On Windows, we recommend
using Cygwin <https://www.cygwin.com/> or the Ubuntu subsystem
<https://docs.microsoft.com/en-us/windows/wsl/install-win10>.

General Introduction: https://ubuntu.com/tutorials/command-line-for-beginners#1-overview

## Getting started on your computer

For this workshop, we will use conda to manage the various libraries needed to perform
analyses using Python. Conda is a tool that allows Python libraries to be installed into
'environments.' This is a folder that lets you manage the needs of different projects
independently; the reasons for this may not be apparent immediately, but using some
sort of virtual environment system of some sort is a standard practice and isolates issues
when they come up. Conda is available from the [Anaconda project home](https://docs.conda.io/projects/conda/en/latest/index.html). We
recommend installing miniconda, though you can read the installation instructions and
decide for yourself which distribution is best for you.

Once you have conda set up, we need to additionally set up Jupyter notebooks. This is
a tool that makes some types of python development easier since it allows you to
run small pieces of code and immediately see the output alongside the code. 
Installation instructions and general information are available from the 
[Jupyter project home](https://jupyterlab.readthedocs.io/en/stable/index.html).

## Getting started on Rhino

If you have been provided with an account on the Rhino computing cluster, these instructions will help you access and setup your account to the point where you can follow these workshop notes and perform analyses. If you are using another system, skip ahead to Setting up JupyterLab.

### Setting up your Rhino2 Account

1\. You can log in to Rhino2 in a terminal window by using any ssh client
to ssh into rhino as follows, replacing the "username" with your username:

    ssh username@rhino2.psych.upenn.edu

and then typing your temporary password when prompted. Once successfully
connected, type:

    passwd

to change your password to something only you know. Please do this as soon as
you have the time!


2\. Once you have your password set up, check to be sure you can log in to
JupyterLab, where you'll be doing most of the workshop work. If you are
connected to the internet on UPenn's campus, you only need to go to
[https://rhino2.psych.upenn.edu:8200](https://rhino2.psych.upenn.edu:8200/) to
access JupyterLab. If you are connecting remotely, follow the rest of this
step. In a terminal where ssh is accessible, replace the "username" with your
username, and open an ssh tunnel by typing:

    ssh -L8000:rhino2.psych.upenn.edu:8200 username@rhino2.psych.upenn.edu

followed by entering your rhino password. In your web browser, navigate to:

[https://127.0.0.1:8000](https://127.0.0.1:8000)

and you should see the JupyterLab interface pop up!  Note that the "s" on https is critical for this to work.  Your browser might warn about this being an insecure connection or invalid certificate, given that 127.0.0.1 (direct to the ssh tunnel on your own computer) is not rhino.  Override this warning and connect anyway, because we are using ssh to provide better security here.  If the connection still fails, go back and make sure that your ssh tunnel was correctly created.


## Setting up your environment 

Once you've installed the necessary tools or have set up your account on Rhino,
you'll need to create a new virtual environment. To do so, open a terminal and run:

    conda create -y -n environmentname python=3.7
    NOTE: 'environmentname' is a placeholder, please replace it with a more descriptive name!

For commands to alter or refer to this environment, you'll need to activate it.
This step will be necessary any time you open a new terminal or restart your session,
but will be remembered for subsequent commands.

    conda activate environmentname
    NOTE: on older versions of conda, you may instead need to use source activate environmentname


Next, you'll need to install a suite of tools for EEG analysis. First,
install MNE by typing the following (be sure you're in the Anaconda
"environment" you just created in Step 1, by typing "source activate
environmentname"). Note that this may take a while, because MNE has a
lot of dependencies:

    conda install -c conda-forge "mne<0.19"
    
**Make sure you include the quotes!!**

Next, install PTSA, which is a set of EEG tools developed by
former lab members:

    conda install -c pennmem ptsa

Install a few extra packages in use for these notes:

    conda install scikit-learn statsmodels seaborn

Finally, you'll need to link JupyterLab with your specific Python
installation.  While still logged in and in your Anaconda "environment",
type:

    conda install ipykernel

and once that's done:

    python -m ipykernel install --user --name environmentname --display-name "environmentname"

You should be all set! Next time you log in to your JupyterLab account,
you should see an option to launch a new notebook with "environmentname"
as your Python environment. If you've been logged in to JupyterLab this
whole time, you may need to log out and log back in again to see this
change take effect.

## Getting the CMLWorkshop JupyterLab notes

In a terminal in the location where you would like to download the workshop
materials, enter the following:

    git clone 'https://github.com/pennmem/CMLWorkshop.git'

    If git is not installed, you can find instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

The workshop will be downloaded to a folder named CMLWorkshop in the
same location where you ran the git clone command.

## Setting up the CMLExamples files

NOTE: instructions for non-lab members are forthcoming. For the moment,
please contact kahana-sysadmin@sas.upenn.edu to request access to this data.

For this workshop, we have bundled a subset of the data collected using
both scalp and intracranial eeg. You will need to provide each notebook code example making use of the
CMLExamples files with how to find the files. The simplest way, if your
system supports it, is to make a symbolic link in your CMLWorkshop
directory to these files. For example, on Rhino this is currently
done by going into the CMLWorkshop directory and entering:

    ln -s /data/examples CMLExamples

## Installing CMLReaders (Rhino users only)

In your ssh terminal to rhino, enter the following commands:

    source activate environmentname
    conda install -c pennmem cmlreaders
    
This package is being phased out, but is still needed for
loading a large portion of data stored on Rhino. Any analyses using
CMLLoad can bbe done nearly equivalently using CMLReaders, though CMLReaders
has access to a much larger set of data on Rhino.

# The workshop

In JupyterLab, navigate to the lecture notes you downloaded using
the file browser section on the left, open the lecture notes, and
proceed through them in order. If appropriate for your background and
situation, jump ahead to the relevant sections to see syntax examples
for common analyses and for using the common tools used by the
Computational Memory Lab.

**Lectures covering the concepts underpinning the analyses covered in
this workshop are available from the [Electrophysiology Workshop 2020](http://memory.psych.upenn.edu/Electrophysiology_Workshop_2020)
page on the Computational Memory Lab wiki.**

### Course Structure
Our goal is to familiarize you with basic Python tools for data science and the libraries developed by our lab and others to facilitate EEG analyses. In order to understand the psychology / neuroscience at play in these analyses, you'll need to watch the associated lectures from the 2020 workshop. To that end, the course outline is as follows: 
* Notebook 1 - **Intro to Python basics, Jupyter Notebooks, Numpy, and Pandas**
* *Lecture 1*
* *Lecture 2*
* Notebook 2 - **Data loading, experimental events, PTSA, and MNE**
* *Lecture 3*
* Notebook 3 - **Working with EEG**
* *Lecture 4*
* Notebook 4 - **Signal processing and spectral analysis**
* *Lecture 5*
* Notebook 5 - **Machine Learning I, sklearn, regression/classification**
* *Lecture 6*
* Notebook 6 - **Machine Learning II, cross-validation, feature selection, other classifiers**

By the end of this sequence, you should be able to carry out EEG/iEEG/ECoG analyses, like computing spectral power and phase, and compute statistics or apply machine learning models to those data.

For **Rhino** users only:
* Notebook 7 - **Parallel computing**
* Notebook 8 - **Parallel computing**
* Notebook 9 - **Biomarkers of Episodic Memory**

These notebooks prepare you for doing in-depth multi-subject analyses with electrophysiological data. Anyone planning to work extensively with CML data should complete them. Notebook 9 is an advanced assignment that will take much longer than any of the others in this workshop - consider it a "final project" of sorts.

Optional appendices:
* *Lecture 8*
* Notebook A1 - **Connectivity**
* *Lecture 7*
* Notebook A2 - **Single Unit Analysis, Spatial Memory**

These notebooks cover advanced topics in computational neuroscience that go beyond the scope of what a beginner might need to know. If you are interested in these topics, or just want to gain some familiarity with them, we encourage you watch the associated lectures and go through the notebooks.