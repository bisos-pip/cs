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

"""
*  [[elisp:(org-cycle)][| ]]  /General/            :: *Common Utilities -- Constants, Variables* [[elisp:(org-cycle)][| ]]
"""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class            ::  Constants    [[elisp:(org-cycle)][| ]]
"""

class Constants:
    """ Example Usage: kpiResolution = iim.Constants(); kpiResolution.Minutes_15 = 1
    """
    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            raise ValueError('Attribute %s already has a value and so cannot be written to' % attr)

        self.__dict__[attr] = value

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class            ::  Variables    [[elisp:(org-cycle)][| ]]
"""

class Variables:
    """ Example Usage: kpiResolution = iim.Variables(); kpiResolution.Minutes_15 = 1
    """
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value


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





####+BEGIN: bx:dblock:python:class :className "Cmnd" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /Cmnd/ object  [[elisp:(org-cycle)][| ]]
"""
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
            outcome.error = OpError.CmndLineUsageError
            outcome.errInfo = errorStr
            return False
        errorStr = self.cmndParamsMandatoryValidate()
        if errorStr:
            outcome.error = OpError.CmndLineUsageError
            outcome.errInfo = errorStr
            return False
        errorStr = self.cmndParamsOptionalValidate()
        if errorStr:
            outcome.error = OpError.CmndLineUsageError
            outcome.errInfo = errorStr
            return False
        return True

    def cmndArgsLenValidate(self,
    ):
        """ If not as expected, return an error string, otherwise, None.

    expectedCmndArgsLen is a dcitionary with 'Min' and 'Max' range.
    """
        cmndArgsLen = len(IcmGlobalContext().icmRunArgsGet().cmndArgs)
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
        G = IcmGlobalContext()
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
        G = IcmGlobalContext()
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

        min, max = cmndArgPositionToMinAndMax(argPosition)

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

            min, max = cmndArgPositionToMinAndMax(argPosition)

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
        G = IcmGlobalContext()
        icmRunArgs = G.icmRunArgsGet()

        applicableCmndKwArgs = dict()

        g_parDict = IcmGlobalContext().icmParamDictGet().parDictGet()

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
        G = IcmGlobalContext()
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



####+BEGIN: bx:icm:python:func :funcName "cmndArgPositionToMinAndMax" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "argPosStr"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /cmndArgPositionToMinAndMax/ retType=bool argsList=(argPosStr)  [[elisp:(org-cycle)][| ]]
"""
def cmndArgPositionToMinAndMax(
    argPosStr,
):
####+END:
    """
** Expecting argPosStr to be either an integer or two intgers delimited by an ampersand
*** returning two integers specifying the range
"""
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
class ArgReq():
    """ Argument Requirements: For Specification Of Required Keyword Arguments.

    Example: ArgReq.Conditional -- to be used at declaration time.
    """
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



####+BEGIN: bx:icm:python:section :title "ICM_Param: ICM Parameter (ICM_Param, ICM_ParamDict)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM_Param: ICM Parameter (ICM_Param, ICM_ParamDict)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:python:enum :enumName "ICM_ParamScope" :comment ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Enum       [[elisp:(outline-show-subtree+toggle)][||]] /ICM_ParamScope/  [[elisp:(org-cycle)][| ]]
#+end_org """
@enum.unique
class ICM_ParamScope(enum.Enum):
####+END:
    TargetParam = 'TargetParam'
    IcmGeneralParam = 'IcmGeneralParam'
    CmndSpecificParam = 'CmndSpecificParam'

# ICM_ParamScope = ucf.enum('TargetParam', 'IcmGeneralParam', 'CmndSpecificParam')

####+BEGIN: bx:dblock:python:class :className "ICM_Param" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /ICM_Param/ object  [[elisp:(org-cycle)][| ]]
"""
class ICM_Param(object):
####+END:
     """Representation of an Interactively Invokable Module Parameter (ICM_Param).

     An ICM Parameter is a superset of an argsparse parameter which also includes:
        - CMND relevance (Mandatory and Optional)
        - Maping onto FILE_Params


     ICM_Param is initially used to setup ArgParse and other user-interface parameter aspects.
     """

     def __init__(self,
                  parName=None,
                  parDescription=None,
                  parDataType=None,
                  parDefault=None,
                  parChoices=None,
                  parScope=None,
                  parMetavar=None,
                  parAction='store',                    # Same as argparse's action
                  parNargs=None,                        # Same as argparse's nargs
                  parCmndApplicability=None,             # List of CMNDs to which this ICM is applicable
                  argparseShortOpt=None,
                  argparseLongOpt=None,
                 ):
         '''Constructor'''
         self.__parName = parName
         self.__parValue = None
         self.__parCmndApplicability = parCmndApplicability
         self.__parDescription = parDescription
         self.__parDataType = parDataType
         self.__parDefault = parDefault
         self.__parChoices = parChoices
         self.__parMetavar = parMetavar
         self.parActionSet(parAction)
         self.parNargsSet(parNargs)
         self.__argparseShortOpt =  argparseShortOpt
         self.__argparseLongOpt =  argparseLongOpt

     def __str__(self):
         return  ("""\
