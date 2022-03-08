import dropbox

class TransferData:
    def __init__(self,acces_token):
        self.acces_token = acces_token
        

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.acces_token)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    acces_token="sl.BDZ5eUpcdfmZH1qHNuoAVQ3qQCo-LBPRIFcdwXgpoHuk7V7QsjIsxEfbq4Uu87WpiILhwTm893muw5HVEHDzWIAzkMl5gsUu_5LlMYv5MzyIy3O9lFsJcEFxx8AepOHYfdKb1TQ"
    transferData = TransferData(acces_token)

    file_from = input("enter the file path to transfer ")
    file_to = input("enter th full path to upload to drpbox")

    transferData.upload_file(file_from, file_to)
    print("file has been moved ")

main()