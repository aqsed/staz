Machine learning competency task

You are given a dataset of RGB images of shoes. Describe a procedure that would sort the shoes into groups by colors, possibly using some machine learning algorithm.
Discuss the advantages/disadvantages of your solutions. Use less than 100 words, please.

Multi classification problem. Using annotated dataset with colors we could train neural network to classify shoes. (Perhaps using yolo if we wanted to know exact location of shoe).
Disadvanteges - difficult implementantion. (Maybe train yolo to detect box of pixels of shoe and calculate color from pixels).

You are given a previously unseen image of a shoe. Design an algorithm that would retrieve 10 most similars shoes from your dataset. Use less than 100 words, please.
Similarity between images could be calculated by distances. Most similar images should have lower distance between input image. (Vector distance).
