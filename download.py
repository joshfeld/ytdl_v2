import os
import subprocess
import glob


class Convert:
    def __init__(self, vid, bit):
        self.vid = vid
        self.bit = bit
        self.err = False

    def clear_files(self):
        # Remove all files from download folder prior to new convert
        for root, directories, files in os.walk(self.dl_path):
            for filename in files:
                fp = os.path.join(root, filename)
                os.remove(fp)

    def dl_convert(self, yturl):
        # Grab video from youtube
        try:
            print("Now downloading")
            download = (
                f'yt-dlp -o "{self.dl_path}'
                + '%(title)s.%(ext)s"'
                + " -f mp4 "
                + f"{yturl}"
            )
            subprocess.call(download, shell=True)
        except Exception:
            self.err = True
            print("File could not be downloaded, make sure the YouTube link is correct")

        # # Clean title
        # for badchar in ['\"', '#', '$', '%', '\'', '*', ',', '.', '/', ':',
        #                 ';', '<', '>', '?', '\\', '^', '|', '~', '\\\\']:
        #     if badchar in ytitle:
        #         ytitle = ytitle.replace(badchar, "")

        # Convert video to mp3
        try:
            file = max(glob.iglob(f"{self.dl_path}*.mp4"), key=os.path.getctime)
            ytitle = file.split("/")[-1]
            command = (
                f'ffmpeg -i "{self.dl_path}'
                + f'{ytitle}" -b:a {self.bit} -vn "{self.dl_path}'
                + f"{ytitle.split('.mp4')[0]}"
                + '.mp3"'
            )
            subprocess.call(command, shell=True)
        except Exception:
            self.err = True
            print("Error in ffmpeg conversion")

        # Delete video if not requested
        if self.vid == 0:
            os.remove(self.dl_path + ytitle)

        if not self.err:
            return "All downloads complete"
        else:
            return "At least one file did not download successfully"

    @property
    def dl_path(self):
        # return r"D:\Programming\ytdl_v2\files" + "\\"
        return r"/files/"
