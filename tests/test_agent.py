import unittest
from src.engine.reasoning import ReasoningEngine

class TestAgent(unittest.TestCase):
    def test_planning(self):
        engine = ReasoningEngine()
        steps = engine.plan_steps("Optimization")
        self.assertEqual(len(steps), 3)

if __name__ == "__main__":
    unittest.main()
