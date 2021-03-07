
import os
from os import path
import shutil

Source_Path = r'\Users\chris\Downloads\CT\temp'
Destination = r'\Users\chris\Downloads\CT\Tumor'
#dst_folder = os.mkdir(Destination)


def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst =  "Tumor" + str(count) + ".jpg"
#str(count)
        # rename all the files
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))



# Driver Code
if __name__ == '__main__':
    main()