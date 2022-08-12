import os
os.environ['NUMEXPR_MAX_THREADS']='104'

import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
              "open-images-v6",
              split="validation",
              label_types=["detections"],dataset_dir='./dataset/backup'
          )

"""

#dataset = foz.load_zoo_dataset(
#              "open-images-v6",
#              split="test",
#              label_types=["detections"],dataset_dir='./dataset/test'
#          )



"""


