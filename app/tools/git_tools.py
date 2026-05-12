from git import Repo

def init_repo(path='.'):
    return Repo.init(path)