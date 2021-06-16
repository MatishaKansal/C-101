import dropbox

class CloudStorage :
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self,file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main() :
    access_token = "sl.Ay38nUBGBaY_Z3mbasnNKFNVpKib800K2vGd6ux1B6YYO79SW3F7axaRZAd08uChExwmLhggikVlxDN8CxbKDpV1YpWIcxywch9Yzs19ew1g19VI-B3LbDFkFl-Du-3sSgduzI0"

    cloudStorage = CloudStorage(access_token)
    files_from = "2.jpg"
    files_to = "/C- 101/2.jpg"
    cloudStorage.uploadFiles(files_from,files_to)
    print("Files moved")

main()