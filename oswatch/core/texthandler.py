class TextHandler(object):
    """docstring for TextHandler"""
    def __init__(self, arg):
        super(TextHandler, self).__init__()
        self.arg = arg
        
    def format_text(text,*x):
        strings=text % (x)
        return strings
