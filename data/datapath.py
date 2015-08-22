import os

# whether or not to download data from remote server
# CHANGE ME if you want download from website
local = True

# environment variabe storing where you put your data
#-----------
# CHANGE ME |
#-----------
os.environ['SEG_3D_SPWW_2015_DATA'] = '/Where/You/Put/Raw/Data'

final_stack = os.path.join(os.environ['SEG_3D_SPWW_2015_DATA'],'final_stack.rsf')

npr3_gathers = os.path.join(os.environ['SEG_3D_SPWW_2015_DATA'],'npr3_gathers.sgy')

npr3_field = os.path.join(os.environ['SEG_3D_SPWW_2015_DATA'],'npr3_field.sgy')

# --------------------------------------------
def makeLinksToRawData():
    rawdata_dst = ['npr3_gathers.sgy','npr3_field.sgy', 'final_stack.rsf']
    rawdata_src = [npr3_gathers, npr3_field, final_stack]
    for i in range(3):
        if not os.path.islink(rawdata_dst[i]) and os.path.isfile(rawdata_src[i]):
            os.symlink(rawdata_src[i], rawdata_dst[i])

# --------------------------------------------
def makeLinksToRSFData():
    npr3_field_rsf = os.path.join(os.environ['SEG_3D_SPWW_2015_DATA'],'npr3_field.rsf')
    npr3_field_hdr_rsf = os.path.join(os.environ['SEG_3D_SPWW_2015_DATA'],'npr3_field_hdr.rsf')
    npr3_gathers_rsf = os.path.join(os.environ['SEG_3D_SPWW_2015_DATA'],'npr3_gathers.rsf')
    npr3_gathers_hdr_rsf = os.path.join(os.environ['SEG_3D_SPWW_2015_DATA'],'npr3_gathers_hdr.rsf')
    rsfdata_dst = ['npr3_field.rsf','npr3_field_hdr.rsf', 'npr3_gathers.rsf','npr3_gathers_hdr.rsf'] 
    rsfdata_src = [npr3_field_rsf,npr3_field_hdr_rsf,npr3_gathers_rsf,npr3_gathers_hdr_rsf] 
    for i in range(4):
        if not os.path.islink(rsfdata_dst[i]) and os.path.isfile(rsfdata_src[i]):
            os.symlink(rsfdata_src[i], rsfdata_dst[i])

