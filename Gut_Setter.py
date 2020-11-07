"""
プロジェクトディレクトリ(これの親ディレクトリ)以下の全プロジェクトを
Gitに上げるプログラム
"""

import os
import subprocess as sp

def main():
  os.chdir("..")
  for project in os.listdir():
    if input("Can I regist {}? [y],n: ".format(project)) is "n":
      continue

    print("-----")
    os.chdir(project)
    sp.run(["git", "init"])
    sp.run(["git", "add", "-A"])
    sp.run(["git", "commit", "-m", "init"])

    sp.run(["gh", "repo", "create", project, "--public"])
    sp.run(["git", "remote", "add", "origin", "https://github.com/we-can-panic/{}.git".format(project)])
    sp.run("git push -u origin master".split())
    os.chdir("..")



if __name__ == '__main__':
  main()
