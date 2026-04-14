import requests

class GitHubUser:
    def __init__(self, username):
        self.risposta = requests.get(f"https://api.github.com/users/{username}")
        self.repos_risposta = requests.get(f"https://api.github.com/users/{username}/repos")

    def mostra(self):
        if self.risposta.status_code == 404:
            print("User non trovato")
        else:
            dati = self.risposta.json()
            print(dati["login"])
            print(dati["public_repos"])
            print(dati["created_at"])
            print(dati["bio"])

    def mostra_repos(self):
        if self.repos_risposta.status_code == 404:
            print("Repo non trovato")
        else:
            repos = self.repos_risposta.json()
            stelle = [repo["stargazers_count"] for repo in repos]
            for repo in repos:
                print(repo["name"], "-", repo["language"], "-", repo["stargazers_count"])
            print("Stelle totali:", sum(stelle))


username = input("Inserisci nome user: ")
utente = GitHubUser(username)
utente.mostra()
utente.mostra_repos()