import os
import psutil
import time


class Spotify:
    def __init__(self):
        self.is_running = Spotify.check_running()
        self.is_playing = True

        if not self.is_running:
            Spotify.launch()

    def launch(self):
        os.system("spotify 1>/dev/null 2>&1 &")
        self.is_running = True

    def play(self):
        time.sleep(1)
        if self.is_running:
            os.system('qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play')
            self.is_playing = True
            return "process success"
        else:
            return "process failed spotify not initialized"

    def pause(self):
        
        if self.is_playing:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause")
            self.is_playing = False
            return "process success"
        else:
            return "process failed spotify not initialized"

    def next(self):
        if self.is_running:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")
            self.is_playing = True
            return "process success"
        else:
            return "process failed spotify not initialized"
            
    
    def play_from_start(self):

        if self.is_running:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")
            self.is_playing = True
            return "process success"
        else:
            return "process failed spotify not initialized"
            

    def stop(self):
        if self.is_running:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop")
            self.is_playing = False
            return "process success"
        else:
            return "process failed spotify not initialized"
            

    def open_playlist(self, URI):
        self.URI = URI
        if self.is_running:
            os.system(f"qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri {self.URI}")
            self.is_playing = True
            return "process success"
        else:
            return "process failed spotify not initialized"
            
    @staticmethod
    def check_running():
        running = False
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                
                if 'spotify' in pinfo['name'].lower() :
                    running = True
            except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
                pass
        return running;


