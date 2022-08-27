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

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Commands Args" :anchor "" :extraInfo ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Commands Args_: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END


####+BEGIN: bx:cs:py3:func :funcName "cmndArgPositionToMinAndMax" :funcType "extTyped" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgPositionToMinAndMax/  [[elisp:(org-cycle)][| ]]
#+end_org """
def cmndArgPositionToMinAndMax(
####+END:
        argPosStr: str,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Expecting argPosStr to be either an integer or two intgers delimited by an ampersand
    returning two integers specifying the range
    #+end_org """

    rangeList = argPosStr.split("&")
    rangeListLen = len(rangeList)

    def errVal():
        return None, None

    if rangeListLen == 0:
        return int(rangeList), int(rangeList)
    else:
        min=int(rangeList[0])

    if rangeListLen == 1:
        return min, min
    elif rangeListLen == 2:
        max=int(rangeList[1])
        return min, max
    else:
        print('rangeListLen not 1 or 2')
        return errVal()


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class            ::  ArgReq -- Obsoleted   [[elisp:(org-cycle)][| ]]
"""
#ArgReq = enum('Mandatory', 'Optional')   # Argument Requirements -- Mandatory Keyword Arguments
####+BEGIN: bx:dblock:python:class :className "ArgReq" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /ArgReq/ object  [[elisp:(org-cycle)][| ]]
#+end_org """
class ArgReq(object):
####+END:
    """ #+begin_org
** [[elisp:(org-cycle)][| DocStr| ]]  Argument Requirements: For Specification Of Required Keyword Arguments.
    Example: ArgReq.Conditional -- to be used at declaration time.
    #+end_org """

    Mandatory = "___Mandatory___"
    Optional = "___Optional___"
    Conditional = "___Conditional___"

    def __init__(self):
        pass

    def isMandatory(self, arg):
        """Predicate."""
        if arg == self.Mandatory:
            return True
        else:
            return False

    def mandatoryValidate(self, arg):
        """Predicate."""
        if self.isMandatory(arg):
            EH_problem_info("Missing Mandatory Argument")
            # It is the caller's frame that is of significance
            raise ValueError("Missing Mandatory Argument: " + ucf.stackFrameInfoGet(2))
        return arg

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndArgs: Per Command Argument" :anchor "" :extraInfo ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndArgs: Per Command Argument_: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END


####+BEGIN: bx:dblock:python:class :className "CmndArgSpec" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /CmndArgSpec/ object  [[elisp:(org-cycle)][| ]]
#+end_org """
class CmndArgSpec(object):
    ####+END:
    """ #+begin_org
    ** [[elisp:(org-cycle)][| DocStr| ]]  Representation of an Interactively Command Module (ICM) Command Argument Sepecification(CmndArgSpec).
    #+end_org """

    def __init__(
            self,
            argName=None,
            argDefault=None,
            argChoices=[],
            argDataType=None,
            argDescription=None,
    ):
        '''Constructor'''
        self.__argName = argName
        self.__argDefault = argDefault
        self.__argValue = None
        self.__argDescription = argDescription
        self.__argDataType = argDataType
        self.__argChoices = argChoices

    def __str__(self):
         return  format(
             'value: ' + str(self.argValueGet())
         )

    def argNameGet(self):
         """  """
         return self.__argName

    def argNameSet(self, argName):
         """        """
         self.__argName = argName

    def argValueGet(self):
         """        """
         return self.__argValue

    def argValueSet(self, value):
         """        """
         self.__argValue = value

    def argDescriptionGet(self):
         """        """
         return self.__argDescription

    def argDescriptionSet(self, argDescription):
         """        """
         self.__argDescription = argDescription

    def argDataTypeGet(self):
         """        """
         return self.__argDataType

    def argDataTypeSet(self, argDataType):
         """        """
         self.__argDataType = argDataType

    def argDefaultGet(self):
         """        """
         return self.__argDefault

    def argDefaultSet(self, argDefault):
         """        """
         self.__argDefault = argDefault

    def argChoicesGet(self):
         """        """
         return self.__argChoices

    def argChoicesSet(self, argChoices):
         """        """
         self.__argChoices = argChoices

####+BEGIN: bx:dblock:python:class :className "CmndArgsSpecDict" :superClass "" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /CmndArgsSpecDict/ object  [[elisp:(org-cycle)][| ]]
#+end_org """
class CmndArgsSpecDict(object):
####+END:
    """ #+begin_org
** [[elisp:(org-cycle)][| DocStr| ]]  ICM Argameters Dictionary -- Collection of ICM_Argam s can be placed in ICM_ArgamDict
    From icmArgamDict
    #+end_org """

    def __init__(self):
         self.__cmndArgsSpecDict = dict()

    def argsDictAdd(
             self,
             argPosition=None,
             argName=None,
             argDefault=None,
             argDescription=None,
             argDataType=None,
             argChoices=None,
    ):
         """        """
         thisArgSpec = CmndArgSpec(
             argName=argName,
             argDefault=argDefault,
             argDescription=argDescription,
             argDataType=argDataType,
             argChoices=argChoices,
         )

         self.argDictAppend(argPosition, thisArgSpec)

    def argDictAppend(
             self,
             argPosition,
             cmndArgSpec,
    ):
         """        """
         self.__cmndArgsSpecDict.update({argPosition:cmndArgSpec})

    def argDictGet(self):
         """        """
         return self.__cmndArgsSpecDict

    def argPositionFind(self, argPosition=None):
         """        """
         return self.__cmndArgsSpecDict[argPosition]


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndArgsLengthIsNotValid    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndArgsLengthIsNotValid(cmndArgs=ArgReq.Mandatory,
                        expected=ArgReq.Mandatory,
                        comparison=ArgReq.Mandatory,
                       ):
    cmndArgsLen=len(cmndArgs)
    if comparison(cmndArgsLen, expected):
        EH_critical_usageError("Bad Number Of cmndArgs: cmndArgs={cmndArgs}"
                                 .format(cmndArgs=cmndArgs))
        return(True)
    return(False)


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndArgsLengthValidate    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndArgsLengthValidate(cmndArgs=ArgReq.Mandatory,
                        expected=ArgReq.Mandatory,
                        comparison=ArgReq.Mandatory,
                       ):
    cmndArgsLen=len(cmndArgs)
    if comparison(cmndArgsLen, expected):
        EH_critical_usageError(f"Bad Number Of cmndArgs: cmndArgs={cmndArgs} cmndArgsLen={cmndArgsLen} expected={expected}")
        return(1)
    return(0)

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  int__gt    [[elisp:(org-cycle)][| ]]
"""

def int__gt(nuOfArgs,  expected):
    if nuOfArgs > expected:
        return True
    else:
        return False


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
