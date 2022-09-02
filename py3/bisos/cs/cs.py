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
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['cs'], }
icmInfo['version'] = '202208264142'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'cs-Panel.org'
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

#from blee.icmPlayer import bleep
####+END:

import __main__

#import types


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


from bisos import cs

from bisos import io
from bisos import bpf

#from bisos.cs import param
#from bisos.cs import arg
from bisos.cs import runArgs

from datetime import datetime
import time

import argparse

# from bisos.bpo import bpo
#from bisos.pals import palsSis
#from bisos.icm import fpath

# from bisos import bpf

# import gnupg

#import logging

import abc

#import shutil

# import pykeepass_cache
# import pykeepass
#

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Cmnd Abstract Class" :anchor ""  :extraInfo "An Expectation Complete Operation"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Cmnd Abstract Class_: |]]  An Expectation Complete Operation  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

G = cs.globalContext.get()


####+BEGIN: bx:dblock:python:class :className "Cmnd" :classType "abs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-abs    [[elisp:(outline-show-subtree+toggle)][||]] /Cmnd/ object  [[elisp:(org-cycle)][| ]]
#+end_org """
class Cmnd(object):
####+END:
    """
** Root class of an ICM's Cmnd.
"""
    cmndParamsMandatory = list()  # ['inFile']
    cmndParamsOptional = list()   # ['perhaps']
    cmndArgsLen = {'Min': 0, 'Max':0,}
    cmndArgsSpecObsoltedByMethod = dict()  # {1: []}

    cmndVisibility = ["all"]  # users, developers, internal
    cmndUsers = []            # lsipusr
    cmndGroups = []           # bystar
    cmndImpact = []           # read, modify

    def __init__(self,
                 cmndLineInputOverRide=None,
                 cmndOutcome = None,
    ):
        self.cmndLineInputOverRide = cmndLineInputOverRide
        self.cmndOutcome = cmndOutcome
        self.obtainDocStr = False

    def docStrClass(self,):
        return self.__class__.__doc__

    def docStrCmndMethod(self,):
        return self.cmnd.__doc__

    def cmndDocStr(self, inStr):
        if self.cmnd.__doc__:
            self.cmnd.__func__.__doc__ = f"""{self.cmnd.__doc__}\n{inStr}"""
        else:
            self.cmnd.__func__.__doc__ = inStr

    def docStrClassSet(self, docStr):
        """attribute '__doc__' of 'method' objects is not writable, so we use class."""
        self.__class__.__doc__ = docStr
        return self.obtainDocStr

    def obtainDocStrSet(self):
        self.obtainDocStr = True

    def docStrCmndDesc(self,):
        return self.cmnd.cmndDesc.__doc__

    def paramsMandatory(self,):
        return self.__class__.cmndParamsMandatory

    def paramsOptional(self,):
        return self.__class__.cmndParamsOptional

    def argsLen(self,):
        return self.__class__.cmndArgsLen

    def argsDesc(self,):
        return self.__class__.cmndArgsSpecObsoltedByMethod

    def users(self,):
        return self.__class__.cmndUsers

    def groups(self,):
        return self.__class__.cmndGroups

    def impact(self,):
        return self.__class__.cmndImpact

    def visibility(self,):
        return self.__class__.cmndVisibility

    def getOpOutcome(self):
        if self.cmndOutcome:
            return self.cmndOutcome
        self.cmndOutcome = bpf.op.Outcome(invokerName=self.myName())
        return self.cmndOutcome
        #return OpOutcome(invokerName=self.myName())

    def cmndLineValidate(
            self,
            outcome,
    ):
        if self.cmndLineInputOverRide:
            return True

        errorStr = self.cmndArgsLenValidate()
        if errorStr:
            outcome.error = bpf.op.OpError.CmndLineUsageError
            outcome.errInfo = errorStr
            return False
        errorStr = self.cmndParamsMandatoryValidate()
        if errorStr:
            outcome.error = bpf.op.OpError.CmndLineUsageError
            outcome.errInfo = errorStr
            return False
        errorStr = self.cmndParamsOptionalValidate()
        if errorStr:
            outcome.error = bpf.op.OpError.CmndLineUsageError
            outcome.errInfo = errorStr
            return False
        return True

    def cmndArgsLenValidate(self,
    ):
        """ If not as expected, return an error string, otherwise, None.

    expectedCmndArgsLen is a dcitionary with 'Min' and 'Max' range.
    """
        G = cs.globalContext.get()
        cmndArgsLen = len(G.icmRunArgsGet().cmndArgs)
        expectedCmndArgsLen = self.__class__.cmndArgsLen

        def errStr():
            errorStr = "Bad Number Of cmndArgs: cmndArgs={cmndArgs} --".format(cmndArgs=cmndArgsLen)
            if expectedCmndArgsLen['Min'] == expectedCmndArgsLen['Max']:
                errorStr = errorStr + "Expected {nu}".format(nu=expectedCmndArgsLen['Min'])
            else:
                errorStr = errorStr + "Expected between {min} and {max}".format(
                    min=expectedCmndArgsLen['Min'],
                    max=expectedCmndArgsLen['Max']
                )
            return errorStr

        if cmndArgsLen < expectedCmndArgsLen['Min']:
            retVal = errStr()
        elif cmndArgsLen > expectedCmndArgsLen['Max']:
            retVal = errStr()
        else:
            retVal = None

        #parser=argparse.ArgumentParser()
        #parser.print_help()

        return(retVal)

    def cmndParamsMandatoryValidate(self,
    ):
        """If not as expected, return an error string, otherwise, None.

    expectedCmndArgsLen is a dcitionary with 'Min' and 'Max' range.
    """

        G = cs.globalContext.get()
        icmRunArgs = G.icmRunArgsGet()
        icmRunArgsDict = vars(icmRunArgs)

        cmndParamsMandatory = self.__class__.cmndParamsMandatory

        for each in cmndParamsMandatory:
            if each in list(icmRunArgsDict.keys()):
                continue
            else:
                return "Unexpected Mandatory Param: param={param} --".format(param=each)

        for each in cmndParamsMandatory:
            if icmRunArgsDict[each] == None:
                return "Missing Mandatory Param: param={param} --".format(param=each)
            else:
                continue

        for each in cmndParamsMandatory:
            exec(
                "G.usageParams.{paramName} = icmRunArgs.{paramName}"
                .format(paramName=each)
            )
        return None

    def cmndParamsOptionalValidate(self,
    ):
        """If not as expected, return an error string, otherwise, None.

    expectedCmndArgsLen is a dcitionary with 'Min' and 'Max' range.
    """
        G = cs.globalContext.get()
        icmRunArgs = G.icmRunArgsGet()
        icmRunArgsDict = vars(icmRunArgs)

        cmndParamsOptional = self.__class__.cmndParamsOptional

        for each in cmndParamsOptional:
            if each in list(icmRunArgsDict.keys()):
                continue
            else:
                return "Unexpected Optional Param: param={param} --".format(param=each)

        for each in cmndParamsOptional:
            #if icmRunArgsDict[each] != None:
            exec(
                "G.usageParams.{paramName} = icmRunArgs.{paramName}"
                .format(paramName=each)
            )
        return None

    def cmndMyName(self):
        return self.__class__.__name__

    def myName(self):
        return self.cmndMyName()

    @abc.abstractmethod
    def cmnd(self, interactive=False):
        print("This is default Cmnd Class Definition -- It is expected to be overwritten. You should never see this.")


    def cmndArgsSpec(self):
        # This is default Cmnd Class Definition -- It is expected to be overwritten. You should never see this."
        return None

    def cmndArgsGet(
            self,
            argPosition,
            cmndArgsSpecDict,
            effectiveArgsList,
    ) -> typing.Optional[list]:

        def argDefaultGet(
                cmndArgsSpecDict,
                argPosition,
        ):
            if cmndArgsSpecDict:
                cmndArgsSpec = cmndArgsSpecDict.argPositionFind(argPosition)
                return cmndArgsSpec.argDefaultGet()
            else:
                return ""

        min, max = cs.arg.cmndArgPositionToMinAndMax(argPosition)

        if min == None:
            return None

        if min == max:
            # We are returning a string as value
            if len(effectiveArgsList) >= (min + 1):
                return effectiveArgsList[min]
            else:
                return argDefaultGet(cmndArgsSpecDict, argPosition)

        elif max == -1:
            argsList = list()
            if len(effectiveArgsList) >= (min + 1):
                for count in range(0, min):
                    effectiveArgsList.pop(count)
                return effectiveArgsList
            else:
                defaultArg = argDefaultGet(cmndArgsSpecDict, argPosition)
                if defaultArg:
                    argsList.append(
                        argDefaultGet(cmndArgsSpecDict, argPosition)
                    )
                return argsList

        else:
            argsList = list()
            if len(effectiveArgsList) >= (min + 1):
                for count in range(min, max):
                    if len(effectiveArgsList) > count:
                        argsList.append(effectiveArgsList[count])
            else:
                defaultArg = argDefaultGet(cmndArgsSpecDict, argPosition)
                if defaultArg:
                    argsList.append(
                        argDefaultGet(cmndArgsSpecDict, argPosition)
                    )
            return argsList


    def cmndArgsValidate(
            self,
            effectiveArgsList,
            cmndArgsSpecDict,
            outcome=None,
    ):
        """
** TODO Place Holder -- Should validate argsList to confirm that it is consistent with cmndArgsSpec
"""
        if not cmndArgsSpecDict:
            return True

        retVal = True

        def reportInvalidCmndLineArgValue(
            cmndLineArgValue,
            argChoices,
        ):
            print("cmndLineArgValue={cmndLineArgValue} is not in {argChoices}".format(
                cmndLineArgValue=cmndLineArgValue, argChoices=argChoices,
            ))
            return False

        cmndArgsSpecDictDict = cmndArgsSpecDict.argDictGet()
        for argPosition, cmndArgSpec in cmndArgsSpecDictDict.items():
            argChoices = cmndArgSpec.argChoicesGet()

            if not argChoices:
                continue

            if argChoices == "any":
                continue

            min, max = cs.arg.cmndArgPositionToMinAndMax(argPosition)

            if min == None:
                # EH_problem()
                return None

            if min == max:
                # There is just one value
                if len(effectiveArgsList) >= (min + 1):
                    cmndLineArgValue =  effectiveArgsList[min]

                    if not cmndLineArgValue in argChoices:
                        retVal = reportInvalidCmndLineArgValue(
                            cmndLineArgValue,
                            argChoices,
                        )

            elif max == -1:
                if len(effectiveArgsList) >= (min + 1):
                    for count in range(0, min):
                        effectiveArgsList.pop(count)
                        for cmndLineArgValue in effectiveArgsList:
                            if not cmndLineArgValue in argChoices:
                                retVal = reportInvalidCmndLineArgValue(
                                    cmndLineArgValue,
                                    argChoices,
                                )

            else:
                for count in range(min, max):
                    if len(effectiveArgsList) >= (count + 1):
                        cmndLineArgValue = effectiveArgsList[count]
                        if not cmndLineArgValue in argChoices:
                            retVal = reportInvalidCmndLineArgValue(
                                cmndLineArgValue,
                                argChoices,
                            )

        return retVal

    def cmndCallTimeKwArgs(self,):
        """
** All value full icmpParams are then written off as file params.
        """
        G = cs.globalContext.get()
        icmRunArgs = G.icmRunArgsGet()

        applicableCmndKwArgs = dict()

        g_parDict = G.icmParamDictGet().parDictGet()

        for each in self.cmndParamsMandatory:
            try:
                eachIcmParam = g_parDict[each]
            except  KeyError:
                print(f"BadUsage: Missing parameter definition: {each}")
                return
            else:
                if not icmRunArgs.__dict__[each]:
                    print(f"BadUsage: Missing mandatory parameter zz: {each}")
                    return
                applicableCmndKwArgs.update({each: icmRunArgs.__dict__[each]})
                continue

        for each in self.cmndParamsOptional:
            try:
                eachIcmParam = g_parDict[each]
            except  KeyError:
                # That is okay. An optionale param was not specified.
                continue
            else:
                applicableCmndKwArgs.update({each: icmRunArgs.__dict__[each]})
                continue

        if icmRunArgs.cmndArgs:
            applicableCmndKwArgs.update({'argsList': icmRunArgs.cmndArgs})

        # print(f"YYY == {applicableCmndKwArgs}")
        return applicableCmndKwArgs

    def invModel(self,
            baseDir,
    ):
        """
** Writes out all inputs of the command as file parameters.
** Can be invoked from cmnd-line with --insAsFPs=basePath instead of cmnd().
** Returns an outcome.
** cmndParamsMandatory and optionals are walked through in icmRunArgs.
** Their values are then set in icmParam.
** All value full icmpParams are then written off as file params.
        """
        G = cs.globalContext.get()
        icmRunArgs = G.icmRunArgsGet()

        # print(f"cmndParamsMandatory={self.cmndParamsMandatory}")
        # print(f"cmndParamsOptional={self.cmndParamsOptional}")

        if not pathlib.Path(baseDir).is_dir():
            print(f"BadUsage: Missing {baseDir}")
            return

        #print(icmRunArgs)

        applicableIcmParams = ICM_ParamDict()

        def absorbApplicableIcmParam(icmParam, each):
            # print(f"4444 {each} {icmRunArgs.__dict__[each]}")
            icmParam.parValueSet(icmRunArgs.__dict__[each])
            applicableIcmParams.parDictAppend(eachIcmParam)

        g_parDict = IcmGlobalContext().icmParamDictGet().parDictGet()

        # print(g_parDict)

        for each in self.cmndParamsMandatory:
            try:
                eachIcmParam = g_parDict[each]
            except  KeyError:
                print(f"BadUsage: Missing parameter definition: {each}")
                return
            else:
                if not icmRunArgs.__dict__[each]:
                    print(f"BadUsage: Missing mandatory parameter: {each}")
                    return
                absorbApplicableIcmParam(eachIcmParam, each,)
                # applicableIcmParams.parDictAppend(eachIcmParam)
                continue

        for each in self.cmndParamsOptional:
            try:
                eachIcmParam = g_parDict[each]
            except  KeyError:
                # That is okay. An optionale param was not specified.
                continue
            else:
                absorbApplicableIcmParam(eachIcmParam, each,)
                continue

        cmndParamsBase = pathlib.Path(baseDir).joinpath('cmndPars')
        cmndParamsBase.mkdir(parents=True, exist_ok=True)

        icmParamsToFileParamsUpdate(
            parRoot=cmndParamsBase,
            icmParams=applicableIcmParams,
        )

        FILE_ParamWriteToPath(
            parNameFullPath=pathlib.Path(baseDir).joinpath('icmName'),
            parValue=G.icmMyName()
        )

        FILE_ParamWriteToPath(
            parNameFullPath=pathlib.Path(baseDir).joinpath('cmndName'),
            parValue=G.icmRunArgsGet().invokes[0]
        )

        print(applicableIcmParams)

        outcome = OpOutcome()
        return outcome

        # icmParam = g_parDict['bpoId']

        # icmParam.parValueSet("ZZZZHHHHLLLL")

        # for each in icmRunArgs.__dict__:
        #     print(each)
        #     if icmRunArgs.__dict__[each]:
        #         print(f"JJMM --- {each}")
        #         print(f"kkjj -- {icmRunArgs.__dict__[each]}")

        #         # g_param = g_parDict[each]

        # for key, icmParam in IcmGlobalContext().icmParamDictGet().parDictGet().items():
        #     if ( icmParam.argsparseShortOptGet() == None )  and ( icmParam.argsparseLongOptGet() == None ):
        #         break
        #     print(f"JJ {key} LL {icmParam}")

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CS Output" :anchor ""  :extraInfo "Perhaps It Belongs In The IO Package"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CS Output_: |]]  Perhaps It Belongs In The IO Package  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:cs:py3:func :funcName "icmOutputBaseGet" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /icmOutputBaseGet/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmOutputBaseGet(
####+END:
) -> str:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """
    return "./"

####+BEGIN: bx:cs:py3:func :funcName "icmOutputXlsGetPath" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /icmOutputXlsGetPath/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmOutputXlsGetPath(
####+END:
        fileBaseName,
) -> str:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """
    ts = time.time()
    st = datetime.fromtimestamp(ts).strftime('%y%m%d%H%M%S')
    fileName = fileBaseName + st + ".xlsx"
    return os.path.join(icmOutputBaseGet(), fileName)


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CS Types Enumeration" :anchor ""  :extraInfo "Needs to be revisited"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CS Types Enumeration_: |]]  Needs to be revisited  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:dblock:python:enum :enumName "ICM_GroupingType" :comment ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Enum       [[elisp:(outline-show-subtree+toggle)][||]] /ICM_GroupingType/  [[elisp:(org-cycle)][| ]]
#+end_org """
@enum.unique
class ICM_GroupingType(enum.Enum):
####+END:
    Pkged = 'Pkged'
    Grouped= 'Grouped'
    Scattered = 'Scattered'
    Unitary = 'Unitary'
    Standalone = 'Standalone'
    Other = 'Other'
    UnSet = 'UnSet'

