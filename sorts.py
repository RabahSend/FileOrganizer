import os

def moveFile(Directory, folder, nameFile):
    path = Directory + folder
    path += '/' + nameFile
    os.rename(Directory + '/' + nameFile, path)

def firstSort(Directory):
    dirs = ["/Multimedia", "/Texts", "/Images", "/Code", "/Videos", "/Audio", "/Archives", "/Other"]

    # giving file extension
    multimedia = ('.pdf', '.pptx', '.xlsx', '.xls', '.csv', 'odp')
    texts = ('.txt', '.docx', '.doc', '.log', '.md', '.odt', '.odg')
    images = ('.jpg', '.jpeg', '.png', '.gif')
    code = ('.py', '.java', '.cpp', '.html', '.css', '.c', '.js&')
    videos = ('.mp4', '.avi', '.mov', '.mkv')
    audio = ('.mp3', '.wav', '.flac')
    archives = ('.zip', '.rar', '.tar.gz')

    for dir in dirs:
        path = Directory + dir
        if not os.path.exists(path):
            os.mkdir(path)

    # iterating over all files
    for file in os.listdir(Directory):
        file_path = Directory + '/' + file
        if os.path.isfile(file_path):
            if file.endswith(multimedia):
                moveFile(Directory, dirs[0], file)
            elif file.endswith(texts):
                moveFile(Directory, dirs[1], file)
            elif file.endswith(images):
                moveFile(Directory, dirs[2], file)
            elif file.endswith(code):
                moveFile(Directory, dirs[3], file)
            elif file.endswith(videos):
                moveFile(Directory, dirs[4], file)
            elif file.endswith(audio):
                moveFile(Directory, dirs[5], file)
            elif file.endswith(archives):
                moveFile(Directory, dirs[6], file)
            else:
                moveFile(Directory, dirs[-1], file)

    for folder in os.listdir(Directory):
        folder_path = os.path.join(Directory, folder)
        print(folder_path)
        if os.path.isdir(folder_path):
           items = os.listdir(folder_path)
           if not items:
               os.rmdir(folder_path)

    return "done!"