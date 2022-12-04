# import required libraries

import json
import requests


def load_candidates(source):
    """
    function imports data from web or json file
    :param source: filename or url with json data
    :return: data from file when detecting ".json" in name, or trying to get data from web in another case
    """
    if ".json" in source:
        with open(source, mode='r', encoding='utf-8') as file:
            return json.load(file)
    else:
        response = requests.get(source)
        return response.json()


def get_candidate_by_id(id, source):
    """
    function finds one candidate from data according its id
    :param id: given id
    :param source: filename or url with json data
    :return: data of person having given id (dict)
    """
    candidates = load_candidates(source)
    for candidate in candidates:
        if candidate["id"] == id:
            return candidate


def get_candidate_by_name(name, source):
    """
    function finds one candidate from data according its name
    :param name: given name
    :param source: filename or url with json data
    :return: data of person having given id (dict)
    """
    candidates = load_candidates(source)
    matched_candidates = []
    for candidate in candidates:
        if name.lower() in candidate["name"].lower():
            matched_candidates.append(candidate)
    return matched_candidates


def get_canidates_by_skill(skill_name, source):
    """
    function searching for persons with required skill
    :param skill_name: required skill
    :param source: filename or url with json data
    :return: list of persons with required skill
    """
    candidates = load_candidates(source)
    return [person for person in candidates if skill_name.lower() in person["skills"].lower().split(", ")]


print(get_candidate_by_name("sh", "candidates.json"))
# print(get_canidates_by_skill("python", "candidates.json"))
# print(load_candidates("candidates.json"))
