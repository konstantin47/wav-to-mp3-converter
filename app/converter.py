from subprocess import call


class Converter:
    def __init__(self, bitrate, input_file, output_file):
        self.bitrate = bitrate
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        result = call(['./ffmpeg', '-i', self.input_file, '-ar',
                       '44100', '-vn', '-ab', self.bitrate, '-f', 'mp3',
                       self.output_file])

        if result == 0:
            return True
        else:
            return False