####+BEGIN: bx:dblock:python:enum :enumName "ICM_PkgedModel" :comment ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Enum       [[elisp:(outline-show-subtree+toggle)][||]] /ICM_PkgedModel/  [[elisp:(org-cycle)][| ]]
#+end_org """
@enum.unique
class ICM_PkgedModel(enum.Enum):
####+END:
    BasicPkg = 'BasicPkg'
    ToicmPkg = 'ToicmPkg'
    EmpnaPkg = 'EmpnaPkg'
    UnSet = 'UnSet'

####+BEGIN: bx:dblock:python:enum :enumName "ICM_CmndParts" :comment ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Enum       [[elisp:(outline-show-subtree+toggle)][||]] /ICM_CmndParts/  [[elisp:(org-cycle)][| ]]
#+end_org """
@enum.unique
class ICM_CmndParts(enum.Enum):
####+END:
    Common = 'Common'
    Param = 'Param'
    Target = 'Target'
    Bxo = 'Bxo'
    Bxsrf = 'Bxsrf'
    UnSet = 'UnSet'

####+BEGIN: bx:dblock:python:enum :enumName "AuxInvokationContext" :comment ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Enum       [[elisp:(outline-show-subtree+toggle)][||]] /AuxInvokationContext/  [[elisp:(org-cycle)][| ]]
#+end_org """
@enum.unique
class AuxInvokationContext(enum.Enum):
####+END:
    UnSet = 'UnSet'
    IcmRole = 'IcmRole'
    CmndParamsAndArgs = 'CmndParamsAndArgs'
    DocString = 'DocString'

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "csuList" :anchor "" :extraInfo "Setup framework functions"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _csuList_: |]]  Setup framework functions  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END

