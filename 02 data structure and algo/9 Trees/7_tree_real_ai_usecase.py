# AI use-case: building a decision tree from a config structure

class DecisionNode:
    def __init__(self, question, left=None, right=None):
        self.question = question  # e.g., "Is Age > 30?"
        self.left = left          # If Yes
        self.right = right        # If No

# Build a decision tree
'''
            Is Age > 30?
            /           \
       Yes /             \ No
        (Buy)         Is Income > 50K?
                         /        \
                      Yes(Buy)   No(Don't Buy)
'''

tree = DecisionNode("Is Age > 30?",
    left=DecisionNode("Buy"),
    right=DecisionNode("Is Income > 50K?",
        left=DecisionNode("Buy"),
        right=DecisionNode("Don't Buy")
    )
)

def traverse(node):
    if node.left is None and node.right is None:
        print("Decision:", node.question)
        return

    print("Question:", node.question)
    traverse(node.left)
    traverse(node.right)

traverse(tree)