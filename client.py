import requests

base_url = "http://chrisbrooks.pythonanywhere.com/api/programmers"

def get_programmer_count():
    """
    Return the number of programmers returned from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    req = requests.get(base_url)
    if req.status_code == 200:
        data = req.json()
        return len(data.get("programmers", []))
    return 0


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    req = requests.get(f"{base_url}/{pid}")
    if req.status_code == 200:
        return req.json()
    return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    r = requests.get(f"{base_url}/by_first_name/{first_name}")
    if r.status_code == 200:
        data = r.json()
        programmers = data.get("programmers", [])
        if programmers:
            prog = programmers[0]
            return f"{prog['first']} {prog['last']}"
    return None