####+BEGIN: bx:cs:py3:func :funcName "csuList_importedModules" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /csuList_importedModules/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def csuList_importedModules(
####+END:
         csuList: list,
) -> list:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Later we may do more.
    #+end_org """

    return csuList

####+BEGIN: bx:cs:py3:func :funcName "csuList_commonParamsSpecify" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /csuList_commonParamsSpecify/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def csuList_commonParamsSpecify(
####+END:
        csuList: list,
        csParams: list,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Walkthrough =csuList=, call module.commonParamsSpecify(=csParams=).
    #+end_org """

    for each in csuList:
        lastPart = each.split(".")[-1]
        #print(lastPart)
        module = sys.modules[each]
        if hasattr(module, "commonParamsSpecify"):
            parsSpecFunc = getattr(module, "commonParamsSpecify")
            parsSpecFunc(csParams)

    return


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Command Line Parsing With argparse" :anchor "" :extraInfo "just arg parse or more?"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Command Line Parsing With argparse_: |]]  just arg parse or more?  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END

####+BEGIN: bx:cs:py3:func :funcName "commonIcmParamsParser" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /commonIcmParamsParser/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def commonIcmParamsParser(
####+END:
        parser,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Module Common Command Line Parameters.
    #+end_org """

    icmParams = commonIcmParamsPrep()

    #argsparseBasedOnCsParams(parser, icmParams)
    argsparseBasedOnCsParams(icmParams)

    return

