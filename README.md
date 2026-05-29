# Face Detection (YOLOv8 + OpenCV)

### Prerequisites
You must need Python 3 and OpenCV installed on your PC.

### Installing
A step by step installation — follow these methods.

1. Create and activate the virtual environment
```
python3 -m venv cv-face
source cv-face/bin/activate
```

2. Install all the requirements
```
pip install -r requirements.txt
```

3. Download the trained model weights

`best.pt` is not included in this repository. Download it manually and place it in the root project folder:
```
your-project/
├── best.pt        ← place it here
├── app.py
├── face_detector.py
└── ...
```

4. Collect face data for each person
```
python app.py
```
Enter the number of persons and their names/IDs when prompted. The script will capture **50 images per person** from your webcam and save them inside the `dataset/` folder.

5. Run the face detector
```
python face_detector.py
```
Press **q** to quit the detection window.

> Detections with confidence **≥ 0.75** are labelled with the person's name; anything below that threshold is shown as **Unknown**.

> Dataset annotation, augmentation, and train/test/val splitting were done on [Roboflow](https://roboflow.com). The annotated dataset was exported and trained on Google Colab using YOLOv8n with a T4 GPU. Training notebook available in `notebook/Face-Detection.ipynb`.

> The trained weights (`best.pt`) are excluded from this repository via `.gitignore`. You can retrain the model yourself using the notebook, or request the weights directly from the author.


<p align="center">
  <img width="800" src="https://github.com/user-attachments/assets/f1588cd6-bf32-41bb-9e27-857c17b55dda" />
</p>