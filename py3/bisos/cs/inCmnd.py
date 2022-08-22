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


####+BEGIN: bx:dblock:python:class :className "Cmnd" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  /Player Support/      :: *Framework cmnds That are expected by the ICM-Player* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  icmLanguage    [[elisp:(org-cycle)][| ]]
"""
class icmLanguage(cs.Cmnd):
    """Returns python"""

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
    ):
        """Part of icm framework."""
        thisOutcome = OpOutcome()
        if interactive:
            print("python")

        return thisOutcome.set(
            opError=OpError.Success,
            opResults="python"
        )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  icmCmndPartIncludes    [[elisp:(org-cycle)][| ]]
"""
class icmCmndPartIncludes(cs.Cmnd):
    """NOTYET Returns True"""

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
    ):
        """Part of icm framework."""

        #if interactive:
            #print "python"

        return True

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  icmInUpdate -- Update    [[elisp:(org-cycle)][| ]]
"""
class icmInUpdate(cs.Cmnd):
    """Given a baseDir, update icmIn"""
    cmndParamsMandatory = None
    cmndParamsOptional = None
    cmndArgsLen = ["1"]

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
            icmsBase=None,  # cmndArgs[0]
    ):
        """Part of icm framework."""

        if interactive:
            G = IcmGlobalContext()
            icmRunArgs = G.icmRunArgsGet()
            icmsBase = icmRunArgs.cmndArgs[0]
        else:
            if not icmsBase:
                EH_problem_usageError("")
                return

        G_myFullName = sys.argv[0]
        G_myName = os.path.basename(G_myFullName)

        icmInBase = icmsBase + "/" + G_myName + "/icmIn"

        print("{icmInBase}".format(icmInBase=icmInBase))

        icmParamsToFileParamsUpdate(
            parRoot="{icmInBase}/paramsFp".format(icmInBase=icmInBase),
            icmParams=G.icmParamDictGet(),
        )

        icmParamsToFileParamsUpdate(
            parRoot="{icmInBase}/commonParamsFp".format(icmInBase=icmInBase),
            icmParams=commonIcmParamsPrep(),
        )

        cmndMainsMethodsToFileParamsUpdate(
            parRoot="{icmInBase}/cmndMainsFp".format(icmInBase=icmInBase),
        )

        cmndLibsMethodsToFileParamsUpdate(
            parRoot="{icmInBase}/cmndLibsFp".format(icmInBase=icmInBase),
        )

        return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  icmInfo    [[elisp:(org-cycle)][| ]]
"""
class icmInfo(cs.Cmnd):
    """Given a baseDir, update icmIn"""
    cmndParamsMandatory = None
    cmndParamsOptional = None
    cmndArgsLen = ["1"]

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
    ):
        """Part of icm framework."""

        # if interactive:
        G = IcmGlobalContext()
        #     icmRunArgs = G.icmRunArgsGet()
        #     icmInBase = icmRunArgs.cmndArgs[0]
        # else:
        #     if not icmInBase:
        #         EH_problem_usageError("")
        #         return

        print("* ICM Specified Parameters")

        icmParams = G.icmParamDictGet()

        for key, icmParam in icmParams.parDictGet().items():
            if ( icmParam.argsparseShortOptGet() == None )  and ( icmParam.argsparseLongOptGet() == None ):
                break

            print("** " + key)
            print("*** " + str(icmParam))

        print("* ICM Common Parameters")

        icmParams = commonIcmParamsPrep()

        for key, icmParam in icmParams.parDictGet().items():
            if ( icmParam.argsparseShortOptGet() == None )  and ( icmParam.argsparseLongOptGet() == None ):
                break

            print("** " + key)
            print("*** " + str(icmParam))

        print("* ICM Mains Methods")

        mainsMethods = cmndList_mainsMethods().cmnd(interactive=False)
        for each in mainsMethods:
            cmndInfo().cmnd(
                interactive=True,
                orgLevel=2,
                cmndName=each,
            )

        print("* ICM Libs Methods")

        libsMethods = cmndList_libsMethods().cmnd(interactive=False)
        for each in libsMethods:
            cmndInfo().cmnd(
                interactive=True,
                orgLevel=2,
                cmndName=each,
            )

        return



"""
####+BEGINNOT: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/topControls.org"
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || FrmWrk-CMND       ::  version    [[elisp:(org-cycle)][| ]]
*       [[elisp:(org-cycle)][| *Version:* | ]]
####+END:
"""
class version(cs.Cmnd):
    """ICM version number."""

    cmndArgsLen={'Min': 0, 'Max':0,}

    #@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,        # Can also be called non-interactively
    ):
        """Version number is obtained from."""
        if interactive:
            print(("* ICM-Version: {ver}".format(ver=str( __version__ ))))
            return
        else:
            return(format(str(__version__)))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  visit    [[elisp:(org-cycle)][| ]]
