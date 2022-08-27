# -*- coding: utf-8 -*-

""" #+begin_org
* *[Summary]* :: A =CS-Lib= for creating and managing BPO's gpg and encryption/decryption.
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
from bisos.cs import globalContext
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['bpoGpg'], }
icmInfo['version'] = '202208073306'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'bpoGpg-Panel.org'
icmInfo['groupingType'] = 'IcmGroupingType-pkged'
icmInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos.crypt/_nodeBase_/fullUsagePanel-en.org][PyFwrk bisos.crypt Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:



####+BEGINNOT: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
#from unisos import ucf
#from unisos import icm

#icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

# G = cs.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

import __main__

import types


import os
import sys
#import select

# import pwd
# import grp
# import collections
import enum
#

#import traceback

# import collections

# import pathlib

# from bisos.platform import bxPlatformConfig
# from bisos.platform import bxPlatformThis

# from bisos.basics import pattern

from bisos import io
from bisos import bpf

import argparse

# from bisos.bpo import bpo
#from bisos.pals import palsSis
#from bisos.icm import fpath

# from bisos import bpf

#from bisos.cs.globalContext import globalContext
from bisos import cs

# import gnupg

import logging

#import shutil

# import pykeepass_cache
# import pykeepass
#



"""
*  [[elisp:(org-cycle)][| ]]  /icmRunArgs/         :: *IcmRunArgs_ -- In support of Run Time ICM Options --  icmRunArgs_isOptionXxSet()* [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:py3:func :funcName "isCallTrackingMonitorOff" :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /isCallTrackingMonitorOff/  [[elisp:(org-cycle)][| ]]
#+end_org """
def isCallTrackingMonitorOff(
####+END:
) -> bool:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Activated with --callTrackings monitor-.
    #+end_org """

    #G = cs.IcmGlobalContext()
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet()
    retVal = False

    for this in icmRunArgs.callTrackings:
        if this == 'monitor-':
            retVal = True

    return retVal

####+BEGIN: bx:icm:py3:func :funcName "isCallTrackingMonitorOn" :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /isCallTrackingMonitorOn/  [[elisp:(org-cycle)][| ]]
#+end_org """
def isCallTrackingMonitorOn(
####+END:
) -> bool:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Activated with --callTrackings monitor+.
    #+end_org """

    #G = cs.IcmGlobalContext()
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet()
    retVal = False

    try:
        callTrackings = icmRunArgs.callTrackings
    except AttributeError:
        callTrackings = []


    for this in callTrackings:
        if this == 'monitor+':
            retVal = True

    return retVal

####+BEGIN: bx:icm:py3:func :funcName "isCallTrackingInvokeOff" :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /isCallTrackingInvokeOff/  [[elisp:(org-cycle)][| ]]
#+end_org """
def isCallTrackingInvokeOff(
####+END:
) -> bool:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Activated with --callTrackings invoke-.
    #+end_org """
    #G = cs.IcmGlobalContext()
    G = globalContext.get()
    icmRunArgs = G.icmRunArgsGet()

    retVal = False

    for this in icmRunArgs.callTrackings:
        if this == 'invoke-':
            retVal = True

    return retVal


####+BEGIN: bx:icm:py3:func :funcName "isRunModeDryRun" :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /isRunModeDryRun/  [[elisp:(org-cycle)][| ]]
#+end_org """
def isRunModeDryRun(
####+END:
) -> bool:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Activated with --runMode dryRun.
    #+end_org """

    #G = cs.IcmGlobalContext()
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet()

    retVal = False

    if icmRunArgs.runMode == 'dryRun':
        retVal = True

    return retVal

####+BEGIN: bx:icm:py3:func :funcName "verbosityLevel" :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /verbosityLevel/  [[elisp:(org-cycle)][| ]]
#+end_org """
def verbosityLevel(
####+END:
) -> int:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Activated with -v number.
    #+end_org """

    #G = cs.IcmGlobalContext()
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet()

    level = icmRunArgs.verbosityLevel
    if level is None:
        return 30

    try: level = int(level)
    except: pass

    return level


####+BEGIN: bx:icm:py3:func :funcName "isDocStringRequested" :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /isDocStringRequested/  [[elisp:(org-cycle)][| ]]
#+end_org """
def isDocStringRequested(
####+END:
) -> bool:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Activated with -i docString.
    #+end_org """

    #G = cs.IcmGlobalContext()
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet()

    retVal = False

    if icmRunArgs.docstring:
        retVal = True

    return retVal

####+BEGIN: bx:icm:py3:func :funcName "loadFiles" :comment "Actualy loads the files." :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /loadFiles/  [[elisp:(org-cycle)][| ]]
#+end_org """
def loadFiles(
####+END:
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Load the python files specified with --load. Actualy loads the files.
    #+end_org """

    #G = cs.IcmGlobalContext()
    G = cs.globalContext.get()
    #print(f"{G}")
    icmRunArgs = G.icmRunArgsGet()

    #print(f"{icmRunArgs}")

    #for this in icmRunArgs.loadFiles:
        #cs.loadFile(this)

####+BEGIN: bx:icm:py3:func :funcName "evalFiles" :comment "Unused But Perhaps Usefull." :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /evalFiles/ =Unused But Perhaps Usefull.=  [[elisp:(org-cycle)][| ]]
#+end_org """
def evalFiles(
####+END:
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] "Eval Files -- Unused But Perhaps Usefull
    #+end_org """

    #G = cs.IcmGlobalContext()
    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet()

    for this in icmRunArgs.loadFiles:
        io.tm.TM_here('Loading: ' + this)
        f = open(this)
        eval(f.read()) # Caution: you must be sure of what's in that file
        f.close()


####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:


####+BEGIN: b:prog:file/endOfFile :extraParams nil
""" #+begin_org
* *[[elisp:(org-cycle)][| END-OF-FILE |]]* :: emacs and org variables and control parameters
#+end_org """
### local variables:
### no-byte-compile: t
### end:
####+END:
