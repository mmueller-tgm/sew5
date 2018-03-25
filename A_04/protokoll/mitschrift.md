---
title:
 - Jenkins protokoll
theme:
 - metropolis
---

# __A_04 Jenkins Müller Protokoll__
*Arbeitsaufwand: 4h*

# Installation
Jenkins wurde mit docker-compose bereitgestellt. Im _Dockerfile_ ist die Container Konfiguration und in _docker-compose.yml_ die Deployment Konfiguration

> docker-comose.yml

```
version: '3.3'

services:
    a04:
        build:
            context: .
        ports:
            - '8080:8080'
        container_name: A_04_Jenkins

```


> Dockerfile

```
from jenkins/jenkins:lts

USER root

RUN apt-get update -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install pylint
RUN apt-get install python3-nose python3-coverage -y

USER jenkins

EXPOSE 8080
```

## initial config

In der Konsole wird das Administrator Passwort angezeigt, mit dem man unter [localhost:8080](localhost:8080) die Konfiguration fortsetzen kann. 

Bei der Frage welche Pakete installiert werden sollen, wurde die Option der vorgeschlagenen Pakete gewählt.

Danach wird ein Administratorkonto erstellt, wo nach einem Benutzernamen, Passwort, Vollen Namen und e-mail gefragt wird.
Das kann aber auch übersprungen werden.

![Admin Konto](images/AdminKonto.png)

## some 
Auf der Weboberfläche kann man unter "__Jenkins verwalten__" "__Plugins verwalten__" auswählen und dort auf den Reiter __Verfügbar__ alle verfügbaren Plugins sehen.

![plugins](images/Plugins.png)


Um die Plugins "__Violations__" und "__Cobertura__" zu installieren muss der jeweilige Name des Plugins unter _Filter_ eingegeben werden. Das Plugin wird mit einem Klick auf die Checkbox ausgewählt, der Button Installation und Neustart installiert dann alle ausgewählten Plugins.

Unter dem Reiter Installiert sind alle installierten Plugins aufgelistet, zusammen mit einer Option jenes zu Deinstallieren.


# Repository
Für die Übung wurde ein Repository([https://github.com/mmueller-tgm/A_04_2018/](https://github.com/mmueller-tgm/A_04_2018/tree/master)) auf [Github](https://github.com) erstellt.


# Jenkins weitere config
Um Jenkins mit git zu verbinden muss bei Jenkins ein Neues Projekt erstellt werden.

![new project](images/newProject.png)

# Build
Um automatisch zu Builden, müsste ich miene Ports Exposen und meine IP Adresse bei GitHub Angeben, dies ist eine Sicherheitslücke und wurde deswegen nicht gemacht. In folgendem Bild ist das Feld, in dem ich meine URL eintragen würde.

![webhook](images/webhook.png)

Es hat nicht funktioniert das Bruch Beispiel zu builden, da er das Paket nicht gefunden hat, der Errorlog von Jenkins ist allerdings vorhanden.

```
Started by user Maximilian Müller
Building in workspace /var/jenkins_home/workspace/Bruch
 > git rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/mmueller-tgm/A_04_2018 # timeout=10
Fetching upstream changes from https://github.com/mmueller-tgm/A_04_2018
 > git --version # timeout=10
 > git fetch --tags --progress https://github.com/mmueller-tgm/A_04_2018 +refs/heads/*:refs/remotes/origin/*
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
 > git rev-parse refs/remotes/origin/origin/master^{commit} # timeout=10
Checking out Revision b93d9bc088a9f8ca85621353a3c9ee45863c0ee8 (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f b93d9bc088a9f8ca85621353a3c9ee45863c0ee8
Commit message: ":cry:"
 > git rev-list --no-walk d3b5332a291b8d3060b9f02fae767bcb90dcf75b # timeout=10
[Bruch] $ /bin/sh -xe /tmp/jenkins5725257645905561998.sh
+ ls -la
total 72
drwxr-xr-x 1 jenkins jenkins   194 Jan 26 16:24 .
drwxr-xr-x 1 jenkins jenkins    10 Jan 26 16:10 ..
-rw-r--r-- 1 jenkins jenkins  5405 Jan 26 16:20 .coverage
drwxr-xr-x 1 jenkins jenkins   136 Jan 26 16:24 .git
-rw-r--r-- 1 jenkins jenkins     2 Jan 26 16:16 .pylintrc
-rw-r--r-- 1 jenkins jenkins  9361 Jan 26 16:10 Bruch.py
-rw-r--r-- 1 jenkins jenkins 35064 Jan 26 16:10 LICENSE
-rw-r--r-- 1 jenkins jenkins    12 Jan 26 16:10 README.md
-rw-r--r-- 1 jenkins jenkins   211 Jan 26 16:10 __init__.py
drwxr-xr-x 1 jenkins jenkins   132 Jan 26 16:16 __pycache__
-rw-r--r-- 1 jenkins jenkins  9361 Jan 26 16:24 bruch.py
drwxr-xr-x 1 jenkins jenkins    44 Jan 26 16:16 docs
-rw-r--r-- 1 jenkins jenkins  1701 Jan 26 16:20 nosetests.xml
drwxr-xr-x 1 jenkins jenkins   336 Jan 26 16:16 test
+ nosetests3 --with-xunit --all-modules --traverse-namespace --with-coverage --cover-inclusive ./test
E
======================================================================
ERROR: Failure: ImportError (No module named 'bruch')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/nose/failure.py", line 39, in runTest
    raise self.exc_val.with_traceback(self.tb)
  File "/usr/lib/python3/dist-packages/nose/loader.py", line 418, in loadTestsFromName
    addr.filename, addr.module)
  File "/usr/lib/python3/dist-packages/nose/importer.py", line 47, in importFromPath
    return self.importFromDir(dir_path, fqname)
  File "/usr/lib/python3/dist-packages/nose/importer.py", line 94, in importFromDir
    mod = load_module(part_fqname, fh, filename, desc)
  File "/usr/lib/python3.5/imp.py", line 244, in load_module
    return load_package(name, filename)
  File "/usr/lib/python3.5/imp.py", line 216, in load_package
    return _load(spec)
  File "<frozen importlib._bootstrap>", line 693, in _load
  File "<frozen importlib._bootstrap>", line 673, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 673, in exec_module
  File "<frozen importlib._bootstrap>", line 222, in _call_with_frames_removed
  File "/var/jenkins_home/workspace/Bruch/__init__.py", line 2, in <module>
    from bruch.Bruch import *       # if this is'nt there sphinx fails to find the class even though the module is
ImportError: No module named 'bruch'

Name                                                              Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------
/usr/lib/python3/dist-packages/nose/case.py                         205    152    26%   5-28, 31, 36, 45, 48, 51, 54-57, 62-63, 67, 72-73, 77-83, 88-99, 106-116, 135-139, 143, 151, 154, 157, 175-178, 181-185, 189-398
/usr/lib/python3/dist-packages/nose/core.py                         169    146    14%   5-32, 35, 40, 46, 52, 57, 63-64, 67-181, 191, 195, 206, 208-341
/usr/lib/python3/dist-packages/nose/failure.py                       25     15    40%   1-21, 29, 33-36, 40-42
/usr/lib/python3/dist-packages/nose/importer.py                     101     57    44%   7-29, 31, 34, 43, 49, 60, 74, 85-92, 97, 99-136, 145, 159-160, 164-167
/usr/lib/python3/dist-packages/nose/loader.py                       348    310    11%   11-60, 81, 88-89, 102-361, 376, 389-401, 407, 423, 428-469, 477, 483-622
/usr/lib/python3/dist-packages/nose/plugins/base.py                 195    191     2%   1-92, 99, 104-724
/usr/lib/python3/dist-packages/nose/plugins/capture.py               56     41    27%   12-55, 61, 66, 71, 81-95, 100, 104-110, 114
/usr/lib/python3/dist-packages/nose/plugins/cover.py                153    149     3%   13-159, 165-168, 174-178, 184-271
/usr/lib/python3/dist-packages/nose/plugins/debug.py                 31     27    13%   7-37, 45-67
/usr/lib/python3/dist-packages/nose/plugins/deprecated.py            16     12    25%   9-37, 41, 45
/usr/lib/python3/dist-packages/nose/plugins/doctests.py             220    212     4%   52-185, 196-452
/usr/lib/python3/dist-packages/nose/plugins/errorclass.py            64     54    16%   95-138, 141, 144-146, 148, 155-209
/usr/lib/python3/dist-packages/nose/plugins/failuredetail.py         20     17    15%   9-30, 34, 38-48
/usr/lib/python3/dist-packages/nose/plugins/isolate.py               34     32     6%   38-58, 64-102
/usr/lib/python3/dist-packages/nose/plugins/logcapture.py           126     97    23%   18-33, 37, 43, 45-75, 81-85, 87-176, 180-186, 201, 206, 211-214, 219, 224-229, 236-239, 242-243
/usr/lib/python3/dist-packages/nose/plugins/manager.py              265    216    18%   51-87, 90-91, 98, 101, 109-110, 113, 130, 146, 150-163, 169-171, 179-183, 187-248, 256-259, 267, 276-284, 286-294, 297-300, 304-460
/usr/lib/python3/dist-packages/nose/plugins/multiprocess.py         490    480     2%   96-219, 228-229, 232, 236-237, 239-835
/usr/lib/python3/dist-packages/nose/plugins/prof.py                  93     89     4%   13-56, 58-68, 74-154
/usr/lib/python3/dist-packages/nose/plugins/skip.py                  22     18    18%   9-53, 58, 62
/usr/lib/python3/dist-packages/nose/plugins/testid.py               135    123     9%   95-134, 139-141, 157-311
/usr/lib/python3/dist-packages/nose/plugins/xunit.py                164     94    43%   42-62, 66, 70, 73-75, 79, 91, 97, 100-102, 107, 111-117, 121-122, 126-156, 163, 166, 171-189, 203, 225-228, 235, 238, 241, 246, 250, 255-259, 263, 267, 271, 275, 281-282, 305-333
/usr/lib/python3/dist-packages/nose/proxy.py                        108     66    39%   18-29, 31-42, 44, 49, 61, 63, 67-77, 79, 85-88, 94-95, 98, 109, 113-115, 119-121, 126, 134-167, 172-175, 181-187
/usr/lib/python3/dist-packages/nose/pyversion.py                    132    126     5%   4-30, 35-69, 75-174, 177-199, 207-211
/usr/lib/python3/dist-packages/nose/result.py                       131     98    25%   11-36, 42, 46-54, 62-64, 70-74, 80, 84-86, 91-96, 100, 107, 112-153, 160-180, 184, 188-198
/usr/lib/python3/dist-packages/nose/selector.py                     134    112    16%   9-34, 36, 39, 47-217, 219, 226-227, 239, 242-246
/usr/lib/python3/dist-packages/nose/suite.py                        396    238    40%   12-50, 56-68, 72-79, 83-94, 100-103, 107, 111-112, 117-147, 153, 161-173, 177, 180-198, 208, 211-216, 220-221, 230-269, 273-274, 276-277, 280, 295-297, 301, 306, 318-323, 326-329, 333-334, 344-345, 354-356, 360, 372, 377-394, 396, 399, 410, 426-427, 430, 438, 443, 445, 448-451, 457, 459, 465, 468-469, 474, 489-539, 542-543, 550, 558-607
/usr/lib/python3/dist-packages/nose/util.py                         351    294    16%   3-135, 146-159, 168-171, 194, 198-233, 265, 268, 282-297, 314-317, 326, 345-441, 451-469, 474, 480, 482, 485, 489-509, 522-669
/usr/lib/python3/dist-packages/pkg_resources/_vendor/six.py         444    442     1%   23-184, 186, 189-868
/usr/lib/python3/dist-packages/pkg_resources/extern/__init__.py      35     32     9%   1-23, 31-73
__init__.py                                                           2      0   100%
-----------------------------------------------------------------------------------------------
TOTAL                                                              4665   3940    16%
----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (errors=1)
Build step 'Execute shell' marked build as failure
Finished: FAILURE
```
