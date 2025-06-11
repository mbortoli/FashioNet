# FashioNet

The project was born as a simple idea for our end-of-course presentation when we remembered an old (but recurring) request from my sister: An app like the one shown in the movie "Clueless."

![I know I know...](https://badulakit.files.wordpress.com/2013/07/closet-cher.jpg)

The idea is to try to classify whether the top part of an outfit (i.e. shirt) matches the bottom part (i.e., pants or shorts).

Unfortunately ~~(or fortunately)~~ we can't digitize all clothes, but we can take pictures of some pieces to use in the dataset. It was created this way using the clothes we own.

With the images prepared, we used the `fastai` library to train two architectures: ResNet34 and ResNet50. This allowed us to consolidate the knowledge acquired during the course and compare the two architectures. We believed that the more complex architecture might classify better, but this was not observed in the final results.

In the end, we observed that the _ResNet34_ architecture outperformed _ResNet50_, something that was verified only when exposing them to images not used in training and validation. This step demonstrates the importance of testing the models.

A idéia basica é tentar classificar se a parte de cima da roupa (i.e. camiseta) combina com a parte de baixo (i.e., calça ou bermuda).

# Notebook

Estão localizados dentro da pasta [`src`](src), sendo: 
* [`nb-train-resnet34.ipynb/nb-train-resnet34.ipynb`](src) - resnet34 training
* [`nb-train-resnet50.ipynb`](src/nb-train-resnet50.ipynb) - resnet50 training
* [`testing.ipynb`](src/testing.ipynb) - Testing the net with new images
* [`make-labels.ipynb`](src/make-labels.ipynb) - `Widget` to assist in manual classification


# The _dataset_

Individual photos were taken of each piece, resulting in 19 top pieces and 15 bottom pieces, which were then cropped to center each one. We then combined the top pieces with the bottoms, generating a total of 285 pairs, with 75% used for training and 25% for validation.

After training, we also generated 12 additional combinations to be used for network testing.

All resulting images were resized to 250x250 pixels for better network performance — but you can test the original ones contained in the [`dataset/v1`](dataset/v1) folder and see how they perform with the same transformations applied by `fastai` :-)

The file [`labeled_v2.csv`](labeled_v2.csv) was created using the [`make-labels`](src/make-labels.ipynb) notebook, where it contains the correct classifications for each image - with external help, because I am part of the target audience.

Example of some generated images::

![IMG](dataset/v2-resized/IMG_8723.JPG-IMG_8747.JPG) ![IMG](dataset/v2-resized/IMG_8723.JPG-IMG_8749.JPG)

Can you tell which one matches and which doesn't? If you can't, this solution is for you too!

# Dependencies

To run the notebooks, the [`fastai v1`](https://github.com/fastai/fastai) library is required.