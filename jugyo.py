#%%
import struct
import gzip
#%%
fpath = "/mnist/train-labels-idx1-ubyte.gz"
with gzip.open(fpath,"rb") as f:
    ##冒頭8バイトを4バイトづつ切って数値で解釈して変数に入れてね
    magic_number,img_count = struct.unpack(">II",f.read(8))
    labels = []