parName: {parName}
value: {value}
description: {description}""".
                  format(
                      parName=self.parNameGet(),
                      value=self.parValueGet(),
                      description=self.parDescriptionGet()
                  )
             )

     def parNameGet(self):
         """  """
         return self.__parName

     def parNameSet(self, parName):
         """        """
         self.__parName = parName

     def parValueGet(self):
         """        """
         return self.__parValue

     def parValueSet(self, value):
         """        """
         self.__parValue = value

     def parDescriptionGet(self):
         """        """
         return self.__parDescription

     def parDescriptionSet(self, parDescription):
         """        """
         self.__parDescription = parDescription

     def parDataTypeGet(self):
         """        """
         return self.__parDataType

     def parDataTypeSet(self, parDataType):
         """        """
         self.__parDataType = parDataType

     def parDefaultGet(self):
         """        """
         return self.__parDefault

     def parDefaultSet(self, parDefault):
         """        """
         self.__parDefault = parDefault

     def parChoicesGet(self):
         """        """
         return self.__parChoices

     def parChoicesSet(self, parChoices):
         """        """
         self.__parChoices = parChoices

     def parActionGet(self):
         """        """
         return self.__parAction

     def parActionSet(self, parAction):
         """        """
         self.__parAction = parAction

     def parNargsGet(self):
         """        """
         return self.__parNargs

     def parNargsSet(self, parNargs):
         """        """
         self.__parNargs = parNargs

     def argsparseShortOptGet(self):
         """        """
         return self.__argparseShortOpt

     def argsparseShortOptSet(self, argsparseShortOpt):
         """        """
         self.__argparseShortOpt = argsparseShortOpt

     def argsparseLongOptGet(self):
         """        """
         return self.__argparseLongOpt

     def argsparseLongOptSet(self, argsparseLongOpt):
         """        """
         self.__argparseLongOpt = argsparseLongOpt

     def readFrom(self, parRoot=None, parName=None):
         """Read into a FILE_param content of parBase/parName.

         Returns a FILE_param which was contailed in parBase/parName.
         """

         absoluteParRoot = os.path.abspath(parRoot)

         if not os.path.isdir(absoluteParRoot):
             return None

         absoluteParBase = os.path.join(absoluteParRoot, parName)

         if not os.path.isdir(absoluteParBase):
             return None

         fileParam = self

         self.__parName = parName

         #
         # Now we will fill fileParam based on the directory content
         #
         for item in os.listdir(absoluteParBase):
             fileFullPath = os.path.join(absoluteParBase, item)
             if os.path.isfile(fileFullPath):

                 if item == 'value':
                     lineString = open(fileFullPath, 'r').read()
                     self.parValueSet(lineString)
                     continue

                 # Rest of the files are expected to be attributes

                 lineString = open(fileFullPath, 'r').read()
                 # NOTYET, check for exceptions
                 eval('self.attr' + str(item).title() + 'Set(lineString)')

         return fileParam

     @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
     def writeAsFileParam(
             self,
             parRoot=None,
     ):
         """Writing a FILE_param content of self.

         Returns a FILE_param which was contailed in parBase/parName.
         """

         absoluteParRoot = os.path.abspath(parRoot)

         if not os.path.isdir(absoluteParRoot):
            try: os.makedirs( absoluteParRoot, 0o775 )
            except OSError: pass

         #print absoluteParRoot

         #print
         #print self.parValueGet()

         parValue = self.parValueGet()
         if not parValue:
             parValue = "unSet"

         FILE_ParamWriteTo(
             parRoot=absoluteParRoot,
             parName=self.parNameGet(),
             parValue=parValue,
         )

         varValueFullPath = os.path.join(
             absoluteParRoot,
             self.parNameGet(),
             'description'
         )

         FV_writeToFilePathAndCreate(
             filePath=varValueFullPath,
             varValue=self.parDescriptionGet(),
         )

         varValueBaseDir = os.path.join(
             absoluteParRoot,
             self.parNameGet(),
             'enums'
         )

         for thisChoice in self.parChoicesGet():
             FV_writeToBaseDirAndCreate(
                 baseDir=varValueBaseDir,
                 varName=thisChoice,
                 varValue="",
             )

####+BEGIN: bx:dblock:python:class :className "ICM_ParamDict" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /ICM_ParamDict/ object  [[elisp:(org-cycle)][| ]]
"""
class ICM_ParamDict(object):
####+END:
     """ICM Parameters Dictionary -- Collection of ICM_Param s can be placed in ICM_ParamDict

     From icmParamDict
     """

     def __init__(self):
         self.__icmParamDict = dict()

     def parDictAdd(self,
                    parName=None,
                    parDescription=None,
                    parDataType=None,
                    parMetavar=None,
                    parDefault=None,
                    parChoices=None,
                    parScope=None,
                    parAction='store',
                    parNargs=None,
                    argparseShortOpt=None,
                    argparseLongOpt=None,
                   ):
         """        """
         thisParam = ICM_Param(parName=parName,
                               parDescription=parDescription,
                               parDataType=parDataType,
                               parMetavar=parMetavar,
                               parDefault=parDefault,
                               parChoices=parChoices,
                               parScope=parScope,
                               parAction=parAction,
                               parNargs=parNargs,
                               argparseShortOpt=argparseShortOpt,
                               argparseLongOpt=argparseLongOpt,
                               )

         self.parDictAppend(thisParam)
         # print(f"rrr {thisParam}")

     def parDictAppend(self, icmParam):
         """        """
         self.__icmParamDict.update({icmParam.parNameGet():icmParam})


     def parDictGet(self):
         """        """
         return self.__icmParamDict

     def parNameFind(self, parName):
         """        """
         found = self.__icmParamDict[parName]
         return found


     def cmndApplicabilityUpdate(self,
                                cmnd=None,
                                mandatoryParams=None,
                                optionalParams=None,
                                ):
         """NOTYET -- Verify That Mandatory and Optional Params for this cmnd have been specified At Runtime."""

         # if icmRunArgs.perfSap:
         #     print(icmRunArgs.perfSap)

         # if icmRunArgs.wsdlUrl:
         #     print(icmRunArgs.wsdlUrl)

         return


####+BEGIN: bx:icm:python:section :title "CmndArgs: Per Command Argument"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *CmndArgs: Per Command Argument*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:python:class :className "CmndArgSpec" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /CmndArgSpec/ object  [[elisp:(org-cycle)][| ]]
"""
class CmndArgSpec(object):
####+END:
     """\
