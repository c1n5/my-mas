#!/usr/bin/env python
import sys
from my_mas.crew import MyMasCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with comprehensive product comparison inputs.
    """
    inputs = {
        'product_category': 'Wireless Earbuds',
        'target_brands': 'Apple AirPods Pro, Sony WF-1000XM4, Bose QuietComfort Earbuds, Samsung Galaxy Buds Pro',
        'needs_features': 'Active noise cancellation, battery life over 6 hours, comfortable fit, water resistance, good sound quality'
    }
    MyMasCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations with product comparison inputs.
    """
    inputs = {
        'product_category': 'Wireless Earbuds',
        'target_brands': 'Apple AirPods Pro, Sony WF-1000XM4, Bose QuietComfort Earbuds, Samsung Galaxy Buds Pro',
        'needs_features': 'Active noise cancellation, battery life over 6 hours, comfortable fit, water resistance, good sound quality'
    }
    try:
        MyMasCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyMasCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results with product comparison inputs.
    """
    inputs = {
        'product_category': 'Wireless Earbuds',
        'target_brands': 'Apple AirPods Pro, Sony WF-1000XM4, Bose QuietComfort Earbuds, Samsung Galaxy Buds Pro',
        'needs_features': 'Active noise cancellation, battery life over 6 hours, comfortable fit, water resistance, good sound quality'
    }
    try:
        MyMasCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
