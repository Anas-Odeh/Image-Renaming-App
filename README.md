# **Image-Renaming-App for Annotated Biological Imaging Data**

  ![ICON-1](https://github.com/Anas-Odeh/Image-Renaming-App/assets/133384773/a0ca77ec-3ca9-430c-b4f5-f7c4c1409045)


# Introduction

The Image-Renaming-App is a specialized software solution based on python programming and designed to address the intricate challenges of organizing and managing annotated imaging data within the biological research domain. By leveraging case viewer annotations, this tool introduces a systematic approach to renaming and consolidating annotated image files, thereby enhancing the efficiency of data retrieval and analysis workflows.

### **The code assumes that each image is stored in a separate subfolder, following the default saving option of the case viewer.**

# Key Features

* Annotation-Based Renaming: The application integrates a robust renaming mechanism that utilizes the metadata from case viewer annotations. This ensures that each image file is renamed in a manner that reflects its specific annotated content, facilitating easier identification and categorization of data.

* Multiple Image formats: '.png', '.jpg', '.jpeg', '.tif'

* Centralized Data Repository: In addition to renaming, the tool compiles all annotated images into a unified directory named "pooled images." This centralized repository enables researchers to access their entire annotated dataset conveniently, streamlining the data analysis process.

* Preservation of Original Data: Recognizing the paramount importance of data integrity in scientific research, the Image-Renaming-App is designed to keep the original images with their annotations intact in their original locations, ensuring the preservation of the initial dataset for verification and reproducibility.

# Deployment and Usage

**Installation**

The Image-Renaming-App is provided as a self-contained executable file [Image-Renaming-App.exe](https://github.com/Anas-Odeh/Image-Renaming-App/releases/tag/v1.0.0), facilitating straightforward deployment without the need for complex setup procedures.

To download the app click on the Image-Renaming-App.exe as shown in the image below:
![image](https://github.com/Anas-Odeh/Image-Renaming-App/assets/133384773/b708e2af-0c70-4ce8-a336-312e3322dbf4)


**Execution**

To initiate the app, simply execute the Image-Renaming-App.exe. The software automatically scans for image files with case viewer annotations within the specified directory, applies the annotation-based renaming protocol, and aggregates the renamed images into the "pooled images" folder.

## **Upon opening the app, you will see the following window:**


![image](https://github.com/Anas-Odeh/Image-Renaming-App/assets/133384773/fafc09c0-6162-4eb6-ab1c-367eddda74f5)

## **Main App window**
![Screenshot (37)](https://github.com/Anas-Odeh/Image-Renaming-App/assets/133384773/731b8396-00bf-4fe7-b3b4-17a60eab32ad)

## **Complete this straightforward process in just a few seconds with only two steps!**

**1. Select the main folder that contains multiple subfolders.**

**2. Start analysis.**


For example, within the main folder named ['Images'](https://github.com/Anas-Odeh/Image-Renaming-App/tree/main/Example%20Images), there are two subfolders named ['Nature'](https://github.com/Anas-Odeh/Image-Renaming-App/tree/main/Example%20Images/Images/Nature), which contains an image called 'Picture 1', and ['River'](https://github.com/Anas-Odeh/Image-Renaming-App/tree/main/Example%20Images/Images/River), which contains an image called 'image'. After running the app, these two images will be renamed to 'Nature' and 'River', respectively. Finally, a new folder called 'Pooled Images' will be created, containing copies of these two images.

---


## **Application Scenarios**

This tool is particularly valuable in fields such as histology, pathology, and environmental biology, where annotated images play a critical role in research documentation and analysis. It offers a streamlined solution for managing large volumes of annotated imaging data, ensuring that researchers can focus on their scientific inquiries with enhanced data organization support.


# **License**

The Image-Renaming-App is distributed under the Apache License 2.0. This license promotes open-source collaboration while providing the necessary legal protection for contributors and users alike. I believe in the power of open science and the positive impact of sharing knowledge and tools within the research community. Figures were Created with BioRender.com.
