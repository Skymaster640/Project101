import dropbox
import os
from dropbox.files import WriteMode

class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken
    def uploadfile(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.accesstoken)
        with open(filefrom, 'rb')as f:
            dbx.filesupload(f.read(),fileto, mode=WriteMode('overwrite'))
        for root, dirs, files in os.walk("C:\Users\skyla\Downloads\Project101\App.txt", topdown = False):
            for file in files:
                print(os.path.join(root, file))
                file = os.path.join(root, file)
                with open(file, "rb") as f:
                    dbx.files_upload(f.read(), fileto, mode=WriteMode('overwrite'))
    
    def main():
        accesstoken = 'sl.A6vOL6po0VUPARM6h8FJET-qrY-NAkUZvqnqqPAg5zH9kuYITaFKFB0dReCnw9h0EwzrwqbF3olLQ3vQGmg_C0MpJMUzBqs4BJQM442Nc7QNbi_VmAy56GKb7YfVPvrHvl6WAt8'
        transferdata = Transferdata(accesstoken)
        filefrom = 'C:\Users\skyla\Downloads\Project101\App.txt'
        fileto = 'Dropbox/App.txt'
        transferdata.uploadfile(filefrom,fileto)
        print('The file has successfully been moved.')
    main()