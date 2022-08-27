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

from bisos import cs
from bisos.cs import inCmnd
from bisos.cs import examples

import argparse

# from bisos.bpo import bpo
#from bisos.pals import palsSis
#from bisos.icm import fpath

# from bisos import bpf

# import gnupg

import logging

#import shutil

# import pykeepass_cache
# import pykeepass
#


####+BEGIN: bx:icm:py3:func :funcName "read" :funcType "extTyped" :retType "extTyped" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /read/  [[elisp:(org-cycle)][| ]]
#+end_org """
def read(
####+END:
) -> str:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Reads stdin. Returns a string. -- Uses mutable list.
    #+end_org """

    stdinAsStr = ""
    #if select.select([sys.stdin, ], [], [], 0.0)[0]:
    if not sys.stdin.isatty():

        msgAsList = []
        for line in sys.stdin:
            msgAsList.append(str(line))

        stdinAsStr = str("".join(msgAsList),)

    return stdinAsStr


####+BEGIN: bx:icm:python:func :funcName "G_main" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass

####+BEGIN: bx:icm:python:icmItem :itemType "Configuration" :itemTitle "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Configuration  :: = =Framework::= g_ Settings -- ICMs Imports =  [[elisp:(org-cycle)][| ]]
"""
####+END:

# g_examples = __main__.examples  # or None
# g_mainEntry = None  # or G_main

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icm2.G_main.py"
"""
*  [[elisp:(beginning-of-buffer)][Top]] # /Dblk-Begin/ # [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

def classedCmndsDict(importedCmndsModules):
    """
** Should be done here, can not be done in icm library because of the evals.
"""
    import importlib
    importedCmndsFilesList=[]
    importedTagsList=[]
    for moduleName in importedCmndsModules:
        #print(f"moduleName={moduleName}")
        moduleNameList = moduleName.split(".")
        importTag = moduleNameList.pop()
        importModule = ".".join(moduleNameList)
        #print(f"importTag= {importTag} -- moduleNameList={moduleNameList} -- importModule={importModule}")
        _tmp = importlib.import_module(importModule)
        exec(f"{importTag} = _tmp.{importTag}") # assignment is a statement
        #eval(f"print({importTag}.__file__)") # DEBUG
        eval(f"importedCmndsFilesList.append({importTag}.__file__)") # expression
        importedTagsList.append(importTag)

    for moduleName in ["bisos.cs.inCmnd", "bisos.cs.examples"]:
        #print(f"moduleName={moduleName}")
        moduleNameList = moduleName.split(".")
        importTag = moduleNameList.pop()
        importModule = ".".join(moduleNameList)
        #print(f"importTag= {importTag} -- moduleNameList={moduleNameList} -- importModule={importModule}")
        _tmp = importlib.import_module(importModule)
        exec(f"{importTag} = _tmp.{importTag}") # assignment is a statement
        #eval(f"print({importTag}.__file__)") # DEBUG
        eval(f"importedCmndsFilesList.append({importTag}.__file__)") # expression
        importedTagsList.append(importTag)


    #print(importedCmndsFilesList)
    #print(importedTagsList)

    callDict = dict()
    for eachCmnd in inCmnd.cmndList_mainsMethods().cmnd(
            interactive=False,
            importedCmnds={}, # __main__.g_importedCmnds -- Being obsoleted
            mainFileName=__main__.__file__,
            importedCmndsFilesList=importedCmndsFilesList,
    ):
        #print(f"eachCmnd={eachCmnd}")
        try:
            callDict[eachCmnd] = eval("__main__.{}".format(eachCmnd))
        except AttributeError:
            #print(f"AttributeError -- __main__.{eachCmnd} -- ignored")
            pass
        except NameError:
            #print(f"NameError -- __main__.{eachCmnd} -- ignored")
            pass
        else:
            #print(f"Added __main__.{eachCmnd}")
            continue

        for importTag in importedTagsList:
            #print(f"trying {importTag}")
            try:
                #print(f"Evaling -- {importTag}.{eachCmnd}")
                eval(f"{importTag}.{eachCmnd}")
            except AttributeError:
                #print(f"AttributeError -- {importTag}.{eachCmnd}")
                continue
            try:
                callDict[eachCmnd] = eval(f"{importTag}.{eachCmnd}")
                #print(f"callDict -- {importTag}.{eachCmnd}")
                break
            except NameError:
                pass


    return callDict


# G = icm.IcmGlobalContext()

# icmInfo = G.icmInfo()

# try:
#    __main__.icmInfo
# except AttributeError:
#     pass
# else:
#     icmInfo.update(__main__.icmInfo)

#     icmInfo['icmName'] = __main__.__icmName__
#     icmInfo['version'] = __main__.__version__
#     icmInfo['status'] = __main__.__status__
#     icmInfo['credits'] = __main__.__credits__

#     G.icmInfoSet(icmInfo)

def g_icmMain(
        noCmndEntry=None,   # To Be Obsoleted
        extraParamsHook=None,
        importedCmndsModules=[],
        icmPreCmndsHook=None,
        icmPostCmndsHook=None,
        icmInfo=None,
):
    """This ICM's specific information is passed to G_mainWithClass"""

    cs.G.icmInfoSet(icmInfo)

    examples = None
    mainEntry = None

    if noCmndEntry:
        if type(noCmndEntry) is types.FunctionType:
            mainEntry = noCmndEntry
            # examples is None
        else:  # We then assume it is a Cmnd
            examples = noCmndEntry
            mainEntry = noCmndEntry

    sys.exit(
        cs.G_mainWithClass(
            inArgv=sys.argv[1:],                 # Mandatory
            #extraArgs=__main__.g_argsExtraSpecify,        # Mandatory
            extraArgs=extraParamsHook,
            G_examples=examples,               # Mandatory
            classedCmndsDict=classedCmndsDict(importedCmndsModules),   # Mandatory
            mainEntry=mainEntry,
            g_icmPreCmnds=icmPreCmndsHook,
            g_icmPostCmnds=icmPostCmndsHook,
        )
    )




def cmndCallParamsValidate(
        callParamDict,
        interactive,
        outcome=None,

):
    """Expected to be used in all CMNDs.

MB-2022 --- This is setting the variable not validating it.
    Perhaps the function should have been cmndCallParamsSet.

Usage Pattern:

    if not icm.cmndCallParamValidate(FPsDir, interactive, outcome=cmndOutcome):
       return cmndOutcome
"""
    #G = IcmGlobalContext()
    #if type(callParamOrList) is not list: callParamOrList = [ callParamOrList ]

    if not outcome:
        outcome = OpOutcome()

    for key  in callParamDict:
        # print(f"111 {key}")
        # interactive could be true in two situations:
        # 1) When a cs is executed on cmnd-line.
        # 2) When a cs is invoked with interactive as true.
        # When (2) callParamDict[key] is expcted to be true by having been specified at invokation.
        #
        if not callParamDict[key]:
            # MB-2022 The logic here seems wrong. When non-interactive, only mandattories
            # should be verified.
            # if not interactive:
            #     return eh_problem_usageError(
            #         outcome,
            #         "Missing Non-Interactive Arg {}".format(key),
            #     )
            if interactive:
                exec("callParamDict[key] = IcmGlobalContext().usageParams." + key)
            # print(f"222 {callParamDict[key]}")


    return True



from bisos.cs import inCmnd


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
