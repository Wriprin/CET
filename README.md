# CET
### A Sample of the CET

> etc...



***

### Sundry

> 🌵 btw, config the token of github, which is turned on **August 13, 2021**：(

```bash
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
```



***

### Reunion the process

```bash
Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET
$ ls
CET/

Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET
$ cd CET/

Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET/CET (main)
$ ls
CET.py  README.md

Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET/CET (main)
$ git log
commit e2bda917be8a29305d1bd64a94e75b713488bc19 (HEAD -> main, origin/main, origin/HEAD)
Author: William Pitt <51706819+Wriprin@users.noreply.github.com>
Date:   Fri Aug 27 22:14:36 2021 +0800

    Initial commit

Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET/CET (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CET.py

nothing added to commit but untracked files present (use "git add" to track)

Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET/CET (main)
$ git add CET.py

Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET/CET (main)
$ git commit -m "commit the sample of CET" CET.py
[main 5a69791] commit the sample of CET
 1 file changed, 100 insertions(+)
 create mode 100644 CET.py

Wriprin@Rocinante MINGW64 ~/OneDrive/root/CET/CET (main)
$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.80 KiB | 1.80 MiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Wriprin/CET
   e2bda91..5a69791  main -> main
```







