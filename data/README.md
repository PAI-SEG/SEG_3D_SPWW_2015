# Data Setup

The raw data files can be downloaded from Amazon server using Madagascar's Fetch command (wget if using SU). However during the workshop, you'd better get a copy from Karl's flash drives.

Once you get a local copy of the raw data files, set the variable in ```datapath.py``` to the directory where you put the raw data:

```python
os.environ['SEG_3D_SPWW_2015_DATA'] = '/Where/You/Put/Raw/Data'
```

Or simply put your raw data files in the ```data``` directory.

If you choose to download raw data from the server, simply set the ```local``` variable in ```datapath.py``` to ```False```, i.e.,

```bash
$less datapath.py | grep local
local = False
```

Run SConstruct to convert raw data to RSF format:

```python
scons 
```

```datapath.py``` provides two functions

```python
makeLinksToRawData()
makeLinksToRSFData()
```
to create symbolic links to the raw data files and RSF format data files.

You can use these two functions to make the raw data and RSF format data available to your working directory. For example, in the ```karl/basic-mad``` example, you could add following lines at the beginning

```python
from rsf.proj import *
sys.path.append('../../DATA')
import datapath
datapath.makeLinksToRawData()
datapath.makeLinksToRSFData()
```
These will create symbolic links to the following files with the same name:

```python
npr3_field.sgy
npr3_gathers.sgy
final_stack.rsf
npr3_field.rsf
npr3_field_hdr.rsf
npr3_gathers.rsf
npr3_gathers_hdr.rsf
```