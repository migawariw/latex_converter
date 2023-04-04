import requests

# GitHubリポジトリの情報
username = "migawariw"
repository = "latex_converter"
branch = "main"  # or whichever branch you want to use
path = "path/to/save/latex/images"  # the directory in the repo where the images will be saved
token = "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"  # this token must have repo access

# LaTeX数式を画像に変換するAPIのエンドポイント
api_endpoint = "https://latex.codecogs.com/png.latex"

# LaTeX数式
latex_formula = "your_latex_formula"

# APIリクエストを送信して画像を取得する
response = requests.get(api_endpoint, params={"code": latex_formula})

# 取得した画像をGitHubリポジトリにアップロードする
url = f"https://api.github.com/repos/{username}/{repository}/contents/{path}/{latex_formula}.png"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.github.v3+json",
}
data = {
    "message": f"Add image of {latex_formula}",
    "content": response.content.decode("utf-8"),
    "branch": branch,
}
response = requests.put(url, headers=headers, json=data)
