import reactor, unittest

class TestReactor(unittest.TestCase):
    
    def test_get_emoji_command_from_string(self):
        valid_emoji_string = "How are you doing :smile:"
        invalid_emoji_string = "How are you doing :dumb_emoji_that_doesnt_exist:"
        malformed_emoji_string = "what is this :thing"
        
