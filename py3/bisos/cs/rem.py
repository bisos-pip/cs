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
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['rem'], }
csInfo['version'] = '202208262617'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'rem-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
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

####+BEGIN: bx:cs:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
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

# from blee.icmPlayer import bleep
####+END:

import __main__

import os
#import select

# import pwd
# import grp
# import collections
#

#import traceback

# import collections

# import pathlib

# from bisos.platform import bxPlatformConfig
# from bisos.platform import bxPlatformThis

# from bisos.basics import pattern

from bisos import io
#from bisos import bpf


#import logging

import abc

#import shutil

# import pykeepass_cache
# import pykeepass
#


####+BEGIN: bx:cs:py3:section :title "Service Specification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Service Specification*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:python:class :className "ROSMU" :superClass "object" :comment "Remote Operations Service Unit" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /ROSMU/ object =Remote Operations Service Unit=  [[elisp:(org-cycle)][| ]]
#+end_org """
class ROSMU(object):
####+END:
    """
** Abstraction of Remote Operations Service Multi-Unit.
"""
####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmuName: str,
            rosmuSpec: str,
    ):
        self._rosmuName = rosmuName  # A named reference to rosmuSpec
        self._rosmuSpec = rosmuSpec  # List Of Units, List Of rosmuStates

####+BEGIN: bx:cs:py3:method :methodName "rosmuName" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuName/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuName(
####+END:
            self,
    ):
        return self._rosmuName

####+BEGIN: bx:cs:py3:method :methodName "rosmuSpec" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuSpec/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuSpec(
####+END:
            self,
    ):
        """
*** ROS Description. The Contract Specification. Points to a file.
        """
        return self._rosmuSpec


####+BEGIN: bx:cs:py3:section :title "Service Access Point"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Service Access Point*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: bx:dblock:python:class :className "RosmuAccessPoint" :superClass "object" :comment "ROSMU Access Point" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /RosmuAccessPoint/ object =ROSMU Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class RosmuAccessPoint(object):
####+END:
    """
** Abstraction of ROSMU Access Point
"""

    rosmuBase = "/bisos/var/gitSh/performer"

####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmu: ROSMU,
            rosmuApName: str,
            performerAddr: str,
            rosmuState: str,
            rosmuFiles: str,
    ):
        self._rosmu = rosmu
        self._rosmuApName = rosmuApName
        self._performerAddr = performerAddr
        self._rosmuState = rosmuState
        self._rosmuFiles = rosmuFiles  # slash root of the file system for this rosmu

####+BEGIN: bx:cs:py3:method :methodName "rosmu" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmu/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmu(
####+END:
            self,
    ):
        return self._rosmu

####+BEGIN: bx:cs:py3:method :methodName "rosmuApName" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuApName/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuApName(
####+END:
            self,
    ):
        return self._rosmuApName

####+BEGIN: bx:cs:py3:method :methodName "performerAddr" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /performerAddr/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def performerAddr(
####+END:
            self,
    ):
        return self._performerAddr


####+BEGIN: bx:dblock:python:class :className "GitSh_RosmuAccessPoint" :superClass "RosmuAccessPoint" :comment "ROSMU Access Point" :classType "subed"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-subed  [[elisp:(outline-show-subtree+toggle)][||]] /GitSh_RosmuAccessPoint/ RosmuAccessPoint =ROSMU Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class GitSh_RosmuAccessPoint(RosmuAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    rosmuPerformerBase = "/bisos/var/gitSh/performer"
    rosmuInvokerBase = "/bisos/var/gitSh/invoker"

####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmu: ROSMU,
            rosmuApName: str,
            performerAddr: str,
    ):
        super().__init__(rosmu, rosmuApName, performerAddr, rosmuState="", rosmuFiles="")

####+BEGIN: bx:cs:py3:method :methodName "rosmuAp_invPath" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuAp_invPath/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuAp_invPath(
####+END:
            self,
    ):
        return (
            os.path.join(__class__.rosmuInvokerBase, self.rosmuApName,)
        )


