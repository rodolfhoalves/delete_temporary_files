""" 
Autor: Rodolfho Queiroz
- Script to delete old files based on timestamp
Obs. You can specify severals paths to delete and some type of files to be excluded from this execution
Last update: 2022-06-15
"""

import os, time, pathlib, shutil



parameters = {
    'remaining_days': 7,
    'paths': [
        "C:\\TMP_FILES",
        "",
        ""],

    'fileTypeExcluded': ['.docx']
}


class DeleteFiles:

    def __init__(self) -> None:
        self.paths = parameters['paths']
        self.remaining_days = parameters['remaining_days']
        self.fileTypeExcluded = parameters['fileTypeExcluded']
        


    def isThereAnyExceptionFile(self) -> bool:
        if len(self.fileTypeExcluded)  != 0:
            return True
        return False
        

    def is_file(self, path: str) -> bool:
        return True if os.path.isfile(path) else False


    def isEmptyDirectory(self, path: str) -> bool:

        try:
            if not self.is_file(path):
                dir = os.listdir(path)
                if len(dir) == 0:
                    return True
                else:
                    return False
        except:
            return False
            
        
    def get_extension_file(self, path: str) -> str:
        
        if self.is_file(path):
            extension = pathlib.Path(path).suffix
            return extension
        else:
            return False
        

    def __get_list_files(self) -> list:
        
        file_lists = []

        for path in self.paths:
            for root, dirs, files in os.walk(path, topdown=True):
                for name in files:
                    pfile = (os.path.join(root, name))
                    file_lists.append(pfile)
                for name in dirs:
                    pfile = (os.path.join(root, name))
                    file_lists.append(pfile)
        return (file_lists)


    def get_list_files(self) -> list:
        objects = []

        tmp_object_files = self.__get_list_files()        
        for file in tmp_object_files:
            if self.is_file(file):
                objects.append(file)

            elif self.isEmptyDirectory(file):
                objects.append(file)

            else:
                pass
        
        return objects



    def get_fileTimeStamp(self, file):
        timestamp_file = os.stat(file).st_ctime
        #print(type(timestamp_file))  
        return timestamp_file


    def computer_timestamp_now(self):
        """ https://www.epochconverter.com/ 
        Return the timestamp from the computer
        """
        return time.time()
    

    def isFileDatedForDelete(self, file) -> bool:
        oneDayInSeconds = 86400
        days_to_keep = self.computer_timestamp_now() - (self.remaining_days * oneDayInSeconds)
        
        if self.get_fileTimeStamp(file) < days_to_keep:
            return True
 
        return False


    def delete(self, file: str):
        if self.isFileDatedForDelete(file):

            try:
                if self.is_file(file):
                    os.remove(file)

                else:
                    shutil.rmtree(file)
                return file

            except:
                pass


    def processOfDelete(self, file: str):

        if self.isThereAnyExceptionFile():
            if self.is_file:
                if not self.get_extension_file(file) in self.fileTypeExcluded:
                    self.delete(file)
            
            if not self.is_file:
                self.delete(file)

        else:
            self.delete(file)
            
        


run = DeleteFiles()
allFiles = run.get_list_files()

for file in allFiles:
    run.processOfDelete(file)




