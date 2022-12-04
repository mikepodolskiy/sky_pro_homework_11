# imports

from flask import Flask, render_template

from utils import load_candidates, get_candidate_by_id, get_candidate_by_name, get_canidates_by_skill

# variables definition
source = "candidates.json"

# starting app
app = Flask(__name__)

@app.route("/")
def all_candidates():
    """
    view for all candidates list with links to their personal pages
    :return: view according template
    """
    candidates = load_candidates(source)
    return render_template('list.html', candidates = candidates)

@app.route("/candidates/<int:id>")
def candidate(id):
    """
    view for candidate page
    :param id: id of required candidate
    :return: view of candidate personal page according to template
    """
    candidate = get_candidate_by_id(id, source)
    if not candidate:
        return "Candidate not found"
    return render_template("card.html", candidate = candidate)

@app.route("/search/<name>")
def search_candidate(name):
    """
    view for search by name results
    :param name: string data to search for in candidates name
    :return:view of search result according to template
    """
    candidates = get_candidate_by_name(name, source)
    number_of_candidates = len(candidates)
    return render_template("search.html", candidates=candidates, number = number_of_candidates)

app.run()


# print(get_candidate_by_id(4, "candidates.json"))