####+BEGIN: bx:cs:py3:method :methodName "rosmuAp_perfPath" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuAp_perfPath/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuAp_perfPath(
####+END:
            self,
    ):
        return (
            os.path.join(__class__.rosmuInvokerBase, self.rosmuApName,)
        )

####+BEGIN: bx:dblock:python:class :className "RPyC_RosmuAccessPoint" :superClass "RosmuAccessPoint" :comment "ROSMU Access Point" :classType "subed"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-subed  [[elisp:(outline-show-subtree+toggle)][||]] /RPyC_RosmuAccessPoint/ RosmuAccessPoint =ROSMU Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class RPyC_RosmuAccessPoint(RosmuAccessPoint):
####+END:
    """
** Abstraction of a SAP.
"""

####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmu: ROSMU,
            rosmuApName: str,
            performerAddr: str,
    ):
        super().__init__(rosmu, rosmuApName, performerAddr, rosmuState="", rosmuFiles="")

####+BEGIN: bx:cs:py3:method :methodName "rosmuAp_invPath" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuAp_invPath/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuAp_invPath(
####+END:
            self,
    ):
        return (
            #os.path.join(__class__.rosmuInvokerBase, self.rosmuApName,)
        )


####+BEGIN: bx:cs:py3:method :methodName "rosmuAp_perfPath" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuAp_perfPath/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuAp_perfPath(
####+END:
            self,
    ):
        return (
            #os.path.join(__class__.rosmuInvokerBase, self.rosmuApName,)
        )


####+BEGIN: bx:cs:py3:section :title "Operations Access Point"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Operations Access Point*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:python:class :className "OperationAccessPoint" :superClass "abc.ABC" :comment "Operation Access Point" :classType "abs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-abs    [[elisp:(outline-show-subtree+toggle)][||]] /OperationAccessPoint/ abc.ABC =Operation Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class OperationAccessPoint(abc.ABC):
####+END:
    """
** Abstraction of An Op AP.
"""

####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmuAp: RosmuAccessPoint,
    ):
        self._rosmuAp = rosmuAp

####+BEGIN: bx:cs:py3:method :methodName "rosmuAp" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuAp/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuAp(
####+END:
            self,
    ):
        return self._rosmuAp

####+BEGIN: bx:cs:py3:method :methodName "invIdCreate" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invIdCreate/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
#+end_org """
    @abc.abstractmethod
    def invIdCreate(
####+END:
            self,
    ):
        self._invId = "NOTYET"  # datetag, plus file check

####+BEGINNOT: bx:cs:py3:method :methodName "invId" :deco "property abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invId/ deco=property abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @property
    @abc.abstractmethod
    def invId(
####+END:
            self,
    ):
        return self._invId

####+BEGIN: bx:cs:py3:method :methodName "invoke" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invoke/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
#+end_org """
    @abc.abstractmethod
    def invoke(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:cs:py3:method :methodName "invokeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
#+end_org """
    @abc.abstractmethod
    def invokeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        pass

####+BEGIN: bx:cs:py3:method :methodName "invokeOutcomeRetreive" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeOutcomeRetreive/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
#+end_org """
    @abc.abstractmethod
    def invokeOutcomeRetreive(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        pass


####+BEGIN: bx:cs:py3:method :methodName "perform" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /perform/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
#+end_org """
    @abc.abstractmethod
    def perform(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        pass

####+BEGIN: bx:cs:py3:method :methodName "performOutcomeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /performOutcomeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
#+end_org """
    @abc.abstractmethod
    def performOutcomeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        pass

####+BEGIN: bx:dblock:python:class :className "GitSh_InvokerOpAP" :superClass "OperationAccessPoint" :comment "Operation Access Point" :classType "subed"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-subed  [[elisp:(outline-show-subtree+toggle)][||]] /GitSh_InvokerOpAP/ OperationAccessPoint =Operation Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class GitSh_InvokerOpAP(OperationAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""


####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmuAp: GitSh_RosmuAccessPoint,
    ):
        self._rosmuAp = rosmuAp


####+BEGIN: bx:cs:py3:method :methodName "invokeIdCreate" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeIdCreate/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invokeIdCreate(
####+END:
            self,
    ):
        self._invId = "NOTYET"  # datetag, plus file check
        self._invIdPath = "NOTYET"

####+BEGIN: bx:cs:py3:method :methodName "invId" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invId/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invId(
####+END:
            self,
    ):
        return self._invId

