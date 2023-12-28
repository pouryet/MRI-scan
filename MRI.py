#Don't forget to put a star
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nibabel as nib

# Load the MRI image
mri_image = nib.load('mri_image.nii')

# Get the image data as a NumPy array
mri_data_array = mri_image.get_fdata()

# Save the data to a CSV file
mri_data_df = pd.DataFrame(mri_data_array)
mri_data_df.to_csv('mri_data.csv', index=False)

# Apply Gaussian smoothing with a sigma of 1.5
from scipy.ndimage import gaussian_filter
mri_data_filtered = gaussian_filter(mri_data_array, sigma=1.5)

# Save the filtered data to a CSV file
mri_data_filtered_df = pd.DataFrame(mri_data_filtered)
mri_data_filtered_df.to_csv('mri_data_filtered.csv', index=False)

# Display the original and filtered images
plt.subplot(121)
plt.imshow(mri_data_array[:, :, 100], cmap='gray')
plt.title('Original MRI Image')
plt.subplot(122)
plt.imshow(mri_data_filtered[:, :, 100], cmap='gray')
plt.title('Filtered MRI Image')
plt.show()
#https://t.me/pouryet
