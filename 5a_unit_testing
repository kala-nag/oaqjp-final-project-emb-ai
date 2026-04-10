from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        # Test for emotion joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], "joy")

        # Test for emotion anger
        result_ = emotion_detector("I am really mad about this")
        self.assertEqual(result_['dominant_emotion'], "anger")

        # Test for emotion disgust
        result_ = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_['dominant_emotion'], "disgust")

        # Test for emotion sadness
        result_ = emotion_detector("I am so sad about this")
        self.assertEqual(result_['dominant_emotion'], "sadness")

        # Test for emotion fear
        result_ = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_['dominant_emotion'], "fear")


unittest.main()
