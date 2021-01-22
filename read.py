import scipy.io


mat = scipy.io.loadmat("C:/Users/anuch\Work/Flie_Project_Survey/AllData/Project_The_Last_Final/EEGData/Movie_P01/EEG_Clip1.mat")
# print(len(mat['ThisEEG']))
# print(mat['ThisEEG'])
y = mat.keys()
x = mat.get("ThisEEG")
print(y)
print(x[7]) # 8 Row 3267 colum