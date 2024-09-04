# Logo Detection 

This project detects Pepsi and Coca-Cola logos in video files using a YOLOv8 object detection model. It processes the video to identify and track these logos, then outputs an annotated video and a JSON file with details of the detections.


## Setup

### Installation

### Effectively configure and run this YOLOv8-based logo detection project.
    
- Install Dependencies

    Ensure that you have Python and pip installed. 
    It is recommended to set up a virtual environment. 

    ```bash
    python -m venv venv
    ```
    ```bash
    source .venv/bin/activate       #for windows use  venv\Scripts\activate     
    ```
    ```bash
    pip install -r requirements.txt
    ```

    This will install all the required dependencies to run this model.


 ### Configure Paths 

To run this project, you will need to set up the path to the video which you want to analyze. 

The path should be configured in the script where the video path is set (replace `<path_to_video>` with your actual video path):

```python
video_path = '<path_to_video>'
```
<!-- !https://github.com/Nikhilpedada/Logo_Detection/blob/0f06541f8b63ad826f2b2c2475feb4598787252e/Screenshot%20(13).png -->

### Running Model

To run the model, use the following command:

```bash
python main.py
```
## Output 

After running the command, the model will process the input video and generate the following output files in the `Output` folder:
- The output JSON file (`results.json`) will contain the timestamps of detected Pepsi and CocaCola logos.

### 1. **Annotated Video**: 
A video file with detected logos annotated.

#### Demo
   <!-- This is the link for the demo video :[ https://drive.google.com/drive/folders/1Fv7yraqVynzzHx4NmnAy-0uqAMt7R2js?usp=drive_link ](https://drive.google.com/file/d/15ouOTf5vbw7jB2W3ffGtIQgZXPpViLi9/view?usp=drive_link)-->
### 2. **JSON File**: 
A file containing the timestamp of each logo detection along with their respective height, width, and distance from the center of the frame in pixels.
<!-- results.json-->
##Demo
<!--https://github.com/Nikhilpedada/Logo_Detection/blob/a550f359f48ef7d716f95d97c967522a45764d89/output_image.jpg-->
## Acknowledgements

 - [Ultralytics/YoloV8](https://github.com/ultralytics/ultralytics)
 - [DataSet](https://universe.roboflow.com/advait-dongre/pepsi-cocacola-images/dataset/1)

