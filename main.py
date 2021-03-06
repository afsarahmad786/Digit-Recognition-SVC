from sklearn import datasets
from sklearn.svm import SVC
from scipy import misc

# Loading Data
digits = datasets.load_digits()
# Extracting data from data set
features = digits.data
# Extracting output corresponding to data set
labels = digits.target

# Training
clf = SVC(gamma=0.001)
clf.fit(features, labels)

# Reading image
img = misc.imread("images_test/9.jpg")
# Resizing image to 8 * 8 = 64
img = misc.imresize(img, (8, 8))
# Updating type from unsigned int 8 to signed float 64
img = img.astype(digits.images.dtype)
# We have data set image of integer pixels in the range 0..16.
img = misc.bytescale(img, high=16, low=0)

x_test = []

# Data Example

# [
#   first row
#   [
#       first column
#       [ 0.  0.  0.],  sum/3.0
#        . . . . . . . .
#       last column
#       [ 0.  0.  0.]
#   ],
#   .  . .  .  .  .
#   last row
#   [
#           first column
#           [ 0.  0.  0.]
#            .  . . . . .
#           last column
#            [ 0.  0.  0.]
#   ]
#  ]

# Converting out 3D array to 1D Array
for each_row in img:
    for each_pixel in each_row:
        x_test.append(((sum(each_pixel))/3.0))

# Predicting output from our Trained Classifier
print(clf.predict([x_test]))