"""
class visit(cs.Cmnd):
    """Visit The ICM Module."""

    cmndArgsLen = {'Min': 0, 'Max':0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,        # Can also be called non-interactively
    ):
        """Use emacs client to visit the ICM module."""

        myName=self.myName()
        G = IcmGlobalContext()
        thisOutcome = OpOutcome(invokerName=myName)

        thisOutcome = subProc_bash(
            """emlVisit -v -n showRun -i gotoPanel {myFullName}"""
            .format(myFullName=G.icmMyFullName()),
            stdin=None, outcome=thisOutcome,
        ).out()

        if thisOutcome.isProblematic():
            return(EH_badOutcome(thisOutcome))

        return thisOutcome


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndInfo    [[elisp:(org-cycle)][| ]]
"""
class cmndInfo(cs.Cmnd):
    """Returns a human oriented string for the specified cmndName's expected pars/args usage."""

    cmndArgsLen={'Min': 1, 'Max':1,}
    cmndArgsSpec = {1: ["cmndName"]}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
            cmndName=None,  # cmndArgs[0]
            orgLevel=2,
    ):
        """Used by ICM Players to inform user of a given cmndName capabilities."""

        myName=self.myName()
        G = IcmGlobalContext()
        thisOutcome = OpOutcome(invokerName=myName)

        if not cmndName:
            if not interactive:
                EH_problem_usageError("")
                return
            cmndName = G.icmRunArgsGet().cmndArgs[0]

        cmndClass = cmndNameToClass(cmndName)
        if not cmndClass: return

        outString = list()

        def orgIndentStr(subLevel): return "*" * (orgLevel + subLevel)

        outString.append("{baseOrgStr} {cmndName}\n".format(
            baseOrgStr=orgIndentStr(0),
            cmndName=cmndName,
        ))
        outString.append("{baseOrgStr} cmndShortDocStr={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndDocStrShort().cmnd(
                interactive=False,
                cmndName=cmndName,
        )))
        outString.append("{baseOrgStr} cmndFullDocStr={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndDocStrFull().cmnd(
                interactive=False,
                cmndName=cmndName,
        )))
        outString.append("{baseOrgStr} classDocStrOf={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=classDocStrOf().cmnd(
                interactive=False,
                argsList=[cmndName],
        )))
        outString.append("{baseOrgStr} cmndParamsMandatory={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().paramsMandatory(),
        ))
        outString.append("{baseOrgStr} cmndParamsOptional={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().paramsOptional(),
        ))
        outString.append("{baseOrgStr} cmndArgsLen={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().argsLen(),
        ))
        outString.append("{baseOrgStr} cmndArgsSpec={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().argsDesc(),
        ))
        outString.append("{baseOrgStr} cmndUsers={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().users(),
        ))
        outString.append("{baseOrgStr} cmndGroups={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().groups(),
        ))
        outString.append("{baseOrgStr} cmndImapct={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().impact(),
        ))
        outString.append("{baseOrgStr} cmndVisibility={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().visibility(),
        ))

        if interactive:
            # print adds an extra line at the end in Python 2.X
            sys.stdout.write("".join(outString))

        return thisOutcome.set(
            opError=OpError.Success,
            opResults="".join(outString)
        )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndInfoEssential    [[elisp:(org-cycle)][| ]]
