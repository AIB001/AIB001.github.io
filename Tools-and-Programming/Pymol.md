<font face='Times'>

# PyMol and .pml scropt
## Generate the .pml script
To generate *Pymol Macro language* Sctipt, before we begin drawing picture in PuMol, we should do some pre-opeartions.

In the "login" interface,click "File":
![image](https://github.com/AIB001/AIB001.github.io/assets/141569168/bf8385d2-0044-4a25-ac10-782bc1d01d0b)

<font face='Times'>
After, we choose the "Log File" and click "Open" and choose the savepath in the browser:

![image](https://github.com/AIB001/AIB001.github.io/assets/141569168/cecf42fd-5c65-4d87-a09d-172df2e191d6)

![image](https://github.com/AIB001/AIB001.github.io/assets/141569168/dff4a044-28e8-40a7-9a75-2e6a54d4445e)

And then, we will obtain the .pml file after our many operations to draw picture.

## Pro-Lig Picture Drawing

```PyMol
cd C:\Users\Apple\Desktop\All_Results\cov
load system.pdb
cd prod2
load_traj \
    C:/Users/Apple/Desktop/All_Results/cov/prod2/prod_nojump.xtc, \
    system, 0, \
    start=1, stop=-1, interval=1

# Select the work object
select ions, all and ((resn SOD) or (resn CLA)); remove ions; delete ions; remove solvent
frame 691
create cluster1, system , 691
delete system 
select ligand, resname LIG
select residues, byres ligand around 4
hide 

bg_color white
show sticks, ligand | residues
hide sticks, h.
zoom lig | residues

# Select color for Residues
color yellow, lig & name C*
color violet, residues & name C*
color marine, residues & name N*
color warmpink, residues & name O*
color gray80, !(lig or residues) & name C*

# Manually add label to 'residues'
# It is suggeted to add label in PowerPoint or in P.S.
set label_size, 30
set label_font_id, 9 # Set label to 'Times'
# hide label

show cartoon
set cartoon_transparency, 0.8
set ray_trace_mode, 1

# ray_trace
ray
```
