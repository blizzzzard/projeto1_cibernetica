import os 
import shutil

from pathlib import Path

import globox


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    if h == 0 or w == 0:
        return 1000
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)



def bbox_yolo(ann_file):

    files = os.listdir(ann_file)

    for f in files:

        txt = open(ann_file + '/' + f, "r")

        ann = txt.read().splitlines()

        new_ann = []
        for a in ann:
            bbox = []
            for b in a.split():
                bbox.insert(len(bbox), int(b))
            aux = convert((512,512), bbox)
            if aux == 1000:
                continue
            count = 0
            aux2 = ''
            for val in aux:
                count += 1
                if count < 4:
                    aux2 += str(val) + ' '
                else:
                    aux2 += str(val)
            new_ann += "0 " + aux2 + "\n"
        
        txt = open(ann_file + '/' + f, "w")
        txt.writelines(new_ann)


def main():

    fold = '0'

    train_file = open("individual_urban_tree_crown_detection-main/img_list/"+fold+'/train.txt', "r")
    train_content = train_file.read().splitlines()
    for f in train_content:
        shutil.copyfile("individual_urban_tree_crown_detection-main/rgb/"+f, "individual_urban_tree_crown_detection-main/split"+fold+"/train/"+f)
        shutil.copyfile(individual_urban_tree_crown_detection-main/bbox_txt/"+os.path.splitext(os.path.basename(f))[0] + ".txt", "individual_urban_tree_crown_detection-main/split"+fold+"/train_ann/"+os.path.splitext(os.path.basename(f))[0] + ".txt")
    
    val_file = open("individual_urban_tree_crown_detection-main/img_list/"+fold+'/val.txt', "r")
    val_content = val_file.read().splitlines()
    for f in val_content:
        shutil.copyfile("individual_urban_tree_crown_detection-main/rgb/"+f, "individual_urban_tree_crown_detection-main/split"+fold+"/val/"+f)
        shutil.copyfile("individual_urban_tree_crown_detection-main/bbox_txt/"+os.path.splitext(os.path.basename(f))[0] + ".txt", "individual_urban_tree_crown_detection-main/split"+fold+"/val_ann/"+os.path.splitext(os.path.basename(f))[0] + ".txt")

    test_file = open("individual_urban_tree_crown_detection-main/img_list/"+fold+'/test.txt', "r")
    test_content = test_file.read().splitlines()
    for f in test_content:
        shutil.copyfile("individual_urban_tree_crown_detection-main/rgb/"+f, "individual_urban_tree_crown_detection-main/split"+fold+"/test/"+f)
        shutil.copyfile("individual_urban_tree_crown_detection-main/bbox_txt/"+os.path.splitext(os.path.basename(f))[0] + ".txt", "individual_urban_tree_crown_detection-main/split"+fold+"/test_ann/"+os.path.splitext(os.path.basename(f))[0] + ".txt")

    
    bbox_yolo("individual_urban_tree_crown_detection-main/split"+fold+"/train_ann")
    bbox_yolo("individual_urban_tree_crown_detection-main/split"+fold+"/val_ann")
    bbox_yolo("individual_urban_tree_crown_detection-main/split"+fold+"/test_ann")


    gts_path = Path("individual_urban_tree_crown_detection-main/split"+fold+"/train_ann")  # Where the .txt files are
    images_path = Path("individual_urban_tree_crown_detection-main/split"+fold+"/train")
    save_file = Path("individual_urban_tree_crown_detection-main/split"+fold+"/instances_train2017.json")

    annotations = globox.AnnotationSet.from_yolo_v5(folder=gts_path, image_folder=images_path)
    annotations.save_coco(save_file, imageid_to_id={'tree': 0}, auto_ids=True)

    gts_path = Path("individual_urban_tree_crown_detection-main/split"+fold+"/val_ann")  # Where the .txt files are
    images_path = Path("individual_urban_tree_crown_detection-main/split"+fold+"/val")
    save_file = Path("individual_urban_tree_crown_detection-main/split"+fold+"/instances_val2017.json")

    annotations = globox.AnnotationSet.from_yolo_v5(folder=gts_path, image_folder=images_path)
    annotations.save_coco(save_file, imageid_to_id={'tree': 0}, auto_ids=True)


    gts_path = Path("individual_urban_tree_crown_detection-main/split"+fold+"/test_ann")  # Where the .txt files are
    images_path = Path("individual_urban_tree_crown_detection-main/split"+fold+"/test")
    save_file = Path("individual_urban_tree_crown_detection-main/split"+fold+"/test.json")

    annotations = globox.AnnotationSet.from_yolo_v5(folder=gts_path, image_folder=images_path)
    annotations.save_coco(save_file, imageid_to_id={'tree': 0}, auto_ids=True)


if __name__ == '__main__':
    main()