"""
class cmndInfoEssential(cs.Cmnd):
    """Returns a human oriented string for the specified cmndName's expected pars/args usage."""
    cmndParamsMandatory = None
    cmndParamsOptional = None
    cmndArgsLen = ["1"]
    cmndArgsSpec = ["cmndName"]

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
            cmndName=None,  # cmndArgs[0]
            orgLevel=2,
    ):
        """Used by ICM Players to inform user of a given cmndName capabilities."""

        myName=self.myName()
        G = IcmGlobalContext()
        thisOutcome = OpOutcome(invokerName=myName)

        if not cmndName:
            if not interactive:
                EH_problem_usageError("")
                return
            cmndName = G.icmRunArgsGet().cmndArgs[0]

        cmndClass = cmndNameToClass(cmndName)
        if not cmndClass: return

        outString = list()

        def orgIndentStr(subLevel): return "*" * (orgLevel + subLevel)

        outString.append("{baseOrgStr} cmndFullDocStr={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndDocStrFull().cmnd(
                interactive=False,
                cmndName=cmndName,
        )))
        outString.append("{baseOrgStr} cmndParamsMandatory={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().paramsMandatory(),
        ))
        outString.append("{baseOrgStr} cmndParamsOptional={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().paramsOptional(),
        ))
        outString.append("{baseOrgStr} cmndArgsLen={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().argsLen(),
        ))
        outString.append("{baseOrgStr} cmndArgsSpec={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().argsDesc(),
        ))
        outString.append("{baseOrgStr} cmndUsers={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().users(),
        ))
        outString.append("{baseOrgStr} cmndGroups={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().groups(),
        ))
        outString.append("{baseOrgStr} cmndImapct={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().impact(),
        ))
        outString.append("{baseOrgStr} cmndVisibility={str}\n".format(
            baseOrgStr=orgIndentStr(1),
            str=cmndClass().visibility(),
        ))

        if interactive:
            # print adds an extra line at the end in Python 2.X
            sys.stdout.write("".join(outString))

        return thisOutcome.set(
            opError=OpError.Success,
            opResults="".join(outString)
        )



"""
*  [[elisp:(org-cycle)][| ]]  /cmndsList_/          :: *cmndsList_ -- List C-CMNDs and F-CMNDs in a given file and in icm library* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndList_allMethods    [[elisp:(org-cycle)][| ]]
"""
class cmndList_allMethods(cs.Cmnd):
    """List All Classed-CMNDs."""

    #Do Not Decorate with  @io.track.subjectToTracking
    def cmnd(self,
            interactive=True,
    ):
        """Is based on subclasses of Cmnd and which are in the main module.
When interactive is false, return the list and when true print it and return the list.
"""
        allClassedCmndNames = cmndSubclassesNames()

        if interactive:
            ucf.listPrintItems(allClassedCmndNames)

        return allClassedCmndNames


####+BEGIN: bx:icm:python:icmItem :itemType "Global" :itemTitle "mainsClassedCmndsGlobal = None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Global         :: mainsClassedCmndsGlobal = None  [[elisp:(org-cycle)][| ]]
"""
####+END:

mainsClassedCmndsGlobal = None

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndList_mainsMethods    [[elisp:(org-cycle)][| ]]
"""
class cmndList_mainsMethods(cs.Cmnd):
    """List All C-CMNDs of the Module."""

    #Do Not Decorate with  @io.track.subjectToTracking
    def cmnd(self,
             interactive=False,
             importedCmnds={},
             mainFileName=None,
             importedCmndsFilesList=[],
    ):
        """Is based on subclasses of Cmnd and which are in the main module.
When interactive is false, return the list and when true print it and return the list.

importedCmndsList was added later with icmMainProxy.
"""

        global mainsClassedCmndsGlobal

        allClassedCmndNames = cmndSubclassesNames()

        if not mainFileName:
            mainFileName = sys.argv[0]

        mainClasses = ucf.ast_topLevelClassNamesInFile(
            mainFileName,
        )

        #print mainClasses

        relevantClasses = mainClasses
        for key, modPath in importedCmnds.items():
            if modPath.endswith('.pyc') and os.path.exists(modPath[:-1]):
                modPath = modPath[:-1]
            relevantClasses += ucf.ast_topLevelClassNamesInFile(modPath)

        for modPath in importedCmndsFilesList:
            if modPath.endswith('.pyc') and os.path.exists(modPath[:-1]):
                modPath = modPath[:-1]
            relevantClasses += ucf.ast_topLevelClassNamesInFile(modPath)

        mainsClassedCmnds = set.intersection(
            set(allClassedCmndNames),
            set(relevantClasses),
        )

        if interactive:
            ucf.listPrintItems(mainsClassedCmnds)

        mainsClassedCmndsGlobal = mainsClassedCmnds

        return mainsClassedCmnds

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndList_libsMethods    [[elisp:(org-cycle)][| ]]
"""
class cmndList_libsMethods(cs.Cmnd):
    """List All NAMES of C-CMNDs of the Libs Module."""

    #@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
    ):
        """Is based on subclasses of Cmnd and which are in the main module.
