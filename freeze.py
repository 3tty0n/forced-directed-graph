from app import app
from flask_frozen import Freezer

freezer = Freezer(app)


@freezer.register_generator
def forced_graph():
    yield '/view/twitter_combined.html'
    yield '/view/com-amazon.ungraph.html'
    yield '/view/BA10000.html'

if __name__ == '__main__':
    freezer.freeze()