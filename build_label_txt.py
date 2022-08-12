import pandas as pd
from PIL import Image
import numpy as np
import os
import cv2


df_label=pd.read_csv('./dataset/val/validation/labels/detections.csv')

Image_ids=df_label['ImageID'].unique()


df_class=pd.read_csv('./dataset/val/validation/metadata/classes.csv',header=None)


class_dict=dict()
for index,row in df_class.iterrows():
    class_dict[row[0]]=index
    
    
def is_exist(img_id,path):
    return os.path.exists(f'{os.path.join(path,img_id)}.jpg')



image_path='./dataset/val/validation/data/'
label_path='./dataset/val/validation/labels/'



for i,img_id in enumerate(Image_ids):
    img_labels=df_label[df_label['ImageID']==img_id]
    if len(img_labels)>0:
        if is_exist(img_id,image_path):
            with open(os.path.join(label_path,img_id+'.txt'),'w') as f:
                for index,row in img_labels.iterrows():
                    XMin=float(row['XMin'])
                    XMax=float(row['XMax'])
                    YMin=float(row['YMin'])
                    YMax=float(row['YMax'])
                    LabelName=row['LabelName']
                    XCentre=(XMin+XMax)/2.0
                    YCentre=(YMin+YMax)/2.0
                    box_w=abs(XMax-XMin)
                    box_h=abs(YMax-YMin)
                    class_id=class_dict[LabelName]
                    box_info=' '.join([str(class_id),str(XCentre),str(YCentre),str(box_w),str(box_h)])
                    f.write(box_info+'\n')
                if i%1000==0:
                    print(i)
                    
                    
import send_email
send_email.send(content='yolo',subject='yolo')