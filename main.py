# imports

from flask import Flask, render_template
from utils import load_candidates, get_candidate_by_id, get_candidate_by_name, get_candidates_by_skill

# variables definition
source = "candidates.json"

# starting app
app = Flask(__name__)


# view of all candidates as required
@app.route("/")
def all_candidates():
    """
    view for all candidates list with links to their personal pages
    :return: view according template
    """
    candidates = load_candidates(source)
    return render_template('list.html', candidates=candidates)


# all candidates pages as required
@app.route("/candidates/<int:id>")
def candidate(id):
    """
    view for candidate page
    :param id: id of required candidate
    :return: view of candidate personal page according to template
    """
    candidate_by_id = get_candidate_by_id(id, source)
    if not candidate:
        return "Candidate not found"
    return render_template("card.html", candidate=candidate_by_id)


# view of search result by name of candidate as required
@app.route("/search/<name>")
def search_candidate(name):
    """
    view for search by name results
    :param name: string data to search for in candidates name
    :return:view of search result according to template
    """
    candidates = get_candidate_by_name(name, source)
    number_of_candidates = len(candidates)
    return render_template("search.html", candidates=candidates, number=number_of_candidates)


# view of search result by skill of candidate as required
@app.route("/skill/<skill>")
def search_candidate_skill(skill):
    """
    view for search by skill results
    :param skill: string data to search for in candidates skills
    :return:view of search result according to template
    """
    candidates = get_candidates_by_skill(skill, source)
    number_of_candidates = len(candidates)
    return render_template("skill.html", candidates=candidates, number=number_of_candidates, skill=skill)


# running app
app.run()