####+BEGIN: bx:cs:py3:func :funcName "argsCommonProc" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /argsCommonProc/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def argsCommonProc(
####+END:
        parser,
) -> None:
     """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Module Common Command Line Parameters.
     #+end_org """

     parser.add_argument(
         '-i',
         '--invokes',
         dest='invokes',
         action='append'
         )

     parser.add_argument(
         '-t',
         '--callTrackings',
         dest='callTrackings',
         action='append',
         choices=['invoke+', 'invoke-', 'monitor+', 'monitor-'],
         default=[]
         )

     parser.add_argument(
         '--runMode',
         dest='runMode',
         action='store',
         choices=['dryRun', 'fullRun', 'runDebug'],
         default='fullRun'
         )

     # NOTYET, delete this
     parser.add_argument(
         '--insAsFPs',
         dest='insAsFPs',
         metavar='ARG',
         action='store',
         default='None',
         help="Emit all inputs as FileParams At Specified Base",
         )

     parser.add_argument(
         '--csBase',
         dest='csBase',
         action='store',
         default='None',
         help="Command Services Base",
         )

     parser.add_argument(
         '--invModel',
         dest='invModel',
         action='store',
         default='None',
         help="Emit all inputs as FileParams At Specified Base",
         )

     parser.add_argument(
         '--perfModel',
         dest='perfModel',
         action='store',
         default='None',
         help="Emit all inputs as FileParams At Specified Base",
         )


     parser.add_argument(
         '-v',
         '--verbosity',
         dest='verbosityLevel',
         metavar='ARG',
         action='store',
         default=None,
         help='Adds a Console Logger for the level specified in the range 1..50'
         )

     parser.add_argument(
         '--logFile',
         dest='logFile',
         metavar='ARG',
         action='store',
         default=None,
         help='Specifies destination LogFile for this run'
         )

     parser.add_argument(
         '--logFileLevel',
         dest='logFileLevel',
         metavar='ARG',
         action='store',
         default=None,
         help=''
         )

     parser.add_argument(
         '--docstring',
         action='store_true',
         dest="docstring"
         )

     parser.add_argument(
         'cmndArgs',
     #dest='cmndArgs',   #
         metavar='CMND',
         nargs='*',
         action='store',
         help='Interactively Invokable Function Arguments'
         )

     parser.add_argument(
         '--load',
         dest='loadFiles',
         action='append',
         default=[]
         )

     return

