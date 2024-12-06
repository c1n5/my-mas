#!/usr/bin/env python
import sys
from my_mas.crew import MyMasCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def get_user_inputs():
    """
    Prompt the user for input values for product comparison.
    """
    product_category = input("Enter the product category: ").strip()
    target_brands = input("Enter the target brands (comma-separated): ").strip()
    key_features = input("Enter the key features: ").strip()
    return {
        'product_category': product_category,
        'target_brands': target_brands,
        'key_features': key_features
    }


def run():
    """
    Run the crew with comprehensive product comparison inputs.
    """
    inputs = get_user_inputs()
    MyMasCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations with product comparison inputs.
    """
    inputs = get_user_inputs()
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
    inputs = get_user_inputs()
    try:
        MyMasCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