####+BEGIN: bx:cs:py3:method :methodName "invoke" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invoke/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invoke(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:cs:py3:method :methodName "invokeSubmit" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeSubmit/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invokeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:cs:py3:method :methodName "invokeOutcomeRetreive" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeOutcomeRetreive/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invokeOutcomeRetreive(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:dblock:python:class :className "GitSh_PerformerOpAP" :superClass "OperationAccessPoint" :comment "Operation Access Point" :classType "subed"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-subed  [[elisp:(outline-show-subtree+toggle)][||]] /GitSh_PerformerOpAP/ OperationAccessPoint =Operation Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class GitSh_PerformerOpAP(OperationAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmuAp: GitSh_RosmuAccessPoint,
    ):
        self._rosmuAp = rosmuAp

####+BEGIN: bx:cs:py3:method :methodName "rosmuAp" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuAp/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuAp(
####+END:
            self,
    ):
        return self._rosmuAp


####+BEGIN: bx:cs:py3:method :methodName "invId" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invId/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def invId(
####+END:
            self,
    ):
        return self._invId

####+BEGIN: bx:cs:py3:method :methodName "perform" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /perform/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def perform(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:cs:py3:method :methodName "performOutcomeSubmit" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /performOutcomeSubmit/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def performOutcomeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")




####+BEGIN: bx:dblock:python:class :className "RPyC_InvokerOpAP" :superClass "OperationAccessPoint" :comment "Operation Access Point" :classType "subed"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-subed  [[elisp:(outline-show-subtree+toggle)][||]] /RPyC_InvokerOpAP/ OperationAccessPoint =Operation Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class RPyC_InvokerOpAP(OperationAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""


####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmuAp: GitSh_RosmuAccessPoint,
    ):
        self._rosmuAp = rosmuAp


####+BEGIN: bx:cs:py3:method :methodName "invokeIdCreate" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeIdCreate/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invokeIdCreate(
####+END:
            self,
    ):
        self._invId = "NOTYET"  # datetag, plus file check
        self._invIdPath = "NOTYET"

####+BEGIN: bx:cs:py3:method :methodName "invId" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invId/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invId(
####+END:
            self,
    ):
        return self._invId

####+BEGIN: bx:cs:py3:method :methodName "invoke" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invoke/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invoke(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:cs:py3:method :methodName "invokeSubmit" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeSubmit/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invokeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:cs:py3:method :methodName "invokeOutcomeRetreive" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invokeOutcomeRetreive/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invokeOutcomeRetreive(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:dblock:python:class :className "RPyC_PerformerOpAP" :superClass "OperationAccessPoint" :comment "Operation Access Point" :classType "subed"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-subed  [[elisp:(outline-show-subtree+toggle)][||]] /RPyC_PerformerOpAP/ OperationAccessPoint =Operation Access Point=  [[elisp:(org-cycle)][| ]]
#+end_org """
class RPyC_PerformerOpAP(OperationAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

####+BEGIN: bx:cs:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosmuAp: GitSh_RosmuAccessPoint,
    ):
        self._rosmuAp = rosmuAp

####+BEGIN: bx:cs:py3:method :methodName "rosmuAp" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /rosmuAp/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def rosmuAp(
####+END:
            self,
    ):
        return self._rosmuAp


####+BEGIN: bx:cs:py3:method :methodName "invId" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /invId/ deco=property  [[elisp:(org-cycle)][| ]]
#+end_org """
    @property
    def invId(
####+END:
            self,
    ):
        return self._invId

####+BEGIN: bx:cs:py3:method :methodName "perform" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /perform/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def perform(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:cs:py3:method :methodName "performOutcomeSubmit" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-       :: /performOutcomeSubmit/ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def performOutcomeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosmuSpec, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")





####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
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