####+BEGIN: bx:cs:py3:func :funcName "G_argsProc" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /G_argsProc/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def G_argsProc(
####+END:
        arguments,
        extraArgs,
):
     """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] ICM-ICM Argument Parser. extraArgs resides in the G_ module.
     #+end_org """

     parser = argparse.ArgumentParser(
         description=__doc__
         )

     G.icmArgsParser = parser

     argsCommonProc(parser)
     #commonIcmParamsPrep()

     if extraArgs:
        #extraArgs(parser)
        extraArgs()

     #
     # The logic below breaks multiple --invokes.
     # Perhaps a distinction between --invoke and --invokes is an answer.
     #
     # We are inserting "--" after -i cmnd
     # to get things like -i run pip install --verbose
     #
     #
     index = 0
     for each in arguments:
         if each == "-i":
             arguments.insert(index+2, "--")
             break
         if each == "--invokes":
             arguments.insert(index+2, "--")
             break
         index = index + 1

     args = parser.parse_args(arguments)

     return args, parser

####+BEGIN: bx:cs:py3:func :funcName "argsparseBasedOnCsParams" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /argsparseBasedOnCsParams/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def argsparseBasedOnCsParams(
####+END:
        #parser,
        icmParams,
) -> None:
     """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Convert icmParams to parser.
     #+end_org """

     parser = G.icmArgsParser

     for key, icmParam in icmParams.parDictGet().items():
         if ( icmParam.argsparseShortOptGet() == None )  and ( icmParam.argsparseLongOptGet() == None ):
             break

         if not icmParam.argsparseShortOptGet() == None:
             parser.add_argument(
                 icmParam.argsparseShortOptGet(),
                 icmParam.argsparseLongOptGet(),
                 dest = icmParam.parNameGet(),
                 nargs = icmParam.parNargsGet(),
                 action=icmParam.parActionGet(),
                 default = icmParam.parDefaultGet(),
                 help=icmParam.parDescriptionGet()
                 )
         else:
             parser.add_argument(
                icmParam.argsparseLongOptGet(),
                dest = icmParam.parNameGet(),
                nargs = icmParam.parNargsGet(),
                metavar = 'ARG',
                action=icmParam.parActionGet(),
                default = icmParam.parDefaultGet(),
                help=icmParam.parDescriptionGet()
                )

     # So that it can be processed later as well.
     G.icmParamDictSet(icmParams)

     return