** Representation of an Interactively Command Module (ICM) Command Argument Sepecification(CmndArgSpec).
     """

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
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /CmndArgsSpecDict/ object  [[elisp:(org-cycle)][| ]]
"""
class CmndArgsSpecDict(object):
####+END:
     """ICM Argameters Dictionary -- Collection of ICM_Argam s can be placed in ICM_ArgamDict

     From icmArgamDict
     """

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
*  [[elisp:(org-cycle)][| ]]  /ICM Output/         :: *icmOutputBaseGet -- icmOutputXlsGetPath(fileBaseName)* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmOutputBaseGet    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmOutputBaseGet():
    return "./"

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmOutputXlsGetPath    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmOutputXlsGetPath(fileBaseName):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%y%m%d%H%M%S')
    fileName = fileBaseName + st + ".xlsx"
    return os.path.join(icmOutputBaseGet(), fileName)

"""
*  [[elisp:(org-cycle)][| ]]  /ICM Lib/            :: *percentage, runOnceOnly, setAdjust*  [[elisp:(org-cycle)][| ]]
"""


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  /G_/                 :: *IcmGlobalContext (G_) -- Class, ICM Singleton Usage, provides global context* [[elisp:(org-cycle)][| ]]
"""

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


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class            ::  IcmGlobalContext    [[elisp:(org-cycle)][| ]]
"""

class IcmGlobalContext():
     """ Singleton Usage Model: Interactively Invokable Module Global Context.
     """

     icmArgsParser = None

     #icmRunArgsThis = None
     icmRunArgsThis = []
     icmParamDict = None       # ICM Specified Parameters in g_argsExtraSpecify()
     thisFuncName = None
     logger = None
     astModuleFunctionsList = None

     _icmInfo = {}

     usageParams = Variables
     usageArgs = Variables

     # ICM-Profile Specifications
     icmGroupingType = ICM_GroupingType.UnSet
     icmPkgedModel = ICM_PkgedModel.UnSet
     icmCmndPartsList = [ICM_CmndParts.UnSet]

     _auxInvokationContext = AuxInvokationContext.UnSet
     _auxInvokationResults = None
     _cmndNames = None # All 3 of the above have been obsoleted

     _cmndFuncsDict = None
     _cmndMethodsDict = None

     lastOpOutcome = None

     def __init__(self):
         pass

     def globalContextSet(self,
                          icmRunArgs=None,
                          icmParamDict=None
                          ):
         """
         """
         #if not icmRunArgs == None:
         self.__class__.icmRunArgsThis = icmRunArgs

         # NOTYET, 2017 -- Review This
         if icmParamDict == None:
             pass
             #self.__class__.icmParamDict = ICM_ParamDict()

         logger = logging.getLogger(io.log.LOGGER)
         self.__class__.logger = logger

         self.__class__.astModuleFunctionsList = bpf.ast.ast_topLevelFunctionsInFile(
             self.icmMyFullName()
         )

     def icmRunArgsGet(self):
         return self.__class__.icmRunArgsThis

     def icmParamDictSet(self, icmParamDict):
         # print(f"XXX {icmParamDict}")
         self.__class__.icmParamDict = icmParamDict

     def icmParamDictGet(self):
         return self.__class__.icmParamDict

     def icmMyFullName(self):
          return os.path.abspath(sys.argv[0])

     def icmMyName(self):
         return os.path.basename(sys.argv[0])

     def icmModuleFunctionsList(self):
         return self.__class__.astModuleFunctionsList

     def curFuncNameSet(self, curFuncName):
         self.__class__.thisFuncName = curFuncName

     def curFuncName(self):
         return self.__class__.thisFuncName

     def auxInvokationContextSet(self, auxInvokationEnum):
         self.__class__._auxInvokationContext = auxInvokationEnum

     def auxInvokationContext(self):
         return self.__class__._auxInvokationContext

     def auxInvokationResultsSet(self, auxInvokationRes):
         self.__class__._auxInvokationResults = auxInvokationRes

     def auxInvokationResults(self):
         return self.__class__._auxInvokationResults

     def icmInfoSet(self, icmInfo):
         self.__class__._icmInfo = icmInfo

     def icmInfo(self):
         return self.__class__._icmInfo


     def cmndNamesSet(self, cmnds):
         self.__class__._cmndNames = cmnds

     def cmndNames(self):
         return self.__class__._cmndNames

     def cmndMethodsDictSet(self, cmnds):
         self.__class__._cmndMethodsDict = cmnds

     def cmndMethodsDict(self):
         return self.__class__._cmndMethodsDict

     def cmndFuncsDictSet(self, cmnds):
         self.__class__._cmndFuncsDict = cmnds

     def cmndFuncsDict(self):
         return self.__class__._cmndFuncsDict

G = IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  commonIcmParamsParser    [[elisp:(org-cycle)][| ]]
"""
def commonIcmParamsParser(parser):
    """Module Common Command Line Parameters.

    NOTYET -- Needs To Be Called
    """
    icmParams = commonIcmParamsPrep()

    argsparseBasedOnIcmParams(parser, icmParams)

    return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  commonIcmParamsPrep    [[elisp:(org-cycle)][| ]]
"""
def commonIcmParamsPrep():
    """Module Common Command Line Parameters.
    """
    icmParams = ICM_ParamDict()

    icmParams.parDictAdd(
        parAction='append',
        parName='callTrackings',
        parDescription="Set monitoring of calls and selected invokes.",
        parDataType=None,
        parDefault=[],
        parChoices=['invoke+', 'invoke-', 'monitor+', 'monitor-'],
        parScope=ICM_ParamScope.TargetParam,
        argparseShortOpt='-t',
        argparseLongOpt='--callTrackings',
        )

    icmParams.parDictAdd(
        parAction='store',
        parName='runMode',
        parDescription="Run Mode as fullRun or dryRun",
        parDataType=None,
        parDefault='fullRun',
        parChoices=['dryRun', 'fullRun', 'runDebug'],
        parScope=ICM_ParamScope.TargetParam,
        #argparseShortOpt='-r',
        argparseLongOpt='--runMode',
        )

    icmParams.parDictAdd(
        parAction='store',
        parName='verbosity',
        parDescription='Adds a Console Logger for the level specified in the range 1..50',
        parDataType=None,
        parDefault='30',
        parMetavar='ARG',
        parChoices=['1', '10', '20', '30', '40', '50',],
        parScope=ICM_ParamScope.TargetParam,
        argparseShortOpt='-v',
        argparseLongOpt='--verbosity',
        )

    icmParams.parDictAdd(
        parAction='store',
        parName='logFile',
        parDescription='Specifies destination LogFile for this run',
        parDataType=None,
        parDefault=None,
        parMetavar='ARG',
        parChoices=[],
        parScope=ICM_ParamScope.TargetParam,
        #argparseShortOpt='-v',
        argparseLongOpt='--logFile',
        )

    icmParams.parDictAdd(
        parAction='store',
        parName='logFileLevel',
        parDescription='Specifies destination LogFile for this run',
        parDataType=None,
        parDefault=None,
        parMetavar='ARG',
        parChoices=[],
        parScope=ICM_ParamScope.TargetParam,
        #argparseShortOpt='-v',
        argparseLongOpt='--logFileLevel',
        )

    icmParams.parDictAdd(
        parAction='store_true',
        parName='docstring',
        parDescription='Docstring',
        parDataType=None,
        parDefault=None,
        parMetavar='ARG',
        parChoices=[],
        parScope=ICM_ParamScope.TargetParam,
        #argparseShortOpt='-v',
        argparseLongOpt='--logFileLevel',
        )

    # icmParams.parDictAdd(
    #     parAction='store',
    #     parName='cmndArgs',
    #     parDescription='Docstring',
    #     parDataType=None,
    #     parDefault=None,
    #     parMetavar='ARG',
    #     parChoices=None,
    #     parScope=ICM_ParamScope.TargetParam,
    #     #argparseShortOpt='-v',
    #     argparseLongOpt='--logFileLevel',
    #     )


    icmParams.parDictAdd(
        parAction='append',
        parName='loadfiles',
        parDescription='Load Files',
        parDataType=None,
        parDefault=None,
        parMetavar='ARG',
        parChoices=[],
        parScope=ICM_ParamScope.TargetParam,
        #argparseShortOpt='-l',
        argparseLongOpt='--load',
        )

    return icmParams


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  argsCommonProc -- Obsoleted By commonIcmParamsPrep??   [[elisp:(org-cycle)][| ]]
"""
#@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def argsCommonProc(parser):

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

"""
*  [[elisp:(org-cycle)][| ]]  getopt.args   :: Arguments Parsing -- G_argsProc based on argparse [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  G_argsProc    [[elisp:(org-cycle)][| ]]
"""
#@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def G_argsProc(arguments, extraArgs):
     """ICM-ICM Argument Parser.

     extraArgs resides in the G_ module.
     """

     parser = argparse.ArgumentParser(
         description=__doc__
         )

     argsCommonProc(parser)
     #commonIcmParamsPrep()

     if extraArgs:
        extraArgs(parser)

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


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  argsparseBasedOnIcmParams    [[elisp:(org-cycle)][| ]]
"""
#subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def argsparseBasedOnIcmParams(parser, icmParams):
     """Convert icmParams to parser
**  [[elisp:(org-cycle)][| ]]  Subject      :: type= is missing -- [[elisp:(org-cycle)][| ]]
     """


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

     return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmParamsToFileParamsUpdate    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmParamsToFileParamsUpdate(
        parRoot,
        icmParams,
):
     """Convert icmParams to parser
**  [[elisp:(org-cycle)][| ]]  Subject      :: type= is missing -- [[elisp:(org-cycle)][| ]]
     """

     LOG_here("Updating icmParams at: {parRoot}".format(parRoot=parRoot))

     for key, icmParam in icmParams.parDictGet().items():
         if ( icmParam.argsparseShortOptGet() == None )  and ( icmParam.argsparseLongOptGet() == None ):
             break

         icmParam.writeAsFileParam(
             parRoot=parRoot,
         )

     return

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndParamsMandatoryAssert    [[elisp:(org-cycle)][| ]]
"""

def cmndParamsMandatoryAssert(paramsList):
        for key, value in paramsList.items():
            if value == None: return(EH_critical_usageError(key))


"""
*  [[elisp:(org-cycle)][| ]]  /G_ examples/        :: *G_commonExamples -- Common features included in G_examples() + devExamples(), etc* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  commonExamples    [[elisp:(org-cycle)][| ]]
"""
class commonExamples(Cmnd):
    """Print common ICM examples."""

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=True,
    ):
        """Provide a menu of common icm examples.
"""
        G_myFullName = sys.argv[0]
        G_myName = os.path.basename(G_myFullName)

        cmndExampleMenuChapter('/Intercatively Invokable Module (ICM) General Usage Model/')

        print(( G_myName + " --help" ))
        print(( G_myName + " -i model" ))
        print(( G_myName + " -i icmHelp" ))
        print(( G_myName + " -i icmOptionsExamples" ))
        print(( G_myName + " -i icmInfo" ))
        print(( G_myName + " -i icmInUpdate ./var" ))
        print(( G_myName + " -i cmndInfo cmndName" ))
        print(( G_myName + " -i cmndInfo cmndInfo" ))
        print(( G_myName + " -i devExamples" ))
        print(( G_myName + " -i describe" ))
        print(( G_myName + " -i describe" + " |" + " emlVisit"))
        print(( G_myName + " -i examples" ))
        print(( G_myName + " -i examples" + " |" + " icmToEmlVisit"))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  G_commonBriefExamples    [[elisp:(org-cycle)][| ]]
"""
#@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def G_commonBriefExamples(interactive=False):

     G_myFullName = sys.argv[0]
     G_myName = os.path.basename(G_myFullName)

     cmndExampleMenuChapter('/Intercatively Invokable Module (ICM) Brief Usage Model/')

     print(( G_myName + " -i commonExamples" + "    # Help, Model, icmOptionsExample"))
     print(( G_myName + " -i describe" + " |" + " emlVisit"))
     print(( G_myName + " -i examples" + " |" + " icmToEmlVisit"))
     print(( G_myName + " -i visit"))
     print(( """emlVisit -v -n showRun -i gotoPanel """ + G_myFullName))

     cmndExampleMenuChapter('*ICM Blee Player Invokations*')
     io.ann.ANN_write("icmPlayer.sh -h -v -n showRun -i grouped {G_myName}".format(G_myName=G_myName))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  devExamples    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def devExamples(interactive=False):

     G_myName = sys.argv[0]

     print("======== Development =========")

     print(("python -m trace -l " + G_myName + " | egrep -v " + '\'/python2.7/|\<string\>\''))
     print(("python -m trace -l " + G_myName))
     print(("python -m trace -t " + G_myName))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmOptionsExamples    [[elisp:(org-cycle)][| ]]
"""

class icmOptionsExamples(Cmnd):
    """Print a summary of the ICM Model."""

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
            interactive=True,
    ):

        G_myFullName = sys.argv[0]
        G_myName = os.path.basename(G_myFullName)

        print("==== cmndEx Built-In Feature Examples =====")

        print(( G_myName + " -i icm.cmndExample arg1 arg2" ))
        print(( G_myName + " -v 20" + " -i icm.cmndExample arg1 arg2" ))
        print(( G_myName + " -v 1" + " -i icm.cmndExample arg1 arg2" ))
        print(( G_myName + " --runMode dryRun" + " -i icm.cmndExample arg1 arg2" ))
        print(( G_myName + " -v 1" + " --callTrackings monitor-" + " -i icm.cmndExample arg1 arg2" ))
        print(( G_myName + " -v 1" + " --callTrackings monitor+" + " --callTrackings invoke+" + " -i icm.cmndExample arg1 arg2" ))
        print(( G_myName + " -v 1" + " --callTrackings monitor-" + " --callTrackings invoke-" + " -i icm.cmndExample arg1 arg2" ))
        print(( G_myName + " --docstring" + " -i describe" ))



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmExampleMyName    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmExampleMyName(myName, myFullName):
    """
    """
    print(("#######  " + '  *' + myName + '*  ' + "  ##########"))
    print(("=======  " + myFullName + "  ==========="))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || CMND       ::  ex_gCommon    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def ex_gCommon():
    """."""
    G = IcmGlobalContext()
    icmExampleMyName(G.icmMyName(), G.icmMyFullName())
    G_commonBriefExamples()
    #G_commonExamples()

"""
*  [[elisp:(org-cycle)][| ]]  /example Seps/       :: *cmndExample -- Simple Usage Example -- Seperators* [[elisp:(org-cycle)][| ]]
"""



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndExampleMenuChapter    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndExampleMenuChapter(title):
    """
    """
    print(("#######  " + title + "  ##########"))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndExampleMenuSection    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndExampleMenuSection(title):
     """
     """
     print(("=======  " + title + "  =========="))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndExampleMenuSubSection    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndExampleMenuSubSection(title):
     """  """
     print(("%%%%%%%  " + title + "  %%%%%%%%%%%"))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndExampleMenuItem    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndExampleMenuItem(
        commandLine,
        icmName=None,          # Defaults to G_myName
        verbosity='basic',
        comment='none',
        icmWrapper=None,
):
    """ vebosity is one of: 'none', 'little', 'some',  'full'
    """
    G_myFullName = sys.argv[0]
    G_myName = os.path.basename(G_myFullName)

    if comment == 'none':
        fullCommandLine = commandLine
    else:
        fullCommandLine = commandLine + '         ' + comment

    if icmName:
        G_myName = icmName

    if icmWrapper:
        G_myName = icmWrapper + " " + G_myName

    if verbosity == 'none':
        #print( G_myName + " -v 30" + " " + fullCommandLine)
        print(( G_myName + " " + fullCommandLine))
    elif verbosity == 'basic':
        print(( G_myName + " -v 1"  + " " + fullCommandLine ))
    elif verbosity == 'little':
        print(( G_myName + " -v 20" + " " + fullCommandLine ))
    elif verbosity == 'some':
        print(( G_myName + " -v 1"  + " --callTrackings monitor-" + " --callTrackings invoke-" + " " + fullCommandLine ))
    elif verbosity == 'full':
        print(( G_myName + " -v 1"  + " --callTrackings monitor+" + " --callTrackings invoke+" + " " + fullCommandLine ))
    else:
        return EH_critical_oops('')



####+BEGINNOT: bx:icm:py3:func :funcName "icmCmndLine" :funcType "str" :retType "" :deco "default" :argsList ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-str   :: /icmCmndLine/ deco=default  [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmCmndLine(
####+END:
        cmndName,    # String
        cmndPars,    # Dictionary
        cmndArgs,    # String
        verbosity='basic',
        comment='none',
        icmWrapper=None,
        icmName=None,
):
    """
** Returns cmndLine as string
    """

    cmndParsStr = ""
    for key in cmndPars:
        cmndParsStr += """--{parName}="{parValue}" """.format(parName=key, parValue=cmndPars[key])

    if not icmName:
        icmName=G.icmMyName()

    dashV = icmVerbosityTagToDashV(verbosity)

    cmndLine = """{icmName} {dashV} {cmndParsStr} -i {cmndName} {cmndArgs}""".format(
        icmName=icmName,
        dashV=dashV,
        cmndName=cmndName, cmndParsStr=cmndParsStr, cmndArgs=cmndArgs
    )
    return cmndLine

####+BEGINNOT: bx:icm:py3:func :funcName "icmVerbosityTagToDashV" :funcType "str" :retType "" :deco "default" :argsList ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-str   :: /icmVerbosityTagToDashV/ deco=default  [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def icmVerbosityTagToDashV(
####+END:
        verbosity,
) -> str:
    result = ""

    if verbosity == 'none':
        result = ""
    elif verbosity == 'basic':
        result = " -v 1"
    elif verbosity == 'little':
        result = " -v 20"
    elif verbosity == 'some':
        result = " -v 1"
    elif verbosity == 'full':
        result = " -v 1 --callTrackings monitor+ --callTrackings invoke+"
    else:
        return EH_critical_oops('')
    return result



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  ex_gCmndMenuItem    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def ex_gExtCmndMenuItem(
        cmndName,    # String
        cmndPars,    # Dictionary
        cmndArgs,    # String
        verbosity='basic',
        comment='none',
        icmWrapper=None,
        icmName=None,
):
    """ vebosity is one of: 'none', 'little', 'some',  'full'
    """

    cmndParsStr = ""
    for key in cmndPars:
        cmndParsStr += """--{parName}="{parValue}" """.format(parName=key, parValue=cmndPars[key])

    cmndLine = """{cmndParsStr} -i {cmndName} {cmndArgs}""".format(
        cmndName=cmndName, cmndParsStr=cmndParsStr, cmndArgs=cmndArgs
    )

    cmndExampleMenuItem(
        commandLine=cmndLine,
        verbosity=verbosity,
        comment=comment,
        icmWrapper=icmWrapper,
        icmName=icmName,
    )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  ex_gCmndMenuItem    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def ex_gCmndMenuItem(
        cmndName,    # String
        cmndPars,    # Dictionary
        cmndArgs,    # String
        verbosity='basic',
        comment='none',
        icmWrapper=None,
        icmName=None,
):
    """ vebosity is one of: 'none', 'little', 'some',  'full'
    """

    cmndParsStr = ""
    for key in cmndPars:
        cmndParsStr += """--{parName}="{parValue}" """.format(parName=key, parValue=cmndPars[key])

    cmndLine = """{cmndParsStr} -i {cmndName} {cmndArgs}""".format(
        cmndName=cmndName, cmndParsStr=cmndParsStr, cmndArgs=cmndArgs
    )

    cmndExampleMenuItem(
        commandLine=cmndLine,
        verbosity=verbosity,
        comment=comment,
        icmWrapper=icmWrapper,
        icmName=icmName,
    )


####+BEGIN: bx:dblock:python:func :funcName "ex_gExecMenuItem" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "execLine wrapper=None comment='none'"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /ex_gExecMenuItem/ retType=bool argsList=(execLine wrapper=None comment='none')  [[elisp:(org-cycle)][| ]]
"""
def ex_gExecMenuItem(
    execLine,
    wrapper=None,
    comment='none',
):
####+END:
    """
** Output an Non-ICM menu line.
"""
    if comment == 'none':
        fullCommandLine = execLine
    else:
        fullCommandLine = execLine + '         ' + comment

    if wrapper:
        fullCommandLine = wrapper + fullCommandLine

    print(fullCommandLine)



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndExampleExternalCmndItem    [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def cmndExampleExternalCmndItem(commandLine,
                               verbosity='basic',
                               comment='none'
                               ):
    """ vebosity is one of: 'none', 'little', 'some',  'full'
                               """
    #G_myFullName = sys.argv[0]
    #G_myName = os.path.basename(G_myFullName)

    if comment == 'none':
        fullCommandLine = commandLine
    else:
        fullCommandLine = commandLine + '         ' + comment

    print( fullCommandLine )

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



"""
*  [[elisp:(org-cycle)][| ]]  /icmRunArgs/         :: *IcmRunArgs_ -- In support of Run Time ICM Options --  icmRunArgs_isOptionXxSet()* [[elisp:(org-cycle)][| ]]
"""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_isCallTrackingMonitorOff    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_isCallTrackingMonitorOff():
    """Activated with --callTrackings monitor-.
    """

    G = IcmGlobalContext()
    icmRunArgs = G.icmRunArgsGet()
    retVal = False

    for this in icmRunArgs.callTrackings:
        if this == 'monitor-':
            retVal = True

    return retVal
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_isCallTrackingMonitorOn    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_isCallTrackingMonitorOn():
    """Activated with --callTrackings monitor-.
    """

    G = IcmGlobalContext()
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
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_isCallTrackingInvokeOff    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_isCallTrackingInvokeOff():
    """Activated with --callTrackings monitor-.
    """
    G = IcmGlobalContext()
    icmRunArgs = G.icmRunArgsGet()

    retVal = False

    for this in icmRunArgs.callTrackings:
        if this == 'invoke-':
            retVal = True

    return retVal

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_isRunModeDryRun    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_isRunModeDryRun():
    """Activated with --runMode dryRun.
    """
    G = IcmGlobalContext()
    icmRunArgs = G.icmRunArgsGet()

    retVal = False

    if icmRunArgs.runMode == 'dryRun':
        retVal = True

    return retVal

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_isRunModeDryRun    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_verbosityLevel():
    """
    """
    G = IcmGlobalContext()
    icmRunArgs = G.icmRunArgsGet()

    level = icmRunArgs.verbosityLevel
    if level is None:
        return 30

    try: level = int(level)
    except: pass

    return level



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_isDocStringRequested    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_isDocStringRequested():
    """Activated with -i docString.
    """
    G = IcmGlobalContext()
    icmRunArgs = G.icmRunArgsGet()

    retVal = False

    if icmRunArgs.docstring:
        retVal = True

    return retVal

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_loadFiles    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_loadFiles():
    """Load the python files specified with --load."""
    G = IcmGlobalContext()
    icmRunArgs = G.icmRunArgsGet()

    for this in icmRunArgs.loadFiles:
        loadFile(this)

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  icmRunArgs_evalFiles    [[elisp:(org-cycle)][| ]]
"""

def icmRunArgs_evalFiles():
    """Eval Files -- Unused But Perhaps Usefull."""
    G = IcmGlobalContext()
    icmRunArgs = G.icmRunArgsGet()

    for this in icmRunArgs.loadFiles:
        TM_here('Loading: ' + this)
        f = open(this)
        eval(f.read()) # Caution: you must be sure of what's in that file
        f.close()

####+BEGIN: bx:icm:python:func :funcName "libUserInit" :funcType "void" :retType "void" :deco "" :argsList "icmLineOpts"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-void      :: /libUserInit/ retType=void argsList=(icmLineOpts)  [[elisp:(org-cycle)][| ]]
"""
def libUserInit(
    icmLineOpts,
):
####+END:
    """ For situations when icm lib is being used outside of an ICM -- in the context of any app.
"""
    parser = argparse.ArgumentParser(
         description=__doc__
    )
    argsCommonProc(parser)

    args = parser.parse_args(icmLineOpts)
    logControler = LOG_Control()
    logControler.loggerSet(args)


"""
*  [[elisp:(org-cycle)][| ]]  /G_main/             :: *G_main -- Invoked from ICM, calls invokesProc* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  G_main    [[elisp:(org-cycle)][| ]]
"""
# DO NOT DECORATE THIS FUNCTION
#@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)   # Log module has not been setup, we can't track this
def G_main(inArgv,
           G_examples,
           extraArgs,
           invokesProc,
           mainEntry=None,
):
    """This is the main entry point for Python.Icm.Icm (InteractiveInvokationModules)
    """

    #
    # The order is important here,
    # 1) Parse The Command Line -- 2) LOG_ usese the command line -- 3) G. setup
    #
    icmRunArgs, icmArgsParser = G_argsProc(inArgv, extraArgs)

    logControler = LOG_Control()
    logControler.loggerSet(icmRunArgs)

    logger = logControler.loggerGet()

    logger.info('Main Started: ' + ucf.stackFrameInfoGet(1) )

    G = IcmGlobalContext()
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


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  G_mainWithClass    [[elisp:(org-cycle)][| ]]
"""
# DO NOT DECORATE THIS FUNCTION
#@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)   # Log module has not been setup, we can't track this
def G_mainWithClass(
        inArgv,
        G_examples,
        extraArgs,
        classedCmndsDict,
        #funcedCmndsDict,
        mainEntry=None,
        g_icmPreCmnds=None,
        g_icmPostCmnds=None,
):
    """This is the main entry point for Python.Icm
    """

    icmRunArgs, icmArgsParser = G_argsProc(inArgv, extraArgs)

    logControler = io.log.LOG_Control()
    logControler.loggerSet(icmRunArgs)

    logger = logControler.loggerGet()

    logger.info('Main Started: ' + bpf.ast.stackFrameInfoGet(1) )

    G = IcmGlobalContext()
    G.globalContextSet( icmRunArgs=icmRunArgs )
    G.icmArgsParser = icmArgsParser
    G.cmndMethodsDictSet(classedCmndsDict)
    #G.cmndFuncsDictSet(funcedCmndsDict)

    icmRunArgs_loadFiles()

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
            if outcome.error != OpError.Success:
                if outcome.error == OpError.CmndLineUsageError:
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

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  invokesProcWithClass    [[elisp:(org-cycle)][| ]]
"""
def invokesProcAllClassed(
        classedCmndsDict,
        icmRunArgs,
):
    """Process all invokations applicable to all (classed+funced of mains+libs) CMNDs."""
    G = IcmGlobalContext()
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
            #print "TM_"
            pass
        else:
            #print(f"Found {classedCmnd}")
            outcome = applyMethodBasedOnContext(classedCmnd)
            continue

        #
        # Next we try cmndList_libsMethods()
        #
        callDict = dict()
        for eachCmnd in cmndList_libsMethods().cmnd(interactive=False):
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
        EH_problem_info("Invalid Action: {invoke}"
                        .format(invoke=invoke))

        print(("Invalid Action: {invoke}"
                        .format(invoke=invoke)))

        outcome = OpOutcome()
        outcome.error = OpError.CmndLineUsageError
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


"""
*  [[elisp:(org-cycle)][| ]]  /Player Support/      :: *Framework cmnds That are expected by the ICM-Player* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  icmLanguage    [[elisp:(org-cycle)][| ]]
"""
class icmLanguage(Cmnd):
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
class icmCmndPartIncludes(Cmnd):
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
class icmInUpdate(Cmnd):
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
class icmInfo(Cmnd):
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
class version(Cmnd):
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
class visit(Cmnd):
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
class cmndInfo(Cmnd):
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
class cmndInfoEssential(Cmnd):
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
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndNameToClass    [[elisp:(org-cycle)][| ]]
"""
def cmndNameToClass(
        cmndName,
):
    """Given cmndName, return cmndClass."""

    G = IcmGlobalContext()
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


"""
*  [[elisp:(org-cycle)][| ]]  /cmndsList_/          :: *cmndsList_ -- List C-CMNDs and F-CMNDs in a given file and in icm library* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndList_allMethods    [[elisp:(org-cycle)][| ]]
"""
class cmndList_allMethods(Cmnd):
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
class cmndList_mainsMethods(Cmnd):
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
class cmndList_libsMethods(Cmnd):
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
class cmndClassDocStr(Cmnd):
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
class cmndHelp(Cmnd):
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
class null(Cmnd):
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
class cmndMethodDocStr(Cmnd):
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
class cmndDocStrShort(Cmnd):
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
class cmndDocStrFull(Cmnd):
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
class classDocStrOf(Cmnd):
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


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndSubclassesNames    [[elisp:(org-cycle)][| ]]
"""
def cmndSubclassesNames():
    """Not using generators by choice."""
    # return [each.__name__ for each in Cmnd.__subclasses__()]
    cmndsNames = list()
    for eachClass in Cmnd.__subclasses__():
        cmndsNames.append(eachClass.__name__)
    return cmndsNames

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndMainsMethodsToFileParamsUpdate    [[elisp:(org-cycle)][| ]]
"""
def cmndMainsMethodsToFileParamsUpdate(
        parRoot,
):
    """ """
    mainsCmndMethods = cmndList_mainsMethods().cmnd()
    for each in mainsCmndMethods:
        cmndToFileParamsUpdate(
            cmndName=each,
            parRoot=parRoot,
        )
    return

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndLibsMethodsToFileParamsUpdate    [[elisp:(org-cycle)][| ]]
"""
def cmndLibsMethodsToFileParamsUpdate(
        parRoot,
):
    """ """
    libsCmndMethods = cmndList_libsMethods().cmnd()
    for each in libsCmndMethods:
        cmndToFileParamsUpdate(
            cmndName=each,
            parRoot=parRoot,
        )
    return

####+BEGIN: bx:icm:python:func :funcName "evalStringInMain" :funcType "succFail" :retType "bool" :deco "" :argsList "inStr"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-succFail  :: /evalStringInMain/ retType=bool argsList=(inStr)  [[elisp:(org-cycle)][| ]]
"""
def evalStringInMain(
    inStr,
):
####+END:
    """
** Given inStr eval that string in __main__.
"""
    LOG_here("Eval-ing: __main__.{}".format(inStr))
    # try
    eval("__main__.{}".format(inStr))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndToFileParamsUpdate    [[elisp:(org-cycle)][| ]]
"""
def cmndToFileParamsUpdate(
        cmndName,
        parRoot,
):
    "Write cmnd as fileParam"

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



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndNameToClass    [[elisp:(org-cycle)][| ]]
"""
def cmndNameToClass(
        cmndName,
):
    """Given cmndName, return cmndClass."""

    G = IcmGlobalContext()
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


"""
*  [[elisp:(org-cycle)][| ]]  /cmndsList_/          :: *cmndsList_ -- List C-CMNDs and F-CMNDs in a given file and in icm library* [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-CMND        ::  cmndList_allMethods    [[elisp:(org-cycle)][| ]]
"""
class cmndList_allMethods(Cmnd):
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
class cmndList_mainsMethods(Cmnd):
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

        mainClasses = bpf.ast.ast_topLevelClassNamesInFile(
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
            relevantClasses += bpf.ast.ast_topLevelClassNamesInFile(modPath)

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
class cmndList_libsMethods(Cmnd):
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
class cmndClassDocStr(Cmnd):
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
class cmndHelp(Cmnd):
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
class null(Cmnd):
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
class cmndMethodDocStr(Cmnd):
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
class cmndDocStrShort(Cmnd):
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
class cmndDocStrFull(Cmnd):
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
class classDocStrOf(Cmnd):
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


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndSubclassesNames    [[elisp:(org-cycle)][| ]]
"""
def cmndSubclassesNames():
    """Not using generators by choice."""
    # return [each.__name__ for each in Cmnd.__subclasses__()]
    cmndsNames = list()
    for eachClass in Cmnd.__subclasses__():
        cmndsNames.append(eachClass.__name__)
    return cmndsNames

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndMainsMethodsToFileParamsUpdate    [[elisp:(org-cycle)][| ]]
"""
def cmndMainsMethodsToFileParamsUpdate(
        parRoot,
):
    """ """
    mainsCmndMethods = cmndList_mainsMethods().cmnd()
    for each in mainsCmndMethods:
        cmndToFileParamsUpdate(
            cmndName=each,
            parRoot=parRoot,
        )
    return

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndLibsMethodsToFileParamsUpdate    [[elisp:(org-cycle)][| ]]
"""
def cmndLibsMethodsToFileParamsUpdate(
        parRoot,
):
    """ """
    libsCmndMethods = cmndList_libsMethods().cmnd()
    for each in libsCmndMethods:
        cmndToFileParamsUpdate(
            cmndName=each,
            parRoot=parRoot,
        )
    return

####+BEGIN: bx:icm:python:func :funcName "evalStringInMain" :funcType "succFail" :retType "bool" :deco "" :argsList "inStr"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-succFail  :: /evalStringInMain/ retType=bool argsList=(inStr)  [[elisp:(org-cycle)][| ]]
"""
def evalStringInMain(
    inStr,
):
####+END:
    """
** Given inStr eval that string in __main__.
"""
    LOG_here("Eval-ing: __main__.{}".format(inStr))
    # try
    eval("__main__.{}".format(inStr))


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func             ::  cmndToFileParamsUpdate    [[elisp:(org-cycle)][| ]]
"""
def cmndToFileParamsUpdate(
        cmndName,
        parRoot,
):
    "Write cmnd as fileParam"

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

    #print(importedCmndsFilesList)
    #print(importedTagsList)

    callDict = dict()
    for eachCmnd in cmndList_mainsMethods().cmnd(
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
                #print("callDict -- {importTag}.{eachCmnd}")
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

    G.icmInfoSet(icmInfo)

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
        G_mainWithClass(
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
