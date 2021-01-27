from .config import HOME
import os.path as osp
import sys
import torch
import torch.utils.data as data
import cv2
import numpy as np
if sys.version_info[0] == 2:
    import xml.etree.cElementTree as ET
else:
    import xml.etree.ElementTree as ET

from pprint import pprint

VOC_CLASSES = ('desk',)  # 修正

dir_cur = osp.dirname(__file__)
dir_voc = osp.join(dir_cur, "..", "VOCdevkit")
VOC_ROOT = osp.abspath(dir_voc)

class VOCAnnotationTransform(object):
    def __init__(self, class_to_ind=None, keep_difficult=False):
        self.class_to_ind = class_to_ind or dict(
            zip(VOC_CLASSES, range(len(VOC_CLASSES))))
        self.keep_difficult = keep_difficult

    def __call__(self, target, width, height):
        res = []
        for obj in target.iter('object'):
            difficult = int(obj.find('difficult').text) == 1
            if not self.keep_difficult and difficult:
                continue
            name = obj.find('name').text.lower().strip()
            bbox = obj.find('bndbox')

            pts = ['xmin', 'ymin', 'xmax', 'ymax']
            bndbox = []
            for i, pt in enumerate(pts):
                cur_pt = int(bbox.find(pt).text) - 1
                cur_pt = cur_pt / width if i % 2 == 0 else cur_pt / height
                bndbox.append(cur_pt)
            label_idx = self.class_to_ind[name]
            bndbox.append(label_idx)
            res += [bndbox]  
        return res  


class VOCDetection(data.Dataset):
    def __init__(self, root,
                 image_sets=[('DESK', 'trainval')],  # 修正  
                 transform=None, target_transform=VOCAnnotationTransform(),
                 dataset_name='VOC0712'):
        self.root = root
        self.image_set = image_sets
        self.transform = transform
        self.target_transform = target_transform
        self.name = dataset_name
        self._annopath = osp.join('%s', 'Annotations', '%s.xml')
        #print("annopath: ", self._annopath)
        self._imgpath = osp.join('%s', 'JPEGImages', '%s.jpg')
        #print("imgpath: ", self._imgpath)
        self.ids = list()
        for (dir, name) in image_sets:  # 修正
            rootpath = osp.join(self.root, dir)  # 修正
            for line in open(osp.join(rootpath, 'ImageSets', 'Main', name + '.txt')):
                #print(line)    //どのファイルを参照してるのか確認したかった
                self.ids.append((rootpath, line.strip()))

    def __getitem__(self, index):
        im, gt, h, w = self.pull_item(index)

        return im, gt

    def __len__(self):
        return len(self.ids)

    def pull_item(self, index):
        img_id = self.ids[index]

        target = ET.parse(self._annopath % img_id).getroot()
        img = cv2.imread(self._imgpath % img_id)

        #print(img.shape) //画像は開けてた
        
        height, width, channels = img.shape
        #print("Width: ",width)
        #print("Height: ",height)

        if self.target_transform is not None:
            #print("Hello") ここのifに入ってるのか知りたかった
            #print("Width: {}\nHeight: {}", format(str(width), str(height)))
            target = self.target_transform(target, width, height)

        if self.transform is not None:
            #pprint(target)
            target = np.array(target)
            #print("target.shape: ", target.shape)
            #print("target: ", target)
            img, boxes, labels = self.transform(img, target[:, :4], target[:, 4])
            img = img[:, :, (2, 1, 0)]
            target = np.hstack((boxes, np.expand_dims(labels, axis=1)))
        return torch.from_numpy(img).permute(2, 0, 1), target, height, width

    def pull_image(self, index):
        img_id = self.ids[index]
        return cv2.imread(self._imgpath % img_id, cv2.IMREAD_COLOR)

    def pull_anno(self, index):
        img_id = self.ids[index]
        anno = ET.parse(self._annopath % img_id).getroot()
        gt = self.target_transform(anno, 1, 1)
        return img_id[1], gt

    def pull_tensor(self, index):
        return torch.Tensor(self.pull_image(index)).unsqueeze_(0)