####+BEGIN: bx:cs:py3:func :funcName "libUserInit" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /libUserInit/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def libUserInit(
####+END:
        icmLineOpts,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] For situations when icm lib is being used outside of an ICM -- in the context of any app.
    #+end_org """
    parser = argparse.ArgumentParser(
         description=__doc__
    )
    argsCommonProc(parser)

    args = parser.parse_args(icmLineOpts)
    logControler = io.log.Control()
    logControler.loggerSet(args)


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "G_main -- Invoked from ICM, calls invokesProc" :anchor "" :extraInfo ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _G_main -- Invoked from ICM, calls invokesProc_: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END

# DO NOT DECORATE THIS FUNCTION

####+BEGIN: bx:cs:py3:func :funcName "G_main" :comment "DO NOT DECORATE THIS FUNCTION" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /G_main/ =DO NOT DECORATE THIS FUNCTION= deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def G_main(
####+END:
        inArgv,
        G_examples,
        extraArgs,
        invokesProc,
        mainEntry=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] This is the main entry point for Python.Icm.Icm (InteractiveInvokationModules)
    #+end_org """

    #
    # The order is important here,
    # 1) Parse The Command Line -- 2) LOG_ usese the command line -- 3) G. setup
    #
    icmRunArgs, icmArgsParser = G_argsProc(inArgv, extraArgs)

    logControler = Control()
    logControler.loggerSet(icmRunArgs)

    logger = logControler.loggerGet()

    logger.info('Main Started: ' + ucf.stackFrameInfoGet(1) )

    G = cs.globalContext.get()
    G.globalContextSet( icmRunArgs=icmRunArgs )
    G.icmArgsParser = icmArgsParser

    icmRunArgs_loadFiles()

    if len( inArgv ) == 0:
        if G_examples:
            G_examples()
            return

    if icmRunArgs.invokes:
        invokesProc()
    else:
        if mainEntry:
            mainEntry()

    return 0

# DO NOT DECORATE THIS FUNCTION
#
####+BEGIN: bx:cs:py3:func :funcName "G_mainWithClass" :comment "DO NOT DECORATE THIS FUNCTION" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /G_mainWithClass/ =DO NOT DECORATE THIS FUNCTION= deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def G_mainWithClass(
####+END:
        inArgv,
        G_examples,
        extraArgs,
        classedCmndsDict,
        #funcedCmndsDict,
        mainEntry=None,
        g_icmPreCmnds=None,
        g_icmPostCmnds=None,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] This is the main entry point for Python.Icm.Icm (InteractiveInvokationModules)
    #+end_org """

    icmRunArgs, icmArgsParser = G_argsProc(inArgv, extraArgs)

    logControler = io.log.Control()
    logControler.loggerSet(icmRunArgs)

    logger = logControler.loggerGet()

    logger.info('Main Started: ' + bpf.ast.stackFrameInfoGet(1) )

    G = cs.globalContext.get()
    G.globalContextSet( icmRunArgs=icmRunArgs )
    G.icmArgsParser = icmArgsParser
    G.cmndMethodsDictSet(classedCmndsDict)
    #G.cmndFuncsDictSet(funcedCmndsDict)

    runArgs.loadFiles()

    if len( inArgv ) == 0:
        if G_examples:
            G_examples().cmnd()
            return

    if icmRunArgs.invokes:
        thisCmndName=icmRunArgs.invokes[0]

        if g_icmPreCmnds:
            g_icmPreCmnds()

        outcome = invokesProcAllClassed(
            classedCmndsDict,
            icmRunArgs
        )

        if g_icmPostCmnds:
            g_icmPostCmnds()


        if not outcome:
            return

        try:
            outcomeError = outcome.error
        except AttributeError:
            ANN_here("Consider returning an outcome. cmnd={cmnd}".format(cmnd=thisCmndName))
            return

        if outcomeError:
            if outcome.error != bpf.op.OpError.Success:
                if outcome.error == bpf.op.OpError.CmndLineUsageError:
                    sys.stderr.write(
                        "{myName}.{cmndName} Command Line Failed: Error={status} -- {errInfo}\n".
                        format(myName=G.icmMyName(),
                               cmndName=thisCmndName,
                               status=outcome.error,
                               errInfo=outcome.errInfo,
                    ))
                    print("------------------")
                    G.icmArgsParser.print_help()
                    print("------------------")
                    print("Run -i usage for more details.")
                else:
                    sys.stderr.write(
                        "{myName}.{cmndName} Failed: Error={status} -- {errInfo}\n".
                        format(myName=G.icmMyName(),
                               cmndName=thisCmndName,
                               status=outcome.error,
                               errInfo=outcome.errInfo,
                    ))
            else:
                #sys.stderr.write("{myName}.{cmndName} Completed Successfully: status={status}\n"
                logger.info(
                    "{myName}.{cmndName} Completed Successfully: status={status}".
                    format(myName=G.icmMyName(),
                           cmndName=thisCmndName,
                           status=outcome.error
                ))
        else:
            #sys.stderr.write("{myName}.{cmndName} Completed Successfully: status={status}\n"
            logger.info(
                "{myName}.{cmndName} Completed Successfully: status={status}".
                format(myName=G.icmMyName(),
                       cmndName=thisCmndName,
                       status=outcome.error
            ))
        return outcome.error
    else:
        if mainEntry:
            import types
            if type(mainEntry) is types.FunctionType:
                mainEntry()
            else:
                cmndKwArgs = mainEntry().cmndCallTimeKwArgs()
                cmndKwArgs.update({'interactive': True})
                outcome = mainEntry().cmnd(**cmndKwArgs)
                return outcome.error

    return 0

