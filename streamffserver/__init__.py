class Streaming(object):
  def __init__(self):
    pass

  def ffserver_config_maker(self, data):
    pass

  def ffserver_config_from_template(self, template_name, data):
    pass

  def stream_mp4_from_mjpeg(self, camera):
    cmd_ffmpeg = "ffmpeg -f mjpeg -i '%(camera_url)s'  -f '%(format)s' '%(output)s'"
    cmd_ffserver = "ffserver -f '%(config_file)'" %({'config_file' : 'test_ffserver.ffm'})

  def streamh264(self):
    pass
