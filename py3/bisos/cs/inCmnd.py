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

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:
####
####+BEGIN: bx:icm:py3:section :title "/Player Support/      :: *Framework cmnds That are expected by the ICM-Player*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] */Player Support/      :: *Framework cmnds That are expected by the ICM-Player**  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "icmLanguage" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<icmLanguage>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class icmLanguage(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns python. Part of icm framework.
        #+end_org """)

        if interactive:
            print("python")

        return cmndOutcome.set(
            opError=bpf.op.OpError.Success,
            opResults="python"
        )

    ####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "icmCmndPartIncludes" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
    """ #+begin_org
    *  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<icmCmndPartIncludes>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
    #+end_org """
    class icmCmndPartIncludes(cs.Cmnd):
        cmndParamsMandatory = [ ]
        cmndParamsOptional = [ ]
        cmndArgsLen = {'Min': 0, 'Max': 0,}

        @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
        def cmnd(self,
            interactive=False,        # Can also be called non-interactively
        ) -> bpf.op.Outcome:
            cmndOutcome = self.getOpOutcome()
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

    ####+END:
            self.cmndDocStr(f""" #+begin_org
    ** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  NOTYET Returns True. Part of icm framework
            #+end_org """)

            return(cmndOutcome)

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "icmInUpdate" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<icmInUpdate>> parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class icmInUpdate(cs.Cmnd):
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
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Given a baseDir, update icmIn. "Part of icm framework.
        #+end_org """)

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

        return(cmndOutcome)

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "csInfoCmnd" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<csInfoCmnd>> parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class csInfoCmnd(cs.Cmnd):
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
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Given a baseDir, update icmIn. Part of icm framework.
        #+end_org """)

        # if interactive:
        G = cs.IcmGlobalContext()
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

        return(cmndOutcome)

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "version" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<version>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class version(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  ICM version number.
        #+end_org """)

        """Version number is obtained from."""
        if interactive:
            print(("* ICM-Version: {ver}".format(ver=str( __version__ ))))
            return
        else:
            return(format(str(__version__)))

        return(cmndOutcome)

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "visit" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<visit>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class visit(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Visit The ICM Module. Use emacs client to visit the ICM module.
        #+end_org """)


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

        return(cmndOutcome)

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndInfo" :comment "" :parsMand "orgLevel" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndInfo>> parsMand=orgLevel parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndInfo(cs.Cmnd):
    cmndParamsMandatory = [ 'orgLevel', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        orgLevel=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'orgLevel': orgLevel, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        orgLevel = callParamsDict['orgLevel']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns a human oriented string for the specified cmndName's expected pars/args usage.
        Used by ICM Players to inform user of a given cmndName capabilities.
        #+end_org """)

        cmndName=None,  # cmndArgs[0]
        orgLevel=2,


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

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndInfoEssential" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndInfoEssential>> parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndInfoEssential(cs.Cmnd):
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
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns a human oriented string for the specified cmndName's expected pars/args usage.
        Used by ICM Players to inform user of a given cmndName capabilities.
        #+end_org """)

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

####+BEGIN: bx:icm:py3:section :title "cmndsList -- List C-CMNDs and F-CMNDs in a given file and in icm librarytitle"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *cmndsList -- List C-CMNDs and F-CMNDs in a given file and in icm librarytitle*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndList_allMethods" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndList_allMethods>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndList_allMethods(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  List All Classed-CMNDs.
        Is based on subclasses of Cmnd and which are in the main module.
When interactive is false, return the list and when true print it and return the list.
        #+end_org """)

        allClassedCmndNames = cs.cmndSubclassesNames()

        if interactive:
            ucf.listPrintItems(allClassedCmndNames)

        return allClassedCmndNames


####+BEGIN: bx:icm:python:icmItem :itemType "Global" :itemTitle "GLOBAL Declaration Of mainsClassedCmndsGlobal = None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Global         :: mainsClassedCmndsGlobal = None  [[elisp:(org-cycle)][| ]]
"""
####+END:

mainsClassedCmndsGlobal = None

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndList_mainsMethods" :comment "USED IN MAIN" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "importedCmnds mainFileName importedCmndsFilesList" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndList_mainsMethods>> =USED IN MAIN= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc=importedCmnds mainFileName importedCmndsFilesList interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndList_mainsMethods(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        importedCmnds=None,         # asFunc when interactive==False
        mainFileName=None,         # asFunc when interactive==False
        importedCmndsFilesList=None,         # asFunc when interactive==False
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        """USED IN MAIN"""
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Is based on subclasses of Cmnd and which are in the main module.
When interactive is false, return the list and when true print it and return the list.

importedCmndsList was added later with icmMainProxy.
*** TODO Should return through cmndOutcome
        #+end_org """)

        global mainsClassedCmndsGlobal

        allClassedCmndNames = cs.cmndSubclassesNames()

        if not mainFileName:
            mainFileName = sys.argv[0]

        mainClasses = bpf.ast.ast_topLevelClassNamesInFile(
            mainFileName,
        )

        #print mainClasses

        relevantClasses = mainClasses
        for key, modPath in importedCmnds.items():
            if modPath.endswith('.pyc') and os.path.exists(modPath[:-1]):
                modPath = modPath[:-1]
            relevantClasses += bpf.ast.ast_topLevelClassNamesInFile(modPath)

        for modPath in importedCmndsFilesList:
            if modPath.endswith('.pyc') and os.path.exists(modPath[:-1]):
                modPath = modPath[:-1]
            relevantClasses += bpf.ast.ast_topLevelClassNamesInFile(modPath)

        mainsClassedCmnds = set.intersection(
            set(allClassedCmndNames),
            set(relevantClasses),
        )

        if interactive:
            bpf.ast.listPrintItems(mainsClassedCmnds)

        mainsClassedCmndsGlobal = mainsClassedCmnds

        return mainsClassedCmnds

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndList_libsMethods" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndList_libsMethods>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndList_libsMethods(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  List All NAMES of C-CMNDs of the Libs Module.
        When interactive is false, return the list and when true print it.

        #+end_org """)


        global mainsClassedCmndsGlobal

        allClassedCmndNames = cs.cmndSubclassesNames()

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

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndClassDocStr" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "1" :asFunc "cmndName" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndClassDocStr>> parsMand= parsOpt= argsMin=0 argsMax=1 asFunc=cmndName interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndClassDocStr(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
        cmndName=None,         # asFunc when interactive==False
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Given a list of cmnds as Args, for each return the the class docStr.
        The Cmnd class from which this is drived, includes docStr extractors.
        #+end_org """)

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

####+BEGIN: bx:cs:py3:cmnd:classHead :modPrefix "" :cmndName "cmndHelp" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndHelp>> parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndHelp(cs.Cmnd):
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
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
        #+end_org """)

        cmndName = effectiveArgsList[0]

        cmndClass = cmndNameToClass(cmndName)
        if not cmndClass: return None

        docStr = cmndClass().cmndDocStr()

        if interactive: print(docStr)
        return docStr


####+BEGIN: bx:cs:py3:cmnd:classHead :modPrefix "" :cmndName "null" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<null>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class null(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] A command that does nothing. The null Command. -- Can be combined with --load.
    When used with --load it can result in execution of loaded extensions.
        #+end_org """)

        return cmndOutcome

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndMethodDocStr" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndMethodDocStr>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndMethodDocStr(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  "Given a list of cmnds as Args, for each return the cmnd() funcs docStr.
        The Cmnd class from which this is drived, includes docStr extractors.
        #+end_org """)

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

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndDocStrShort" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndDocStrShort>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndDocStrShort(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Given a list of cmnds as Args, for each return the the class docStr.
        The Cmnd class from which this is drived, includes docStr extractors.
        #+end_org """)

        classDocStr = cmndClassDocStr().cmnd(
                interactive=False,
                cmndName=cmndName,
        )
        if not classDocStr: return None

        shortDocStr = ucf.STR_getFirstLine(classDocStr)

        if interactive: print(shortDocStr)
        return shortDocStr

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "cmndDocStrFull" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "cmndName" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<cmndDocStrFull>> parsMand= parsOpt= argsMin=0 argsMax=0 asFunc=cmndName interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndDocStrFull(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        cmndName=None,         # asFunc when interactive==False
    ) -> bpf.op.Outcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Given a list of cmnds as Args, for each return the cmnd() funcs docStr.
        The Cmnd class from which this is drived, includes docStr extractors.
        #+end_org """)

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

####+BEGIN: bx:cs:py3:cmnd:classHead :cmndName "classDocStrOf" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<classDocStrOf>> parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
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
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  fullUpdate docString is here.
        #+end_org """)

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