####+BEGIN: bx:cs:py3:func :funcName "invokesProcAllClassed" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /invokesProcAllClassed/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def invokesProcAllClassed(
####+END:
        classedCmndsDict,
        icmRunArgs,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Process all invokations applicable to all (classed+funced of mains+libs) CMNDs.
    #+end_org """

    G = cs.globalContext.get()
    icmRunArgs = G.icmRunArgsGet()

    def applyMethodBasedOnContext(
            classedCmnd,
    ):
        """ Chooses the method to apply Cmnd() to.
        """
        invModel = icmRunArgs.invModel  # This can be a "None" string but not a None
        csBase = icmRunArgs.csBase

        if invModel != "None":
            if csBase == "None":
                print(f"BadUsage: Missing csBase, invModel={invModel}")
                outcome = OpOutcome()
                outcome.error = OpError.CmndLineUsageError
                outcome.errInfo = f"BadUsage: Missing csBase, invModel={invModel}"
            else:
                outcome = classedCmnd().invModel(csBase)
        else:
            #
            # applicableIcmParams = classedCmnd().absorbApplicableIcmParam()
            # outcome = classedCmnd().cmnd(**applicableIcmParams)
            #
            cmndKwArgs = classedCmnd().cmndCallTimeKwArgs()
            cmndKwArgs.update({'interactive': True})
            outcome = classedCmnd().cmnd(**cmndKwArgs)
        return outcome

    for invoke in icmRunArgs.invokes:
        #print(f"Looking for {invoke}")
        #
        # First we try cmndList_mainsMethods()
        #
        try:
            classedCmnd = classedCmndsDict[invoke]
        except  KeyError:
            #print("TM_ Key Error")
            pass
        else:
            #print(f"Found {classedCmnd}")
            outcome = applyMethodBasedOnContext(classedCmnd)
            continue

        #
        # Next we try cmndList_libsMethods()
        #
        callDict = dict()
        for eachCmnd in cs.inCmnd.cmndList_libsMethods().cmnd(interactive=False):
            #print(f"looking at {eachCmnd}")
            try:
                callDict[eachCmnd] = eval("{eachCmnd}".format(eachCmnd=eachCmnd))
            except NameError:
                # print(("EH_problem -- Skipping-b eval({eachCmnd})".format(eachCmnd=eachCmnd)))
                continue

        try:
            classedCmnd = callDict[invoke]
        except  KeyError:
            pass
        else:
            outcome = applyMethodBasedOnContext(classedCmnd)
            continue

        #
        # We tried everything and could not find any
        #

        # BUG, NOTYET, EH_problem goes to -v 20
        io.eh.EH_problem_info("Invalid Action: {invoke}"
                        .format(invoke=invoke))

        print(("Invalid Action: {invoke}"
                        .format(invoke=invoke)))

        outcome = bpf.op.Outcome()
        outcome.error = bpf.op.OpError.CmndLineUsageError
        outcome.errInfo = "Invalid Action: {invoke}".format(invoke=invoke)

    perfModel = icmRunArgs.perfModel  # This can be a "None" string but not a None

    #     if insAsFP_baseDir != "None":
    if perfModel != "None":
        print("Capturing outcome")
        csBase = icmRunArgs.csBase
        if csBase == "None":
            print(f"Missing csBase")
        else:
            FILE_ParamWriteToPath(
                parNameFullPath=pathlib.Path(csBase).joinpath('result'),
                parValue=outcome.results
            )


    # Check for perfModel and capture outcome
    return(outcome)

####+BEGIN: bx:cs:py3:func :funcName "cmndNameToClass" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /cmndNameToClass/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndNameToClass(
####+END:
        cmndName: str,
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Given cmndName, return cmndClass.
    #+end_org """

    G = cs.globalContext.get()
    classedCmndsDict = G.cmndMethodsDict()

    try:
        classedCmnd = classedCmndsDict[cmndName]
    except  KeyError:
        #print "TM_"
        pass
    else:
        return classedCmnd

    try:
        cmndClass = eval("{cmndName}".format(cmndName=cmndName))
    except NameError:
        return None

    if cmndName in cmndSubclassesNames():
        return cmndClass
    else:
        return None




