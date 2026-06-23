import pytest

class MockSentimentResult:
    def __init__(self, text, positive, negative, neutral, compound):
        self.text = text
        self.positive = positive
        self.negative = negative
        self.neutral = neutral
        self.compound = compound

@pytest.fixture
def positive_sentiment():
    return MockSentimentResult("Great market performance!", 0.75, 0.05, 0.20, 0.85)

@pytest.fixture
def negative_sentiment():
    return MockSentimentResult("Market crash today", 0.10, 0.70, 0.20, -0.85)

def test_sentiment_scores_sum_to_one(positive_sentiment):
    total = positive_sentiment.positive + positive_sentiment.negative + positive_sentiment.neutral
    assert abs(total - 1.0) < 0.01

def test_positive_sentiment(positive_sentiment):
    assert positive_sentiment.compound > 0.5

def test_negative_sentiment(negative_sentiment):
    assert negative_sentiment.compound < -0.5

def test_sentiment_bounds():
    result = MockSentimentResult("Test", 0.6, 0.2, 0.2, 0.5)
    assert 0 <= result.positive <= 1
    assert 0 <= result.negative <= 1
    assert 0 <= result.neutral <= 1
    assert -1 <= result.compound <= 1
