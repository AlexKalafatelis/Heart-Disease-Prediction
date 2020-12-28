"""
Download dataset from Kaggle

https://www.kaggle.com/ronitf/heart-disease-uci
"""

from google.colab import files
files.upload()

!ls -lha kaggle.json

!pip install -q kaggle

# The Kaggle API client expects this file to be in ~/.kaggle,
# so move it there.
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

# This permissions change avoids a warning on Kaggle tool startup.
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets list -s Heart

!kaggle datasets download -d ronitf/heart-disease-uci

!unzip \*.zip
