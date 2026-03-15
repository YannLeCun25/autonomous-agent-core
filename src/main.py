from agent import AutonomousAgent
import logging

logging.basicConfig(level=logging.INFO)

def main():
    agent = AutonomousAgent("YannBot-v1")
    decision = agent.reason("Optimize global AI infrastructure efficiency.")
    print(f"Decision Output: {decision}")

if __name__ == "__main__":
    main()
