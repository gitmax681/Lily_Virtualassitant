import os
import psutil
import time


class Spotify:
    def __init__(self):
        self.is_running = Spotify.check_running()
        self.is_playing = True

        if not self.is_running:
            Spotify.launch(self)
        time.sleep(3)

    def launch(self):
        os.system("spotify 1>/dev/null 2>&1 &")
        self.is_running = True

    def play(self):
        if self.is_running:
            os.system('qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play')
            self.is_playing = True
            
        else:
            Spotify.launch(self)            
            time.sleep(7)
            Spotify.play()

    def pause(self):
        
        if self.is_playing:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause")
            self.is_playing = False

    def next(self):
        if self.is_running:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")
            self.is_playing = True
            
    
    def play_from_start(self):

        if self.is_running:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")
            self.is_playing = True


    def stop(self):
        if self.is_running:
            os.system("qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop")
            self.is_playing = False

            

    def open_playlist(self, URI):
        self.URI = URI
        if self.is_running:
            os.system(f"qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri {self.URI}")
            self.is_playing = True
            return True
        else:
            return False
            
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