####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "cmndsList -- List C-CMNDs and F-CMNDs in a given file and in icm library" :anchor "" :extraInfo ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _cmndsList -- List C-CMNDs and F-CMNDs in a given file and in icm library_: |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END


####+BEGIN: bx:cs:py3:func :funcName "cmndSubclassesNames" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /cmndSubclassesNames/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndSubclassesNames(
####+END:
):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Not using generators by choice.
    #+end_org """

    # return [each.__name__ for each in Cmnd.__subclasses__()]
    cmndsNames = list()
    for eachClass in Cmnd.__subclasses__():
        cmndsNames.append(eachClass.__name__)
    return cmndsNames

####+BEGIN: bx:cs:py3:func :funcName "cmndMainsMethodsToFileParamsUpdate" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /cmndMainsMethodsToFileParamsUpdate/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndMainsMethodsToFileParamsUpdate(
####+END:
        parRoot: str,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """
    mainsCmndMethods = cmndList_mainsMethods().cmnd()
    for each in mainsCmndMethods:
        cmndToFileParamsUpdate(
            cmndName=each,
            parRoot=parRoot,
        )
    return


####+BEGIN: bx:cs:py3:func :funcName "cmndLibsMethodsToFileParamsUpdate" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /cmndLibsMethodsToFileParamsUpdate/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndLibsMethodsToFileParamsUpdate(
####+END:
        parRoot: str,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """
    libsCmndMethods = cmndList_libsMethods().cmnd()
    for each in libsCmndMethods:
        cmndToFileParamsUpdate(
            cmndName=each,
            parRoot=parRoot,
        )
    return

####+BEGIN: bx:cs:py3:func :funcName "evalStringInMain" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /evalStringInMain/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def evalStringInMain(
####+END:
        inStr: str,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Given inStr eval that string in __main__.
    #+end_org """
    LOG_here("Eval-ing: __main__.{}".format(inStr))
    # try
    eval("__main__.{}".format(inStr))


####+BEGIN: bx:cs:py3:func :funcName "cmndToFileParamsUpdate" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /cmndToFileParamsUpdate/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndToFileParamsUpdate(
####+END:
        cmndName,
        parRoot,
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Write cmnd as fileParam.
    #+end_org """

    absoluteParRoot = os.path.abspath(parRoot)

    if not os.path.isdir(absoluteParRoot):
        try: os.makedirs( absoluteParRoot, 0o775 )
        except OSError: pass

    parValue = "unSet"

    FILE_ParamWriteTo(
        parRoot=absoluteParRoot,
        parName=cmndName,
        parValue=parValue,
    )

    def writeCmndAttrFV(
            cmndName,
            attrName,
            attrValue,
    ):
        varValueFullPath = os.path.join(
            absoluteParRoot,
            cmndName,
            attrName,
        )
        FV_writeToFilePathAndCreate(
            filePath=varValueFullPath,
            varValue=attrValue,
        )


    docStr = cmndDocStrShort().cmnd(
        cmndName=cmndName,
    )
    writeCmndAttrFV(
        cmndName=cmndName,
        attrName='description',
        attrValue=docStr,
    )

    docStr = cmndDocStrFull().cmnd(
        cmndName=cmndName,
    )
    writeCmndAttrFV(
        cmndName=cmndName,
        attrName='fullDesc',
        attrValue=docStr,
    )

    cmndClass = cmndNameToClass(cmndName)
    if not cmndClass: return

    writeCmndAttrFV(
        cmndName=cmndName,
        attrName='paramsMandatory',
        attrValue=cmndClass().paramsMandatory(),
    )
    writeCmndAttrFV(
        cmndName=cmndName,
        attrName='paramsOptional',
        attrValue=cmndClass().paramsOptional(),
    )
    writeCmndAttrFV(
        cmndName=cmndName,
        attrName='cmndInfo',
        attrValue=cmndInfoEssential().cmnd(
            interactive=False,
            orgLevel=2,
            cmndName=cmndName,
        )
    )

    return

####+BEGIN: bx:cs:py3:func :funcName "cmndCallParamsValidate" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /cmndCallParamsValidate/ deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndCallParamsValidate(
####+END:
        callParamDict,
        interactive,
        outcome=None,

):
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Expected to be used in all CMNDs.


MB-2022 --- This is setting the variable not validating it.
    Perhaps the function should have been cmndCallParamsSet.

Usage Pattern:

    if not icm.cmndCallParamValidate(FPsDir, interactive, outcome=cmndOutcome):
       return cmndOutcome

    #+end_org """

    #G = cs.globalContext.get()
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


####+BEGIN: bx:icm:python:icmItem :itemType "Global" :itemTitle "mainsClassedCmndsGlobal = None"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Global     [[elisp:(outline-show-subtree+toggle)][||]] mainsClassedCmndsGlobal = None  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

mainsClassedCmndsGlobal = None




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
