from os.path import isfile
import pickle

class SchoolDB:

    def __init__(self, school_initializer):

        self.school_initializer = school_initializer
        self.file_name = r".\data\enroll.dat" #changed from ' r".\enroll.dat" '
        self.load_data() #changed from class attribute self.data = data

    def load_data(self):

        if (isfile(self.file_name)):#isfile from os.path

            self.file = open(self.file_name, 'rb')
            self.enrollments = pickle.load(self.file)
            self.file.close()

        else:
            self.enrollments = self.school_initializer.enrollments

    def save_data(self):
#       Save data, open file and dump pcikle only enrollments and file attributes
        self.file = open(self.file_name, 'wb')
        pickle.dump(self.enrollments, self.file)
        self.file.close()