When interactive is false, return the list and when true print it.
"""

        global mainsClassedCmndsGlobal

        allClassedCmndNames = cmndSubclassesNames()

        #mainClasses = ucf.ast_topLevelClassNamesInFile(
        #    sys.argv[0]
        #)

        #ANN_here(allClassedCmndNames)
        #print mainClasses
        #libsClassedCmnds = set(allClassedCmndNames) - set(mainClasses)
        libsClassedCmnds = set(allClassedCmndNames) - set(mainsClassedCmndsGlobal)

        if interactive:
            ucf.listPrintItems(libsClassedCmnds)

        return libsClassedCmnds

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndClassDocStr    [[elisp:(org-cycle)][| ]]
"""
class cmndClassDocStr(cs.Cmnd):
    """Given a list of cmnds as Args, for each return the the class docStr."""
    cmndParamsMandatory = None
    cmndParamsOptional = None
    cmndArgsLen = ["1"]

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
            cmndName=None,
    ):
        """The Cmnd class from which this is drived, includes docStr extractors.\
"""
        G = IcmGlobalContext()
        if not cmndName:
            if not interactive:
                EH_problem_usageError("")
                return None
            cmndName = G.icmRunArgsGet().cmndArgs[0]

        cmndClass = cmndNameToClass(cmndName)
        if not cmndClass: return None

        docStr = cmndClass().docStrClass()

        if interactive: print(docStr)

        return docStr

####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "lib" :cmndName "cmndHelp" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /cmndHelp/ parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class cmndHelp(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=None,         # or Args-Input
    ):
        G = IcmGlobalContext()
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        cmndName = effectiveArgsList[0]

        cmndClass = cmndNameToClass(cmndName)
        if not cmndClass: return None

        docStr = cmndClass().cmndDocStr()

        if interactive: print(docStr)
        return docStr


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "lib" :cmndName "null" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /null/ parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class null(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):

        G = IcmGlobalContext()
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        return cmndOutcome

    def cmndDesc(): """
** A command that does nothing. The null Command. -- Can be combined with --load.
    When used with --load it can result in execution of loaded extensions.
"""


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndFuncDocStr    [[elisp:(org-cycle)][| ]]
"""
class cmndMethodDocStr(cs.Cmnd):
    """Given a list of cmnds as Args, for each return the cmnd() funcs docStr."""
    cmndParamsMandatory = None
    cmndParamsOptional = None
    cmndArgsLen = ["1"]

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
            cmndName=None,
    ):
        """The Cmnd class from which this is drived, includes docStr extractors.\
"""
        G = IcmGlobalContext()
        if not cmndName:
            if not interactive:
                EH_problem_usageError("")
                return
            cmndName = G.icmRunArgsGet().cmndArgs[0]

        cmndClass = cmndNameToClass(cmndName)
        if not cmndClass: return

        docStr = cmndClass().docStrCmndMethod()

        if interactive:
            print(docStr)

        return docStr


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndDocStrShort    [[elisp:(org-cycle)][| ]]
"""
class cmndDocStrShort(cs.Cmnd):
    """Given a list of cmnds as Args, for each return the the class docStr."""
    cmndParamsMandatory = None
    cmndParamsOptional = None
    cmndArgsLen = ["1"]

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
            cmndName=None,
    ):
        """The Cmnd class from which this is drived, includes docStr extractors.\
"""
        classDocStr = cmndClassDocStr().cmnd(
                interactive=False,
                cmndName=cmndName,
        )
        if not classDocStr: return None

        shortDocStr = ucf.STR_getFirstLine(classDocStr)

        if interactive: print(shortDocStr)
        return shortDocStr

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndDocStrLong    [[elisp:(org-cycle)][| ]]
"""
class cmndDocStrFull(cs.Cmnd):
    """Given a list of cmnds as Args, for each return the cmnd() funcs docStr."""
    cmndParamsMandatory = None
    cmndParamsOptional = None
    cmndArgsLen = ["1"]

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=False,
            cmndName=None,
    ):
        """The Cmnd class from which this is drived, includes docStr extractors.\
"""
        classDocStr = cmndClassDocStr().cmnd(
                interactive=False,
                cmndName=cmndName,
        )
        if not classDocStr: return None

        methodDocStr = cmndMethodDocStr().cmnd(
                interactive=False,
                cmndName=cmndName,
        )
        if not methodDocStr: return None

        longDocStr = classDocStr + "\n" + methodDocStr

        if interactive: print(longDocStr)
        return longDocStr


#
# NOTYET. Added on 12/16/2021.

####+BEGINNOT: bx:icm:python:cmnd:classHead :cmndName "classDocStrOf" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /classDocStrOf/ parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class classDocStrOf(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        if self.docStrClassSet("""\
** fullUpdate docString is here."""
                               ): return cmndOutcome

        #thisCmnd = fullUpdate()
        thisCmnd = eval(f"__main__.{effectiveArgsList[0]}()")
        thisCmnd.obtainDocStrSet()
        thisCmnd.cmnd()
        return f"{thisCmnd.docStrClass()}"


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
