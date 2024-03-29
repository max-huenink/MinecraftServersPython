import zipfile
import os

def zip_folder(folder_path, output_path):
        parent_folder = os.path.dirname(folder_path)
        # Retrieve the paths of the folder contents.
        contents = os.walk(folder_path)
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
                # Include all subfolders, including empty ones.
                for folder_name in folders:
                        absolute_path = os.path.join(root, folder_name)
                        relative_path = absolute_path.replace(parent_folder + '\\', '')
                        print("Adding '%s' to archive." % absolute_path)
                        zip_file.write(absolute_path, relative_path)
                for file_name in files:
                        absolute_path = os.path.join(root, file_name)
                        relative_path = absolute_path.replace(parent_folder + '\\', '')
                        print("Adding '%s' to archive." % absolute_path)
                        zip_file.write(absolute_path, relative_path)
        print("'%s' created successfully." % output_path)
        zip_file.close()